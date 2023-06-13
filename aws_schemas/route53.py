from datetime import datetime
import typing
import enum

import pydantic


class _Route53ModelBase(
    pydantic.BaseModel,
    frozen=True,
    use_enum_values=True,
    allow_population_by_field_name=True,
    extra=pydantic.Extra.allow,
):
    def dict(self, by_alias=True, **kwargs) -> dict:
        return super().dict(by_alias=True, **kwargs)

    def json(self, by_alias=True, **kwargs) -> dict:
        return super().json(by_alias=True, **kwargs)


ARN: str = pydantic.constr(min_length=20, max_length=2048, regex=r".*\S.*")
AWSAccountID: str = pydantic.constr()
AccountLimitType: str = pydantic.constr()
AlarmName: str = pydantic.constr(min_length=1, max_length=256)
AliasHealthEnabled: bool = pydantic.conbool()
AssociateVPCComment: str = pydantic.constr()
ChangeAction: str = pydantic.constr()
ChangeId: str = pydantic.constr(min_length=1, max_length=6500)
ChangeStatus: str = pydantic.constr()
Cidr: str = pydantic.constr(min_length=1, max_length=50, regex=r".*\S.*")
CidrCollectionChangeAction: str = pydantic.constr()
CidrLocationNameDefaultAllowed: str = pydantic.constr(
    min_length=1, max_length=16, regex=r"[0-9A-Za-z_\-\*]+"
)
CidrLocationNameDefaultNotAllowed: str = pydantic.constr(
    min_length=1, max_length=16, regex=r"[0-9A-Za-z_\-]+"
)
CidrNonce: str = pydantic.constr(min_length=1, max_length=64, regex=r"\p{ASCII}+")
CloudWatchLogsLogGroupArn: str = pydantic.constr()
CloudWatchRegion: str = pydantic.constr(min_length=1, max_length=64)
CollectionName: str = pydantic.constr(
    min_length=1, max_length=64, regex=r"[0-9A-Za-z_\-]+"
)
CollectionVersion: int = pydantic.conint()
ComparisonOperator: str = pydantic.constr()
DNSName: str = pydantic.constr(max_length=1024)
DNSRCode: str = pydantic.constr()
DimensionField: str = pydantic.constr(min_length=1, max_length=255)
Disabled: bool = pydantic.conbool()
DisassociateVPCComment: str = pydantic.constr()
EnableSNI: bool = pydantic.conbool()
ErrorMessage: str = pydantic.constr()
EvaluationPeriods: int = pydantic.conint(ge=1)
FailureThreshold: int = pydantic.conint(ge=1, le=10)
FullyQualifiedDomainName: str = pydantic.constr(max_length=255)
GeoLocationContinentCode: str = pydantic.constr(min_length=2, max_length=2)
GeoLocationContinentName: str = pydantic.constr(min_length=1, max_length=32)
GeoLocationCountryCode: str = pydantic.constr(min_length=1, max_length=2)
GeoLocationCountryName: str = pydantic.constr(min_length=1, max_length=64)
GeoLocationSubdivisionCode: str = pydantic.constr(min_length=1, max_length=3)
GeoLocationSubdivisionName: str = pydantic.constr(min_length=1, max_length=64)
HealthCheckCount: int = pydantic.conint()
HealthCheckId: str = pydantic.constr(max_length=64)
HealthCheckNonce: str = pydantic.constr(min_length=1, max_length=64)
HealthCheckRegion: str = pydantic.constr(min_length=1, max_length=64)
HealthCheckType: str = pydantic.constr()
HealthCheckVersion: int = pydantic.conint()
HealthThreshold: int = pydantic.conint(le=256)
HostedZoneCount: int = pydantic.conint()
HostedZoneLimitType: str = pydantic.constr()
HostedZoneOwningService: str = pydantic.constr(max_length=128)
HostedZoneRRSetCount: int = pydantic.conint()
IPAddress: str = pydantic.constr(
    max_length=45,
    regex=r"(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)",
)
IPAddressCidr: str = pydantic.constr()
InsufficientDataHealthStatus: str = pydantic.constr()
Inverted: bool = pydantic.conbool()
IsPrivateZone: bool = pydantic.conbool()
LimitValue: int = pydantic.conint()
MaxResults: str = pydantic.constr()
MeasureLatency: bool = pydantic.conbool()
Message: str = pydantic.constr(max_length=1024)
MetricName: str = pydantic.constr(min_length=1, max_length=255)
Nameserver: str = pydantic.constr(max_length=255)
Namespace: str = pydantic.constr(min_length=1, max_length=255)
Nonce: str = pydantic.constr(min_length=1, max_length=128)
PageMarker: str = pydantic.constr(max_length=64)
PageMaxItems: str = pydantic.constr()
PageTruncated: bool = pydantic.conbool()
PaginationToken: str = pydantic.constr(max_length=1024)
Period: int = pydantic.conint(ge=60)
Port: int = pydantic.conint(ge=1, le=65535)
QueryLoggingConfigId: str = pydantic.constr(min_length=1, max_length=36)
RData: str = pydantic.constr(max_length=4000)
RRType: str = pydantic.constr()
RecordDataEntry: str = pydantic.constr(max_length=512)
RequestInterval: int = pydantic.conint(ge=10, le=30)
ResettableElementName: str = pydantic.constr(min_length=1, max_length=64)
ResourceDescription: str = pydantic.constr(max_length=256)
ResourceId: str = pydantic.constr(max_length=32)
ResourcePath: str = pydantic.constr(max_length=255)
ResourceRecordSetFailover: str = pydantic.constr()
ResourceRecordSetIdentifier: str = pydantic.constr(min_length=1, max_length=128)
ResourceRecordSetMultiValueAnswer: bool = pydantic.conbool()
ResourceRecordSetRegion: str = pydantic.constr(min_length=1, max_length=64)
ResourceRecordSetWeight: int = pydantic.conint()
ResourceURI: str = pydantic.constr(max_length=1024)
ReusableDelegationSetLimitType: str = pydantic.constr()
RoutingControlArn: str = pydantic.constr(min_length=1, max_length=255)
SearchString: str = pydantic.constr(max_length=255)
ServeSignature: str = pydantic.constr(min_length=1, max_length=1024)
ServicePrincipal: str = pydantic.constr(max_length=128)
SigningKeyInteger: int = pydantic.conint()
SigningKeyName: str = pydantic.constr(min_length=3, max_length=128)
SigningKeyStatus: str = pydantic.constr(min_length=5, max_length=150)
SigningKeyStatusMessage: str = pydantic.constr(max_length=512)
SigningKeyString: str = pydantic.constr()
SigningKeyTag: int = pydantic.conint(le=65536)
Statistic: str = pydantic.constr()
Status: str = pydantic.constr()
SubnetMask: str = pydantic.constr(max_length=3)
TTL: int = pydantic.conint()
TagKey: str = pydantic.constr(max_length=128)
TagResourceId: str = pydantic.constr(max_length=64)
TagResourceType: str = pydantic.constr()
TagValue: str = pydantic.constr(max_length=256)
Threshold: float = pydantic.confloat()
TimeStamp: datetime = pydantic.condate()
TrafficPolicyComment: str = pydantic.constr(max_length=1024)
TrafficPolicyDocument: str = pydantic.constr(max_length=102400)
TrafficPolicyId: str = pydantic.constr(min_length=1, max_length=36)
TrafficPolicyInstanceCount: int = pydantic.conint()
TrafficPolicyInstanceId: str = pydantic.constr(min_length=1, max_length=36)
TrafficPolicyInstanceState: str = pydantic.constr()
TrafficPolicyName: str = pydantic.constr(max_length=512)
TrafficPolicyVersion: int = pydantic.conint(ge=1, le=1000)
TrafficPolicyVersionMarker: str = pydantic.constr(max_length=4)
TransportProtocol: str = pydantic.constr()
UUID: str = pydantic.constr(regex=r"[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}")
UsageCount: int = pydantic.conint()
VPCId: str = pydantic.constr(max_length=1024)
VPCRegion: str = pydantic.constr(min_length=1, max_length=64)

