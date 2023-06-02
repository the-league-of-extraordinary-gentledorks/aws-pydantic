from datetime import datetime
import typing
import enum

import pydantic


class _ACMBase(
    pydantic.BaseModel,
    frozen=True,
    use_enum_values=True,
    allow_population_by_field_name=True,
):
    def dict(self, by_alias=True, **kwargs) -> dict:
        return super().dict(by_alias=True, **kwargs)


Arn: str = pydantic.constr(
    min=20,
    max=2048,
    pattern=r"arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*",
)
AvailabilityErrorMessage: str = pydantic.constr()
CertificateBody: str = pydantic.constr(
    min=1,
    max=32768,
    pattern=r"-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?",
)
CertificateBodyBlob: bytes = pydantic.conbytes(min=1, max=32768)
CertificateChain: str = pydantic.constr(
    min=1,
    max=2097152,
    pattern=r"(-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}\u000D?\u000A)*-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?",
)
CertificateChainBlob: bytes = pydantic.conbytes(min=1, max=2097152)
CertificateStatus: str = pydantic.constr()
CertificateTransparencyLoggingPreference: str = pydantic.constr()
CertificateType: str = pydantic.constr()
DomainNameString: str = pydantic.constr(
    min=1,
    max=253,
    pattern=r"^(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$",
)
DomainStatus: str = pydantic.constr()
ExtendedKeyUsageName: str = pydantic.constr()
FailureReason: str = pydantic.constr()
IdempotencyToken: str = pydantic.constr(min=1, max=32, pattern=r"\w+")
KeyAlgorithm: str = pydantic.constr()
KeyUsageName: str = pydantic.constr()
MaxItems: int = pydantic.conint(min=1, max=1000)
NextToken: str = pydantic.constr(
    min=1, max=10000, pattern=r"[\u0009\u000A\u000D\u0020-\u00FF]*"
)
NullableBoolean: bool = pydantic.conbool()
PassphraseBlob: bytes = pydantic.conbytes(min=4, max=128)
PcaArn: str = pydantic.constr(
    min=20,
    max=2048,
    pattern=r"arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*",
)
PositiveInteger: int = pydantic.conint(min=1)
PrivateKey: str = pydantic.constr(
    min=1,
    max=524288,
    pattern=r"-{5}BEGIN PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END PRIVATE KEY-{5}(\u000D?\u000A)?",
)
PrivateKeyBlob: bytes = pydantic.conbytes(min=1, max=5120)
RecordType: str = pydantic.constr()
RenewalEligibility: str = pydantic.constr()
RenewalStatus: str = pydantic.constr()
RevocationReason: str = pydantic.constr()
ServiceErrorMessage: str = pydantic.constr()
SortBy: str = pydantic.constr()
SortOrder: str = pydantic.constr()
String: str = pydantic.constr()
TStamp: datetime = pydantic.condate()
TagKey: str = pydantic.constr(min=1, max=128, pattern=r"[\p{L}\p{Z}\p{N}_.:\/=+\-@]*")
TagValue: str = pydantic.constr(max=256, pattern=r"[\p{L}\p{Z}\p{N}_.:\/=+\-@]*")
ValidationExceptionMessage: str = pydantic.constr()
ValidationMethod: str = pydantic.constr()

CertificateStatuses = typing.List["CertificateStatus"]
CertificateSummaryList = typing.List["CertificateSummary"]
DomainList = typing.List["DomainNameString"]
DomainValidationList = typing.List["DomainValidation"]
DomainValidationOptionList = typing.List["DomainValidationOption"]
ExtendedKeyUsageFilterList = typing.List["ExtendedKeyUsageName"]
ExtendedKeyUsageList = typing.List["ExtendedKeyUsage"]
ExtendedKeyUsageNames = typing.List["ExtendedKeyUsageName"]
InUseList = typing.List["String"]
KeyAlgorithmList = typing.List["KeyAlgorithm"]
KeyUsageFilterList = typing.List["KeyUsageName"]
KeyUsageList = typing.List["KeyUsage"]
KeyUsageNames = typing.List["KeyUsageName"]
TagList = typing.List["Tag"]
ValidationEmailList = typing.List["String"]


class CertificateStatus(enum.Enum):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"


