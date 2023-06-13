import argparse
import os
import json
import keyword
import re
import typing

from jinja2 import Environment, PackageLoader
import pydantic

from devtools import debug

from hacks import TOKEN_REPLACEMENTS

WORKING_DIR = os.getcwd()

ATOMIC_TYPES = {
    "string",
    "blob",
    "integer",
    "boolean",
    "timestamp",
    "double",
    "long",
    "map",
    "float"
}

ATOMIC_MAPPING = {
    "string": "str",
    "blob": "bytes",
    "integer": "int",
    "boolean": "bool",
    "timestamp": "date",
    "TStamp": "date",
    "double": "float",
    "long": "int",
    "map": "dict",
    "float": "float"
}


TRANSLATION_TABLE = str.maketrans({
    "-": "_",
    ".": "_",
    "/": "_",
    ":": "_",
    " ": "_", 
    "(": None,
    ")": None
})

ShapeDict = typing.Dict[str, "Shape"]
SHAPES: ShapeDict = {}

jinja_environment = Environment(
    loader=PackageLoader("handler"),
    lstrip_blocks=True,
    trim_blocks=True,
    keep_trailing_newline=True,
    extensions=["jinja2_strcase.StrcaseExtension"],
)


class Member(pydantic.BaseModel):
    shape: str
    ref: typing.Optional["Shape"]
    alias: typing.Optional[str] = None


class Shape(pydantic.BaseModel):
    type: typing.Literal[
        "string",
        "blob",
        "integer",
        "structure",
        "list",
        "boolean",
        "timestamp",
        "double",
        "long",
        "map",
        "float"
    ]

    alias: typing.Optional[str] = None
    members: typing.Dict[str, Member] = pydantic.Field(default_factory=dict)
    member: typing.Dict[str, typing.Any] = pydantic.Field(default_factory=dict)

    documentation: typing.Optional[str]
    exception: bool = False
    synthetic: bool = False
    enum: typing.List[str] = pydantic.Field(default_factory=set)

    # string validation / constraints
    max: typing.Optional[int]
    min: typing.Optional[int]
    pattern: typing.Optional[str]

    @property
    def is_atomic(self):
        return self.type in ATOMIC_TYPES

    @property
    def is_list(self):
        return self.type == "list"


Member.update_forward_refs()


def parse_shapes(service_object):
    for name, shape in service_object["shapes"].items():
        parsed_shape = Shape.parse_obj(shape)
        SHAPES[name] = parsed_shape


def fixup_shape_references():
    for name, shape in SHAPES.items():
        for member, member_shape in shape.members.items():
            if member_shape.shape == "TStamp":
                referenced_shape = "datetime"
            else:
                referenced_shape = SHAPES[member_shape.shape]

            member_shape.ref = referenced_shape


def find_structs(shapes: ShapeDict) -> typing.Iterator[typing.Tuple[str, Shape]]:
    for name, shape in shapes.items():
        if shape.type == "structure" and not shape.exception:
            yield (name, shape)


def find_lists(shapes: ShapeDict) -> typing.Iterator[typing.Tuple[str, Shape]]:
    for name, shape in shapes.items():
        if shape.type == "list":
            yield (name, shape)


def find_atomic_shapes(shapes: ShapeDict) -> typing.Iterator[typing.Tuple[str, Shape]]:
    for name, shape in shapes.items():
        if shape.is_atomic:
            yield (name, shape)


def find_enums(shapes: ShapeDict) -> typing.Iterator[typing.Tuple[str, Shape]]:
    for name, shape in shapes.items():
        if shape.enum:
            yield name, shape


def generate_schema_for_service(filename):
    file_path = os.path.join(WORKING_DIR, filename)

    with open(file_path, "r") as fd:
        service = json.load(fd)
        parse_shapes(service)
        return service


def render_imports(metadata):
    template = jinja_environment.get_template("imports.j2")
    return template.render(metadata=metadata)


def render_atomic(name, shape: Shape):
    template = jinja_environment.get_template("atomic.j2")
    constraints = {}  # "min": shape.min, "max": shape.max, "pattern": }

    if shape.min:
        if shape.type == "string":
            constraints["min_length"] = shape.min
        elif shape.type == "integer":
            constraints["ge"] = shape.min

    if shape.max:
        if shape.type == "string":
            constraints["max_length"] = shape.max
        elif shape.type == "integer":
            constraints["le"] = shape.max

    if shape.pattern:
        constraints["regex"] = f"r'{shape.pattern}'"

    return template.render(
        shape_name=name, type=ATOMIC_MAPPING[shape.type], constraints=constraints
    )


def render_list(name, shape):
    template = jinja_environment.get_template("list.j2")
    # debug(shape)
    return template.render(shape_name=name, **shape.dict())


def render_enum_shape(name: str, shape: Shape):
    template = jinja_environment.get_template("enum.j2")
    members = {}
    
    for member in shape.enum:
        key = member.upper()
        # key = re.sub(r"[-./: ]", "_", key)
        # key = re.sub(r"[()]", "", key)
        key = key.translate(TRANSLATION_TABLE)

        members[key] = member

    return template.render(shape_name=name, members=members)


def fix_member_name(name: str) -> str:
    if name in TOKEN_REPLACEMENTS:
        return TOKEN_REPLACEMENTS[name]

    if keyword.iskeyword(name.lower()):
        return f"{name}_"

    return name


def render_struct_shape(metadata: dict, name: str, shape: Shape):
    template = jinja_environment.get_template("structure.j2")
    members: typing.Dict[str, Member] = {}

    if shape.member:
        debug(shape.member)

    if shape.members:
        for member_name, member_shape in shape.members.items():
            fixup = fix_member_name(member_name)
            members[fixup] = member_shape
            if fixup != member_name:
                members[fixup].alias = member_name

    return template.render(metadata=metadata, shape_name=name, members=members)


def render_update_forward_ref(name: str, shape: Shape):
    template = jinja_environment.get_template("update_ref.j2")
    return template.render(
        shape_name=name,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    ret = generate_schema_for_service(args.filename)
    fixup_shape_references()

    with open(
        os.path.join("aws_schemas", f"{ret['metadata']['endpointPrefix']}.py"), "w"
    ) as fw:
        fw.write(render_imports(ret["metadata"]))
        fw.write("\r\n\r\n")

        for name, shape in find_atomic_shapes(SHAPES):
            fw.write(render_atomic(name, shape))

        fw.write("\r\n")

        for name, shape in find_lists(SHAPES):
            fw.write(render_list(name, shape))

        fw.write("\r\n")

        for name, enum in find_enums(SHAPES):
            fw.write(render_enum_shape(name, enum))
            # break

        for name, struct in find_structs(SHAPES):
            fw.write(render_struct_shape(ret["metadata"], name, struct))

        for name, struct in find_structs(SHAPES):
            fw.write(render_update_forward_ref(name, struct))

    # debug(enums)
    # debug(SHAPES)
    # debug(SHAPES["ServiceErrorMessage"])


if __name__ == "__main__":
    main()