Changes = typing.List["Change"]
CheckerIpRanges = typing.List["IPAddressCidr"]
ChildHealthCheckList = typing.List["HealthCheckId"]
CidrBlockSummaries = typing.List["CidrBlockSummary"]
CidrCollectionChanges = typing.List["CidrCollectionChange"]
CidrList = typing.List["Cidr"]
CollectionSummaries = typing.List["CollectionSummary"]
DelegationSetNameServers = typing.List["DNSName"]
DelegationSets = typing.List["DelegationSet"]
DimensionList = typing.List["Dimension"]
ErrorMessages = typing.List["ErrorMessage"]
GeoLocationDetailsList = typing.List["GeoLocationDetails"]
HealthCheckObservations = typing.List["HealthCheckObservation"]
HealthCheckRegionList = typing.List["HealthCheckRegion"]
HealthChecks = typing.List["HealthCheck"]
HostedZoneSummaries = typing.List["HostedZoneSummary"]
HostedZones = typing.List["HostedZone"]
KeySigningKeys = typing.List["KeySigningKey"]
LocationSummaries = typing.List["LocationSummary"]
QueryLoggingConfigs = typing.List["QueryLoggingConfig"]
RecordData = typing.List["RecordDataEntry"]
ResettableElementNameList = typing.List["ResettableElementName"]
ResourceRecordSets = typing.List["ResourceRecordSet"]
ResourceRecords = typing.List["ResourceRecord"]
ResourceTagSetList = typing.List["ResourceTagSet"]
TagKeyList = typing.List["TagKey"]
TagList = typing.List["Tag"]
TagResourceIdList = typing.List["TagResourceId"]
TrafficPolicies = typing.List["TrafficPolicy"]
TrafficPolicyInstances = typing.List["TrafficPolicyInstance"]
TrafficPolicySummaries = typing.List["TrafficPolicySummary"]
VPCs = typing.List["VPC"]


class AccountLimitType(enum.Enum):
    MAX_HEALTH_CHECKS_BY_OWNER = "MAX_HEALTH_CHECKS_BY_OWNER"
    MAX_HOSTED_ZONES_BY_OWNER = "MAX_HOSTED_ZONES_BY_OWNER"
    MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER = "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER"
    MAX_REUSABLE_DELEGATION_SETS_BY_OWNER = "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER"
    MAX_TRAFFIC_POLICIES_BY_OWNER = "MAX_TRAFFIC_POLICIES_BY_OWNER"


