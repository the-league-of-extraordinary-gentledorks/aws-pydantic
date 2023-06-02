import argparse
import os
import json
import keyword
import typing

from jinja2 import Environment, PackageLoader, select_autoescape
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
}

ShapeDict = typing.Dict[str, "Shape"]
SHAPES: ShapeDict = {}

STRUCTURES: dict = {}

env = Environment(
    loader=PackageLoader("handler"),
    # autoescape=select_autoescape(),
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
    ]

    alias: typing.Optional[str] = None
    members: typing.Dict[str, Member] = pydantic.Field(default_factory=dict)
    member: typing.Dict[str, typing.Any] = pydantic.Field(default_factory=dict)

    documentation: typing.Optional[str]
    exception: bool = False
    synthetic: bool = False
    enum: typing.List[str] = pydantic.Field(default_factory=set)

    # string validation
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
        # debug(name, shape)
        for member, shape in shape.members.items():
            if shape.shape == "TStamp":
                referenced_shape = "datetime"
            else:
                referenced_shape = SHAPES[shape.shape]
            shape.ref = referenced_shape


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


def get_service_object(file_obj):
    return json.load(file_obj)


def generate_schema_for_service(filename):
    file_path = os.path.join(WORKING_DIR, filename)

    with open(file_path, "r") as fd:
        service = get_service_object(fd)
        parse_shapes(service)
        return service


def render_imports(metadata):
    template = env.get_template("imports.j2")
    return template.render(metadata=metadata)


def render_atomic(name, shape):
    template = env.get_template("atomic.j2")
    constraints = {}  # "min": shape.min, "max": shape.max, "pattern": }
    if shape.min:
        constraints["min"] = shape.min

    if shape.max:
        constraints["max"] = shape.max

    if shape.pattern:
        constraints["pattern"] = f"r'{shape.pattern}'"

    return template.render(
        shape_name=name, type=ATOMIC_MAPPING[shape.type], constraints=constraints
    )


def render_list(name, shape):
    template = env.get_template("list.j2")
    # debug(shape)
    return template.render(shape_name=name, **shape.dict())


def render_enum_shape(name: str, shape: Shape):
    template = env.get_template("enum.j2")
    members = {}
    for member in shape.enum:
        key = member.upper()
        key = key.replace("-", "_")
        key = key.replace(".", "_")
        key = key.replace("/", "_")
        members[key] = member

    return template.render(shape_name=name, members=members)


def fix_member_name(name: str) -> str:
    if name in TOKEN_REPLACEMENTS:
        return TOKEN_REPLACEMENTS[name]

    if keyword.iskeyword(name.lower()):
        return f"{name}_"

    return name


def render_struct_shape(metadata: dict, name: str, shape: Shape):
    template = env.get_template("structure.j2")
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
    template = env.get_template("update_ref.j2")
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
