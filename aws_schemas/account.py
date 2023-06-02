from datetime import datetime
import typing
import enum

import pydantic


class _AccountBase(
    pydantic.BaseModel,
    frozen=True,
    use_enum_values=True,
    allow_population_by_field_name=True,
):
    def dict(self, by_alias=True, **kwargs) -> dict:
        return super().dict(by_alias=True, **kwargs)


AccountId: str = pydantic.constr(pattern=r"^\d{12}$")
AddressLine: str = pydantic.constr(min=1, max=60)
AlternateContactType: str = pydantic.constr()
City: str = pydantic.constr(min=1, max=50)
CompanyName: str = pydantic.constr(min=1, max=50)
ContactInformationPhoneNumber: str = pydantic.constr(
    min=1, max=20, pattern=r"^[+][\s0-9()-]+$"
)
CountryCode: str = pydantic.constr(min=2, max=2)
DistrictOrCounty: str = pydantic.constr(min=1, max=50)
EmailAddress: str = pydantic.constr(
    min=1, max=254, pattern=r"^[\s]*[\w+=.#|!&-]+@[\w.-]+\.[\w]+[\s]*$"
)
FullName: str = pydantic.constr(min=1, max=50)
ListRegionsRequestMaxResultsInteger: int = pydantic.conint(min=1, max=50)
ListRegionsRequestNextTokenString: str = pydantic.constr(max=1000)
Name: str = pydantic.constr(min=1, max=64)
PhoneNumber: str = pydantic.constr(min=1, max=25, pattern=r"^[\s0-9()+-]+$")
PostalCode: str = pydantic.constr(min=1, max=20)
RegionName: str = pydantic.constr(min=1, max=50)
RegionOptStatus: str = pydantic.constr()
SensitiveString: str = pydantic.constr()
StateOrRegion: str = pydantic.constr(min=1, max=50)
String: str = pydantic.constr()
Title: str = pydantic.constr(min=1, max=50)
ValidationExceptionReason: str = pydantic.constr()
WebsiteUrl: str = pydantic.constr(min=1, max=256)

RegionOptList = typing.List["Region"]
RegionOptStatusList = typing.List["RegionOptStatus"]
ValidationExceptionFieldList = typing.List["ValidationExceptionField"]


class AlternateContactType(enum.Enum):
    BILLING = "BILLING"
    OPERATIONS = "OPERATIONS"
    SECURITY = "SECURITY"


class RegionOptStatus(enum.Enum):
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    ENABLED_BY_DEFAULT = "ENABLED_BY_DEFAULT"


class ValidationExceptionReason(enum.Enum):
    INVALIDREGIONOPTTARGET = "invalidRegionOptTarget"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"


class AlternateContact(_AccountBase):
    alternate_contact_type: AlternateContactType = pydantic.Field(
        None, alias="AlternateContactType"
    )
    email_address: EmailAddress = pydantic.Field(None, alias="EmailAddress")
    name: Name = pydantic.Field(None, alias="Name")
    phone_number: PhoneNumber = pydantic.Field(None, alias="PhoneNumber")
    title: Title = pydantic.Field(None, alias="Title")


class ContactInformation(_AccountBase):
    address_line_1: AddressLine = pydantic.Field(None, alias="AddressLine1")
    address_line_2: AddressLine = pydantic.Field(None, alias="AddressLine2")
    address_line_3: AddressLine = pydantic.Field(None, alias="AddressLine3")
    city: City = pydantic.Field(None, alias="City")
    company_name: CompanyName = pydantic.Field(None, alias="CompanyName")
    country_code: CountryCode = pydantic.Field(None, alias="CountryCode")
    district_or_county: DistrictOrCounty = pydantic.Field(
        None, alias="DistrictOrCounty"
    )
    full_name: FullName = pydantic.Field(None, alias="FullName")
    phone_number: ContactInformationPhoneNumber = pydantic.Field(
        None, alias="PhoneNumber"
    )
    postal_code: PostalCode = pydantic.Field(None, alias="PostalCode")
    state_or_region: StateOrRegion = pydantic.Field(None, alias="StateOrRegion")
    website_url: WebsiteUrl = pydantic.Field(None, alias="WebsiteUrl")


class DeleteAlternateContactRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    alternate_contact_type: AlternateContactType = pydantic.Field(
        None, alias="AlternateContactType"
    )


class DisableRegionRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    region_name: RegionName = pydantic.Field(None, alias="RegionName")


class EnableRegionRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    region_name: RegionName = pydantic.Field(None, alias="RegionName")


class GetAlternateContactRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    alternate_contact_type: AlternateContactType = pydantic.Field(
        None, alias="AlternateContactType"
    )


class GetAlternateContactResponse(_AccountBase):
    alternate_contact: "AlternateContact" = pydantic.Field(
        None, alias="AlternateContact"
    )


class GetContactInformationRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")


class GetContactInformationResponse(_AccountBase):
    contact_information: "ContactInformation" = pydantic.Field(
        None, alias="ContactInformation"
    )


class GetRegionOptStatusRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    region_name: RegionName = pydantic.Field(None, alias="RegionName")


class GetRegionOptStatusResponse(_AccountBase):
    region_name: RegionName = pydantic.Field(None, alias="RegionName")
    region_opt_status: RegionOptStatus = pydantic.Field(None, alias="RegionOptStatus")


class ListRegionsRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    max_results: ListRegionsRequestMaxResultsInteger = pydantic.Field(
        None, alias="MaxResults"
    )
    next_token: ListRegionsRequestNextTokenString = pydantic.Field(
        None, alias="NextToken"
    )
    region_opt_status_contains: RegionOptStatusList = pydantic.Field(
        None, alias="RegionOptStatusContains"
    )


class ListRegionsResponse(_AccountBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    regions: RegionOptList = pydantic.Field(None, alias="Regions")


class PutAlternateContactRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    alternate_contact_type: AlternateContactType = pydantic.Field(
        None, alias="AlternateContactType"
    )
    email_address: EmailAddress = pydantic.Field(None, alias="EmailAddress")
    name: Name = pydantic.Field(None, alias="Name")
    phone_number: PhoneNumber = pydantic.Field(None, alias="PhoneNumber")
    title: Title = pydantic.Field(None, alias="Title")


class PutContactInformationRequest(_AccountBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    contact_information: "ContactInformation" = pydantic.Field(
        None, alias="ContactInformation"
    )


class Region(_AccountBase):
    region_name: RegionName = pydantic.Field(None, alias="RegionName")
    region_opt_status: RegionOptStatus = pydantic.Field(None, alias="RegionOptStatus")


class ValidationExceptionField(_AccountBase):
    message: SensitiveString = pydantic.Field(None, alias="message")
    name: String = pydantic.Field(None, alias="name")


AlternateContact.update_forward_refs()
ContactInformation.update_forward_refs()
DeleteAlternateContactRequest.update_forward_refs()
DisableRegionRequest.update_forward_refs()
EnableRegionRequest.update_forward_refs()
GetAlternateContactRequest.update_forward_refs()
GetAlternateContactResponse.update_forward_refs()
GetContactInformationRequest.update_forward_refs()
GetContactInformationResponse.update_forward_refs()
GetRegionOptStatusRequest.update_forward_refs()
GetRegionOptStatusResponse.update_forward_refs()
ListRegionsRequest.update_forward_refs()
ListRegionsResponse.update_forward_refs()
PutAlternateContactRequest.update_forward_refs()
PutContactInformationRequest.update_forward_refs()
Region.update_forward_refs()
ValidationExceptionField.update_forward_refs()