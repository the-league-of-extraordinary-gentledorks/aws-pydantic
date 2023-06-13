from datetime import datetime
import typing
import enum

import pydantic


class _ACMPCAModelBase(pydantic.BaseModel, frozen=True, use_enum_values=True, allow_population_by_field_name=True, extra=pydantic.Extra.allow):
    def dict(self, by_alias=True, **kwargs) -> dict:
        return super().dict(by_alias=True, **kwargs)
    
    def json(self, by_alias=True, **kwargs) -> dict:
        return super().json(by_alias=True, **kwargs)

ASN1PrintableString64: str = pydantic.constr(max_length=64, regex=r'[a-zA-Z0-9\'()+-.?:/= ]*')
AWSPolicy: str = pydantic.constr(min_length=1, max_length=20480, regex=r'[\u0009\u000A\u000D\u0020-\u00FF]+')
AccessMethodType: str = pydantic.constr()
AccountId: str = pydantic.constr(min_length=12, max_length=12, regex=r'[0-9]+')
ActionType: str = pydantic.constr()
Arn: str = pydantic.constr(min_length=5, max_length=200, regex=r'arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*')
AuditReportId: str = pydantic.constr(min_length=36, max_length=36, regex=r'[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')
AuditReportResponseFormat: str = pydantic.constr()
AuditReportStatus: str = pydantic.constr()
Base64String1To4096: str = pydantic.constr(min_length=1, max_length=4096, regex=r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
Boolean: bool = pydantic.conbool()
CertificateAuthorityStatus: str = pydantic.constr()
CertificateAuthorityType: str = pydantic.constr()
CertificateAuthorityUsageMode: str = pydantic.constr()
CertificateBody: str = pydantic.constr()
CertificateBodyBlob: bytes = pydantic.conbytes()
CertificateChain: str = pydantic.constr()
CertificateChainBlob: bytes = pydantic.conbytes()
CnameString: str = pydantic.constr(max_length=253, regex=r'^[-a-zA-Z0-9;/?:@&=+$,%_.!~*()\']*$')
CountryCodeString: str = pydantic.constr(min_length=2, max_length=2, regex=r'[A-Za-z]{2}')
CsrBlob: bytes = pydantic.conbytes()
CsrBody: str = pydantic.constr()
CustomObjectIdentifier: str = pydantic.constr(max_length=64, regex=r'^([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})$')
ExtendedKeyUsageType: str = pydantic.constr()
FailureReason: str = pydantic.constr()
IdempotencyToken: str = pydantic.constr(min_length=1, max_length=36, regex=r'[\u0009\u000A\u000D\u0020-\u00FF]*')
Integer1To5000: int = pydantic.conint(ge=1, le=5000)
KeyAlgorithm: str = pydantic.constr()
KeyStorageSecurityStandard: str = pydantic.constr()
MaxResults: int = pydantic.conint(ge=1, le=1000)
NextToken: str = pydantic.constr(min_length=1, max_length=500)
PermanentDeletionTimeInDays: int = pydantic.conint(ge=7, le=30)
PolicyQualifierId: str = pydantic.constr()
PositiveLong: int = pydantic.conint()
Principal: str = pydantic.constr(max_length=128, regex=r'^[^*]+$')
ResourceOwner: str = pydantic.constr()
RevocationReason: str = pydantic.constr()
S3BucketName: str = pydantic.constr(min_length=3, max_length=63)
S3BucketName3To255: str = pydantic.constr(min_length=3, max_length=255, regex=r'^[-a-zA-Z0-9._/]+$')
S3Key: str = pydantic.constr(max_length=1024)
S3ObjectAcl: str = pydantic.constr()
SigningAlgorithm: str = pydantic.constr()
String: str = pydantic.constr()
String128: str = pydantic.constr(max_length=128)
String16: str = pydantic.constr(max_length=16)
String1To256: str = pydantic.constr(min_length=1, max_length=256)
String253: str = pydantic.constr(max_length=253)
String256: str = pydantic.constr(max_length=256)
String3: str = pydantic.constr(max_length=3)
String39: str = pydantic.constr(max_length=39)
String40: str = pydantic.constr(max_length=40)
String5: str = pydantic.constr(max_length=5)
String64: str = pydantic.constr(max_length=64)
TStamp: datetime = pydantic.condate()
TagKey: str = pydantic.constr(min_length=1, max_length=128, regex=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$')
TagValue: str = pydantic.constr(max_length=256, regex=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$')
ValidityPeriodType: str = pydantic.constr()

AccessDescriptionList = typing.List["AccessDescription"]
ActionList = typing.List["ActionType"]
CertificateAuthorities = typing.List["CertificateAuthority"]
CertificatePolicyList = typing.List["PolicyInformation"]
CustomAttributeList = typing.List["CustomAttribute"]
CustomExtensionList = typing.List["CustomExtension"]
ExtendedKeyUsageList = typing.List["ExtendedKeyUsage"]
GeneralNameList = typing.List["GeneralName"]
PermissionList = typing.List["Permission"]
PolicyQualifierInfoList = typing.List["PolicyQualifierInfo"]
TagList = typing.List["Tag"]

class AccessMethodType(enum.Enum):
    CA_REPOSITORY = 'CA_REPOSITORY'
    RESOURCE_PKI_MANIFEST = 'RESOURCE_PKI_MANIFEST'
    RESOURCE_PKI_NOTIFY = 'RESOURCE_PKI_NOTIFY'

class ActionType(enum.Enum):
    ISSUECERTIFICATE = 'IssueCertificate'
    GETCERTIFICATE = 'GetCertificate'
    LISTPERMISSIONS = 'ListPermissions'

class AuditReportResponseFormat(enum.Enum):
    JSON = 'JSON'
    CSV = 'CSV'

class AuditReportStatus(enum.Enum):
    CREATING = 'CREATING'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'

class CertificateAuthorityStatus(enum.Enum):
    CREATING = 'CREATING'
    PENDING_CERTIFICATE = 'PENDING_CERTIFICATE'
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    DISABLED = 'DISABLED'
    EXPIRED = 'EXPIRED'
    FAILED = 'FAILED'

class CertificateAuthorityType(enum.Enum):
    ROOT = 'ROOT'
    SUBORDINATE = 'SUBORDINATE'

class CertificateAuthorityUsageMode(enum.Enum):
    GENERAL_PURPOSE = 'GENERAL_PURPOSE'
    SHORT_LIVED_CERTIFICATE = 'SHORT_LIVED_CERTIFICATE'

class ExtendedKeyUsageType(enum.Enum):
    SERVER_AUTH = 'SERVER_AUTH'
    CLIENT_AUTH = 'CLIENT_AUTH'
    CODE_SIGNING = 'CODE_SIGNING'
    EMAIL_PROTECTION = 'EMAIL_PROTECTION'
    TIME_STAMPING = 'TIME_STAMPING'
    OCSP_SIGNING = 'OCSP_SIGNING'
    SMART_CARD_LOGIN = 'SMART_CARD_LOGIN'
    DOCUMENT_SIGNING = 'DOCUMENT_SIGNING'
    CERTIFICATE_TRANSPARENCY = 'CERTIFICATE_TRANSPARENCY'

class FailureReason(enum.Enum):
    REQUEST_TIMED_OUT = 'REQUEST_TIMED_OUT'
    UNSUPPORTED_ALGORITHM = 'UNSUPPORTED_ALGORITHM'
    OTHER = 'OTHER'

class KeyAlgorithm(enum.Enum):
    RSA_2048 = 'RSA_2048'
    RSA_4096 = 'RSA_4096'
    EC_PRIME256V1 = 'EC_prime256v1'
    EC_SECP384R1 = 'EC_secp384r1'

class KeyStorageSecurityStandard(enum.Enum):
    FIPS_140_2_LEVEL_2_OR_HIGHER = 'FIPS_140_2_LEVEL_2_OR_HIGHER'
    FIPS_140_2_LEVEL_3_OR_HIGHER = 'FIPS_140_2_LEVEL_3_OR_HIGHER'

class PolicyQualifierId(enum.Enum):
    CPS = 'CPS'

class ResourceOwner(enum.Enum):
    SELF = 'SELF'
    OTHER_ACCOUNTS = 'OTHER_ACCOUNTS'

class RevocationReason(enum.Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    KEY_COMPROMISE = 'KEY_COMPROMISE'
    CERTIFICATE_AUTHORITY_COMPROMISE = 'CERTIFICATE_AUTHORITY_COMPROMISE'
    AFFILIATION_CHANGED = 'AFFILIATION_CHANGED'
    SUPERSEDED = 'SUPERSEDED'
    CESSATION_OF_OPERATION = 'CESSATION_OF_OPERATION'
    PRIVILEGE_WITHDRAWN = 'PRIVILEGE_WITHDRAWN'
    A_A_COMPROMISE = 'A_A_COMPROMISE'

class S3ObjectAcl(enum.Enum):
    PUBLIC_READ = 'PUBLIC_READ'
    BUCKET_OWNER_FULL_CONTROL = 'BUCKET_OWNER_FULL_CONTROL'

class SigningAlgorithm(enum.Enum):
    SHA256WITHECDSA = 'SHA256WITHECDSA'
    SHA384WITHECDSA = 'SHA384WITHECDSA'
    SHA512WITHECDSA = 'SHA512WITHECDSA'
    SHA256WITHRSA = 'SHA256WITHRSA'
    SHA384WITHRSA = 'SHA384WITHRSA'
    SHA512WITHRSA = 'SHA512WITHRSA'

class ValidityPeriodType(enum.Enum):
    END_DATE = 'END_DATE'
    ABSOLUTE = 'ABSOLUTE'
    DAYS = 'DAYS'
    MONTHS = 'MONTHS'
    YEARS = 'YEARS'

class ASN1Subject(_ACMPCAModelBase):
    country: CountryCodeString = pydantic.Field(None, alias="Country")
    organization: String64 = pydantic.Field(None, alias="Organization")
    organizational_unit: String64 = pydantic.Field(None, alias="OrganizationalUnit")
    distinguished_name_qualifier: ASN1PrintableString64 = pydantic.Field(None, alias="DistinguishedNameQualifier")
    state: String128 = pydantic.Field(None, alias="State")
    common_name: String64 = pydantic.Field(None, alias="CommonName")
    serial_number: ASN1PrintableString64 = pydantic.Field(None, alias="SerialNumber")
    locality: String128 = pydantic.Field(None, alias="Locality")
    title: String64 = pydantic.Field(None, alias="Title")
    surname: String40 = pydantic.Field(None, alias="Surname")
    given_name: String16 = pydantic.Field(None, alias="GivenName")
    initials: String5 = pydantic.Field(None, alias="Initials")
    pseudonym: String128 = pydantic.Field(None, alias="Pseudonym")
    generation_qualifier: String3 = pydantic.Field(None, alias="GenerationQualifier")
    custom_attributes: CustomAttributeList = pydantic.Field(None, alias="CustomAttributes")

class AccessDescription(_ACMPCAModelBase):
    access_method: 'AccessMethod' = pydantic.Field(None, alias="AccessMethod")
    access_location: 'GeneralName' = pydantic.Field(None, alias="AccessLocation")

class AccessMethod(_ACMPCAModelBase):
    custom_object_identifier: CustomObjectIdentifier = pydantic.Field(None, alias="CustomObjectIdentifier")
    access_method_type: AccessMethodType = pydantic.Field(None, alias="AccessMethodType")

class ApiPassthrough(_ACMPCAModelBase):
    extensions: 'Extensions' = pydantic.Field(None, alias="Extensions")
    subject: 'ASN1Subject' = pydantic.Field(None, alias="Subject")

class CertificateAuthority(_ACMPCAModelBase):
    arn: Arn = pydantic.Field(None, alias="Arn")
    owner_account: AccountId = pydantic.Field(None, alias="OwnerAccount")
    created_at: 'TStamp' = pydantic.Field(None, alias="CreatedAt")
    last_state_change_at: 'TStamp' = pydantic.Field(None, alias="LastStateChangeAt")
    type: CertificateAuthorityType = pydantic.Field(None, alias="Type")
    serial: String = pydantic.Field(None, alias="Serial")
    status: CertificateAuthorityStatus = pydantic.Field(None, alias="Status")
    not_before: 'TStamp' = pydantic.Field(None, alias="NotBefore")
    not_after: 'TStamp' = pydantic.Field(None, alias="NotAfter")
    failure_reason: FailureReason = pydantic.Field(None, alias="FailureReason")
    certificate_authority_configuration: 'CertificateAuthorityConfiguration' = pydantic.Field(None, alias="CertificateAuthorityConfiguration")
    revocation_configuration: 'RevocationConfiguration' = pydantic.Field(None, alias="RevocationConfiguration")
    restorable_until: 'TStamp' = pydantic.Field(None, alias="RestorableUntil")
    key_storage_security_standard: KeyStorageSecurityStandard = pydantic.Field(None, alias="KeyStorageSecurityStandard")
    usage_mode: CertificateAuthorityUsageMode = pydantic.Field(None, alias="UsageMode")

class CertificateAuthorityConfiguration(_ACMPCAModelBase):
    key_algorithm: KeyAlgorithm = pydantic.Field(None, alias="KeyAlgorithm")
    signing_algorithm: SigningAlgorithm = pydantic.Field(None, alias="SigningAlgorithm")
    subject: 'ASN1Subject' = pydantic.Field(None, alias="Subject")
    csr_extensions: 'CsrExtensions' = pydantic.Field(None, alias="CsrExtensions")

class CreateCertificateAuthorityAuditReportRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    s_3_bucket_name: S3BucketName = pydantic.Field(None, alias="S3BucketName")
    audit_report_response_format: AuditReportResponseFormat = pydantic.Field(None, alias="AuditReportResponseFormat")

class CreateCertificateAuthorityAuditReportResponse(_ACMPCAModelBase):
    audit_report_id: AuditReportId = pydantic.Field(None, alias="AuditReportId")
    s_3_key: S3Key = pydantic.Field(None, alias="S3Key")

class CreateCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_configuration: 'CertificateAuthorityConfiguration' = pydantic.Field(None, alias="CertificateAuthorityConfiguration")
    revocation_configuration: 'RevocationConfiguration' = pydantic.Field(None, alias="RevocationConfiguration")
    certificate_authority_type: CertificateAuthorityType = pydantic.Field(None, alias="CertificateAuthorityType")
    idempotency_token: IdempotencyToken = pydantic.Field(None, alias="IdempotencyToken")
    key_storage_security_standard: KeyStorageSecurityStandard = pydantic.Field(None, alias="KeyStorageSecurityStandard")
    tags: TagList = pydantic.Field(None, alias="Tags")
    usage_mode: CertificateAuthorityUsageMode = pydantic.Field(None, alias="UsageMode")

class CreateCertificateAuthorityResponse(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")

class CreatePermissionRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    principal: Principal = pydantic.Field(None, alias="Principal")
    source_account: AccountId = pydantic.Field(None, alias="SourceAccount")
    actions: ActionList = pydantic.Field(None, alias="Actions")

class CrlConfiguration(_ACMPCAModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    expiration_in_days: Integer1To5000 = pydantic.Field(None, alias="ExpirationInDays")
    custom_cname: CnameString = pydantic.Field(None, alias="CustomCname")
    s_3_bucket_name: S3BucketName3To255 = pydantic.Field(None, alias="S3BucketName")
    s_3_object_acl: S3ObjectAcl = pydantic.Field(None, alias="S3ObjectAcl")

class CsrExtensions(_ACMPCAModelBase):
    key_usage: 'KeyUsage' = pydantic.Field(None, alias="KeyUsage")
    subject_information_access: AccessDescriptionList = pydantic.Field(None, alias="SubjectInformationAccess")

class CustomAttribute(_ACMPCAModelBase):
    object_identifier: CustomObjectIdentifier = pydantic.Field(None, alias="ObjectIdentifier")
    value: String1To256 = pydantic.Field(None, alias="Value")

class CustomExtension(_ACMPCAModelBase):
    object_identifier: CustomObjectIdentifier = pydantic.Field(None, alias="ObjectIdentifier")
    value: Base64String1To4096 = pydantic.Field(None, alias="Value")
    critical: Boolean = pydantic.Field(None, alias="Critical")

class DeleteCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    permanent_deletion_time_in_days: PermanentDeletionTimeInDays = pydantic.Field(None, alias="PermanentDeletionTimeInDays")

class DeletePermissionRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    principal: Principal = pydantic.Field(None, alias="Principal")
    source_account: AccountId = pydantic.Field(None, alias="SourceAccount")

class DeletePolicyRequest(_ACMPCAModelBase):
    resource_arn: Arn = pydantic.Field(None, alias="ResourceArn")

class DescribeCertificateAuthorityAuditReportRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    audit_report_id: AuditReportId = pydantic.Field(None, alias="AuditReportId")

class DescribeCertificateAuthorityAuditReportResponse(_ACMPCAModelBase):
    audit_report_status: AuditReportStatus = pydantic.Field(None, alias="AuditReportStatus")
    s_3_bucket_name: S3BucketName = pydantic.Field(None, alias="S3BucketName")
    s_3_key: S3Key = pydantic.Field(None, alias="S3Key")
    created_at: 'TStamp' = pydantic.Field(None, alias="CreatedAt")

class DescribeCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")

class DescribeCertificateAuthorityResponse(_ACMPCAModelBase):
    certificate_authority: 'CertificateAuthority' = pydantic.Field(None, alias="CertificateAuthority")

class EdiPartyName(_ACMPCAModelBase):
    party_name: String256 = pydantic.Field(None, alias="PartyName")
    name_assigner: String256 = pydantic.Field(None, alias="NameAssigner")

class ExtendedKeyUsage(_ACMPCAModelBase):
    extended_key_usage_type: ExtendedKeyUsageType = pydantic.Field(None, alias="ExtendedKeyUsageType")
    extended_key_usage_object_identifier: CustomObjectIdentifier = pydantic.Field(None, alias="ExtendedKeyUsageObjectIdentifier")

class Extensions(_ACMPCAModelBase):
    certificate_policies: CertificatePolicyList = pydantic.Field(None, alias="CertificatePolicies")
    extended_key_usage: ExtendedKeyUsageList = pydantic.Field(None, alias="ExtendedKeyUsage")
    key_usage: 'KeyUsage' = pydantic.Field(None, alias="KeyUsage")
    subject_alternative_names: GeneralNameList = pydantic.Field(None, alias="SubjectAlternativeNames")
    custom_extensions: CustomExtensionList = pydantic.Field(None, alias="CustomExtensions")

class GeneralName(_ACMPCAModelBase):
    other_name: 'OtherName' = pydantic.Field(None, alias="OtherName")
    rfc_822_name: String256 = pydantic.Field(None, alias="Rfc822Name")
    dns_name: String253 = pydantic.Field(None, alias="DnsName")
    directory_name: 'ASN1Subject' = pydantic.Field(None, alias="DirectoryName")
    edi_party_name: 'EdiPartyName' = pydantic.Field(None, alias="EdiPartyName")
    uniform_resource_identifier: String253 = pydantic.Field(None, alias="UniformResourceIdentifier")
    ip_address: String39 = pydantic.Field(None, alias="IpAddress")
    registered_id: CustomObjectIdentifier = pydantic.Field(None, alias="RegisteredId")

class GetCertificateAuthorityCertificateRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")

class GetCertificateAuthorityCertificateResponse(_ACMPCAModelBase):
    certificate: CertificateBody = pydantic.Field(None, alias="Certificate")
    certificate_chain: CertificateChain = pydantic.Field(None, alias="CertificateChain")

class GetCertificateAuthorityCsrRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")

class GetCertificateAuthorityCsrResponse(_ACMPCAModelBase):
    csr: CsrBody = pydantic.Field(None, alias="Csr")

class GetCertificateRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")

class GetCertificateResponse(_ACMPCAModelBase):
    certificate: CertificateBody = pydantic.Field(None, alias="Certificate")
    certificate_chain: CertificateChain = pydantic.Field(None, alias="CertificateChain")

class GetPolicyRequest(_ACMPCAModelBase):
    resource_arn: Arn = pydantic.Field(None, alias="ResourceArn")

class GetPolicyResponse(_ACMPCAModelBase):
    policy: AWSPolicy = pydantic.Field(None, alias="Policy")

class ImportCertificateAuthorityCertificateRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    certificate: CertificateBodyBlob = pydantic.Field(None, alias="Certificate")
    certificate_chain: CertificateChainBlob = pydantic.Field(None, alias="CertificateChain")

class IssueCertificateRequest(_ACMPCAModelBase):
    api_passthrough: 'ApiPassthrough' = pydantic.Field(None, alias="ApiPassthrough")
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    csr: CsrBlob = pydantic.Field(None, alias="Csr")
    signing_algorithm: SigningAlgorithm = pydantic.Field(None, alias="SigningAlgorithm")
    template_arn: Arn = pydantic.Field(None, alias="TemplateArn")
    validity: 'Validity' = pydantic.Field(None, alias="Validity")
    validity_not_before: 'Validity' = pydantic.Field(None, alias="ValidityNotBefore")
    idempotency_token: IdempotencyToken = pydantic.Field(None, alias="IdempotencyToken")

class IssueCertificateResponse(_ACMPCAModelBase):
    certificate_arn: Arn = pydantic.Field(None, alias="CertificateArn")

class KeyUsage(_ACMPCAModelBase):
    digital_signature: Boolean = pydantic.Field(None, alias="DigitalSignature")
    non_repudiation: Boolean = pydantic.Field(None, alias="NonRepudiation")
    key_encipherment: Boolean = pydantic.Field(None, alias="KeyEncipherment")
    data_encipherment: Boolean = pydantic.Field(None, alias="DataEncipherment")
    key_agreement: Boolean = pydantic.Field(None, alias="KeyAgreement")
    key_cert_sign: Boolean = pydantic.Field(None, alias="KeyCertSign")
    crl_sign: Boolean = pydantic.Field(None, alias="CRLSign")
    encipher_only: Boolean = pydantic.Field(None, alias="EncipherOnly")
    decipher_only: Boolean = pydantic.Field(None, alias="DecipherOnly")

class ListCertificateAuthoritiesRequest(_ACMPCAModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")
    resource_owner: ResourceOwner = pydantic.Field(None, alias="ResourceOwner")

class ListCertificateAuthoritiesResponse(_ACMPCAModelBase):
    certificate_authorities: CertificateAuthorities = pydantic.Field(None, alias="CertificateAuthorities")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class ListPermissionsRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")

class ListPermissionsResponse(_ACMPCAModelBase):
    permissions: PermissionList = pydantic.Field(None, alias="Permissions")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class ListTagsRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")

class ListTagsResponse(_ACMPCAModelBase):
    tags: TagList = pydantic.Field(None, alias="Tags")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class OcspConfiguration(_ACMPCAModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    ocsp_custom_cname: CnameString = pydantic.Field(None, alias="OcspCustomCname")

class OtherName(_ACMPCAModelBase):
    type_id: CustomObjectIdentifier = pydantic.Field(None, alias="TypeId")
    value: String256 = pydantic.Field(None, alias="Value")

class Permission(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    created_at: 'TStamp' = pydantic.Field(None, alias="CreatedAt")
    principal: Principal = pydantic.Field(None, alias="Principal")
    source_account: AccountId = pydantic.Field(None, alias="SourceAccount")
    actions: ActionList = pydantic.Field(None, alias="Actions")
    policy: AWSPolicy = pydantic.Field(None, alias="Policy")

class PolicyInformation(_ACMPCAModelBase):
    cert_policy_id: CustomObjectIdentifier = pydantic.Field(None, alias="CertPolicyId")
    policy_qualifiers: PolicyQualifierInfoList = pydantic.Field(None, alias="PolicyQualifiers")

class PolicyQualifierInfo(_ACMPCAModelBase):
    policy_qualifier_id: PolicyQualifierId = pydantic.Field(None, alias="PolicyQualifierId")
    qualifier: 'Qualifier' = pydantic.Field(None, alias="Qualifier")

class PutPolicyRequest(_ACMPCAModelBase):
    resource_arn: Arn = pydantic.Field(None, alias="ResourceArn")
    policy: AWSPolicy = pydantic.Field(None, alias="Policy")

class Qualifier(_ACMPCAModelBase):
    cps_uri: String256 = pydantic.Field(None, alias="CpsUri")

class RestoreCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")

class RevocationConfiguration(_ACMPCAModelBase):
    crl_configuration: 'CrlConfiguration' = pydantic.Field(None, alias="CrlConfiguration")
    ocsp_configuration: 'OcspConfiguration' = pydantic.Field(None, alias="OcspConfiguration")

class RevokeCertificateRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    certificate_serial: String128 = pydantic.Field(None, alias="CertificateSerial")
    revocation_reason: RevocationReason = pydantic.Field(None, alias="RevocationReason")

class Tag(_ACMPCAModelBase):
    key: TagKey = pydantic.Field(None, alias="Key")
    value: TagValue = pydantic.Field(None, alias="Value")

class TagCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    tags: TagList = pydantic.Field(None, alias="Tags")

class UntagCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    tags: TagList = pydantic.Field(None, alias="Tags")

class UpdateCertificateAuthorityRequest(_ACMPCAModelBase):
    certificate_authority_arn: Arn = pydantic.Field(None, alias="CertificateAuthorityArn")
    revocation_configuration: 'RevocationConfiguration' = pydantic.Field(None, alias="RevocationConfiguration")
    status: CertificateAuthorityStatus = pydantic.Field(None, alias="Status")

class Validity(_ACMPCAModelBase):
    value: PositiveLong = pydantic.Field(None, alias="Value")
    type: ValidityPeriodType = pydantic.Field(None, alias="Type")

ASN1Subject.update_forward_refs()
AccessDescription.update_forward_refs()
AccessMethod.update_forward_refs()
ApiPassthrough.update_forward_refs()
CertificateAuthority.update_forward_refs()
CertificateAuthorityConfiguration.update_forward_refs()
CreateCertificateAuthorityAuditReportRequest.update_forward_refs()
CreateCertificateAuthorityAuditReportResponse.update_forward_refs()
CreateCertificateAuthorityRequest.update_forward_refs()
CreateCertificateAuthorityResponse.update_forward_refs()
CreatePermissionRequest.update_forward_refs()
CrlConfiguration.update_forward_refs()
CsrExtensions.update_forward_refs()
CustomAttribute.update_forward_refs()
CustomExtension.update_forward_refs()
DeleteCertificateAuthorityRequest.update_forward_refs()
DeletePermissionRequest.update_forward_refs()
DeletePolicyRequest.update_forward_refs()
DescribeCertificateAuthorityAuditReportRequest.update_forward_refs()
DescribeCertificateAuthorityAuditReportResponse.update_forward_refs()
DescribeCertificateAuthorityRequest.update_forward_refs()
DescribeCertificateAuthorityResponse.update_forward_refs()
EdiPartyName.update_forward_refs()
ExtendedKeyUsage.update_forward_refs()
Extensions.update_forward_refs()
GeneralName.update_forward_refs()
GetCertificateAuthorityCertificateRequest.update_forward_refs()
GetCertificateAuthorityCertificateResponse.update_forward_refs()
GetCertificateAuthorityCsrRequest.update_forward_refs()
GetCertificateAuthorityCsrResponse.update_forward_refs()
GetCertificateRequest.update_forward_refs()
GetCertificateResponse.update_forward_refs()
GetPolicyRequest.update_forward_refs()
GetPolicyResponse.update_forward_refs()
ImportCertificateAuthorityCertificateRequest.update_forward_refs()
IssueCertificateRequest.update_forward_refs()
IssueCertificateResponse.update_forward_refs()
KeyUsage.update_forward_refs()
ListCertificateAuthoritiesRequest.update_forward_refs()
ListCertificateAuthoritiesResponse.update_forward_refs()
ListPermissionsRequest.update_forward_refs()
ListPermissionsResponse.update_forward_refs()
ListTagsRequest.update_forward_refs()
ListTagsResponse.update_forward_refs()
OcspConfiguration.update_forward_refs()
OtherName.update_forward_refs()
Permission.update_forward_refs()
PolicyInformation.update_forward_refs()
PolicyQualifierInfo.update_forward_refs()
PutPolicyRequest.update_forward_refs()
Qualifier.update_forward_refs()
RestoreCertificateAuthorityRequest.update_forward_refs()
RevocationConfiguration.update_forward_refs()
RevokeCertificateRequest.update_forward_refs()
Tag.update_forward_refs()
TagCertificateAuthorityRequest.update_forward_refs()
UntagCertificateAuthorityRequest.update_forward_refs()
UpdateCertificateAuthorityRequest.update_forward_refs()
Validity.update_forward_refs()