class ChangeAction(enum.Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    UPSERT = "UPSERT"


class ChangeStatus(enum.Enum):
    PENDING = "PENDING"
    INSYNC = "INSYNC"


class CidrCollectionChangeAction(enum.Enum):
    PUT = "PUT"
    DELETE_IF_EXISTS = "DELETE_IF_EXISTS"


class CloudWatchRegion(enum.Enum):
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    CA_CENTRAL_1 = "ca-central-1"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    AP_EAST_1 = "ap-east-1"
    ME_SOUTH_1 = "me-south-1"
    ME_CENTRAL_1 = "me-central-1"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    CN_NORTH_1 = "cn-north-1"
    AF_SOUTH_1 = "af-south-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    US_GOV_WEST_1 = "us-gov-west-1"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_ISO_EAST_1 = "us-iso-east-1"
    US_ISO_WEST_1 = "us-iso-west-1"
    US_ISOB_EAST_1 = "us-isob-east-1"
    AP_SOUTHEAST_4 = "ap-southeast-4"


class ComparisonOperator(enum.Enum):
    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"


class HealthCheckRegion(enum.Enum):
    US_EAST_1 = "us-east-1"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    EU_WEST_1 = "eu-west-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_NORTHEAST_1 = "ap-northeast-1"
    SA_EAST_1 = "sa-east-1"


class HealthCheckType(enum.Enum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    HTTP_STR_MATCH = "HTTP_STR_MATCH"
    HTTPS_STR_MATCH = "HTTPS_STR_MATCH"
    TCP = "TCP"
    CALCULATED = "CALCULATED"
    CLOUDWATCH_METRIC = "CLOUDWATCH_METRIC"
    RECOVERY_CONTROL = "RECOVERY_CONTROL"


class HostedZoneLimitType(enum.Enum):
    MAX_RRSETS_BY_ZONE = "MAX_RRSETS_BY_ZONE"
    MAX_VPCS_ASSOCIATED_BY_ZONE = "MAX_VPCS_ASSOCIATED_BY_ZONE"


class InsufficientDataHealthStatus(enum.Enum):
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    LASTKNOWNSTATUS = "LastKnownStatus"


class RRType(enum.Enum):
    SOA = "SOA"
    A = "A"
    TXT = "TXT"
    NS = "NS"
    CNAME = "CNAME"
    MX = "MX"
    NAPTR = "NAPTR"
    PTR = "PTR"
    SRV = "SRV"
    SPF = "SPF"
    AAAA = "AAAA"
    CAA = "CAA"
    DS = "DS"


class ResettableElementName(enum.Enum):
    FULLYQUALIFIEDDOMAINNAME = "FullyQualifiedDomainName"
    REGIONS = "Regions"
    RESOURCEPATH = "ResourcePath"
    CHILDHEALTHCHECKS = "ChildHealthChecks"


class ResourceRecordSetFailover(enum.Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"


class ResourceRecordSetRegion(enum.Enum):
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    CA_CENTRAL_1 = "ca-central-1"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    CN_NORTH_1 = "cn-north-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    AP_EAST_1 = "ap-east-1"
    ME_SOUTH_1 = "me-south-1"
    ME_CENTRAL_1 = "me-central-1"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AF_SOUTH_1 = "af-south-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    AP_SOUTHEAST_4 = "ap-southeast-4"


class ReusableDelegationSetLimitType(enum.Enum):
    MAX_ZONES_BY_REUSABLE_DELEGATION_SET = "MAX_ZONES_BY_REUSABLE_DELEGATION_SET"


class Statistic(enum.Enum):
    AVERAGE = "Average"
    SUM = "Sum"
    SAMPLECOUNT = "SampleCount"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"


class TagResourceType(enum.Enum):
    HEALTHCHECK = "healthcheck"
    HOSTEDZONE = "hostedzone"


class VPCRegion(enum.Enum):
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    AP_EAST_1 = "ap-east-1"
    ME_SOUTH_1 = "me-south-1"
    US_GOV_WEST_1 = "us-gov-west-1"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_ISO_EAST_1 = "us-iso-east-1"
    US_ISO_WEST_1 = "us-iso-west-1"
    US_ISOB_EAST_1 = "us-isob-east-1"
    ME_CENTRAL_1 = "me-central-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    CA_CENTRAL_1 = "ca-central-1"
    CN_NORTH_1 = "cn-north-1"
    AF_SOUTH_1 = "af-south-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    AP_SOUTHEAST_4 = "ap-southeast-4"


class AccountLimit(_Route53ModelBase):
    type: AccountLimitType = pydantic.Field(None, alias="Type")
    value: LimitValue = pydantic.Field(None, alias="Value")


class ActivateKeySigningKeyRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    name: SigningKeyName = pydantic.Field(None, alias="Name")


class ActivateKeySigningKeyResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class AlarmIdentifier(_Route53ModelBase):
    region: CloudWatchRegion = pydantic.Field(None, alias="Region")
    name: AlarmName = pydantic.Field(None, alias="Name")


class AliasTarget(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    dns_name: DNSName = pydantic.Field(None, alias="DNSName")
    evaluate_target_health: AliasHealthEnabled = pydantic.Field(
        None, alias="EvaluateTargetHealth"
    )


class AssociateVPCWithHostedZoneRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")
    comment: AssociateVPCComment = pydantic.Field(None, alias="Comment")


class AssociateVPCWithHostedZoneResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class Change(_Route53ModelBase):
    action: ChangeAction = pydantic.Field(None, alias="Action")
    resource_record_set: "ResourceRecordSet" = pydantic.Field(
        None, alias="ResourceRecordSet"
    )


class ChangeBatch(_Route53ModelBase):
    comment: ResourceDescription = pydantic.Field(None, alias="Comment")
    changes: Changes = pydantic.Field(None, alias="Changes")


class ChangeCidrCollectionRequest(_Route53ModelBase):
    id: UUID = pydantic.Field(None, alias="Id")
    collection_version: CollectionVersion = pydantic.Field(
        None, alias="CollectionVersion"
    )
    changes: CidrCollectionChanges = pydantic.Field(None, alias="Changes")


class ChangeCidrCollectionResponse(_Route53ModelBase):
    id: ChangeId = pydantic.Field(None, alias="Id")


class ChangeInfo(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")
    status: ChangeStatus = pydantic.Field(None, alias="Status")
    submitted_at: TimeStamp = pydantic.Field(None, alias="SubmittedAt")
    comment: ResourceDescription = pydantic.Field(None, alias="Comment")


class ChangeResourceRecordSetsRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    change_batch: "ChangeBatch" = pydantic.Field(None, alias="ChangeBatch")


class ChangeResourceRecordSetsResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class ChangeTagsForResourceRequest(_Route53ModelBase):
    resource_type: TagResourceType = pydantic.Field(None, alias="ResourceType")
    resource_id: TagResourceId = pydantic.Field(None, alias="ResourceId")
    add_tags: TagList = pydantic.Field(None, alias="AddTags")
    remove_tag_keys: TagKeyList = pydantic.Field(None, alias="RemoveTagKeys")


class ChangeTagsForResourceResponse(_Route53ModelBase):
    pass


class CidrBlockSummary(_Route53ModelBase):
    cidr_block: Cidr = pydantic.Field(None, alias="CidrBlock")
    location_name: CidrLocationNameDefaultNotAllowed = pydantic.Field(
        None, alias="LocationName"
    )


class CidrCollection(_Route53ModelBase):
    arn: ARN = pydantic.Field(None, alias="Arn")
    id: UUID = pydantic.Field(None, alias="Id")
    name: CollectionName = pydantic.Field(None, alias="Name")
    version: CollectionVersion = pydantic.Field(None, alias="Version")


class CidrCollectionChange(_Route53ModelBase):
    location_name: CidrLocationNameDefaultNotAllowed = pydantic.Field(
        None, alias="LocationName"
    )
    action: CidrCollectionChangeAction = pydantic.Field(None, alias="Action")
    cidr_list: CidrList = pydantic.Field(None, alias="CidrList")


class CidrRoutingConfig(_Route53ModelBase):
    collection_id: UUID = pydantic.Field(None, alias="CollectionId")
    location_name: CidrLocationNameDefaultAllowed = pydantic.Field(
        None, alias="LocationName"
    )


class CloudWatchAlarmConfiguration(_Route53ModelBase):
    evaluation_periods: EvaluationPeriods = pydantic.Field(
        None, alias="EvaluationPeriods"
    )
    threshold: Threshold = pydantic.Field(None, alias="Threshold")
    comparison_operator: ComparisonOperator = pydantic.Field(
        None, alias="ComparisonOperator"
    )
    period: Period = pydantic.Field(None, alias="Period")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    statistic: Statistic = pydantic.Field(None, alias="Statistic")
    dimensions: DimensionList = pydantic.Field(None, alias="Dimensions")


class CollectionSummary(_Route53ModelBase):
    arn: ARN = pydantic.Field(None, alias="Arn")
    id: UUID = pydantic.Field(None, alias="Id")
    name: CollectionName = pydantic.Field(None, alias="Name")
    version: CollectionVersion = pydantic.Field(None, alias="Version")


class CreateCidrCollectionRequest(_Route53ModelBase):
    name: CollectionName = pydantic.Field(None, alias="Name")
    caller_reference: CidrNonce = pydantic.Field(None, alias="CallerReference")


class CreateCidrCollectionResponse(_Route53ModelBase):
    collection: "CidrCollection" = pydantic.Field(None, alias="Collection")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateHealthCheckRequest(_Route53ModelBase):
    caller_reference: HealthCheckNonce = pydantic.Field(None, alias="CallerReference")
    health_check_config: "HealthCheckConfig" = pydantic.Field(
        None, alias="HealthCheckConfig"
    )


class CreateHealthCheckResponse(_Route53ModelBase):
    health_check: "HealthCheck" = pydantic.Field(None, alias="HealthCheck")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateHostedZoneRequest(_Route53ModelBase):
    name: DNSName = pydantic.Field(None, alias="Name")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")
    caller_reference: Nonce = pydantic.Field(None, alias="CallerReference")
    hosted_zone_config: "HostedZoneConfig" = pydantic.Field(
        None, alias="HostedZoneConfig"
    )
    delegation_set_id: ResourceId = pydantic.Field(None, alias="DelegationSetId")


class CreateHostedZoneResponse(_Route53ModelBase):
    hosted_zone: "HostedZone" = pydantic.Field(None, alias="HostedZone")
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")
    delegation_set: "DelegationSet" = pydantic.Field(None, alias="DelegationSet")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateKeySigningKeyRequest(_Route53ModelBase):
    caller_reference: Nonce = pydantic.Field(None, alias="CallerReference")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    key_management_service_arn: SigningKeyString = pydantic.Field(
        None, alias="KeyManagementServiceArn"
    )
    name: SigningKeyName = pydantic.Field(None, alias="Name")
    status: SigningKeyStatus = pydantic.Field(None, alias="Status")


class CreateKeySigningKeyResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")
    key_signing_key: "KeySigningKey" = pydantic.Field(None, alias="KeySigningKey")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateQueryLoggingConfigRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    cloud_watch_logs_log_group_arn: CloudWatchLogsLogGroupArn = pydantic.Field(
        None, alias="CloudWatchLogsLogGroupArn"
    )


class CreateQueryLoggingConfigResponse(_Route53ModelBase):
    query_logging_config: "QueryLoggingConfig" = pydantic.Field(
        None, alias="QueryLoggingConfig"
    )
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateReusableDelegationSetRequest(_Route53ModelBase):
    caller_reference: Nonce = pydantic.Field(None, alias="CallerReference")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")


class CreateReusableDelegationSetResponse(_Route53ModelBase):
    delegation_set: "DelegationSet" = pydantic.Field(None, alias="DelegationSet")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateTrafficPolicyInstanceRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    name: DNSName = pydantic.Field(None, alias="Name")
    ttl: TTL = pydantic.Field(None, alias="TTL")
    traffic_policy_id: TrafficPolicyId = pydantic.Field(None, alias="TrafficPolicyId")
    traffic_policy_version: TrafficPolicyVersion = pydantic.Field(
        None, alias="TrafficPolicyVersion"
    )


class CreateTrafficPolicyInstanceResponse(_Route53ModelBase):
    traffic_policy_instance: "TrafficPolicyInstance" = pydantic.Field(
        None, alias="TrafficPolicyInstance"
    )
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateTrafficPolicyRequest(_Route53ModelBase):
    name: TrafficPolicyName = pydantic.Field(None, alias="Name")
    document: TrafficPolicyDocument = pydantic.Field(None, alias="Document")
    comment: TrafficPolicyComment = pydantic.Field(None, alias="Comment")


class CreateTrafficPolicyResponse(_Route53ModelBase):
    traffic_policy: "TrafficPolicy" = pydantic.Field(None, alias="TrafficPolicy")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateTrafficPolicyVersionRequest(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    document: TrafficPolicyDocument = pydantic.Field(None, alias="Document")
    comment: TrafficPolicyComment = pydantic.Field(None, alias="Comment")


class CreateTrafficPolicyVersionResponse(_Route53ModelBase):
    traffic_policy: "TrafficPolicy" = pydantic.Field(None, alias="TrafficPolicy")
    location: ResourceURI = pydantic.Field(None, alias="Location")


class CreateVPCAssociationAuthorizationRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")


class CreateVPCAssociationAuthorizationResponse(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")


class DNSSECStatus(_Route53ModelBase):
    serve_signature: ServeSignature = pydantic.Field(None, alias="ServeSignature")
    status_message: SigningKeyStatusMessage = pydantic.Field(
        None, alias="StatusMessage"
    )


class DeactivateKeySigningKeyRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    name: SigningKeyName = pydantic.Field(None, alias="Name")


class DeactivateKeySigningKeyResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class DelegationSet(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")
    caller_reference: Nonce = pydantic.Field(None, alias="CallerReference")
    name_servers: DelegationSetNameServers = pydantic.Field(None, alias="NameServers")


class DeleteCidrCollectionRequest(_Route53ModelBase):
    id: UUID = pydantic.Field(None, alias="Id")


class DeleteCidrCollectionResponse(_Route53ModelBase):
    pass


class DeleteHealthCheckRequest(_Route53ModelBase):
    health_check_id: HealthCheckId = pydantic.Field(None, alias="HealthCheckId")


class DeleteHealthCheckResponse(_Route53ModelBase):
    pass


class DeleteHostedZoneRequest(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")


class DeleteHostedZoneResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class DeleteKeySigningKeyRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    name: SigningKeyName = pydantic.Field(None, alias="Name")


class DeleteKeySigningKeyResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class DeleteQueryLoggingConfigRequest(_Route53ModelBase):
    id: QueryLoggingConfigId = pydantic.Field(None, alias="Id")


class DeleteQueryLoggingConfigResponse(_Route53ModelBase):
    pass


class DeleteReusableDelegationSetRequest(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")


class DeleteReusableDelegationSetResponse(_Route53ModelBase):
    pass


class DeleteTrafficPolicyInstanceRequest(_Route53ModelBase):
    id: TrafficPolicyInstanceId = pydantic.Field(None, alias="Id")


class DeleteTrafficPolicyInstanceResponse(_Route53ModelBase):
    pass


class DeleteTrafficPolicyRequest(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    version: TrafficPolicyVersion = pydantic.Field(None, alias="Version")


class DeleteTrafficPolicyResponse(_Route53ModelBase):
    pass


class DeleteVPCAssociationAuthorizationRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")


class DeleteVPCAssociationAuthorizationResponse(_Route53ModelBase):
    pass


class Dimension(_Route53ModelBase):
    name: DimensionField = pydantic.Field(None, alias="Name")
    value: DimensionField = pydantic.Field(None, alias="Value")


class DisableHostedZoneDNSSECRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")


class DisableHostedZoneDNSSECResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class DisassociateVPCFromHostedZoneRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    vpc: "VPC" = pydantic.Field(None, alias="VPC")
    comment: DisassociateVPCComment = pydantic.Field(None, alias="Comment")


class DisassociateVPCFromHostedZoneResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class EnableHostedZoneDNSSECRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")


class EnableHostedZoneDNSSECResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class GeoLocation(_Route53ModelBase):
    continent_code: GeoLocationContinentCode = pydantic.Field(
        None, alias="ContinentCode"
    )
    country_code: GeoLocationCountryCode = pydantic.Field(None, alias="CountryCode")
    subdivision_code: GeoLocationSubdivisionCode = pydantic.Field(
        None, alias="SubdivisionCode"
    )


class GeoLocationDetails(_Route53ModelBase):
    continent_code: GeoLocationContinentCode = pydantic.Field(
        None, alias="ContinentCode"
    )
    continent_name: GeoLocationContinentName = pydantic.Field(
        None, alias="ContinentName"
    )
    country_code: GeoLocationCountryCode = pydantic.Field(None, alias="CountryCode")
    country_name: GeoLocationCountryName = pydantic.Field(None, alias="CountryName")
    subdivision_code: GeoLocationSubdivisionCode = pydantic.Field(
        None, alias="SubdivisionCode"
    )
    subdivision_name: GeoLocationSubdivisionName = pydantic.Field(
        None, alias="SubdivisionName"
    )


class GetAccountLimitRequest(_Route53ModelBase):
    type: AccountLimitType = pydantic.Field(None, alias="Type")


class GetAccountLimitResponse(_Route53ModelBase):
    limit: "AccountLimit" = pydantic.Field(None, alias="Limit")
    count: UsageCount = pydantic.Field(None, alias="Count")


class GetChangeRequest(_Route53ModelBase):
    id: ChangeId = pydantic.Field(None, alias="Id")


class GetChangeResponse(_Route53ModelBase):
    change_info: "ChangeInfo" = pydantic.Field(None, alias="ChangeInfo")


class GetCheckerIpRangesRequest(_Route53ModelBase):
    pass


class GetCheckerIpRangesResponse(_Route53ModelBase):
    checker_ip_ranges: CheckerIpRanges = pydantic.Field(None, alias="CheckerIpRanges")


class GetDNSSECRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")


class GetDNSSECResponse(_Route53ModelBase):
    status: "DNSSECStatus" = pydantic.Field(None, alias="Status")
    key_signing_keys: KeySigningKeys = pydantic.Field(None, alias="KeySigningKeys")


class GetGeoLocationRequest(_Route53ModelBase):
    continent_code: GeoLocationContinentCode = pydantic.Field(
        None, alias="ContinentCode"
    )
    country_code: GeoLocationCountryCode = pydantic.Field(None, alias="CountryCode")
    subdivision_code: GeoLocationSubdivisionCode = pydantic.Field(
        None, alias="SubdivisionCode"
    )


class GetGeoLocationResponse(_Route53ModelBase):
    geo_location_details: "GeoLocationDetails" = pydantic.Field(
        None, alias="GeoLocationDetails"
    )


class GetHealthCheckCountRequest(_Route53ModelBase):
    pass


class GetHealthCheckCountResponse(_Route53ModelBase):
    health_check_count: HealthCheckCount = pydantic.Field(
        None, alias="HealthCheckCount"
    )


class GetHealthCheckLastFailureReasonRequest(_Route53ModelBase):
    health_check_id: HealthCheckId = pydantic.Field(None, alias="HealthCheckId")


class GetHealthCheckLastFailureReasonResponse(_Route53ModelBase):
    health_check_observations: HealthCheckObservations = pydantic.Field(
        None, alias="HealthCheckObservations"
    )


class GetHealthCheckRequest(_Route53ModelBase):
    health_check_id: HealthCheckId = pydantic.Field(None, alias="HealthCheckId")


class GetHealthCheckResponse(_Route53ModelBase):
    health_check: "HealthCheck" = pydantic.Field(None, alias="HealthCheck")


class GetHealthCheckStatusRequest(_Route53ModelBase):
    health_check_id: HealthCheckId = pydantic.Field(None, alias="HealthCheckId")


class GetHealthCheckStatusResponse(_Route53ModelBase):
    health_check_observations: HealthCheckObservations = pydantic.Field(
        None, alias="HealthCheckObservations"
    )


class GetHostedZoneCountRequest(_Route53ModelBase):
    pass


class GetHostedZoneCountResponse(_Route53ModelBase):
    hosted_zone_count: HostedZoneCount = pydantic.Field(None, alias="HostedZoneCount")


class GetHostedZoneLimitRequest(_Route53ModelBase):
    type: HostedZoneLimitType = pydantic.Field(None, alias="Type")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")


class GetHostedZoneLimitResponse(_Route53ModelBase):
    limit: "HostedZoneLimit" = pydantic.Field(None, alias="Limit")
    count: UsageCount = pydantic.Field(None, alias="Count")


class GetHostedZoneRequest(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")


class GetHostedZoneResponse(_Route53ModelBase):
    hosted_zone: "HostedZone" = pydantic.Field(None, alias="HostedZone")
    delegation_set: "DelegationSet" = pydantic.Field(None, alias="DelegationSet")
    vp_cs: VPCs = pydantic.Field(None, alias="VPCs")


class GetQueryLoggingConfigRequest(_Route53ModelBase):
    id: QueryLoggingConfigId = pydantic.Field(None, alias="Id")


class GetQueryLoggingConfigResponse(_Route53ModelBase):
    query_logging_config: "QueryLoggingConfig" = pydantic.Field(
        None, alias="QueryLoggingConfig"
    )


class GetReusableDelegationSetLimitRequest(_Route53ModelBase):
    type: ReusableDelegationSetLimitType = pydantic.Field(None, alias="Type")
    delegation_set_id: ResourceId = pydantic.Field(None, alias="DelegationSetId")


class GetReusableDelegationSetLimitResponse(_Route53ModelBase):
    limit: "ReusableDelegationSetLimit" = pydantic.Field(None, alias="Limit")
    count: UsageCount = pydantic.Field(None, alias="Count")


class GetReusableDelegationSetRequest(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")


class GetReusableDelegationSetResponse(_Route53ModelBase):
    delegation_set: "DelegationSet" = pydantic.Field(None, alias="DelegationSet")


class GetTrafficPolicyInstanceCountRequest(_Route53ModelBase):
    pass


class GetTrafficPolicyInstanceCountResponse(_Route53ModelBase):
    traffic_policy_instance_count: TrafficPolicyInstanceCount = pydantic.Field(
        None, alias="TrafficPolicyInstanceCount"
    )


class GetTrafficPolicyInstanceRequest(_Route53ModelBase):
    id: TrafficPolicyInstanceId = pydantic.Field(None, alias="Id")


class GetTrafficPolicyInstanceResponse(_Route53ModelBase):
    traffic_policy_instance: "TrafficPolicyInstance" = pydantic.Field(
        None, alias="TrafficPolicyInstance"
    )


class GetTrafficPolicyRequest(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    version: TrafficPolicyVersion = pydantic.Field(None, alias="Version")


class GetTrafficPolicyResponse(_Route53ModelBase):
    traffic_policy: "TrafficPolicy" = pydantic.Field(None, alias="TrafficPolicy")


class HealthCheck(_Route53ModelBase):
    id: HealthCheckId = pydantic.Field(None, alias="Id")
    caller_reference: HealthCheckNonce = pydantic.Field(None, alias="CallerReference")
    linked_service: "LinkedService" = pydantic.Field(None, alias="LinkedService")
    health_check_config: "HealthCheckConfig" = pydantic.Field(
        None, alias="HealthCheckConfig"
    )
    health_check_version: HealthCheckVersion = pydantic.Field(
        None, alias="HealthCheckVersion"
    )
    cloud_watch_alarm_configuration: "CloudWatchAlarmConfiguration" = pydantic.Field(
        None, alias="CloudWatchAlarmConfiguration"
    )


class HealthCheckConfig(_Route53ModelBase):
    ip_address: IPAddress = pydantic.Field(None, alias="IPAddress")
    port: Port = pydantic.Field(None, alias="Port")
    type: HealthCheckType = pydantic.Field(None, alias="Type")
    resource_path: ResourcePath = pydantic.Field(None, alias="ResourcePath")
    fully_qualified_domain_name: FullyQualifiedDomainName = pydantic.Field(
        None, alias="FullyQualifiedDomainName"
    )
    search_string: SearchString = pydantic.Field(None, alias="SearchString")
    request_interval: RequestInterval = pydantic.Field(None, alias="RequestInterval")
    failure_threshold: FailureThreshold = pydantic.Field(None, alias="FailureThreshold")
    measure_latency: MeasureLatency = pydantic.Field(None, alias="MeasureLatency")
    inverted: Inverted = pydantic.Field(None, alias="Inverted")
    disabled: Disabled = pydantic.Field(None, alias="Disabled")
    health_threshold: HealthThreshold = pydantic.Field(None, alias="HealthThreshold")
    child_health_checks: ChildHealthCheckList = pydantic.Field(
        None, alias="ChildHealthChecks"
    )
    enable_sni: EnableSNI = pydantic.Field(None, alias="EnableSNI")
    regions: HealthCheckRegionList = pydantic.Field(None, alias="Regions")
    alarm_identifier: "AlarmIdentifier" = pydantic.Field(None, alias="AlarmIdentifier")
    insufficient_data_health_status: InsufficientDataHealthStatus = pydantic.Field(
        None, alias="InsufficientDataHealthStatus"
    )
    routing_control_arn: RoutingControlArn = pydantic.Field(
        None, alias="RoutingControlArn"
    )


class HealthCheckObservation(_Route53ModelBase):
    region: HealthCheckRegion = pydantic.Field(None, alias="Region")
    ip_address: IPAddress = pydantic.Field(None, alias="IPAddress")
    status_report: "StatusReport" = pydantic.Field(None, alias="StatusReport")


class HostedZone(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")
    name: DNSName = pydantic.Field(None, alias="Name")
    caller_reference: Nonce = pydantic.Field(None, alias="CallerReference")
    config: "HostedZoneConfig" = pydantic.Field(None, alias="Config")
    resource_record_set_count: HostedZoneRRSetCount = pydantic.Field(
        None, alias="ResourceRecordSetCount"
    )
    linked_service: "LinkedService" = pydantic.Field(None, alias="LinkedService")


class HostedZoneConfig(_Route53ModelBase):
    comment: ResourceDescription = pydantic.Field(None, alias="Comment")
    private_zone: IsPrivateZone = pydantic.Field(None, alias="PrivateZone")


class HostedZoneLimit(_Route53ModelBase):
    type: HostedZoneLimitType = pydantic.Field(None, alias="Type")
    value: LimitValue = pydantic.Field(None, alias="Value")


class HostedZoneOwner(_Route53ModelBase):
    owning_account: AWSAccountID = pydantic.Field(None, alias="OwningAccount")
    owning_service: HostedZoneOwningService = pydantic.Field(
        None, alias="OwningService"
    )


class HostedZoneSummary(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    name: DNSName = pydantic.Field(None, alias="Name")
    owner: "HostedZoneOwner" = pydantic.Field(None, alias="Owner")


class KeySigningKey(_Route53ModelBase):
    name: SigningKeyName = pydantic.Field(None, alias="Name")
    kms_arn: SigningKeyString = pydantic.Field(None, alias="KmsArn")
    flag: SigningKeyInteger = pydantic.Field(None, alias="Flag")
    signing_algorithm_mnemonic: SigningKeyString = pydantic.Field(
        None, alias="SigningAlgorithmMnemonic"
    )
    signing_algorithm_type: SigningKeyInteger = pydantic.Field(
        None, alias="SigningAlgorithmType"
    )
    digest_algorithm_mnemonic: SigningKeyString = pydantic.Field(
        None, alias="DigestAlgorithmMnemonic"
    )
    digest_algorithm_type: SigningKeyInteger = pydantic.Field(
        None, alias="DigestAlgorithmType"
    )
    key_tag: SigningKeyTag = pydantic.Field(None, alias="KeyTag")
    digest_value: SigningKeyString = pydantic.Field(None, alias="DigestValue")
    public_key: SigningKeyString = pydantic.Field(None, alias="PublicKey")
    ds_record: SigningKeyString = pydantic.Field(None, alias="DSRecord")
    dnskey_record: SigningKeyString = pydantic.Field(None, alias="DNSKEYRecord")
    status: SigningKeyStatus = pydantic.Field(None, alias="Status")
    status_message: SigningKeyStatusMessage = pydantic.Field(
        None, alias="StatusMessage"
    )
    created_date: TimeStamp = pydantic.Field(None, alias="CreatedDate")
    last_modified_date: TimeStamp = pydantic.Field(None, alias="LastModifiedDate")


class LinkedService(_Route53ModelBase):
    service_principal: ServicePrincipal = pydantic.Field(None, alias="ServicePrincipal")
    description: ResourceDescription = pydantic.Field(None, alias="Description")


class ListCidrBlocksRequest(_Route53ModelBase):
    collection_id: UUID = pydantic.Field(None, alias="CollectionId")
    location_name: CidrLocationNameDefaultNotAllowed = pydantic.Field(
        None, alias="LocationName"
    )
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")


class ListCidrBlocksResponse(_Route53ModelBase):
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    cidr_blocks: CidrBlockSummaries = pydantic.Field(None, alias="CidrBlocks")


class ListCidrCollectionsRequest(_Route53ModelBase):
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")


class ListCidrCollectionsResponse(_Route53ModelBase):
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    cidr_collections: CollectionSummaries = pydantic.Field(
        None, alias="CidrCollections"
    )


class ListCidrLocationsRequest(_Route53ModelBase):
    collection_id: UUID = pydantic.Field(None, alias="CollectionId")
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")


class ListCidrLocationsResponse(_Route53ModelBase):
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    cidr_locations: LocationSummaries = pydantic.Field(None, alias="CidrLocations")


class ListGeoLocationsRequest(_Route53ModelBase):
    start_continent_code: GeoLocationContinentCode = pydantic.Field(
        None, alias="StartContinentCode"
    )
    start_country_code: GeoLocationCountryCode = pydantic.Field(
        None, alias="StartCountryCode"
    )
    start_subdivision_code: GeoLocationSubdivisionCode = pydantic.Field(
        None, alias="StartSubdivisionCode"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListGeoLocationsResponse(_Route53ModelBase):
    geo_location_details_list: GeoLocationDetailsList = pydantic.Field(
        None, alias="GeoLocationDetailsList"
    )
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    next_continent_code: GeoLocationContinentCode = pydantic.Field(
        None, alias="NextContinentCode"
    )
    next_country_code: GeoLocationCountryCode = pydantic.Field(
        None, alias="NextCountryCode"
    )
    next_subdivision_code: GeoLocationSubdivisionCode = pydantic.Field(
        None, alias="NextSubdivisionCode"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListHealthChecksRequest(_Route53ModelBase):
    marker: PageMarker = pydantic.Field(None, alias="Marker")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListHealthChecksResponse(_Route53ModelBase):
    health_checks: HealthChecks = pydantic.Field(None, alias="HealthChecks")
    marker: PageMarker = pydantic.Field(None, alias="Marker")
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    next_marker: PageMarker = pydantic.Field(None, alias="NextMarker")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListHostedZonesByNameRequest(_Route53ModelBase):
    dns_name: DNSName = pydantic.Field(None, alias="DNSName")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListHostedZonesByNameResponse(_Route53ModelBase):
    hosted_zones: HostedZones = pydantic.Field(None, alias="HostedZones")
    dns_name: DNSName = pydantic.Field(None, alias="DNSName")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    next_dns_name: DNSName = pydantic.Field(None, alias="NextDNSName")
    next_hosted_zone_id: ResourceId = pydantic.Field(None, alias="NextHostedZoneId")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListHostedZonesByVPCRequest(_Route53ModelBase):
    vpc_id: VPCId = pydantic.Field(None, alias="VPCId")
    vpc_region: VPCRegion = pydantic.Field(None, alias="VPCRegion")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")


class ListHostedZonesByVPCResponse(_Route53ModelBase):
    hosted_zone_summaries: HostedZoneSummaries = pydantic.Field(
        None, alias="HostedZoneSummaries"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")


class ListHostedZonesRequest(_Route53ModelBase):
    marker: PageMarker = pydantic.Field(None, alias="Marker")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")
    delegation_set_id: ResourceId = pydantic.Field(None, alias="DelegationSetId")


class ListHostedZonesResponse(_Route53ModelBase):
    hosted_zones: HostedZones = pydantic.Field(None, alias="HostedZones")
    marker: PageMarker = pydantic.Field(None, alias="Marker")
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    next_marker: PageMarker = pydantic.Field(None, alias="NextMarker")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListQueryLoggingConfigsRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")


class ListQueryLoggingConfigsResponse(_Route53ModelBase):
    query_logging_configs: QueryLoggingConfigs = pydantic.Field(
        None, alias="QueryLoggingConfigs"
    )
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")


class ListResourceRecordSetsRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    start_record_name: DNSName = pydantic.Field(None, alias="StartRecordName")
    start_record_type: RRType = pydantic.Field(None, alias="StartRecordType")
    start_record_identifier: ResourceRecordSetIdentifier = pydantic.Field(
        None, alias="StartRecordIdentifier"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListResourceRecordSetsResponse(_Route53ModelBase):
    resource_record_sets: ResourceRecordSets = pydantic.Field(
        None, alias="ResourceRecordSets"
    )
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    next_record_name: DNSName = pydantic.Field(None, alias="NextRecordName")
    next_record_type: RRType = pydantic.Field(None, alias="NextRecordType")
    next_record_identifier: ResourceRecordSetIdentifier = pydantic.Field(
        None, alias="NextRecordIdentifier"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListReusableDelegationSetsRequest(_Route53ModelBase):
    marker: PageMarker = pydantic.Field(None, alias="Marker")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListReusableDelegationSetsResponse(_Route53ModelBase):
    delegation_sets: DelegationSets = pydantic.Field(None, alias="DelegationSets")
    marker: PageMarker = pydantic.Field(None, alias="Marker")
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    next_marker: PageMarker = pydantic.Field(None, alias="NextMarker")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTagsForResourceRequest(_Route53ModelBase):
    resource_type: TagResourceType = pydantic.Field(None, alias="ResourceType")
    resource_id: TagResourceId = pydantic.Field(None, alias="ResourceId")


class ListTagsForResourceResponse(_Route53ModelBase):
    resource_tag_set: "ResourceTagSet" = pydantic.Field(None, alias="ResourceTagSet")


class ListTagsForResourcesRequest(_Route53ModelBase):
    resource_type: TagResourceType = pydantic.Field(None, alias="ResourceType")
    resource_ids: TagResourceIdList = pydantic.Field(None, alias="ResourceIds")


class ListTagsForResourcesResponse(_Route53ModelBase):
    resource_tag_sets: ResourceTagSetList = pydantic.Field(
        None, alias="ResourceTagSets"
    )


class ListTrafficPoliciesRequest(_Route53ModelBase):
    traffic_policy_id_marker: TrafficPolicyId = pydantic.Field(
        None, alias="TrafficPolicyIdMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPoliciesResponse(_Route53ModelBase):
    traffic_policy_summaries: TrafficPolicySummaries = pydantic.Field(
        None, alias="TrafficPolicySummaries"
    )
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    traffic_policy_id_marker: TrafficPolicyId = pydantic.Field(
        None, alias="TrafficPolicyIdMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyInstancesByHostedZoneRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    traffic_policy_instance_name_marker: DNSName = pydantic.Field(
        None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: RRType = pydantic.Field(
        None, alias="TrafficPolicyInstanceTypeMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyInstancesByHostedZoneResponse(_Route53ModelBase):
    traffic_policy_instances: TrafficPolicyInstances = pydantic.Field(
        None, alias="TrafficPolicyInstances"
    )
    traffic_policy_instance_name_marker: DNSName = pydantic.Field(
        None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: RRType = pydantic.Field(
        None, alias="TrafficPolicyInstanceTypeMarker"
    )
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyInstancesByPolicyRequest(_Route53ModelBase):
    traffic_policy_id: TrafficPolicyId = pydantic.Field(None, alias="TrafficPolicyId")
    traffic_policy_version: TrafficPolicyVersion = pydantic.Field(
        None, alias="TrafficPolicyVersion"
    )
    hosted_zone_id_marker: ResourceId = pydantic.Field(None, alias="HostedZoneIdMarker")
    traffic_policy_instance_name_marker: DNSName = pydantic.Field(
        None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: RRType = pydantic.Field(
        None, alias="TrafficPolicyInstanceTypeMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyInstancesByPolicyResponse(_Route53ModelBase):
    traffic_policy_instances: TrafficPolicyInstances = pydantic.Field(
        None, alias="TrafficPolicyInstances"
    )
    hosted_zone_id_marker: ResourceId = pydantic.Field(None, alias="HostedZoneIdMarker")
    traffic_policy_instance_name_marker: DNSName = pydantic.Field(
        None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: RRType = pydantic.Field(
        None, alias="TrafficPolicyInstanceTypeMarker"
    )
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyInstancesRequest(_Route53ModelBase):
    hosted_zone_id_marker: ResourceId = pydantic.Field(None, alias="HostedZoneIdMarker")
    traffic_policy_instance_name_marker: DNSName = pydantic.Field(
        None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: RRType = pydantic.Field(
        None, alias="TrafficPolicyInstanceTypeMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyInstancesResponse(_Route53ModelBase):
    traffic_policy_instances: TrafficPolicyInstances = pydantic.Field(
        None, alias="TrafficPolicyInstances"
    )
    hosted_zone_id_marker: ResourceId = pydantic.Field(None, alias="HostedZoneIdMarker")
    traffic_policy_instance_name_marker: DNSName = pydantic.Field(
        None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: RRType = pydantic.Field(
        None, alias="TrafficPolicyInstanceTypeMarker"
    )
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyVersionsRequest(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    traffic_policy_version_marker: TrafficPolicyVersionMarker = pydantic.Field(
        None, alias="TrafficPolicyVersionMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListTrafficPolicyVersionsResponse(_Route53ModelBase):
    traffic_policies: TrafficPolicies = pydantic.Field(None, alias="TrafficPolicies")
    is_truncated: PageTruncated = pydantic.Field(None, alias="IsTruncated")
    traffic_policy_version_marker: TrafficPolicyVersionMarker = pydantic.Field(
        None, alias="TrafficPolicyVersionMarker"
    )
    max_items: PageMaxItems = pydantic.Field(None, alias="MaxItems")


class ListVPCAssociationAuthorizationsRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")


class ListVPCAssociationAuthorizationsResponse(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    next_token: PaginationToken = pydantic.Field(None, alias="NextToken")
    vp_cs: VPCs = pydantic.Field(None, alias="VPCs")


class LocationSummary(_Route53ModelBase):
    location_name: CidrLocationNameDefaultAllowed = pydantic.Field(
        None, alias="LocationName"
    )


class QueryLoggingConfig(_Route53ModelBase):
    id: QueryLoggingConfigId = pydantic.Field(None, alias="Id")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    cloud_watch_logs_log_group_arn: CloudWatchLogsLogGroupArn = pydantic.Field(
        None, alias="CloudWatchLogsLogGroupArn"
    )


class ResourceRecord(_Route53ModelBase):
    value: RData = pydantic.Field(None, alias="Value")


class ResourceRecordSet(_Route53ModelBase):
    name: DNSName = pydantic.Field(None, alias="Name")
    type: RRType = pydantic.Field(None, alias="Type")
    set_identifier: ResourceRecordSetIdentifier = pydantic.Field(
        None, alias="SetIdentifier"
    )
    weight: ResourceRecordSetWeight = pydantic.Field(None, alias="Weight")
    region: ResourceRecordSetRegion = pydantic.Field(None, alias="Region")
    geo_location: "GeoLocation" = pydantic.Field(None, alias="GeoLocation")
    failover: ResourceRecordSetFailover = pydantic.Field(None, alias="Failover")
    multi_value_answer: ResourceRecordSetMultiValueAnswer = pydantic.Field(
        None, alias="MultiValueAnswer"
    )
    ttl: TTL = pydantic.Field(None, alias="TTL")
    resource_records: ResourceRecords = pydantic.Field(None, alias="ResourceRecords")
    alias_target: "AliasTarget" = pydantic.Field(None, alias="AliasTarget")
    health_check_id: HealthCheckId = pydantic.Field(None, alias="HealthCheckId")
    traffic_policy_instance_id: TrafficPolicyInstanceId = pydantic.Field(
        None, alias="TrafficPolicyInstanceId"
    )
    cidr_routing_config: "CidrRoutingConfig" = pydantic.Field(
        None, alias="CidrRoutingConfig"
    )


class ResourceTagSet(_Route53ModelBase):
    resource_type: TagResourceType = pydantic.Field(None, alias="ResourceType")
    resource_id: TagResourceId = pydantic.Field(None, alias="ResourceId")
    tags: TagList = pydantic.Field(None, alias="Tags")


class ReusableDelegationSetLimit(_Route53ModelBase):
    type: ReusableDelegationSetLimitType = pydantic.Field(None, alias="Type")
    value: LimitValue = pydantic.Field(None, alias="Value")


class StatusReport(_Route53ModelBase):
    status: Status = pydantic.Field(None, alias="Status")
    checked_time: TimeStamp = pydantic.Field(None, alias="CheckedTime")


class Tag(_Route53ModelBase):
    key: TagKey = pydantic.Field(None, alias="Key")
    value: TagValue = pydantic.Field(None, alias="Value")


class TestDNSAnswerRequest(_Route53ModelBase):
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    record_name: DNSName = pydantic.Field(None, alias="RecordName")
    record_type: RRType = pydantic.Field(None, alias="RecordType")
    resolver_ip: IPAddress = pydantic.Field(None, alias="ResolverIP")
    edns_0_client_subnet_ip: IPAddress = pydantic.Field(
        None, alias="EDNS0ClientSubnetIP"
    )
    edns_0_client_subnet_mask: SubnetMask = pydantic.Field(
        None, alias="EDNS0ClientSubnetMask"
    )


class TestDNSAnswerResponse(_Route53ModelBase):
    nameserver: Nameserver = pydantic.Field(None, alias="Nameserver")
    record_name: DNSName = pydantic.Field(None, alias="RecordName")
    record_type: RRType = pydantic.Field(None, alias="RecordType")
    record_data: RecordData = pydantic.Field(None, alias="RecordData")
    response_code: DNSRCode = pydantic.Field(None, alias="ResponseCode")
    protocol: TransportProtocol = pydantic.Field(None, alias="Protocol")


class TrafficPolicy(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    version: TrafficPolicyVersion = pydantic.Field(None, alias="Version")
    name: TrafficPolicyName = pydantic.Field(None, alias="Name")
    type: RRType = pydantic.Field(None, alias="Type")
    document: TrafficPolicyDocument = pydantic.Field(None, alias="Document")
    comment: TrafficPolicyComment = pydantic.Field(None, alias="Comment")


class TrafficPolicyInstance(_Route53ModelBase):
    id: TrafficPolicyInstanceId = pydantic.Field(None, alias="Id")
    hosted_zone_id: ResourceId = pydantic.Field(None, alias="HostedZoneId")
    name: DNSName = pydantic.Field(None, alias="Name")
    ttl: TTL = pydantic.Field(None, alias="TTL")
    state: TrafficPolicyInstanceState = pydantic.Field(None, alias="State")
    message: Message = pydantic.Field(None, alias="Message")
    traffic_policy_id: TrafficPolicyId = pydantic.Field(None, alias="TrafficPolicyId")
    traffic_policy_version: TrafficPolicyVersion = pydantic.Field(
        None, alias="TrafficPolicyVersion"
    )
    traffic_policy_type: RRType = pydantic.Field(None, alias="TrafficPolicyType")


class TrafficPolicySummary(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    name: TrafficPolicyName = pydantic.Field(None, alias="Name")
    type: RRType = pydantic.Field(None, alias="Type")
    latest_version: TrafficPolicyVersion = pydantic.Field(None, alias="LatestVersion")
    traffic_policy_count: TrafficPolicyVersion = pydantic.Field(
        None, alias="TrafficPolicyCount"
    )


class UpdateHealthCheckRequest(_Route53ModelBase):
    health_check_id: HealthCheckId = pydantic.Field(None, alias="HealthCheckId")
    health_check_version: HealthCheckVersion = pydantic.Field(
        None, alias="HealthCheckVersion"
    )
    ip_address: IPAddress = pydantic.Field(None, alias="IPAddress")
    port: Port = pydantic.Field(None, alias="Port")
    resource_path: ResourcePath = pydantic.Field(None, alias="ResourcePath")
    fully_qualified_domain_name: FullyQualifiedDomainName = pydantic.Field(
        None, alias="FullyQualifiedDomainName"
    )
    search_string: SearchString = pydantic.Field(None, alias="SearchString")
    failure_threshold: FailureThreshold = pydantic.Field(None, alias="FailureThreshold")
    inverted: Inverted = pydantic.Field(None, alias="Inverted")
    disabled: Disabled = pydantic.Field(None, alias="Disabled")
    health_threshold: HealthThreshold = pydantic.Field(None, alias="HealthThreshold")
    child_health_checks: ChildHealthCheckList = pydantic.Field(
        None, alias="ChildHealthChecks"
    )
    enable_sni: EnableSNI = pydantic.Field(None, alias="EnableSNI")
    regions: HealthCheckRegionList = pydantic.Field(None, alias="Regions")
    alarm_identifier: "AlarmIdentifier" = pydantic.Field(None, alias="AlarmIdentifier")
    insufficient_data_health_status: InsufficientDataHealthStatus = pydantic.Field(
        None, alias="InsufficientDataHealthStatus"
    )
    reset_elements: ResettableElementNameList = pydantic.Field(
        None, alias="ResetElements"
    )


class UpdateHealthCheckResponse(_Route53ModelBase):
    health_check: "HealthCheck" = pydantic.Field(None, alias="HealthCheck")


class UpdateHostedZoneCommentRequest(_Route53ModelBase):
    id: ResourceId = pydantic.Field(None, alias="Id")
    comment: ResourceDescription = pydantic.Field(None, alias="Comment")


class UpdateHostedZoneCommentResponse(_Route53ModelBase):
    hosted_zone: "HostedZone" = pydantic.Field(None, alias="HostedZone")


class UpdateTrafficPolicyCommentRequest(_Route53ModelBase):
    id: TrafficPolicyId = pydantic.Field(None, alias="Id")
    version: TrafficPolicyVersion = pydantic.Field(None, alias="Version")
    comment: TrafficPolicyComment = pydantic.Field(None, alias="Comment")


class UpdateTrafficPolicyCommentResponse(_Route53ModelBase):
    traffic_policy: "TrafficPolicy" = pydantic.Field(None, alias="TrafficPolicy")


class UpdateTrafficPolicyInstanceRequest(_Route53ModelBase):
    id: TrafficPolicyInstanceId = pydantic.Field(None, alias="Id")
    ttl: TTL = pydantic.Field(None, alias="TTL")
    traffic_policy_id: TrafficPolicyId = pydantic.Field(None, alias="TrafficPolicyId")
    traffic_policy_version: TrafficPolicyVersion = pydantic.Field(
        None, alias="TrafficPolicyVersion"
    )


class UpdateTrafficPolicyInstanceResponse(_Route53ModelBase):
    traffic_policy_instance: "TrafficPolicyInstance" = pydantic.Field(
        None, alias="TrafficPolicyInstance"
    )


class VPC(_Route53ModelBase):
    vpc_region: VPCRegion = pydantic.Field(None, alias="VPCRegion")
    vpc_id: VPCId = pydantic.Field(None, alias="VPCId")


AccountLimit.update_forward_refs()
ActivateKeySigningKeyRequest.update_forward_refs()
ActivateKeySigningKeyResponse.update_forward_refs()
AlarmIdentifier.update_forward_refs()
AliasTarget.update_forward_refs()
AssociateVPCWithHostedZoneRequest.update_forward_refs()
AssociateVPCWithHostedZoneResponse.update_forward_refs()
Change.update_forward_refs()
ChangeBatch.update_forward_refs()
ChangeCidrCollectionRequest.update_forward_refs()
ChangeCidrCollectionResponse.update_forward_refs()
ChangeInfo.update_forward_refs()
ChangeResourceRecordSetsRequest.update_forward_refs()
ChangeResourceRecordSetsResponse.update_forward_refs()
ChangeTagsForResourceRequest.update_forward_refs()
ChangeTagsForResourceResponse.update_forward_refs()
CidrBlockSummary.update_forward_refs()
CidrCollection.update_forward_refs()
CidrCollectionChange.update_forward_refs()
CidrRoutingConfig.update_forward_refs()
CloudWatchAlarmConfiguration.update_forward_refs()
CollectionSummary.update_forward_refs()
CreateCidrCollectionRequest.update_forward_refs()
CreateCidrCollectionResponse.update_forward_refs()
CreateHealthCheckRequest.update_forward_refs()
CreateHealthCheckResponse.update_forward_refs()
CreateHostedZoneRequest.update_forward_refs()
CreateHostedZoneResponse.update_forward_refs()
CreateKeySigningKeyRequest.update_forward_refs()
CreateKeySigningKeyResponse.update_forward_refs()
CreateQueryLoggingConfigRequest.update_forward_refs()
CreateQueryLoggingConfigResponse.update_forward_refs()
CreateReusableDelegationSetRequest.update_forward_refs()
CreateReusableDelegationSetResponse.update_forward_refs()
CreateTrafficPolicyInstanceRequest.update_forward_refs()
CreateTrafficPolicyInstanceResponse.update_forward_refs()
CreateTrafficPolicyRequest.update_forward_refs()
CreateTrafficPolicyResponse.update_forward_refs()
CreateTrafficPolicyVersionRequest.update_forward_refs()
CreateTrafficPolicyVersionResponse.update_forward_refs()
CreateVPCAssociationAuthorizationRequest.update_forward_refs()
CreateVPCAssociationAuthorizationResponse.update_forward_refs()
DNSSECStatus.update_forward_refs()
DeactivateKeySigningKeyRequest.update_forward_refs()
DeactivateKeySigningKeyResponse.update_forward_refs()
DelegationSet.update_forward_refs()
DeleteCidrCollectionRequest.update_forward_refs()
DeleteCidrCollectionResponse.update_forward_refs()
DeleteHealthCheckRequest.update_forward_refs()
DeleteHealthCheckResponse.update_forward_refs()
DeleteHostedZoneRequest.update_forward_refs()
DeleteHostedZoneResponse.update_forward_refs()
DeleteKeySigningKeyRequest.update_forward_refs()
DeleteKeySigningKeyResponse.update_forward_refs()
DeleteQueryLoggingConfigRequest.update_forward_refs()
DeleteQueryLoggingConfigResponse.update_forward_refs()
DeleteReusableDelegationSetRequest.update_forward_refs()
DeleteReusableDelegationSetResponse.update_forward_refs()
DeleteTrafficPolicyInstanceRequest.update_forward_refs()
DeleteTrafficPolicyInstanceResponse.update_forward_refs()
DeleteTrafficPolicyRequest.update_forward_refs()
DeleteTrafficPolicyResponse.update_forward_refs()
DeleteVPCAssociationAuthorizationRequest.update_forward_refs()
DeleteVPCAssociationAuthorizationResponse.update_forward_refs()
Dimension.update_forward_refs()
DisableHostedZoneDNSSECRequest.update_forward_refs()
DisableHostedZoneDNSSECResponse.update_forward_refs()
DisassociateVPCFromHostedZoneRequest.update_forward_refs()
DisassociateVPCFromHostedZoneResponse.update_forward_refs()
EnableHostedZoneDNSSECRequest.update_forward_refs()
EnableHostedZoneDNSSECResponse.update_forward_refs()
GeoLocation.update_forward_refs()
GeoLocationDetails.update_forward_refs()
GetAccountLimitRequest.update_forward_refs()
GetAccountLimitResponse.update_forward_refs()
GetChangeRequest.update_forward_refs()
GetChangeResponse.update_forward_refs()
GetCheckerIpRangesRequest.update_forward_refs()
GetCheckerIpRangesResponse.update_forward_refs()
GetDNSSECRequest.update_forward_refs()
GetDNSSECResponse.update_forward_refs()
GetGeoLocationRequest.update_forward_refs()
GetGeoLocationResponse.update_forward_refs()
GetHealthCheckCountRequest.update_forward_refs()
GetHealthCheckCountResponse.update_forward_refs()
GetHealthCheckLastFailureReasonRequest.update_forward_refs()
GetHealthCheckLastFailureReasonResponse.update_forward_refs()
GetHealthCheckRequest.update_forward_refs()
GetHealthCheckResponse.update_forward_refs()
GetHealthCheckStatusRequest.update_forward_refs()
GetHealthCheckStatusResponse.update_forward_refs()
GetHostedZoneCountRequest.update_forward_refs()
GetHostedZoneCountResponse.update_forward_refs()
GetHostedZoneLimitRequest.update_forward_refs()
GetHostedZoneLimitResponse.update_forward_refs()
GetHostedZoneRequest.update_forward_refs()
GetHostedZoneResponse.update_forward_refs()
GetQueryLoggingConfigRequest.update_forward_refs()
GetQueryLoggingConfigResponse.update_forward_refs()
GetReusableDelegationSetLimitRequest.update_forward_refs()
GetReusableDelegationSetLimitResponse.update_forward_refs()
GetReusableDelegationSetRequest.update_forward_refs()
GetReusableDelegationSetResponse.update_forward_refs()
GetTrafficPolicyInstanceCountRequest.update_forward_refs()
GetTrafficPolicyInstanceCountResponse.update_forward_refs()
GetTrafficPolicyInstanceRequest.update_forward_refs()
GetTrafficPolicyInstanceResponse.update_forward_refs()
GetTrafficPolicyRequest.update_forward_refs()
GetTrafficPolicyResponse.update_forward_refs()
HealthCheck.update_forward_refs()
HealthCheckConfig.update_forward_refs()
HealthCheckObservation.update_forward_refs()
HostedZone.update_forward_refs()
HostedZoneConfig.update_forward_refs()
HostedZoneLimit.update_forward_refs()
HostedZoneOwner.update_forward_refs()
HostedZoneSummary.update_forward_refs()
KeySigningKey.update_forward_refs()
LinkedService.update_forward_refs()
ListCidrBlocksRequest.update_forward_refs()
ListCidrBlocksResponse.update_forward_refs()
ListCidrCollectionsRequest.update_forward_refs()
ListCidrCollectionsResponse.update_forward_refs()
ListCidrLocationsRequest.update_forward_refs()
ListCidrLocationsResponse.update_forward_refs()
ListGeoLocationsRequest.update_forward_refs()
ListGeoLocationsResponse.update_forward_refs()
ListHealthChecksRequest.update_forward_refs()
ListHealthChecksResponse.update_forward_refs()
ListHostedZonesByNameRequest.update_forward_refs()
ListHostedZonesByNameResponse.update_forward_refs()
ListHostedZonesByVPCRequest.update_forward_refs()
ListHostedZonesByVPCResponse.update_forward_refs()
ListHostedZonesRequest.update_forward_refs()
ListHostedZonesResponse.update_forward_refs()
ListQueryLoggingConfigsRequest.update_forward_refs()
ListQueryLoggingConfigsResponse.update_forward_refs()
ListResourceRecordSetsRequest.update_forward_refs()
ListResourceRecordSetsResponse.update_forward_refs()
ListReusableDelegationSetsRequest.update_forward_refs()
ListReusableDelegationSetsResponse.update_forward_refs()
ListTagsForResourceRequest.update_forward_refs()
ListTagsForResourceResponse.update_forward_refs()
ListTagsForResourcesRequest.update_forward_refs()
ListTagsForResourcesResponse.update_forward_refs()
ListTrafficPoliciesRequest.update_forward_refs()
ListTrafficPoliciesResponse.update_forward_refs()
ListTrafficPolicyInstancesByHostedZoneRequest.update_forward_refs()
ListTrafficPolicyInstancesByHostedZoneResponse.update_forward_refs()
ListTrafficPolicyInstancesByPolicyRequest.update_forward_refs()
ListTrafficPolicyInstancesByPolicyResponse.update_forward_refs()
ListTrafficPolicyInstancesRequest.update_forward_refs()
ListTrafficPolicyInstancesResponse.update_forward_refs()
ListTrafficPolicyVersionsRequest.update_forward_refs()
ListTrafficPolicyVersionsResponse.update_forward_refs()
ListVPCAssociationAuthorizationsRequest.update_forward_refs()
ListVPCAssociationAuthorizationsResponse.update_forward_refs()
LocationSummary.update_forward_refs()
QueryLoggingConfig.update_forward_refs()
ResourceRecord.update_forward_refs()
ResourceRecordSet.update_forward_refs()
ResourceTagSet.update_forward_refs()
ReusableDelegationSetLimit.update_forward_refs()
StatusReport.update_forward_refs()
Tag.update_forward_refs()
TestDNSAnswerRequest.update_forward_refs()
TestDNSAnswerResponse.update_forward_refs()
TrafficPolicy.update_forward_refs()
TrafficPolicyInstance.update_forward_refs()
TrafficPolicySummary.update_forward_refs()
UpdateHealthCheckRequest.update_forward_refs()
UpdateHealthCheckResponse.update_forward_refs()
UpdateHostedZoneCommentRequest.update_forward_refs()
UpdateHostedZoneCommentResponse.update_forward_refs()
UpdateTrafficPolicyCommentRequest.update_forward_refs()
UpdateTrafficPolicyCommentResponse.update_forward_refs()
UpdateTrafficPolicyInstanceRequest.update_forward_refs()
UpdateTrafficPolicyInstanceResponse.update_forward_refs()
VPC.update_forward_refs()