class CertificateTransparencyLoggingPreference(enum.Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CertificateType(enum.Enum):
    IMPORTED = "IMPORTED"
    AMAZON_ISSUED = "AMAZON_ISSUED"
    PRIVATE = "PRIVATE"


class DomainStatus(enum.Enum):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class ExtendedKeyUsageName(enum.Enum):
    TLS_WEB_SERVER_AUTHENTICATION = "TLS_WEB_SERVER_AUTHENTICATION"
    TLS_WEB_CLIENT_AUTHENTICATION = "TLS_WEB_CLIENT_AUTHENTICATION"
    CODE_SIGNING = "CODE_SIGNING"
    EMAIL_PROTECTION = "EMAIL_PROTECTION"
    TIME_STAMPING = "TIME_STAMPING"
    OCSP_SIGNING = "OCSP_SIGNING"
    IPSEC_END_SYSTEM = "IPSEC_END_SYSTEM"
    IPSEC_TUNNEL = "IPSEC_TUNNEL"
    IPSEC_USER = "IPSEC_USER"
    ANY = "ANY"
    NONE = "NONE"
    CUSTOM = "CUSTOM"


class FailureReason(enum.Enum):
    NO_AVAILABLE_CONTACTS = "NO_AVAILABLE_CONTACTS"
    ADDITIONAL_VERIFICATION_REQUIRED = "ADDITIONAL_VERIFICATION_REQUIRED"
    DOMAIN_NOT_ALLOWED = "DOMAIN_NOT_ALLOWED"
    INVALID_PUBLIC_DOMAIN = "INVALID_PUBLIC_DOMAIN"
    DOMAIN_VALIDATION_DENIED = "DOMAIN_VALIDATION_DENIED"
    CAA_ERROR = "CAA_ERROR"
    PCA_LIMIT_EXCEEDED = "PCA_LIMIT_EXCEEDED"
    PCA_INVALID_ARN = "PCA_INVALID_ARN"
    PCA_INVALID_STATE = "PCA_INVALID_STATE"
    PCA_REQUEST_FAILED = "PCA_REQUEST_FAILED"
    PCA_NAME_CONSTRAINTS_VALIDATION = "PCA_NAME_CONSTRAINTS_VALIDATION"
    PCA_RESOURCE_NOT_FOUND = "PCA_RESOURCE_NOT_FOUND"
    PCA_INVALID_ARGS = "PCA_INVALID_ARGS"
    PCA_INVALID_DURATION = "PCA_INVALID_DURATION"
    PCA_ACCESS_DENIED = "PCA_ACCESS_DENIED"
    SLR_NOT_FOUND = "SLR_NOT_FOUND"
    OTHER = "OTHER"


class KeyAlgorithm(enum.Enum):
    RSA_1024 = "RSA_1024"
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"
    EC_PRIME256V1 = "EC_prime256v1"
    EC_SECP384R1 = "EC_secp384r1"
    EC_SECP521R1 = "EC_secp521r1"


class KeyUsageName(enum.Enum):
    DIGITAL_SIGNATURE = "DIGITAL_SIGNATURE"
    NON_REPUDIATION = "NON_REPUDIATION"
    KEY_ENCIPHERMENT = "KEY_ENCIPHERMENT"
    DATA_ENCIPHERMENT = "DATA_ENCIPHERMENT"
    KEY_AGREEMENT = "KEY_AGREEMENT"
    CERTIFICATE_SIGNING = "CERTIFICATE_SIGNING"
    CRL_SIGNING = "CRL_SIGNING"
    ENCIPHER_ONLY = "ENCIPHER_ONLY"
    DECIPHER_ONLY = "DECIPHER_ONLY"
    ANY = "ANY"
    CUSTOM = "CUSTOM"


class RecordType(enum.Enum):
    CNAME = "CNAME"


class RenewalEligibility(enum.Enum):
    ELIGIBLE = "ELIGIBLE"
    INELIGIBLE = "INELIGIBLE"


class RenewalStatus(enum.Enum):
    PENDING_AUTO_RENEWAL = "PENDING_AUTO_RENEWAL"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class RevocationReason(enum.Enum):
    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CA_COMPROMISE = "CA_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERCEDED = "SUPERCEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    CERTIFICATE_HOLD = "CERTIFICATE_HOLD"
    REMOVE_FROM_CRL = "REMOVE_FROM_CRL"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


class SortBy(enum.Enum):
    CREATED_AT = "CREATED_AT"


class SortOrder(enum.Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ValidationMethod(enum.Enum):
    EMAIL = "EMAIL"
    DNS = "DNS"


class AddTagsToCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    tags: TagList = pydantic.Field(None, alias="Tags")


class CertificateDetail(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    domain_name: DomainNameString = pydantic.Field(None, alias="DomainName")
    subject_alternative_names: DomainList = pydantic.Field(
        None, alias="SubjectAlternativeNames"
    )
    domain_validation_options: DomainValidationList = pydantic.Field(
        None, alias="DomainValidationOptions"
    )
    serial: String = pydantic.Field(None, alias="Serial")
    subject: String = pydantic.Field(None, alias="Subject")
    issuer: String = pydantic.Field(None, alias="Issuer")
    created_at: "TStamp" = pydantic.Field(None, alias="CreatedAt")
    issued_at: "TStamp" = pydantic.Field(None, alias="IssuedAt")
    imported_at: "TStamp" = pydantic.Field(None, alias="ImportedAt")
    status: CertificateStatus = pydantic.Field(None, alias="Status")
    revoked_at: "TStamp" = pydantic.Field(None, alias="RevokedAt")
    revocation_reason: RevocationReason = pydantic.Field(None, alias="RevocationReason")
    not_before: "TStamp" = pydantic.Field(None, alias="NotBefore")
    not_after: "TStamp" = pydantic.Field(None, alias="NotAfter")
    key_algorithm: KeyAlgorithm = pydantic.Field(None, alias="KeyAlgorithm")
    signature_algorithm: String = pydantic.Field(None, alias="SignatureAlgorithm")
    in_use_by: InUseList = pydantic.Field(None, alias="InUseBy")
    failure_reason: FailureReason = pydantic.Field(None, alias="FailureReason")
    type: CertificateType = pydantic.Field(None, alias="Type")
    renewal_summary: "RenewalSummary" = pydantic.Field(None, alias="RenewalSummary")
    key_usages: KeyUsageList = pydantic.Field(None, alias="KeyUsages")
    extended_key_usages: ExtendedKeyUsageList = pydantic.Field(
        None, alias="ExtendedKeyUsages"
    )
    certificate_authority_arn: Arn = pydantic.Field(
        None, alias="CertificateAuthorityArn"
    )
    renewal_eligibility: RenewalEligibility = pydantic.Field(
        None, alias="RenewalEligibility"
    )
    options: "CertificateOptions" = pydantic.Field(None, alias="Options")


class CertificateOptions(_ACMBase):
    certificate_transparency_logging_preference: CertificateTransparencyLoggingPreference = pydantic.Field(
        None, alias="CertificateTransparencyLoggingPreference"
    )


class CertificateSummary(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    domain_name: DomainNameString = pydantic.Field(None, alias="DomainName")
    subject_alternative_name_summaries: DomainList = pydantic.Field(
        None, alias="SubjectAlternativeNameSummaries"
    )
    has_additional_subject_alternative_names: NullableBoolean = pydantic.Field(
        None, alias="HasAdditionalSubjectAlternativeNames"
    )
    status: CertificateStatus = pydantic.Field(None, alias="Status")
    type: CertificateType = pydantic.Field(None, alias="Type")
    key_algorithm: KeyAlgorithm = pydantic.Field(None, alias="KeyAlgorithm")
    key_usages: KeyUsageNames = pydantic.Field(None, alias="KeyUsages")
    extended_key_usages: ExtendedKeyUsageNames = pydantic.Field(
        None, alias="ExtendedKeyUsages"
    )
    in_use: NullableBoolean = pydantic.Field(None, alias="InUse")
    exported: NullableBoolean = pydantic.Field(None, alias="Exported")
    renewal_eligibility: RenewalEligibility = pydantic.Field(
        None, alias="RenewalEligibility"
    )
    not_before: "TStamp" = pydantic.Field(None, alias="NotBefore")
    not_after: "TStamp" = pydantic.Field(None, alias="NotAfter")
    created_at: "TStamp" = pydantic.Field(None, alias="CreatedAt")
    issued_at: "TStamp" = pydantic.Field(None, alias="IssuedAt")
    imported_at: "TStamp" = pydantic.Field(None, alias="ImportedAt")
    revoked_at: "TStamp" = pydantic.Field(None, alias="RevokedAt")


class DeleteCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class DescribeCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class DescribeCertificateResponse(_ACMBase):
    certificate: "CertificateDetail" = pydantic.Field(None, alias="Certificate")


class DomainValidation(_ACMBase):
    domain_name: DomainNameString = pydantic.Field(None, alias="DomainName")
    validation_emails: ValidationEmailList = pydantic.Field(
        None, alias="ValidationEmails"
    )
    validation_domain: DomainNameString = pydantic.Field(None, alias="ValidationDomain")
    validation_status: DomainStatus = pydantic.Field(None, alias="ValidationStatus")
    resource_record: "ResourceRecord" = pydantic.Field(None, alias="ResourceRecord")
    validation_method: ValidationMethod = pydantic.Field(None, alias="ValidationMethod")


class DomainValidationOption(_ACMBase):
    domain_name: DomainNameString = pydantic.Field(None, alias="DomainName")
    validation_domain: DomainNameString = pydantic.Field(None, alias="ValidationDomain")


class ExpiryEventsConfiguration(_ACMBase):
    days_before_expiry: PositiveInteger = pydantic.Field(None, alias="DaysBeforeExpiry")


class ExportCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    passphrase: PassphraseBlob = pydantic.Field(None, alias="Passphrase")


class ExportCertificateResponse(_ACMBase):
    certificate: CertificateBody = pydantic.Field(None, alias="Certificate")
    certificate_chain: CertificateChain = pydantic.Field(None, alias="CertificateChain")
    private_key: PrivateKey = pydantic.Field(None, alias="PrivateKey")


class ExtendedKeyUsage(_ACMBase):
    name: ExtendedKeyUsageName = pydantic.Field(None, alias="Name")
    oid: String = pydantic.Field(None, alias="OID")


class Filters(_ACMBase):
    extended_key_usage: ExtendedKeyUsageFilterList = pydantic.Field(
        None, alias="extendedKeyUsage"
    )
    key_usage: KeyUsageFilterList = pydantic.Field(None, alias="keyUsage")
    key_types: KeyAlgorithmList = pydantic.Field(None, alias="keyTypes")


class GetAccountConfigurationResponse(_ACMBase):
    expiry_events: "ExpiryEventsConfiguration" = pydantic.Field(
        None, alias="ExpiryEvents"
    )


class GetCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class GetCertificateResponse(_ACMBase):
    certificate: CertificateBody = pydantic.Field(None, alias="Certificate")
    certificate_chain: CertificateChain = pydantic.Field(None, alias="CertificateChain")


class ImportCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    certificate: CertificateBodyBlob = pydantic.Field(None, alias="Certificate")
    private_key: PrivateKeyBlob = pydantic.Field(None, alias="PrivateKey")
    certificate_chain: CertificateChainBlob = pydantic.Field(
        None, alias="CertificateChain"
    )
    tags: TagList = pydantic.Field(None, alias="Tags")


class ImportCertificateResponse(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class KeyUsage(_ACMBase):
    name: KeyUsageName = pydantic.Field(None, alias="Name")


class ListCertificatesRequest(_ACMBase):
    certificate_statuses: CertificateStatuses = pydantic.Field(
        None, alias="CertificateStatuses"
    )
    includes: "Filters" = pydantic.Field(None, alias="Includes")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_items: MaxItems = pydantic.Field(None, alias="MaxItems")
    sort_by: SortBy = pydantic.Field(None, alias="SortBy")
    sort_order: SortOrder = pydantic.Field(None, alias="SortOrder")


class ListCertificatesResponse(_ACMBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    certificate_summary_list: CertificateSummaryList = pydantic.Field(
        None, alias="CertificateSummaryList"
    )


class ListTagsForCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class ListTagsForCertificateResponse(_ACMBase):
    tags: TagList = pydantic.Field(None, alias="Tags")


class PutAccountConfigurationRequest(_ACMBase):
    expiry_events: "ExpiryEventsConfiguration" = pydantic.Field(
        None, alias="ExpiryEvents"
    )
    idempotency_token: IdempotencyToken = pydantic.Field(None, alias="IdempotencyToken")


class RemoveTagsFromCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    tags: TagList = pydantic.Field(None, alias="Tags")


class RenewCertificateRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class RenewalSummary(_ACMBase):
    renewal_status: RenewalStatus = pydantic.Field(None, alias="RenewalStatus")
    domain_validation_options: DomainValidationList = pydantic.Field(
        None, alias="DomainValidationOptions"
    )
    renewal_status_reason: FailureReason = pydantic.Field(
        None, alias="RenewalStatusReason"
    )
    updated_at: "TStamp" = pydantic.Field(None, alias="UpdatedAt")


class RequestCertificateRequest(_ACMBase):
    domain_name: DomainNameString = pydantic.Field(None, alias="DomainName")
    validation_method: ValidationMethod = pydantic.Field(None, alias="ValidationMethod")
    subject_alternative_names: DomainList = pydantic.Field(
        None, alias="SubjectAlternativeNames"
    )
    idempotency_token: IdempotencyToken = pydantic.Field(None, alias="IdempotencyToken")
    domain_validation_options: DomainValidationOptionList = pydantic.Field(
        None, alias="DomainValidationOptions"
    )
    options: "CertificateOptions" = pydantic.Field(None, alias="Options")
    certificate_authority_arn: PcaArn = pydantic.Field(
        None, alias="CertificateAuthorityArn"
    )
    tags: TagList = pydantic.Field(None, alias="Tags")
    key_algorithm: KeyAlgorithm = pydantic.Field(None, alias="KeyAlgorithm")


class RequestCertificateResponse(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")


class ResendValidationEmailRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    domain: DomainNameString = pydantic.Field(None, alias="Domain")
    validation_domain: DomainNameString = pydantic.Field(None, alias="ValidationDomain")


class ResourceRecord(_ACMBase):
    name: String = pydantic.Field(None, alias="Name")
    type: RecordType = pydantic.Field(None, alias="Type")
    value: String = pydantic.Field(None, alias="Value")


class Tag(_ACMBase):
    key: TagKey = pydantic.Field(None, alias="Key")
    value: TagValue = pydantic.Field(None, alias="Value")


class UpdateCertificateOptionsRequest(_ACMBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")
    options: "CertificateOptions" = pydantic.Field(None, alias="Options")


AddTagsToCertificateRequest.update_forward_refs()
CertificateDetail.update_forward_refs()
CertificateOptions.update_forward_refs()
CertificateSummary.update_forward_refs()
DeleteCertificateRequest.update_forward_refs()
DescribeCertificateRequest.update_forward_refs()
DescribeCertificateResponse.update_forward_refs()
DomainValidation.update_forward_refs()
DomainValidationOption.update_forward_refs()
ExpiryEventsConfiguration.update_forward_refs()
ExportCertificateRequest.update_forward_refs()
ExportCertificateResponse.update_forward_refs()
ExtendedKeyUsage.update_forward_refs()
Filters.update_forward_refs()
GetAccountConfigurationResponse.update_forward_refs()
GetCertificateRequest.update_forward_refs()
GetCertificateResponse.update_forward_refs()
ImportCertificateRequest.update_forward_refs()
ImportCertificateResponse.update_forward_refs()
KeyUsage.update_forward_refs()
ListCertificatesRequest.update_forward_refs()
ListCertificatesResponse.update_forward_refs()
ListTagsForCertificateRequest.update_forward_refs()
ListTagsForCertificateResponse.update_forward_refs()
PutAccountConfigurationRequest.update_forward_refs()
RemoveTagsFromCertificateRequest.update_forward_refs()
RenewCertificateRequest.update_forward_refs()
RenewalSummary.update_forward_refs()
RequestCertificateRequest.update_forward_refs()
RequestCertificateResponse.update_forward_refs()
ResendValidationEmailRequest.update_forward_refs()
ResourceRecord.update_forward_refs()
Tag.update_forward_refs()
UpdateCertificateOptionsRequest.update_forward_refs()
