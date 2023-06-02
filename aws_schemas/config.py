from datetime import datetime
import typing
import enum

import pydantic


class _ConfigServiceModelBase(
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


ARN: str = pydantic.constr()
AccountId: str = pydantic.constr(regex=r"\d{12}")
AggregateConformancePackComplianceSummaryGroupKey: str = pydantic.constr()
AggregatedSourceStatusType: str = pydantic.constr()
AggregatedSourceType: str = pydantic.constr()
AllSupported: bool = pydantic.conbool()
AmazonResourceName: str = pydantic.constr(min_length=1, max_length=1000)
Annotation: str = pydantic.constr(max_length=256)
AutoRemediationAttemptSeconds: int = pydantic.conint()
AutoRemediationAttempts: int = pydantic.conint(ge=1, le=25)
AvailabilityZone: str = pydantic.constr()
AwsRegion: str = pydantic.constr(min_length=1, max_length=64)
BaseResourceId: str = pydantic.constr(min_length=1, max_length=768)
Boolean: bool = pydantic.conbool()
ChannelName: str = pydantic.constr(min_length=1, max_length=256)
ChronologicalOrder: str = pydantic.constr()
ClientToken: str = pydantic.constr(min_length=64, max_length=256)
ComplianceScore: str = pydantic.constr()
ComplianceType: str = pydantic.constr()
ConfigRuleComplianceSummaryGroupKey: str = pydantic.constr()
ConfigRuleName: str = pydantic.constr(min_length=1, max_length=128, regex=r".*\S.*")
ConfigRuleState: str = pydantic.constr()
Configuration: str = pydantic.constr()
ConfigurationAggregatorArn: str = pydantic.constr(
    regex=r"arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:config-aggregator/config-aggregator-[a-z\d]+"
)
ConfigurationAggregatorName: str = pydantic.constr(
    min_length=1, max_length=256, regex=r"[\w\-]+"
)
ConfigurationItemCaptureTime: datetime = pydantic.condate()
ConfigurationItemMD5Hash: str = pydantic.constr()
ConfigurationItemStatus: str = pydantic.constr()
ConfigurationStateId: str = pydantic.constr()
ConformancePackArn: str = pydantic.constr(min_length=1, max_length=2048)
ConformancePackComplianceType: str = pydantic.constr()
ConformancePackId: str = pydantic.constr(min_length=1, max_length=1024)
ConformancePackName: str = pydantic.constr(
    min_length=1, max_length=256, regex=r"[a-zA-Z][-a-zA-Z0-9]*"
)
ConformancePackState: str = pydantic.constr()
ConformancePackStatusReason: str = pydantic.constr(max_length=2000)
CosmosPageLimit: int = pydantic.conint(le=100)
Date: datetime = pydantic.condate()
DeliveryS3Bucket: str = pydantic.constr(max_length=63)
DeliveryS3KeyPrefix: str = pydantic.constr(max_length=1024)
DeliveryStatus: str = pydantic.constr()
DescribeConformancePackComplianceLimit: int = pydantic.conint(le=1000)
DescribePendingAggregationRequestsLimit: int = pydantic.conint(le=20)
EarlierTime: datetime = pydantic.condate()
EmptiableStringWithCharLimit256: str = pydantic.constr(max_length=256)
ErrorMessage: str = pydantic.constr()
EvaluationContextIdentifier: str = pydantic.constr(min_length=1, max_length=128)
EvaluationMode: str = pydantic.constr()
EvaluationTimeout: int = pydantic.conint(le=3600)
EventSource: str = pydantic.constr()
Expression: str = pydantic.constr(min_length=1, max_length=4096)
FieldName: str = pydantic.constr()
GetConformancePackComplianceDetailsLimit: int = pydantic.conint(le=100)
GroupByAPILimit: int = pydantic.conint(le=1000)
IncludeGlobalResourceTypes: bool = pydantic.conbool()
Integer: int = pydantic.conint()
LastUpdatedTime: datetime = pydantic.condate()
LaterTime: datetime = pydantic.condate()
Limit: int = pydantic.conint(le=100)
ListResourceEvaluationsPageItemLimit: int = pydantic.conint(le=100)
Long: int = pydantic.conint()
MaximumExecutionFrequency: str = pydantic.constr()
MemberAccountRuleStatus: str = pydantic.constr()
MessageType: str = pydantic.constr()
Name: str = pydantic.constr()
NextToken: str = pydantic.constr()
OrderingTimestamp: datetime = pydantic.condate()
OrganizationConfigRuleName: str = pydantic.constr(
    min_length=1, max_length=64, regex=r".*\S.*"
)
OrganizationConfigRuleTriggerType: str = pydantic.constr()
OrganizationConfigRuleTriggerTypeNoSN: str = pydantic.constr()
OrganizationConformancePackName: str = pydantic.constr(
    min_length=1, max_length=128, regex=r"[a-zA-Z][-a-zA-Z0-9]*"
)
OrganizationResourceDetailedStatus: str = pydantic.constr()
OrganizationResourceStatus: str = pydantic.constr()
OrganizationRuleStatus: str = pydantic.constr()
Owner: str = pydantic.constr()
PageSizeLimit: int = pydantic.conint(le=20)
ParameterName: str = pydantic.constr(max_length=255)
ParameterValue: str = pydantic.constr(max_length=4096)
Percentage: int = pydantic.conint(ge=1, le=100)
PolicyRuntime: str = pydantic.constr(
    min_length=1, max_length=64, regex=r"guard\-2\.x\.x"
)
PolicyText: str = pydantic.constr(max_length=10000)
QueryArn: str = pydantic.constr(
    min_length=1,
    max_length=500,
    regex=r"^arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:stored-query/[a-zA-Z0-9-_]+/query-[a-zA-Z\d-_/]+$",
)
QueryDescription: str = pydantic.constr(max_length=256, regex=r"[\s\S]*")
QueryExpression: str = pydantic.constr(min_length=1, max_length=4096, regex=r"[\s\S]*")
QueryId: str = pydantic.constr(min_length=1, max_length=36, regex=r"^\S+$")
QueryName: str = pydantic.constr(min_length=1, max_length=64, regex=r"^[a-zA-Z0-9-_]+$")
RecorderName: str = pydantic.constr(min_length=1, max_length=256)
RecorderStatus: str = pydantic.constr()
RecordingStrategyType: str = pydantic.constr()
RelatedEvent: str = pydantic.constr()
RelationshipName: str = pydantic.constr()
RemediationExecutionState: str = pydantic.constr()
RemediationExecutionStepState: str = pydantic.constr()
RemediationParameters: dict = pydantic.condict()
RemediationTargetType: str = pydantic.constr()
ResourceConfiguration: str = pydantic.constr(min_length=1, max_length=51200)
ResourceConfigurationSchemaType: str = pydantic.constr()
ResourceCountGroupKey: str = pydantic.constr()
ResourceCreationTime: datetime = pydantic.condate()
ResourceDeletionTime: datetime = pydantic.condate()
ResourceEvaluationId: str = pydantic.constr(min_length=1, max_length=128)
ResourceEvaluationStatus: str = pydantic.constr()
ResourceId: str = pydantic.constr(min_length=1, max_length=768)
ResourceName: str = pydantic.constr()
ResourceType: str = pydantic.constr()
ResourceTypeString: str = pydantic.constr(min_length=1, max_length=196)
ResourceValueType: str = pydantic.constr()
RetentionConfigurationName: str = pydantic.constr(
    min_length=1, max_length=256, regex=r"[\w\-]+"
)
RetentionPeriodInDays: int = pydantic.conint(ge=30, le=2557)
RuleLimit: int = pydantic.conint(le=50)
SSMDocumentName: str = pydantic.constr(regex=r"^[a-zA-Z0-9_\-.:/]{3,200}$")
SSMDocumentVersion: str = pydantic.constr(regex=r"([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)")
SchemaVersionId: str = pydantic.constr(
    min_length=1, max_length=128, regex=r"[A-Za-z0-9-]+"
)
SortBy: str = pydantic.constr()
SortOrder: str = pydantic.constr()
StackArn: str = pydantic.constr(min_length=1, max_length=2048)
String: str = pydantic.constr()
StringWithCharLimit1024: str = pydantic.constr(min_length=1, max_length=1024)
StringWithCharLimit128: str = pydantic.constr(min_length=1, max_length=128)
StringWithCharLimit2048: str = pydantic.constr(min_length=1, max_length=2048)
StringWithCharLimit256: str = pydantic.constr(min_length=1, max_length=256)
StringWithCharLimit256Min0: str = pydantic.constr(max_length=256)
StringWithCharLimit64: str = pydantic.constr(min_length=1, max_length=64)
StringWithCharLimit768: str = pydantic.constr(min_length=1, max_length=768)
SupplementaryConfiguration: dict = pydantic.condict()
SupplementaryConfigurationName: str = pydantic.constr()
SupplementaryConfigurationValue: str = pydantic.constr()
TagKey: str = pydantic.constr(min_length=1, max_length=128)
TagValue: str = pydantic.constr(max_length=256)
Tags: dict = pydantic.condict()
TemplateBody: str = pydantic.constr(min_length=1, max_length=51200)
TemplateS3Uri: str = pydantic.constr(min_length=1, max_length=1024, regex=r"s3://.*")
Value: str = pydantic.constr()
Version: str = pydantic.constr()

AccountAggregationSourceAccountList = typing.List["AccountId"]
AccountAggregationSourceList = typing.List["AccountAggregationSource"]
AggregateComplianceByConfigRuleList = typing.List["AggregateComplianceByConfigRule"]
AggregateComplianceByConformancePackList = typing.List[
    "AggregateComplianceByConformancePack"
]
AggregateComplianceCountList = typing.List["AggregateComplianceCount"]
AggregateConformancePackComplianceSummaryList = typing.List[
    "AggregateConformancePackComplianceSummary"
]
AggregateEvaluationResultList = typing.List["AggregateEvaluationResult"]
AggregatedSourceStatusList = typing.List["AggregatedSourceStatus"]
AggregatedSourceStatusTypeList = typing.List["AggregatedSourceStatusType"]
AggregationAuthorizationList = typing.List["AggregationAuthorization"]
AggregatorRegionList = typing.List["String"]
BaseConfigurationItems = typing.List["BaseConfigurationItem"]
ComplianceByConfigRules = typing.List["ComplianceByConfigRule"]
ComplianceByResources = typing.List["ComplianceByResource"]
ComplianceResourceTypes = typing.List["StringWithCharLimit256"]
ComplianceSummariesByResourceType = typing.List["ComplianceSummaryByResourceType"]
ComplianceTypes = typing.List["ComplianceType"]
ConfigRuleEvaluationStatusList = typing.List["ConfigRuleEvaluationStatus"]
ConfigRuleNames = typing.List["ConfigRuleName"]
ConfigRules = typing.List["ConfigRule"]
ConfigurationAggregatorList = typing.List["ConfigurationAggregator"]
ConfigurationAggregatorNameList = typing.List["ConfigurationAggregatorName"]
ConfigurationItemList = typing.List["ConfigurationItem"]
ConfigurationRecorderList = typing.List["ConfigurationRecorder"]
ConfigurationRecorderNameList = typing.List["RecorderName"]
ConfigurationRecorderStatusList = typing.List["ConfigurationRecorderStatus"]
ConformancePackComplianceResourceIds = typing.List["StringWithCharLimit256"]
ConformancePackComplianceScores = typing.List["ConformancePackComplianceScore"]
ConformancePackComplianceSummaryList = typing.List["ConformancePackComplianceSummary"]
ConformancePackConfigRuleNames = typing.List["StringWithCharLimit64"]
ConformancePackDetailList = typing.List["ConformancePackDetail"]
ConformancePackInputParameters = typing.List["ConformancePackInputParameter"]
ConformancePackNameFilter = typing.List["ConformancePackName"]
ConformancePackNamesList = typing.List["ConformancePackName"]
ConformancePackNamesToSummarizeList = typing.List["ConformancePackName"]
ConformancePackRuleComplianceList = typing.List["ConformancePackRuleCompliance"]
ConformancePackRuleEvaluationResultsList = typing.List[
    "ConformancePackEvaluationResult"
]
ConformancePackStatusDetailsList = typing.List["ConformancePackStatusDetail"]
ControlsList = typing.List["StringWithCharLimit128"]
DebugLogDeliveryAccounts = typing.List["AccountId"]
DeliveryChannelList = typing.List["DeliveryChannel"]
DeliveryChannelNameList = typing.List["ChannelName"]
DeliveryChannelStatusList = typing.List["DeliveryChannelStatus"]
DiscoveredResourceIdentifierList = typing.List["AggregateResourceIdentifier"]
EvaluationModes = typing.List["EvaluationModeConfiguration"]
EvaluationResults = typing.List["EvaluationResult"]
Evaluations = typing.List["Evaluation"]
ExcludedAccounts = typing.List["AccountId"]
FailedDeleteRemediationExceptionsBatches = typing.List[
    "FailedDeleteRemediationExceptionsBatch"
]
FailedRemediationBatches = typing.List["FailedRemediationBatch"]
FailedRemediationExceptionBatches = typing.List["FailedRemediationExceptionBatch"]
FieldInfoList = typing.List["FieldInfo"]
GroupedResourceCountList = typing.List["GroupedResourceCount"]
OrganizationConfigRuleDetailedStatus = typing.List["MemberAccountStatus"]
OrganizationConfigRuleNames = typing.List["StringWithCharLimit64"]
OrganizationConfigRuleStatuses = typing.List["OrganizationConfigRuleStatus"]
OrganizationConfigRuleTriggerTypeNoSNs = typing.List[
    "OrganizationConfigRuleTriggerTypeNoSN"
]
OrganizationConfigRuleTriggerTypes = typing.List["OrganizationConfigRuleTriggerType"]
OrganizationConfigRules = typing.List["OrganizationConfigRule"]
OrganizationConformancePackDetailedStatuses = typing.List[
    "OrganizationConformancePackDetailedStatus"
]
OrganizationConformancePackNames = typing.List["OrganizationConformancePackName"]
OrganizationConformancePackStatuses = typing.List["OrganizationConformancePackStatus"]
OrganizationConformancePacks = typing.List["OrganizationConformancePack"]
PendingAggregationRequestList = typing.List["PendingAggregationRequest"]
ReevaluateConfigRuleNames = typing.List["ConfigRuleName"]
RelatedEventList = typing.List["RelatedEvent"]
RelationshipList = typing.List["Relationship"]
RemediationConfigurations = typing.List["RemediationConfiguration"]
RemediationExceptionResourceKeys = typing.List["RemediationExceptionResourceKey"]
RemediationExceptions = typing.List["RemediationException"]
RemediationExecutionStatuses = typing.List["RemediationExecutionStatus"]
RemediationExecutionSteps = typing.List["RemediationExecutionStep"]
ResourceCounts = typing.List["ResourceCount"]
ResourceEvaluations = typing.List["ResourceEvaluation"]
ResourceIdList = typing.List["ResourceId"]
ResourceIdentifierList = typing.List["ResourceIdentifier"]
ResourceIdentifiersList = typing.List["AggregateResourceIdentifier"]
ResourceKeys = typing.List["ResourceKey"]
ResourceTypeList = typing.List["ResourceType"]
ResourceTypes = typing.List["StringWithCharLimit256"]
ResourceTypesScope = typing.List["StringWithCharLimit256"]
Results = typing.List["String"]
RetentionConfigurationList = typing.List["RetentionConfiguration"]
RetentionConfigurationNameList = typing.List["RetentionConfigurationName"]
SourceDetails = typing.List["SourceDetail"]
StaticParameterValues = typing.List["StringWithCharLimit256"]
StoredQueryMetadataList = typing.List["StoredQueryMetadata"]
TagKeyList = typing.List["TagKey"]
TagList = typing.List["Tag"]
TagsList = typing.List["Tag"]
UnprocessedResourceIdentifierList = typing.List["AggregateResourceIdentifier"]


class AggregateConformancePackComplianceSummaryGroupKey(enum.Enum):
    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


class AggregatedSourceStatusType(enum.Enum):
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    OUTDATED = "OUTDATED"


class AggregatedSourceType(enum.Enum):
    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"


class ChronologicalOrder(enum.Enum):
    REVERSE = "Reverse"
    FORWARD = "Forward"


class ComplianceType(enum.Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class ConfigRuleComplianceSummaryGroupKey(enum.Enum):
    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


class ConfigRuleState(enum.Enum):
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETING_RESULTS = "DELETING_RESULTS"
    EVALUATING = "EVALUATING"


class ConfigurationItemStatus(enum.Enum):
    OK = "OK"
    RESOURCEDISCOVERED = "ResourceDiscovered"
    RESOURCENOTRECORDED = "ResourceNotRecorded"
    RESOURCEDELETED = "ResourceDeleted"
    RESOURCEDELETEDNOTRECORDED = "ResourceDeletedNotRecorded"


class ConformancePackComplianceType(enum.Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class ConformancePackState(enum.Enum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class DeliveryStatus(enum.Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
    NOT_APPLICABLE = "Not_Applicable"


class EvaluationMode(enum.Enum):
    DETECTIVE = "DETECTIVE"
    PROACTIVE = "PROACTIVE"


class EventSource(enum.Enum):
    AWS_CONFIG = "aws.config"


class MaximumExecutionFrequency(enum.Enum):
    ONE_HOUR = "One_Hour"
    THREE_HOURS = "Three_Hours"
    SIX_HOURS = "Six_Hours"
    TWELVE_HOURS = "Twelve_Hours"
    TWENTYFOUR_HOURS = "TwentyFour_Hours"


class MemberAccountRuleStatus(enum.Enum):
    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class MessageType(enum.Enum):
    CONFIGURATIONITEMCHANGENOTIFICATION = "ConfigurationItemChangeNotification"
    CONFIGURATIONSNAPSHOTDELIVERYCOMPLETED = "ConfigurationSnapshotDeliveryCompleted"
    SCHEDULEDNOTIFICATION = "ScheduledNotification"
    OVERSIZEDCONFIGURATIONITEMCHANGENOTIFICATION = (
        "OversizedConfigurationItemChangeNotification"
    )


class OrganizationConfigRuleTriggerType(enum.Enum):
    CONFIGURATIONITEMCHANGENOTIFICATION = "ConfigurationItemChangeNotification"
    OVERSIZEDCONFIGURATIONITEMCHANGENOTIFICATION = (
        "OversizedConfigurationItemChangeNotification"
    )
    SCHEDULEDNOTIFICATION = "ScheduledNotification"


class OrganizationConfigRuleTriggerTypeNoSN(enum.Enum):
    CONFIGURATIONITEMCHANGENOTIFICATION = "ConfigurationItemChangeNotification"
    OVERSIZEDCONFIGURATIONITEMCHANGENOTIFICATION = (
        "OversizedConfigurationItemChangeNotification"
    )


class OrganizationResourceDetailedStatus(enum.Enum):
    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class OrganizationResourceStatus(enum.Enum):
    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class OrganizationRuleStatus(enum.Enum):
    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class Owner(enum.Enum):
    CUSTOM_LAMBDA = "CUSTOM_LAMBDA"
    AWS = "AWS"
    CUSTOM_POLICY = "CUSTOM_POLICY"


class RecorderStatus(enum.Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILURE = "Failure"


class RecordingStrategyType(enum.Enum):
    ALL_SUPPORTED_RESOURCE_TYPES = "ALL_SUPPORTED_RESOURCE_TYPES"
    INCLUSION_BY_RESOURCE_TYPES = "INCLUSION_BY_RESOURCE_TYPES"
    EXCLUSION_BY_RESOURCE_TYPES = "EXCLUSION_BY_RESOURCE_TYPES"


class RemediationExecutionState(enum.Enum):
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class RemediationExecutionStepState(enum.Enum):
    SUCCEEDED = "SUCCEEDED"
    PENDING = "PENDING"
    FAILED = "FAILED"


class RemediationTargetType(enum.Enum):
    SSM_DOCUMENT = "SSM_DOCUMENT"


class ResourceConfigurationSchemaType(enum.Enum):
    CFN_RESOURCE_SCHEMA = "CFN_RESOURCE_SCHEMA"


class ResourceCountGroupKey(enum.Enum):
    RESOURCE_TYPE = "RESOURCE_TYPE"
    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


class ResourceEvaluationStatus(enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class ResourceType(enum.Enum):
    AWS__EC2__CUSTOMERGATEWAY = "AWS::EC2::CustomerGateway"
    AWS__EC2__EIP = "AWS::EC2::EIP"
    AWS__EC2__HOST = "AWS::EC2::Host"
    AWS__EC2__INSTANCE = "AWS::EC2::Instance"
    AWS__EC2__INTERNETGATEWAY = "AWS::EC2::InternetGateway"
    AWS__EC2__NETWORKACL = "AWS::EC2::NetworkAcl"
    AWS__EC2__NETWORKINTERFACE = "AWS::EC2::NetworkInterface"
    AWS__EC2__ROUTETABLE = "AWS::EC2::RouteTable"
    AWS__EC2__SECURITYGROUP = "AWS::EC2::SecurityGroup"
    AWS__EC2__SUBNET = "AWS::EC2::Subnet"
    AWS__CLOUDTRAIL__TRAIL = "AWS::CloudTrail::Trail"
    AWS__EC2__VOLUME = "AWS::EC2::Volume"
    AWS__EC2__VPC = "AWS::EC2::VPC"
    AWS__EC2__VPNCONNECTION = "AWS::EC2::VPNConnection"
    AWS__EC2__VPNGATEWAY = "AWS::EC2::VPNGateway"
    AWS__EC2__REGISTEREDHAINSTANCE = "AWS::EC2::RegisteredHAInstance"
    AWS__EC2__NATGATEWAY = "AWS::EC2::NatGateway"
    AWS__EC2__EGRESSONLYINTERNETGATEWAY = "AWS::EC2::EgressOnlyInternetGateway"
    AWS__EC2__VPCENDPOINT = "AWS::EC2::VPCEndpoint"
    AWS__EC2__VPCENDPOINTSERVICE = "AWS::EC2::VPCEndpointService"
    AWS__EC2__FLOWLOG = "AWS::EC2::FlowLog"
    AWS__EC2__VPCPEERINGCONNECTION = "AWS::EC2::VPCPeeringConnection"
    AWS__ELASTICSEARCH__DOMAIN = "AWS::Elasticsearch::Domain"
    AWS__IAM__GROUP = "AWS::IAM::Group"
    AWS__IAM__POLICY = "AWS::IAM::Policy"
    AWS__IAM__ROLE = "AWS::IAM::Role"
    AWS__IAM__USER = "AWS::IAM::User"
    AWS__ELASTICLOADBALANCINGV2__LOADBALANCER = (
        "AWS::ElasticLoadBalancingV2::LoadBalancer"
    )
    AWS__ACM__CERTIFICATE = "AWS::ACM::Certificate"
    AWS__RDS__DBINSTANCE = "AWS::RDS::DBInstance"
    AWS__RDS__DBSUBNETGROUP = "AWS::RDS::DBSubnetGroup"
    AWS__RDS__DBSECURITYGROUP = "AWS::RDS::DBSecurityGroup"
    AWS__RDS__DBSNAPSHOT = "AWS::RDS::DBSnapshot"
    AWS__RDS__DBCLUSTER = "AWS::RDS::DBCluster"
    AWS__RDS__DBCLUSTERSNAPSHOT = "AWS::RDS::DBClusterSnapshot"
    AWS__RDS__EVENTSUBSCRIPTION = "AWS::RDS::EventSubscription"
    AWS__S3__BUCKET = "AWS::S3::Bucket"
    AWS__S3__ACCOUNTPUBLICACCESSBLOCK = "AWS::S3::AccountPublicAccessBlock"
    AWS__REDSHIFT__CLUSTER = "AWS::Redshift::Cluster"
    AWS__REDSHIFT__CLUSTERSNAPSHOT = "AWS::Redshift::ClusterSnapshot"
    AWS__REDSHIFT__CLUSTERPARAMETERGROUP = "AWS::Redshift::ClusterParameterGroup"
    AWS__REDSHIFT__CLUSTERSECURITYGROUP = "AWS::Redshift::ClusterSecurityGroup"
    AWS__REDSHIFT__CLUSTERSUBNETGROUP = "AWS::Redshift::ClusterSubnetGroup"
    AWS__REDSHIFT__EVENTSUBSCRIPTION = "AWS::Redshift::EventSubscription"
    AWS__SSM__MANAGEDINSTANCEINVENTORY = "AWS::SSM::ManagedInstanceInventory"
    AWS__CLOUDWATCH__ALARM = "AWS::CloudWatch::Alarm"
    AWS__CLOUDFORMATION__STACK = "AWS::CloudFormation::Stack"
    AWS__ELASTICLOADBALANCING__LOADBALANCER = "AWS::ElasticLoadBalancing::LoadBalancer"
    AWS__AUTOSCALING__AUTOSCALINGGROUP = "AWS::AutoScaling::AutoScalingGroup"
    AWS__AUTOSCALING__LAUNCHCONFIGURATION = "AWS::AutoScaling::LaunchConfiguration"
    AWS__AUTOSCALING__SCALINGPOLICY = "AWS::AutoScaling::ScalingPolicy"
    AWS__AUTOSCALING__SCHEDULEDACTION = "AWS::AutoScaling::ScheduledAction"
    AWS__DYNAMODB__TABLE = "AWS::DynamoDB::Table"
    AWS__CODEBUILD__PROJECT = "AWS::CodeBuild::Project"
    AWS__WAF__RATEBASEDRULE = "AWS::WAF::RateBasedRule"
    AWS__WAF__RULE = "AWS::WAF::Rule"
    AWS__WAF__RULEGROUP = "AWS::WAF::RuleGroup"
    AWS__WAF__WEBACL = "AWS::WAF::WebACL"
    AWS__WAFREGIONAL__RATEBASEDRULE = "AWS::WAFRegional::RateBasedRule"
    AWS__WAFREGIONAL__RULE = "AWS::WAFRegional::Rule"
    AWS__WAFREGIONAL__RULEGROUP = "AWS::WAFRegional::RuleGroup"
    AWS__WAFREGIONAL__WEBACL = "AWS::WAFRegional::WebACL"
    AWS__CLOUDFRONT__DISTRIBUTION = "AWS::CloudFront::Distribution"
    AWS__CLOUDFRONT__STREAMINGDISTRIBUTION = "AWS::CloudFront::StreamingDistribution"
    AWS__LAMBDA__FUNCTION = "AWS::Lambda::Function"
    AWS__NETWORKFIREWALL__FIREWALL = "AWS::NetworkFirewall::Firewall"
    AWS__NETWORKFIREWALL__FIREWALLPOLICY = "AWS::NetworkFirewall::FirewallPolicy"
    AWS__NETWORKFIREWALL__RULEGROUP = "AWS::NetworkFirewall::RuleGroup"
    AWS__ELASTICBEANSTALK__APPLICATION = "AWS::ElasticBeanstalk::Application"
    AWS__ELASTICBEANSTALK__APPLICATIONVERSION = (
        "AWS::ElasticBeanstalk::ApplicationVersion"
    )
    AWS__ELASTICBEANSTALK__ENVIRONMENT = "AWS::ElasticBeanstalk::Environment"
    AWS__WAFV2__WEBACL = "AWS::WAFv2::WebACL"
    AWS__WAFV2__RULEGROUP = "AWS::WAFv2::RuleGroup"
    AWS__WAFV2__IPSET = "AWS::WAFv2::IPSet"
    AWS__WAFV2__REGEXPATTERNSET = "AWS::WAFv2::RegexPatternSet"
    AWS__WAFV2__MANAGEDRULESET = "AWS::WAFv2::ManagedRuleSet"
    AWS__XRAY__ENCRYPTIONCONFIG = "AWS::XRay::EncryptionConfig"
    AWS__SSM__ASSOCIATIONCOMPLIANCE = "AWS::SSM::AssociationCompliance"
    AWS__SSM__PATCHCOMPLIANCE = "AWS::SSM::PatchCompliance"
    AWS__SHIELD__PROTECTION = "AWS::Shield::Protection"
    AWS__SHIELDREGIONAL__PROTECTION = "AWS::ShieldRegional::Protection"
    AWS__CONFIG__CONFORMANCEPACKCOMPLIANCE = "AWS::Config::ConformancePackCompliance"
    AWS__CONFIG__RESOURCECOMPLIANCE = "AWS::Config::ResourceCompliance"
    AWS__APIGATEWAY__STAGE = "AWS::ApiGateway::Stage"
    AWS__APIGATEWAY__RESTAPI = "AWS::ApiGateway::RestApi"
    AWS__APIGATEWAYV2__STAGE = "AWS::ApiGatewayV2::Stage"
    AWS__APIGATEWAYV2__API = "AWS::ApiGatewayV2::Api"
    AWS__CODEPIPELINE__PIPELINE = "AWS::CodePipeline::Pipeline"
    AWS__SERVICECATALOG__CLOUDFORMATIONPROVISIONEDPRODUCT = (
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct"
    )
    AWS__SERVICECATALOG__CLOUDFORMATIONPRODUCT = (
        "AWS::ServiceCatalog::CloudFormationProduct"
    )
    AWS__SERVICECATALOG__PORTFOLIO = "AWS::ServiceCatalog::Portfolio"
    AWS__SQS__QUEUE = "AWS::SQS::Queue"
    AWS__KMS__KEY = "AWS::KMS::Key"
    AWS__QLDB__LEDGER = "AWS::QLDB::Ledger"
    AWS__SECRETSMANAGER__SECRET = "AWS::SecretsManager::Secret"
    AWS__SNS__TOPIC = "AWS::SNS::Topic"
    AWS__SSM__FILEDATA = "AWS::SSM::FileData"
    AWS__BACKUP__BACKUPPLAN = "AWS::Backup::BackupPlan"
    AWS__BACKUP__BACKUPSELECTION = "AWS::Backup::BackupSelection"
    AWS__BACKUP__BACKUPVAULT = "AWS::Backup::BackupVault"
    AWS__BACKUP__RECOVERYPOINT = "AWS::Backup::RecoveryPoint"
    AWS__ECR__REPOSITORY = "AWS::ECR::Repository"
    AWS__ECS__CLUSTER = "AWS::ECS::Cluster"
    AWS__ECS__SERVICE = "AWS::ECS::Service"
    AWS__ECS__TASKDEFINITION = "AWS::ECS::TaskDefinition"
    AWS__EFS__ACCESSPOINT = "AWS::EFS::AccessPoint"
    AWS__EFS__FILESYSTEM = "AWS::EFS::FileSystem"
    AWS__EKS__CLUSTER = "AWS::EKS::Cluster"
    AWS__OPENSEARCH__DOMAIN = "AWS::OpenSearch::Domain"
    AWS__EC2__TRANSITGATEWAY = "AWS::EC2::TransitGateway"
    AWS__KINESIS__STREAM = "AWS::Kinesis::Stream"
    AWS__KINESIS__STREAMCONSUMER = "AWS::Kinesis::StreamConsumer"
    AWS__CODEDEPLOY__APPLICATION = "AWS::CodeDeploy::Application"
    AWS__CODEDEPLOY__DEPLOYMENTCONFIG = "AWS::CodeDeploy::DeploymentConfig"
    AWS__CODEDEPLOY__DEPLOYMENTGROUP = "AWS::CodeDeploy::DeploymentGroup"
    AWS__EC2__LAUNCHTEMPLATE = "AWS::EC2::LaunchTemplate"
    AWS__ECR__PUBLICREPOSITORY = "AWS::ECR::PublicRepository"
    AWS__GUARDDUTY__DETECTOR = "AWS::GuardDuty::Detector"
    AWS__EMR__SECURITYCONFIGURATION = "AWS::EMR::SecurityConfiguration"
    AWS__SAGEMAKER__CODEREPOSITORY = "AWS::SageMaker::CodeRepository"
    AWS__ROUTE53RESOLVER__RESOLVERENDPOINT = "AWS::Route53Resolver::ResolverEndpoint"
    AWS__ROUTE53RESOLVER__RESOLVERRULE = "AWS::Route53Resolver::ResolverRule"
    AWS__ROUTE53RESOLVER__RESOLVERRULEASSOCIATION = (
        "AWS::Route53Resolver::ResolverRuleAssociation"
    )
    AWS__DMS__REPLICATIONSUBNETGROUP = "AWS::DMS::ReplicationSubnetGroup"
    AWS__DMS__EVENTSUBSCRIPTION = "AWS::DMS::EventSubscription"
    AWS__MSK__CLUSTER = "AWS::MSK::Cluster"
    AWS__STEPFUNCTIONS__ACTIVITY = "AWS::StepFunctions::Activity"
    AWS__WORKSPACES__WORKSPACE = "AWS::WorkSpaces::Workspace"
    AWS__WORKSPACES__CONNECTIONALIAS = "AWS::WorkSpaces::ConnectionAlias"
    AWS__SAGEMAKER__MODEL = "AWS::SageMaker::Model"
    AWS__ELASTICLOADBALANCINGV2__LISTENER = "AWS::ElasticLoadBalancingV2::Listener"
    AWS__STEPFUNCTIONS__STATEMACHINE = "AWS::StepFunctions::StateMachine"
    AWS__BATCH__JOBQUEUE = "AWS::Batch::JobQueue"
    AWS__BATCH__COMPUTEENVIRONMENT = "AWS::Batch::ComputeEnvironment"
    AWS__ACCESSANALYZER__ANALYZER = "AWS::AccessAnalyzer::Analyzer"
    AWS__ATHENA__WORKGROUP = "AWS::Athena::WorkGroup"
    AWS__ATHENA__DATACATALOG = "AWS::Athena::DataCatalog"
    AWS__DETECTIVE__GRAPH = "AWS::Detective::Graph"
    AWS__GLOBALACCELERATOR__ACCELERATOR = "AWS::GlobalAccelerator::Accelerator"
    AWS__GLOBALACCELERATOR__ENDPOINTGROUP = "AWS::GlobalAccelerator::EndpointGroup"
    AWS__GLOBALACCELERATOR__LISTENER = "AWS::GlobalAccelerator::Listener"
    AWS__EC2__TRANSITGATEWAYATTACHMENT = "AWS::EC2::TransitGatewayAttachment"
    AWS__EC2__TRANSITGATEWAYROUTETABLE = "AWS::EC2::TransitGatewayRouteTable"
    AWS__DMS__CERTIFICATE = "AWS::DMS::Certificate"
    AWS__APPCONFIG__APPLICATION = "AWS::AppConfig::Application"
    AWS__APPSYNC__GRAPHQLAPI = "AWS::AppSync::GraphQLApi"
    AWS__DATASYNC__LOCATIONSMB = "AWS::DataSync::LocationSMB"
    AWS__DATASYNC__LOCATIONFSXLUSTRE = "AWS::DataSync::LocationFSxLustre"
    AWS__DATASYNC__LOCATIONS3 = "AWS::DataSync::LocationS3"
    AWS__DATASYNC__LOCATIONEFS = "AWS::DataSync::LocationEFS"
    AWS__DATASYNC__TASK = "AWS::DataSync::Task"
    AWS__DATASYNC__LOCATIONNFS = "AWS::DataSync::LocationNFS"
    AWS__EC2__NETWORKINSIGHTSACCESSSCOPEANALYSIS = (
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis"
    )
    AWS__EKS__FARGATEPROFILE = "AWS::EKS::FargateProfile"
    AWS__GLUE__JOB = "AWS::Glue::Job"
    AWS__GUARDDUTY__THREATINTELSET = "AWS::GuardDuty::ThreatIntelSet"
    AWS__GUARDDUTY__IPSET = "AWS::GuardDuty::IPSet"
    AWS__SAGEMAKER__WORKTEAM = "AWS::SageMaker::Workteam"
    AWS__SAGEMAKER__NOTEBOOKINSTANCELIFECYCLECONFIG = (
        "AWS::SageMaker::NotebookInstanceLifecycleConfig"
    )
    AWS__SERVICEDISCOVERY__SERVICE = "AWS::ServiceDiscovery::Service"
    AWS__SERVICEDISCOVERY__PUBLICDNSNAMESPACE = (
        "AWS::ServiceDiscovery::PublicDnsNamespace"
    )
    AWS__SES__CONTACTLIST = "AWS::SES::ContactList"
    AWS__SES__CONFIGURATIONSET = "AWS::SES::ConfigurationSet"
    AWS__ROUTE53__HOSTEDZONE = "AWS::Route53::HostedZone"
    AWS__IOTEVENTS__INPUT = "AWS::IoTEvents::Input"
    AWS__IOTEVENTS__DETECTORMODEL = "AWS::IoTEvents::DetectorModel"
    AWS__IOTEVENTS__ALARMMODEL = "AWS::IoTEvents::AlarmModel"
    AWS__SERVICEDISCOVERY__HTTPNAMESPACE = "AWS::ServiceDiscovery::HttpNamespace"
    AWS__EVENTS__EVENTBUS = "AWS::Events::EventBus"
    AWS__IMAGEBUILDER__CONTAINERRECIPE = "AWS::ImageBuilder::ContainerRecipe"
    AWS__IMAGEBUILDER__DISTRIBUTIONCONFIGURATION = (
        "AWS::ImageBuilder::DistributionConfiguration"
    )
    AWS__IMAGEBUILDER__INFRASTRUCTURECONFIGURATION = (
        "AWS::ImageBuilder::InfrastructureConfiguration"
    )
    AWS__DATASYNC__LOCATIONOBJECTSTORAGE = "AWS::DataSync::LocationObjectStorage"
    AWS__DATASYNC__LOCATIONHDFS = "AWS::DataSync::LocationHDFS"
    AWS__GLUE__CLASSIFIER = "AWS::Glue::Classifier"
    AWS__ROUTE53RECOVERYREADINESS__CELL = "AWS::Route53RecoveryReadiness::Cell"
    AWS__ROUTE53RECOVERYREADINESS__READINESSCHECK = (
        "AWS::Route53RecoveryReadiness::ReadinessCheck"
    )
    AWS__ECR__REGISTRYPOLICY = "AWS::ECR::RegistryPolicy"
    AWS__BACKUP__REPORTPLAN = "AWS::Backup::ReportPlan"
    AWS__LIGHTSAIL__CERTIFICATE = "AWS::Lightsail::Certificate"
    AWS__RUM__APPMONITOR = "AWS::RUM::AppMonitor"
    AWS__EVENTS__ENDPOINT = "AWS::Events::Endpoint"
    AWS__SES__RECEIPTRULESET = "AWS::SES::ReceiptRuleSet"
    AWS__EVENTS__ARCHIVE = "AWS::Events::Archive"
    AWS__EVENTS__APIDESTINATION = "AWS::Events::ApiDestination"
    AWS__LIGHTSAIL__DISK = "AWS::Lightsail::Disk"
    AWS__FIS__EXPERIMENTTEMPLATE = "AWS::FIS::ExperimentTemplate"
    AWS__DATASYNC__LOCATIONFSXWINDOWS = "AWS::DataSync::LocationFSxWindows"
    AWS__SES__RECEIPTFILTER = "AWS::SES::ReceiptFilter"
    AWS__GUARDDUTY__FILTER = "AWS::GuardDuty::Filter"
    AWS__SES__TEMPLATE = "AWS::SES::Template"
    AWS__AMAZONMQ__BROKER = "AWS::AmazonMQ::Broker"
    AWS__APPCONFIG__ENVIRONMENT = "AWS::AppConfig::Environment"
    AWS__APPCONFIG__CONFIGURATIONPROFILE = "AWS::AppConfig::ConfigurationProfile"
    AWS__CLOUD9__ENVIRONMENTEC2 = "AWS::Cloud9::EnvironmentEC2"
    AWS__EVENTSCHEMAS__REGISTRY = "AWS::EventSchemas::Registry"
    AWS__EVENTSCHEMAS__REGISTRYPOLICY = "AWS::EventSchemas::RegistryPolicy"
    AWS__EVENTSCHEMAS__DISCOVERER = "AWS::EventSchemas::Discoverer"
    AWS__FRAUDDETECTOR__LABEL = "AWS::FraudDetector::Label"
    AWS__FRAUDDETECTOR__ENTITYTYPE = "AWS::FraudDetector::EntityType"
    AWS__FRAUDDETECTOR__VARIABLE = "AWS::FraudDetector::Variable"
    AWS__FRAUDDETECTOR__OUTCOME = "AWS::FraudDetector::Outcome"
    AWS__IOT__AUTHORIZER = "AWS::IoT::Authorizer"
    AWS__IOT__SECURITYPROFILE = "AWS::IoT::SecurityProfile"
    AWS__IOT__ROLEALIAS = "AWS::IoT::RoleAlias"
    AWS__IOT__DIMENSION = "AWS::IoT::Dimension"
    AWS__IOTANALYTICS__DATASTORE = "AWS::IoTAnalytics::Datastore"
    AWS__LIGHTSAIL__BUCKET = "AWS::Lightsail::Bucket"
    AWS__LIGHTSAIL__STATICIP = "AWS::Lightsail::StaticIp"
    AWS__MEDIAPACKAGE__PACKAGINGGROUP = "AWS::MediaPackage::PackagingGroup"
    AWS__ROUTE53RECOVERYREADINESS__RECOVERYGROUP = (
        "AWS::Route53RecoveryReadiness::RecoveryGroup"
    )
    AWS__RESILIENCEHUB__RESILIENCYPOLICY = "AWS::ResilienceHub::ResiliencyPolicy"
    AWS__TRANSFER__WORKFLOW = "AWS::Transfer::Workflow"
    AWS__EKS__IDENTITYPROVIDERCONFIG = "AWS::EKS::IdentityProviderConfig"
    AWS__EKS__ADDON = "AWS::EKS::Addon"
    AWS__GLUE__MLTRANSFORM = "AWS::Glue::MLTransform"
    AWS__IOT__POLICY = "AWS::IoT::Policy"
    AWS__IOT__MITIGATIONACTION = "AWS::IoT::MitigationAction"
    AWS__IOTTWINMAKER__WORKSPACE = "AWS::IoTTwinMaker::Workspace"
    AWS__IOTTWINMAKER__ENTITY = "AWS::IoTTwinMaker::Entity"
    AWS__IOTANALYTICS__DATASET = "AWS::IoTAnalytics::Dataset"
    AWS__IOTANALYTICS__PIPELINE = "AWS::IoTAnalytics::Pipeline"
    AWS__IOTANALYTICS__CHANNEL = "AWS::IoTAnalytics::Channel"
    AWS__IOTSITEWISE__DASHBOARD = "AWS::IoTSiteWise::Dashboard"
    AWS__IOTSITEWISE__PROJECT = "AWS::IoTSiteWise::Project"
    AWS__IOTSITEWISE__PORTAL = "AWS::IoTSiteWise::Portal"
    AWS__IOTSITEWISE__ASSETMODEL = "AWS::IoTSiteWise::AssetModel"
    AWS__IVS__CHANNEL = "AWS::IVS::Channel"
    AWS__IVS__RECORDINGCONFIGURATION = "AWS::IVS::RecordingConfiguration"
    AWS__IVS__PLAYBACKKEYPAIR = "AWS::IVS::PlaybackKeyPair"
    AWS__KINESISANALYTICSV2__APPLICATION = "AWS::KinesisAnalyticsV2::Application"
    AWS__RDS__GLOBALCLUSTER = "AWS::RDS::GlobalCluster"
    AWS__S3__MULTIREGIONACCESSPOINT = "AWS::S3::MultiRegionAccessPoint"
    AWS__DEVICEFARM__TESTGRIDPROJECT = "AWS::DeviceFarm::TestGridProject"
    AWS__BUDGETS__BUDGETSACTION = "AWS::Budgets::BudgetsAction"
    AWS__LEX__BOT = "AWS::Lex::Bot"
    AWS__CODEGURUREVIEWER__REPOSITORYASSOCIATION = (
        "AWS::CodeGuruReviewer::RepositoryAssociation"
    )
    AWS__IOT__CUSTOMMETRIC = "AWS::IoT::CustomMetric"
    AWS__ROUTE53RESOLVER__FIREWALLDOMAINLIST = (
        "AWS::Route53Resolver::FirewallDomainList"
    )
    AWS__ROBOMAKER__ROBOTAPPLICATIONVERSION = "AWS::RoboMaker::RobotApplicationVersion"
    AWS__EC2__TRAFFICMIRRORSESSION = "AWS::EC2::TrafficMirrorSession"
    AWS__IOTSITEWISE__GATEWAY = "AWS::IoTSiteWise::Gateway"
    AWS__LEX__BOTALIAS = "AWS::Lex::BotAlias"
    AWS__LOOKOUTMETRICS__ALERT = "AWS::LookoutMetrics::Alert"
    AWS__IOT__ACCOUNTAUDITCONFIGURATION = "AWS::IoT::AccountAuditConfiguration"
    AWS__EC2__TRAFFICMIRRORTARGET = "AWS::EC2::TrafficMirrorTarget"
    AWS__S3__STORAGELENS = "AWS::S3::StorageLens"
    AWS__IOT__SCHEDULEDAUDIT = "AWS::IoT::ScheduledAudit"
    AWS__EVENTS__CONNECTION = "AWS::Events::Connection"
    AWS__EVENTSCHEMAS__SCHEMA = "AWS::EventSchemas::Schema"
    AWS__MEDIAPACKAGE__PACKAGINGCONFIGURATION = (
        "AWS::MediaPackage::PackagingConfiguration"
    )
    AWS__KINESISVIDEO__SIGNALINGCHANNEL = "AWS::KinesisVideo::SignalingChannel"
    AWS__APPSTREAM__DIRECTORYCONFIG = "AWS::AppStream::DirectoryConfig"
    AWS__LOOKOUTVISION__PROJECT = "AWS::LookoutVision::Project"
    AWS__ROUTE53RECOVERYCONTROL__CLUSTER = "AWS::Route53RecoveryControl::Cluster"
    AWS__ROUTE53RECOVERYCONTROL__SAFETYRULE = "AWS::Route53RecoveryControl::SafetyRule"
    AWS__ROUTE53RECOVERYCONTROL__CONTROLPANEL = (
        "AWS::Route53RecoveryControl::ControlPanel"
    )
    AWS__ROUTE53RECOVERYCONTROL__ROUTINGCONTROL = (
        "AWS::Route53RecoveryControl::RoutingControl"
    )
    AWS__ROUTE53RECOVERYREADINESS__RESOURCESET = (
        "AWS::Route53RecoveryReadiness::ResourceSet"
    )
    AWS__ROBOMAKER__SIMULATIONAPPLICATION = "AWS::RoboMaker::SimulationApplication"
    AWS__ROBOMAKER__ROBOTAPPLICATION = "AWS::RoboMaker::RobotApplication"
    AWS__HEALTHLAKE__FHIRDATASTORE = "AWS::HealthLake::FHIRDatastore"
    AWS__PINPOINT__SEGMENT = "AWS::Pinpoint::Segment"
    AWS__PINPOINT__APPLICATIONSETTINGS = "AWS::Pinpoint::ApplicationSettings"
    AWS__EVENTS__RULE = "AWS::Events::Rule"
    AWS__EC2__DHCPOPTIONS = "AWS::EC2::DHCPOptions"
    AWS__EC2__NETWORKINSIGHTSPATH = "AWS::EC2::NetworkInsightsPath"
    AWS__EC2__TRAFFICMIRRORFILTER = "AWS::EC2::TrafficMirrorFilter"
    AWS__EC2__IPAM = "AWS::EC2::IPAM"
    AWS__IOTTWINMAKER__SCENE = "AWS::IoTTwinMaker::Scene"
    AWS__NETWORKMANAGER__TRANSITGATEWAYREGISTRATION = (
        "AWS::NetworkManager::TransitGatewayRegistration"
    )
    AWS__CUSTOMERPROFILES__DOMAIN = "AWS::CustomerProfiles::Domain"
    AWS__AUTOSCALING__WARMPOOL = "AWS::AutoScaling::WarmPool"
    AWS__CONNECT__PHONENUMBER = "AWS::Connect::PhoneNumber"
    AWS__APPCONFIG__DEPLOYMENTSTRATEGY = "AWS::AppConfig::DeploymentStrategy"
    AWS__APPFLOW__FLOW = "AWS::AppFlow::Flow"
    AWS__AUDITMANAGER__ASSESSMENT = "AWS::AuditManager::Assessment"
    AWS__CLOUDWATCH__METRICSTREAM = "AWS::CloudWatch::MetricStream"
    AWS__DEVICEFARM__INSTANCEPROFILE = "AWS::DeviceFarm::InstanceProfile"
    AWS__DEVICEFARM__PROJECT = "AWS::DeviceFarm::Project"
    AWS__EC2__EC2FLEET = "AWS::EC2::EC2Fleet"
    AWS__EC2__SUBNETROUTETABLEASSOCIATION = "AWS::EC2::SubnetRouteTableAssociation"
    AWS__ECR__PULLTHROUGHCACHERULE = "AWS::ECR::PullThroughCacheRule"
    AWS__GROUNDSTATION__CONFIG = "AWS::GroundStation::Config"
    AWS__IMAGEBUILDER__IMAGEPIPELINE = "AWS::ImageBuilder::ImagePipeline"
    AWS__IOT__FLEETMETRIC = "AWS::IoT::FleetMetric"
    AWS__IOTWIRELESS__SERVICEPROFILE = "AWS::IoTWireless::ServiceProfile"
    AWS__NETWORKMANAGER__DEVICE = "AWS::NetworkManager::Device"
    AWS__NETWORKMANAGER__GLOBALNETWORK = "AWS::NetworkManager::GlobalNetwork"
    AWS__NETWORKMANAGER__LINK = "AWS::NetworkManager::Link"
    AWS__NETWORKMANAGER__SITE = "AWS::NetworkManager::Site"
    AWS__PANORAMA__PACKAGE = "AWS::Panorama::Package"
    AWS__PINPOINT__APP = "AWS::Pinpoint::App"
    AWS__REDSHIFT__SCHEDULEDACTION = "AWS::Redshift::ScheduledAction"
    AWS__ROUTE53RESOLVER__FIREWALLRULEGROUPASSOCIATION = (
        "AWS::Route53Resolver::FirewallRuleGroupAssociation"
    )
    AWS__SAGEMAKER__APPIMAGECONFIG = "AWS::SageMaker::AppImageConfig"
    AWS__SAGEMAKER__IMAGE = "AWS::SageMaker::Image"


class ResourceValueType(enum.Enum):
    RESOURCE_ID = "RESOURCE_ID"


class SortBy(enum.Enum):
    SCORE = "SCORE"


class SortOrder(enum.Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class AccountAggregationSource(_ConfigServiceModelBase):
    account_ids: AccountAggregationSourceAccountList = pydantic.Field(
        None, alias="AccountIds"
    )
    all_aws_regions: Boolean = pydantic.Field(None, alias="AllAwsRegions")
    aws_regions: AggregatorRegionList = pydantic.Field(None, alias="AwsRegions")


class AggregateComplianceByConfigRule(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    compliance: "Compliance" = pydantic.Field(None, alias="Compliance")
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class AggregateComplianceByConformancePack(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    compliance: "AggregateConformancePackCompliance" = pydantic.Field(
        None, alias="Compliance"
    )
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class AggregateComplianceCount(_ConfigServiceModelBase):
    group_name: StringWithCharLimit256 = pydantic.Field(None, alias="GroupName")
    compliance_summary: "ComplianceSummary" = pydantic.Field(
        None, alias="ComplianceSummary"
    )


class AggregateConformancePackCompliance(_ConfigServiceModelBase):
    compliance_type: ConformancePackComplianceType = pydantic.Field(
        None, alias="ComplianceType"
    )
    compliant_rule_count: Integer = pydantic.Field(None, alias="CompliantRuleCount")
    non_compliant_rule_count: Integer = pydantic.Field(
        None, alias="NonCompliantRuleCount"
    )
    total_rule_count: Integer = pydantic.Field(None, alias="TotalRuleCount")


class AggregateConformancePackComplianceCount(_ConfigServiceModelBase):
    compliant_conformance_pack_count: Integer = pydantic.Field(
        None, alias="CompliantConformancePackCount"
    )
    non_compliant_conformance_pack_count: Integer = pydantic.Field(
        None, alias="NonCompliantConformancePackCount"
    )


class AggregateConformancePackComplianceFilters(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    compliance_type: ConformancePackComplianceType = pydantic.Field(
        None, alias="ComplianceType"
    )
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class AggregateConformancePackComplianceSummary(_ConfigServiceModelBase):
    compliance_summary: "AggregateConformancePackComplianceCount" = pydantic.Field(
        None, alias="ComplianceSummary"
    )
    group_name: StringWithCharLimit256 = pydantic.Field(None, alias="GroupName")


class AggregateConformancePackComplianceSummaryFilters(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class AggregateEvaluationResult(_ConfigServiceModelBase):
    evaluation_result_identifier: "EvaluationResultIdentifier" = pydantic.Field(
        None, alias="EvaluationResultIdentifier"
    )
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    result_recorded_time: Date = pydantic.Field(None, alias="ResultRecordedTime")
    config_rule_invoked_time: Date = pydantic.Field(None, alias="ConfigRuleInvokedTime")
    annotation: StringWithCharLimit256 = pydantic.Field(None, alias="Annotation")
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class AggregateResourceIdentifier(_ConfigServiceModelBase):
    source_account_id: AccountId = pydantic.Field(None, alias="SourceAccountId")
    source_region: AwsRegion = pydantic.Field(None, alias="SourceRegion")
    resource_id: ResourceId = pydantic.Field(None, alias="ResourceId")
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    resource_name: ResourceName = pydantic.Field(None, alias="ResourceName")


class AggregatedSourceStatus(_ConfigServiceModelBase):
    source_id: String = pydantic.Field(None, alias="SourceId")
    source_type: AggregatedSourceType = pydantic.Field(None, alias="SourceType")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")
    last_update_status: AggregatedSourceStatusType = pydantic.Field(
        None, alias="LastUpdateStatus"
    )
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")
    last_error_code: String = pydantic.Field(None, alias="LastErrorCode")
    last_error_message: String = pydantic.Field(None, alias="LastErrorMessage")


class AggregationAuthorization(_ConfigServiceModelBase):
    aggregation_authorization_arn: String = pydantic.Field(
        None, alias="AggregationAuthorizationArn"
    )
    authorized_account_id: AccountId = pydantic.Field(None, alias="AuthorizedAccountId")
    authorized_aws_region: AwsRegion = pydantic.Field(None, alias="AuthorizedAwsRegion")
    creation_time: Date = pydantic.Field(None, alias="CreationTime")


class BaseConfigurationItem(_ConfigServiceModelBase):
    version: Version = pydantic.Field(None, alias="version")
    account_id: AccountId = pydantic.Field(None, alias="accountId")
    configuration_item_capture_time: ConfigurationItemCaptureTime = pydantic.Field(
        None, alias="configurationItemCaptureTime"
    )
    configuration_item_status: ConfigurationItemStatus = pydantic.Field(
        None, alias="configurationItemStatus"
    )
    configuration_state_id: ConfigurationStateId = pydantic.Field(
        None, alias="configurationStateId"
    )
    arn: ARN = pydantic.Field(None, alias="arn")
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="resourceId")
    resource_name: ResourceName = pydantic.Field(None, alias="resourceName")
    aws_region: AwsRegion = pydantic.Field(None, alias="awsRegion")
    availability_zone: AvailabilityZone = pydantic.Field(None, alias="availabilityZone")
    resource_creation_time: ResourceCreationTime = pydantic.Field(
        None, alias="resourceCreationTime"
    )
    configuration: Configuration = pydantic.Field(None, alias="configuration")
    supplementary_configuration: SupplementaryConfiguration = pydantic.Field(
        None, alias="supplementaryConfiguration"
    )


class BatchGetAggregateResourceConfigRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    resource_identifiers: ResourceIdentifiersList = pydantic.Field(
        None, alias="ResourceIdentifiers"
    )


class BatchGetAggregateResourceConfigResponse(_ConfigServiceModelBase):
    base_configuration_items: BaseConfigurationItems = pydantic.Field(
        None, alias="BaseConfigurationItems"
    )
    unprocessed_resource_identifiers: UnprocessedResourceIdentifierList = (
        pydantic.Field(None, alias="UnprocessedResourceIdentifiers")
    )


class BatchGetResourceConfigRequest(_ConfigServiceModelBase):
    resource_keys: ResourceKeys = pydantic.Field(None, alias="resourceKeys")


class BatchGetResourceConfigResponse(_ConfigServiceModelBase):
    base_configuration_items: BaseConfigurationItems = pydantic.Field(
        None, alias="baseConfigurationItems"
    )
    unprocessed_resource_keys: ResourceKeys = pydantic.Field(
        None, alias="unprocessedResourceKeys"
    )


class Compliance(_ConfigServiceModelBase):
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    compliance_contributor_count: "ComplianceContributorCount" = pydantic.Field(
        None, alias="ComplianceContributorCount"
    )


class ComplianceByConfigRule(_ConfigServiceModelBase):
    config_rule_name: StringWithCharLimit64 = pydantic.Field(
        None, alias="ConfigRuleName"
    )
    compliance: "Compliance" = pydantic.Field(None, alias="Compliance")


class ComplianceByResource(_ConfigServiceModelBase):
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_id: BaseResourceId = pydantic.Field(None, alias="ResourceId")
    compliance: "Compliance" = pydantic.Field(None, alias="Compliance")


class ComplianceContributorCount(_ConfigServiceModelBase):
    capped_count: Integer = pydantic.Field(None, alias="CappedCount")
    cap_exceeded: Boolean = pydantic.Field(None, alias="CapExceeded")


class ComplianceSummary(_ConfigServiceModelBase):
    compliant_resource_count: "ComplianceContributorCount" = pydantic.Field(
        None, alias="CompliantResourceCount"
    )
    non_compliant_resource_count: "ComplianceContributorCount" = pydantic.Field(
        None, alias="NonCompliantResourceCount"
    )
    compliance_summary_timestamp: Date = pydantic.Field(
        None, alias="ComplianceSummaryTimestamp"
    )


class ComplianceSummaryByResourceType(_ConfigServiceModelBase):
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    compliance_summary: "ComplianceSummary" = pydantic.Field(
        None, alias="ComplianceSummary"
    )


class ConfigExportDeliveryInfo(_ConfigServiceModelBase):
    last_status: DeliveryStatus = pydantic.Field(None, alias="lastStatus")
    last_error_code: String = pydantic.Field(None, alias="lastErrorCode")
    last_error_message: String = pydantic.Field(None, alias="lastErrorMessage")
    last_attempt_time: Date = pydantic.Field(None, alias="lastAttemptTime")
    last_successful_time: Date = pydantic.Field(None, alias="lastSuccessfulTime")
    next_delivery_time: Date = pydantic.Field(None, alias="nextDeliveryTime")


class ConfigRule(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    config_rule_arn: StringWithCharLimit256 = pydantic.Field(
        None, alias="ConfigRuleArn"
    )
    config_rule_id: StringWithCharLimit64 = pydantic.Field(None, alias="ConfigRuleId")
    description: EmptiableStringWithCharLimit256 = pydantic.Field(
        None, alias="Description"
    )
    scope: "Scope" = pydantic.Field(None, alias="Scope")
    source: "Source" = pydantic.Field(None, alias="Source")
    input_parameters: StringWithCharLimit1024 = pydantic.Field(
        None, alias="InputParameters"
    )
    maximum_execution_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="MaximumExecutionFrequency"
    )
    config_rule_state: ConfigRuleState = pydantic.Field(None, alias="ConfigRuleState")
    created_by: StringWithCharLimit256 = pydantic.Field(None, alias="CreatedBy")
    evaluation_modes: EvaluationModes = pydantic.Field(None, alias="EvaluationModes")


class ConfigRuleComplianceFilters(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class ConfigRuleComplianceSummaryFilters(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")


class ConfigRuleEvaluationStatus(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    config_rule_arn: String = pydantic.Field(None, alias="ConfigRuleArn")
    config_rule_id: String = pydantic.Field(None, alias="ConfigRuleId")
    last_successful_invocation_time: Date = pydantic.Field(
        None, alias="LastSuccessfulInvocationTime"
    )
    last_failed_invocation_time: Date = pydantic.Field(
        None, alias="LastFailedInvocationTime"
    )
    last_successful_evaluation_time: Date = pydantic.Field(
        None, alias="LastSuccessfulEvaluationTime"
    )
    last_failed_evaluation_time: Date = pydantic.Field(
        None, alias="LastFailedEvaluationTime"
    )
    first_activated_time: Date = pydantic.Field(None, alias="FirstActivatedTime")
    last_deactivated_time: Date = pydantic.Field(None, alias="LastDeactivatedTime")
    last_error_code: String = pydantic.Field(None, alias="LastErrorCode")
    last_error_message: String = pydantic.Field(None, alias="LastErrorMessage")
    first_evaluation_started: Boolean = pydantic.Field(
        None, alias="FirstEvaluationStarted"
    )
    last_debug_log_delivery_status: String = pydantic.Field(
        None, alias="LastDebugLogDeliveryStatus"
    )
    last_debug_log_delivery_status_reason: String = pydantic.Field(
        None, alias="LastDebugLogDeliveryStatusReason"
    )
    last_debug_log_delivery_time: Date = pydantic.Field(
        None, alias="LastDebugLogDeliveryTime"
    )


class ConfigSnapshotDeliveryProperties(_ConfigServiceModelBase):
    delivery_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="deliveryFrequency"
    )


class ConfigStreamDeliveryInfo(_ConfigServiceModelBase):
    last_status: DeliveryStatus = pydantic.Field(None, alias="lastStatus")
    last_error_code: String = pydantic.Field(None, alias="lastErrorCode")
    last_error_message: String = pydantic.Field(None, alias="lastErrorMessage")
    last_status_change_time: Date = pydantic.Field(None, alias="lastStatusChangeTime")


class ConfigurationAggregator(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    configuration_aggregator_arn: ConfigurationAggregatorArn = pydantic.Field(
        None, alias="ConfigurationAggregatorArn"
    )
    account_aggregation_sources: AccountAggregationSourceList = pydantic.Field(
        None, alias="AccountAggregationSources"
    )
    organization_aggregation_source: "OrganizationAggregationSource" = pydantic.Field(
        None, alias="OrganizationAggregationSource"
    )
    creation_time: Date = pydantic.Field(None, alias="CreationTime")
    last_updated_time: Date = pydantic.Field(None, alias="LastUpdatedTime")
    created_by: StringWithCharLimit256 = pydantic.Field(None, alias="CreatedBy")


class ConfigurationItem(_ConfigServiceModelBase):
    version: Version = pydantic.Field(None, alias="version")
    account_id: AccountId = pydantic.Field(None, alias="accountId")
    configuration_item_capture_time: ConfigurationItemCaptureTime = pydantic.Field(
        None, alias="configurationItemCaptureTime"
    )
    configuration_item_status: ConfigurationItemStatus = pydantic.Field(
        None, alias="configurationItemStatus"
    )
    configuration_state_id: ConfigurationStateId = pydantic.Field(
        None, alias="configurationStateId"
    )
    configuration_item_md_5_hash: ConfigurationItemMD5Hash = pydantic.Field(
        None, alias="configurationItemMD5Hash"
    )
    arn: ARN = pydantic.Field(None, alias="arn")
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="resourceId")
    resource_name: ResourceName = pydantic.Field(None, alias="resourceName")
    aws_region: AwsRegion = pydantic.Field(None, alias="awsRegion")
    availability_zone: AvailabilityZone = pydantic.Field(None, alias="availabilityZone")
    resource_creation_time: ResourceCreationTime = pydantic.Field(
        None, alias="resourceCreationTime"
    )
    tags: Tags = pydantic.Field(None, alias="tags")
    related_events: RelatedEventList = pydantic.Field(None, alias="relatedEvents")
    relationships: RelationshipList = pydantic.Field(None, alias="relationships")
    configuration: Configuration = pydantic.Field(None, alias="configuration")
    supplementary_configuration: SupplementaryConfiguration = pydantic.Field(
        None, alias="supplementaryConfiguration"
    )


class ConfigurationRecorder(_ConfigServiceModelBase):
    name: RecorderName = pydantic.Field(None, alias="name")
    role_arn: String = pydantic.Field(None, alias="roleARN")
    recording_group: "RecordingGroup" = pydantic.Field(None, alias="recordingGroup")


class ConfigurationRecorderStatus(_ConfigServiceModelBase):
    name: String = pydantic.Field(None, alias="name")
    last_start_time: Date = pydantic.Field(None, alias="lastStartTime")
    last_stop_time: Date = pydantic.Field(None, alias="lastStopTime")
    recording: Boolean = pydantic.Field(None, alias="recording")
    last_status: RecorderStatus = pydantic.Field(None, alias="lastStatus")
    last_error_code: String = pydantic.Field(None, alias="lastErrorCode")
    last_error_message: String = pydantic.Field(None, alias="lastErrorMessage")
    last_status_change_time: Date = pydantic.Field(None, alias="lastStatusChangeTime")


class ConformancePackComplianceFilters(_ConfigServiceModelBase):
    config_rule_names: ConformancePackConfigRuleNames = pydantic.Field(
        None, alias="ConfigRuleNames"
    )
    compliance_type: ConformancePackComplianceType = pydantic.Field(
        None, alias="ComplianceType"
    )


class ConformancePackComplianceScore(_ConfigServiceModelBase):
    score: ComplianceScore = pydantic.Field(None, alias="Score")
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    last_updated_time: LastUpdatedTime = pydantic.Field(None, alias="LastUpdatedTime")


class ConformancePackComplianceScoresFilters(_ConfigServiceModelBase):
    conformance_pack_names: ConformancePackNameFilter = pydantic.Field(
        None, alias="ConformancePackNames"
    )


class ConformancePackComplianceSummary(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    conformance_pack_compliance_status: ConformancePackComplianceType = pydantic.Field(
        None, alias="ConformancePackComplianceStatus"
    )


class ConformancePackDetail(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    conformance_pack_arn: ConformancePackArn = pydantic.Field(
        None, alias="ConformancePackArn"
    )
    conformance_pack_id: ConformancePackId = pydantic.Field(
        None, alias="ConformancePackId"
    )
    delivery_s_3_bucket: DeliveryS3Bucket = pydantic.Field(
        None, alias="DeliveryS3Bucket"
    )
    delivery_s_3_key_prefix: DeliveryS3KeyPrefix = pydantic.Field(
        None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: ConformancePackInputParameters = pydantic.Field(
        None, alias="ConformancePackInputParameters"
    )
    last_update_requested_time: Date = pydantic.Field(
        None, alias="LastUpdateRequestedTime"
    )
    created_by: StringWithCharLimit256 = pydantic.Field(None, alias="CreatedBy")
    template_ssm_document_details: "TemplateSSMDocumentDetails" = pydantic.Field(
        None, alias="TemplateSSMDocumentDetails"
    )


class ConformancePackEvaluationFilters(_ConfigServiceModelBase):
    config_rule_names: ConformancePackConfigRuleNames = pydantic.Field(
        None, alias="ConfigRuleNames"
    )
    compliance_type: ConformancePackComplianceType = pydantic.Field(
        None, alias="ComplianceType"
    )
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_ids: ConformancePackComplianceResourceIds = pydantic.Field(
        None, alias="ResourceIds"
    )


class ConformancePackEvaluationResult(_ConfigServiceModelBase):
    compliance_type: ConformancePackComplianceType = pydantic.Field(
        None, alias="ComplianceType"
    )
    evaluation_result_identifier: "EvaluationResultIdentifier" = pydantic.Field(
        None, alias="EvaluationResultIdentifier"
    )
    config_rule_invoked_time: Date = pydantic.Field(None, alias="ConfigRuleInvokedTime")
    result_recorded_time: Date = pydantic.Field(None, alias="ResultRecordedTime")
    annotation: Annotation = pydantic.Field(None, alias="Annotation")


class ConformancePackInputParameter(_ConfigServiceModelBase):
    parameter_name: ParameterName = pydantic.Field(None, alias="ParameterName")
    parameter_value: ParameterValue = pydantic.Field(None, alias="ParameterValue")


class ConformancePackRuleCompliance(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    compliance_type: ConformancePackComplianceType = pydantic.Field(
        None, alias="ComplianceType"
    )
    controls: ControlsList = pydantic.Field(None, alias="Controls")


class ConformancePackStatusDetail(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    conformance_pack_id: ConformancePackId = pydantic.Field(
        None, alias="ConformancePackId"
    )
    conformance_pack_arn: ConformancePackArn = pydantic.Field(
        None, alias="ConformancePackArn"
    )
    conformance_pack_state: ConformancePackState = pydantic.Field(
        None, alias="ConformancePackState"
    )
    stack_arn: StackArn = pydantic.Field(None, alias="StackArn")
    conformance_pack_status_reason: ConformancePackStatusReason = pydantic.Field(
        None, alias="ConformancePackStatusReason"
    )
    last_update_requested_time: Date = pydantic.Field(
        None, alias="LastUpdateRequestedTime"
    )
    last_update_completed_time: Date = pydantic.Field(
        None, alias="LastUpdateCompletedTime"
    )


class CustomPolicyDetails(_ConfigServiceModelBase):
    policy_runtime: PolicyRuntime = pydantic.Field(None, alias="PolicyRuntime")
    policy_text: PolicyText = pydantic.Field(None, alias="PolicyText")
    enable_debug_log_delivery: Boolean = pydantic.Field(
        None, alias="EnableDebugLogDelivery"
    )


class DeleteAggregationAuthorizationRequest(_ConfigServiceModelBase):
    authorized_account_id: AccountId = pydantic.Field(None, alias="AuthorizedAccountId")
    authorized_aws_region: AwsRegion = pydantic.Field(None, alias="AuthorizedAwsRegion")


class DeleteConfigRuleRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")


class DeleteConfigurationAggregatorRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )


class DeleteConfigurationRecorderRequest(_ConfigServiceModelBase):
    configuration_recorder_name: RecorderName = pydantic.Field(
        None, alias="ConfigurationRecorderName"
    )


class DeleteConformancePackRequest(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )


class DeleteDeliveryChannelRequest(_ConfigServiceModelBase):
    delivery_channel_name: ChannelName = pydantic.Field(
        None, alias="DeliveryChannelName"
    )


class DeleteEvaluationResultsRequest(_ConfigServiceModelBase):
    config_rule_name: StringWithCharLimit64 = pydantic.Field(
        None, alias="ConfigRuleName"
    )


class DeleteEvaluationResultsResponse(_ConfigServiceModelBase):
    pass


class DeleteOrganizationConfigRuleRequest(_ConfigServiceModelBase):
    organization_config_rule_name: OrganizationConfigRuleName = pydantic.Field(
        None, alias="OrganizationConfigRuleName"
    )


class DeleteOrganizationConformancePackRequest(_ConfigServiceModelBase):
    organization_conformance_pack_name: OrganizationConformancePackName = (
        pydantic.Field(None, alias="OrganizationConformancePackName")
    )


class DeletePendingAggregationRequestRequest(_ConfigServiceModelBase):
    requester_account_id: AccountId = pydantic.Field(None, alias="RequesterAccountId")
    requester_aws_region: AwsRegion = pydantic.Field(None, alias="RequesterAwsRegion")


class DeleteRemediationConfigurationRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_type: String = pydantic.Field(None, alias="ResourceType")


class DeleteRemediationConfigurationResponse(_ConfigServiceModelBase):
    pass


class DeleteRemediationExceptionsRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_keys: RemediationExceptionResourceKeys = pydantic.Field(
        None, alias="ResourceKeys"
    )


class DeleteRemediationExceptionsResponse(_ConfigServiceModelBase):
    failed_batches: FailedDeleteRemediationExceptionsBatches = pydantic.Field(
        None, alias="FailedBatches"
    )


class DeleteResourceConfigRequest(_ConfigServiceModelBase):
    resource_type: ResourceTypeString = pydantic.Field(None, alias="ResourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="ResourceId")


class DeleteRetentionConfigurationRequest(_ConfigServiceModelBase):
    retention_configuration_name: RetentionConfigurationName = pydantic.Field(
        None, alias="RetentionConfigurationName"
    )


class DeleteStoredQueryRequest(_ConfigServiceModelBase):
    query_name: QueryName = pydantic.Field(None, alias="QueryName")


class DeleteStoredQueryResponse(_ConfigServiceModelBase):
    pass


class DeliverConfigSnapshotRequest(_ConfigServiceModelBase):
    delivery_channel_name: ChannelName = pydantic.Field(
        None, alias="deliveryChannelName"
    )


class DeliverConfigSnapshotResponse(_ConfigServiceModelBase):
    config_snapshot_id: String = pydantic.Field(None, alias="configSnapshotId")


class DeliveryChannel(_ConfigServiceModelBase):
    name: ChannelName = pydantic.Field(None, alias="name")
    s_3_bucket_name: String = pydantic.Field(None, alias="s3BucketName")
    s_3_key_prefix: String = pydantic.Field(None, alias="s3KeyPrefix")
    s_3_kms_key_arn: String = pydantic.Field(None, alias="s3KmsKeyArn")
    sns_topic_arn: String = pydantic.Field(None, alias="snsTopicARN")
    config_snapshot_delivery_properties: "ConfigSnapshotDeliveryProperties" = (
        pydantic.Field(None, alias="configSnapshotDeliveryProperties")
    )


class DeliveryChannelStatus(_ConfigServiceModelBase):
    name: String = pydantic.Field(None, alias="name")
    config_snapshot_delivery_info: "ConfigExportDeliveryInfo" = pydantic.Field(
        None, alias="configSnapshotDeliveryInfo"
    )
    config_history_delivery_info: "ConfigExportDeliveryInfo" = pydantic.Field(
        None, alias="configHistoryDeliveryInfo"
    )
    config_stream_delivery_info: "ConfigStreamDeliveryInfo" = pydantic.Field(
        None, alias="configStreamDeliveryInfo"
    )


class DescribeAggregateComplianceByConfigRulesRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    filters: "ConfigRuleComplianceFilters" = pydantic.Field(None, alias="Filters")
    limit: GroupByAPILimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAggregateComplianceByConfigRulesResponse(_ConfigServiceModelBase):
    aggregate_compliance_by_config_rules: AggregateComplianceByConfigRuleList = (
        pydantic.Field(None, alias="AggregateComplianceByConfigRules")
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAggregateComplianceByConformancePacksRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    filters: "AggregateConformancePackComplianceFilters" = pydantic.Field(
        None, alias="Filters"
    )
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAggregateComplianceByConformancePacksResponse(_ConfigServiceModelBase):
    aggregate_compliance_by_conformance_packs: AggregateComplianceByConformancePackList = pydantic.Field(
        None, alias="AggregateComplianceByConformancePacks"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAggregationAuthorizationsRequest(_ConfigServiceModelBase):
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeAggregationAuthorizationsResponse(_ConfigServiceModelBase):
    aggregation_authorizations: AggregationAuthorizationList = pydantic.Field(
        None, alias="AggregationAuthorizations"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeComplianceByConfigRuleRequest(_ConfigServiceModelBase):
    config_rule_names: ConfigRuleNames = pydantic.Field(None, alias="ConfigRuleNames")
    compliance_types: ComplianceTypes = pydantic.Field(None, alias="ComplianceTypes")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeComplianceByConfigRuleResponse(_ConfigServiceModelBase):
    compliance_by_config_rules: ComplianceByConfigRules = pydantic.Field(
        None, alias="ComplianceByConfigRules"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeComplianceByResourceRequest(_ConfigServiceModelBase):
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_id: BaseResourceId = pydantic.Field(None, alias="ResourceId")
    compliance_types: ComplianceTypes = pydantic.Field(None, alias="ComplianceTypes")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeComplianceByResourceResponse(_ConfigServiceModelBase):
    compliance_by_resources: ComplianceByResources = pydantic.Field(
        None, alias="ComplianceByResources"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeConfigRuleEvaluationStatusRequest(_ConfigServiceModelBase):
    config_rule_names: ConfigRuleNames = pydantic.Field(None, alias="ConfigRuleNames")
    next_token: String = pydantic.Field(None, alias="NextToken")
    limit: RuleLimit = pydantic.Field(None, alias="Limit")


class DescribeConfigRuleEvaluationStatusResponse(_ConfigServiceModelBase):
    config_rules_evaluation_status: ConfigRuleEvaluationStatusList = pydantic.Field(
        None, alias="ConfigRulesEvaluationStatus"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeConfigRulesFilters(_ConfigServiceModelBase):
    evaluation_mode: EvaluationMode = pydantic.Field(None, alias="EvaluationMode")


class DescribeConfigRulesRequest(_ConfigServiceModelBase):
    config_rule_names: ConfigRuleNames = pydantic.Field(None, alias="ConfigRuleNames")
    next_token: String = pydantic.Field(None, alias="NextToken")
    filters: "DescribeConfigRulesFilters" = pydantic.Field(None, alias="Filters")


class DescribeConfigRulesResponse(_ConfigServiceModelBase):
    config_rules: ConfigRules = pydantic.Field(None, alias="ConfigRules")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeConfigurationAggregatorSourcesStatusRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    update_status: AggregatedSourceStatusTypeList = pydantic.Field(
        None, alias="UpdateStatus"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")
    limit: Limit = pydantic.Field(None, alias="Limit")


class DescribeConfigurationAggregatorSourcesStatusResponse(_ConfigServiceModelBase):
    aggregated_source_status_list: AggregatedSourceStatusList = pydantic.Field(
        None, alias="AggregatedSourceStatusList"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeConfigurationAggregatorsRequest(_ConfigServiceModelBase):
    configuration_aggregator_names: ConfigurationAggregatorNameList = pydantic.Field(
        None, alias="ConfigurationAggregatorNames"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")
    limit: Limit = pydantic.Field(None, alias="Limit")


class DescribeConfigurationAggregatorsResponse(_ConfigServiceModelBase):
    configuration_aggregators: ConfigurationAggregatorList = pydantic.Field(
        None, alias="ConfigurationAggregators"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeConfigurationRecorderStatusRequest(_ConfigServiceModelBase):
    configuration_recorder_names: ConfigurationRecorderNameList = pydantic.Field(
        None, alias="ConfigurationRecorderNames"
    )


class DescribeConfigurationRecorderStatusResponse(_ConfigServiceModelBase):
    configuration_recorders_status: ConfigurationRecorderStatusList = pydantic.Field(
        None, alias="ConfigurationRecordersStatus"
    )


class DescribeConfigurationRecordersRequest(_ConfigServiceModelBase):
    configuration_recorder_names: ConfigurationRecorderNameList = pydantic.Field(
        None, alias="ConfigurationRecorderNames"
    )


class DescribeConfigurationRecordersResponse(_ConfigServiceModelBase):
    configuration_recorders: ConfigurationRecorderList = pydantic.Field(
        None, alias="ConfigurationRecorders"
    )


class DescribeConformancePackComplianceRequest(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    filters: "ConformancePackComplianceFilters" = pydantic.Field(None, alias="Filters")
    limit: DescribeConformancePackComplianceLimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeConformancePackComplianceResponse(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    conformance_pack_rule_compliance_list: ConformancePackRuleComplianceList = (
        pydantic.Field(None, alias="ConformancePackRuleComplianceList")
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeConformancePackStatusRequest(_ConfigServiceModelBase):
    conformance_pack_names: ConformancePackNamesList = pydantic.Field(
        None, alias="ConformancePackNames"
    )
    limit: PageSizeLimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeConformancePackStatusResponse(_ConfigServiceModelBase):
    conformance_pack_status_details: ConformancePackStatusDetailsList = pydantic.Field(
        None, alias="ConformancePackStatusDetails"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeConformancePacksRequest(_ConfigServiceModelBase):
    conformance_pack_names: ConformancePackNamesList = pydantic.Field(
        None, alias="ConformancePackNames"
    )
    limit: PageSizeLimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeConformancePacksResponse(_ConfigServiceModelBase):
    conformance_pack_details: ConformancePackDetailList = pydantic.Field(
        None, alias="ConformancePackDetails"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeDeliveryChannelStatusRequest(_ConfigServiceModelBase):
    delivery_channel_names: DeliveryChannelNameList = pydantic.Field(
        None, alias="DeliveryChannelNames"
    )


class DescribeDeliveryChannelStatusResponse(_ConfigServiceModelBase):
    delivery_channels_status: DeliveryChannelStatusList = pydantic.Field(
        None, alias="DeliveryChannelsStatus"
    )


class DescribeDeliveryChannelsRequest(_ConfigServiceModelBase):
    delivery_channel_names: DeliveryChannelNameList = pydantic.Field(
        None, alias="DeliveryChannelNames"
    )


class DescribeDeliveryChannelsResponse(_ConfigServiceModelBase):
    delivery_channels: DeliveryChannelList = pydantic.Field(
        None, alias="DeliveryChannels"
    )


class DescribeOrganizationConfigRuleStatusesRequest(_ConfigServiceModelBase):
    organization_config_rule_names: OrganizationConfigRuleNames = pydantic.Field(
        None, alias="OrganizationConfigRuleNames"
    )
    limit: CosmosPageLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConfigRuleStatusesResponse(_ConfigServiceModelBase):
    organization_config_rule_statuses: OrganizationConfigRuleStatuses = pydantic.Field(
        None, alias="OrganizationConfigRuleStatuses"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConfigRulesRequest(_ConfigServiceModelBase):
    organization_config_rule_names: OrganizationConfigRuleNames = pydantic.Field(
        None, alias="OrganizationConfigRuleNames"
    )
    limit: CosmosPageLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConfigRulesResponse(_ConfigServiceModelBase):
    organization_config_rules: OrganizationConfigRules = pydantic.Field(
        None, alias="OrganizationConfigRules"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConformancePackStatusesRequest(_ConfigServiceModelBase):
    organization_conformance_pack_names: OrganizationConformancePackNames = (
        pydantic.Field(None, alias="OrganizationConformancePackNames")
    )
    limit: CosmosPageLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConformancePackStatusesResponse(_ConfigServiceModelBase):
    organization_conformance_pack_statuses: OrganizationConformancePackStatuses = (
        pydantic.Field(None, alias="OrganizationConformancePackStatuses")
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConformancePacksRequest(_ConfigServiceModelBase):
    organization_conformance_pack_names: OrganizationConformancePackNames = (
        pydantic.Field(None, alias="OrganizationConformancePackNames")
    )
    limit: CosmosPageLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeOrganizationConformancePacksResponse(_ConfigServiceModelBase):
    organization_conformance_packs: OrganizationConformancePacks = pydantic.Field(
        None, alias="OrganizationConformancePacks"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribePendingAggregationRequestsRequest(_ConfigServiceModelBase):
    limit: DescribePendingAggregationRequestsLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribePendingAggregationRequestsResponse(_ConfigServiceModelBase):
    pending_aggregation_requests: PendingAggregationRequestList = pydantic.Field(
        None, alias="PendingAggregationRequests"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeRemediationConfigurationsRequest(_ConfigServiceModelBase):
    config_rule_names: ConfigRuleNames = pydantic.Field(None, alias="ConfigRuleNames")


class DescribeRemediationConfigurationsResponse(_ConfigServiceModelBase):
    remediation_configurations: RemediationConfigurations = pydantic.Field(
        None, alias="RemediationConfigurations"
    )


class DescribeRemediationExceptionsRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_keys: RemediationExceptionResourceKeys = pydantic.Field(
        None, alias="ResourceKeys"
    )
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeRemediationExceptionsResponse(_ConfigServiceModelBase):
    remediation_exceptions: RemediationExceptions = pydantic.Field(
        None, alias="RemediationExceptions"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeRemediationExecutionStatusRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_keys: ResourceKeys = pydantic.Field(None, alias="ResourceKeys")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeRemediationExecutionStatusResponse(_ConfigServiceModelBase):
    remediation_execution_statuses: RemediationExecutionStatuses = pydantic.Field(
        None, alias="RemediationExecutionStatuses"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class DescribeRetentionConfigurationsRequest(_ConfigServiceModelBase):
    retention_configuration_names: RetentionConfigurationNameList = pydantic.Field(
        None, alias="RetentionConfigurationNames"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeRetentionConfigurationsResponse(_ConfigServiceModelBase):
    retention_configurations: RetentionConfigurationList = pydantic.Field(
        None, alias="RetentionConfigurations"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class Evaluation(_ConfigServiceModelBase):
    compliance_resource_type: StringWithCharLimit256 = pydantic.Field(
        None, alias="ComplianceResourceType"
    )
    compliance_resource_id: BaseResourceId = pydantic.Field(
        None, alias="ComplianceResourceId"
    )
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    annotation: StringWithCharLimit256 = pydantic.Field(None, alias="Annotation")
    ordering_timestamp: OrderingTimestamp = pydantic.Field(
        None, alias="OrderingTimestamp"
    )


class EvaluationContext(_ConfigServiceModelBase):
    evaluation_context_identifier: EvaluationContextIdentifier = pydantic.Field(
        None, alias="EvaluationContextIdentifier"
    )


class EvaluationModeConfiguration(_ConfigServiceModelBase):
    mode: EvaluationMode = pydantic.Field(None, alias="Mode")


class EvaluationResult(_ConfigServiceModelBase):
    evaluation_result_identifier: "EvaluationResultIdentifier" = pydantic.Field(
        None, alias="EvaluationResultIdentifier"
    )
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    result_recorded_time: Date = pydantic.Field(None, alias="ResultRecordedTime")
    config_rule_invoked_time: Date = pydantic.Field(None, alias="ConfigRuleInvokedTime")
    annotation: StringWithCharLimit256 = pydantic.Field(None, alias="Annotation")
    result_token: String = pydantic.Field(None, alias="ResultToken")


class EvaluationResultIdentifier(_ConfigServiceModelBase):
    evaluation_result_qualifier: "EvaluationResultQualifier" = pydantic.Field(
        None, alias="EvaluationResultQualifier"
    )
    ordering_timestamp: Date = pydantic.Field(None, alias="OrderingTimestamp")
    resource_evaluation_id: ResourceEvaluationId = pydantic.Field(
        None, alias="ResourceEvaluationId"
    )


class EvaluationResultQualifier(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_id: BaseResourceId = pydantic.Field(None, alias="ResourceId")
    evaluation_mode: EvaluationMode = pydantic.Field(None, alias="EvaluationMode")


class EvaluationStatus(_ConfigServiceModelBase):
    status: ResourceEvaluationStatus = pydantic.Field(None, alias="Status")
    failure_reason: StringWithCharLimit1024 = pydantic.Field(
        None, alias="FailureReason"
    )


class ExclusionByResourceTypes(_ConfigServiceModelBase):
    resource_types: ResourceTypeList = pydantic.Field(None, alias="resourceTypes")


class ExecutionControls(_ConfigServiceModelBase):
    ssm_controls: "SsmControls" = pydantic.Field(None, alias="SsmControls")


class ExternalEvaluation(_ConfigServiceModelBase):
    compliance_resource_type: StringWithCharLimit256 = pydantic.Field(
        None, alias="ComplianceResourceType"
    )
    compliance_resource_id: BaseResourceId = pydantic.Field(
        None, alias="ComplianceResourceId"
    )
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    annotation: StringWithCharLimit256 = pydantic.Field(None, alias="Annotation")
    ordering_timestamp: OrderingTimestamp = pydantic.Field(
        None, alias="OrderingTimestamp"
    )


class FailedDeleteRemediationExceptionsBatch(_ConfigServiceModelBase):
    failure_message: String = pydantic.Field(None, alias="FailureMessage")
    failed_items: RemediationExceptionResourceKeys = pydantic.Field(
        None, alias="FailedItems"
    )


class FailedRemediationBatch(_ConfigServiceModelBase):
    failure_message: String = pydantic.Field(None, alias="FailureMessage")
    failed_items: RemediationConfigurations = pydantic.Field(None, alias="FailedItems")


class FailedRemediationExceptionBatch(_ConfigServiceModelBase):
    failure_message: String = pydantic.Field(None, alias="FailureMessage")
    failed_items: RemediationExceptions = pydantic.Field(None, alias="FailedItems")


class FieldInfo(_ConfigServiceModelBase):
    name: FieldName = pydantic.Field(None, alias="Name")


class GetAggregateComplianceDetailsByConfigRuleRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    aws_region: AwsRegion = pydantic.Field(None, alias="AwsRegion")
    compliance_type: ComplianceType = pydantic.Field(None, alias="ComplianceType")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateComplianceDetailsByConfigRuleResponse(_ConfigServiceModelBase):
    aggregate_evaluation_results: AggregateEvaluationResultList = pydantic.Field(
        None, alias="AggregateEvaluationResults"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateConfigRuleComplianceSummaryRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    filters: "ConfigRuleComplianceSummaryFilters" = pydantic.Field(
        None, alias="Filters"
    )
    group_by_key: ConfigRuleComplianceSummaryGroupKey = pydantic.Field(
        None, alias="GroupByKey"
    )
    limit: GroupByAPILimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateConfigRuleComplianceSummaryResponse(_ConfigServiceModelBase):
    group_by_key: StringWithCharLimit256 = pydantic.Field(None, alias="GroupByKey")
    aggregate_compliance_counts: AggregateComplianceCountList = pydantic.Field(
        None, alias="AggregateComplianceCounts"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateConformancePackComplianceSummaryRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    filters: "AggregateConformancePackComplianceSummaryFilters" = pydantic.Field(
        None, alias="Filters"
    )
    group_by_key: AggregateConformancePackComplianceSummaryGroupKey = pydantic.Field(
        None, alias="GroupByKey"
    )
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateConformancePackComplianceSummaryResponse(_ConfigServiceModelBase):
    aggregate_conformance_pack_compliance_summaries: AggregateConformancePackComplianceSummaryList = pydantic.Field(
        None, alias="AggregateConformancePackComplianceSummaries"
    )
    group_by_key: StringWithCharLimit256 = pydantic.Field(None, alias="GroupByKey")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateDiscoveredResourceCountsRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    filters: "ResourceCountFilters" = pydantic.Field(None, alias="Filters")
    group_by_key: ResourceCountGroupKey = pydantic.Field(None, alias="GroupByKey")
    limit: GroupByAPILimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateDiscoveredResourceCountsResponse(_ConfigServiceModelBase):
    total_discovered_resources: Long = pydantic.Field(
        None, alias="TotalDiscoveredResources"
    )
    group_by_key: StringWithCharLimit256 = pydantic.Field(None, alias="GroupByKey")
    grouped_resource_counts: GroupedResourceCountList = pydantic.Field(
        None, alias="GroupedResourceCounts"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetAggregateResourceConfigRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    resource_identifier: "AggregateResourceIdentifier" = pydantic.Field(
        None, alias="ResourceIdentifier"
    )


class GetAggregateResourceConfigResponse(_ConfigServiceModelBase):
    configuration_item: "ConfigurationItem" = pydantic.Field(
        None, alias="ConfigurationItem"
    )


class GetComplianceDetailsByConfigRuleRequest(_ConfigServiceModelBase):
    config_rule_name: StringWithCharLimit64 = pydantic.Field(
        None, alias="ConfigRuleName"
    )
    compliance_types: ComplianceTypes = pydantic.Field(None, alias="ComplianceTypes")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetComplianceDetailsByConfigRuleResponse(_ConfigServiceModelBase):
    evaluation_results: EvaluationResults = pydantic.Field(
        None, alias="EvaluationResults"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetComplianceDetailsByResourceRequest(_ConfigServiceModelBase):
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_id: BaseResourceId = pydantic.Field(None, alias="ResourceId")
    compliance_types: ComplianceTypes = pydantic.Field(None, alias="ComplianceTypes")
    next_token: String = pydantic.Field(None, alias="NextToken")
    resource_evaluation_id: ResourceEvaluationId = pydantic.Field(
        None, alias="ResourceEvaluationId"
    )


class GetComplianceDetailsByResourceResponse(_ConfigServiceModelBase):
    evaluation_results: EvaluationResults = pydantic.Field(
        None, alias="EvaluationResults"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class GetComplianceSummaryByConfigRuleResponse(_ConfigServiceModelBase):
    compliance_summary: "ComplianceSummary" = pydantic.Field(
        None, alias="ComplianceSummary"
    )


class GetComplianceSummaryByResourceTypeRequest(_ConfigServiceModelBase):
    resource_types: ResourceTypes = pydantic.Field(None, alias="ResourceTypes")


class GetComplianceSummaryByResourceTypeResponse(_ConfigServiceModelBase):
    compliance_summaries_by_resource_type: ComplianceSummariesByResourceType = (
        pydantic.Field(None, alias="ComplianceSummariesByResourceType")
    )


class GetConformancePackComplianceDetailsRequest(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    filters: "ConformancePackEvaluationFilters" = pydantic.Field(None, alias="Filters")
    limit: GetConformancePackComplianceDetailsLimit = pydantic.Field(
        None, alias="Limit"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetConformancePackComplianceDetailsResponse(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    conformance_pack_rule_evaluation_results: ConformancePackRuleEvaluationResultsList = pydantic.Field(
        None, alias="ConformancePackRuleEvaluationResults"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetConformancePackComplianceSummaryRequest(_ConfigServiceModelBase):
    conformance_pack_names: ConformancePackNamesToSummarizeList = pydantic.Field(
        None, alias="ConformancePackNames"
    )
    limit: PageSizeLimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetConformancePackComplianceSummaryResponse(_ConfigServiceModelBase):
    conformance_pack_compliance_summary_list: ConformancePackComplianceSummaryList = (
        pydantic.Field(None, alias="ConformancePackComplianceSummaryList")
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class GetCustomRulePolicyRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")


class GetCustomRulePolicyResponse(_ConfigServiceModelBase):
    policy_text: PolicyText = pydantic.Field(None, alias="PolicyText")


class GetDiscoveredResourceCountsRequest(_ConfigServiceModelBase):
    resource_types: ResourceTypes = pydantic.Field(None, alias="resourceTypes")
    limit: Limit = pydantic.Field(None, alias="limit")
    next_token: NextToken = pydantic.Field(None, alias="nextToken")


class GetDiscoveredResourceCountsResponse(_ConfigServiceModelBase):
    total_discovered_resources: Long = pydantic.Field(
        None, alias="totalDiscoveredResources"
    )
    resource_counts: ResourceCounts = pydantic.Field(None, alias="resourceCounts")
    next_token: NextToken = pydantic.Field(None, alias="nextToken")


class GetOrganizationConfigRuleDetailedStatusRequest(_ConfigServiceModelBase):
    organization_config_rule_name: OrganizationConfigRuleName = pydantic.Field(
        None, alias="OrganizationConfigRuleName"
    )
    filters: "StatusDetailFilters" = pydantic.Field(None, alias="Filters")
    limit: CosmosPageLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class GetOrganizationConfigRuleDetailedStatusResponse(_ConfigServiceModelBase):
    organization_config_rule_detailed_status: OrganizationConfigRuleDetailedStatus = (
        pydantic.Field(None, alias="OrganizationConfigRuleDetailedStatus")
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class GetOrganizationConformancePackDetailedStatusRequest(_ConfigServiceModelBase):
    organization_conformance_pack_name: OrganizationConformancePackName = (
        pydantic.Field(None, alias="OrganizationConformancePackName")
    )
    filters: "OrganizationResourceDetailedStatusFilters" = pydantic.Field(
        None, alias="Filters"
    )
    limit: CosmosPageLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class GetOrganizationConformancePackDetailedStatusResponse(_ConfigServiceModelBase):
    organization_conformance_pack_detailed_statuses: OrganizationConformancePackDetailedStatuses = pydantic.Field(
        None, alias="OrganizationConformancePackDetailedStatuses"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class GetOrganizationCustomRulePolicyRequest(_ConfigServiceModelBase):
    organization_config_rule_name: OrganizationConfigRuleName = pydantic.Field(
        None, alias="OrganizationConfigRuleName"
    )


class GetOrganizationCustomRulePolicyResponse(_ConfigServiceModelBase):
    policy_text: PolicyText = pydantic.Field(None, alias="PolicyText")


class GetResourceConfigHistoryRequest(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="resourceId")
    later_time: LaterTime = pydantic.Field(None, alias="laterTime")
    earlier_time: EarlierTime = pydantic.Field(None, alias="earlierTime")
    chronological_order: ChronologicalOrder = pydantic.Field(
        None, alias="chronologicalOrder"
    )
    limit: Limit = pydantic.Field(None, alias="limit")
    next_token: NextToken = pydantic.Field(None, alias="nextToken")


class GetResourceConfigHistoryResponse(_ConfigServiceModelBase):
    configuration_items: ConfigurationItemList = pydantic.Field(
        None, alias="configurationItems"
    )
    next_token: NextToken = pydantic.Field(None, alias="nextToken")


class GetResourceEvaluationSummaryRequest(_ConfigServiceModelBase):
    resource_evaluation_id: ResourceEvaluationId = pydantic.Field(
        None, alias="ResourceEvaluationId"
    )


class GetResourceEvaluationSummaryResponse(_ConfigServiceModelBase):
    resource_evaluation_id: ResourceEvaluationId = pydantic.Field(
        None, alias="ResourceEvaluationId"
    )
    evaluation_mode: EvaluationMode = pydantic.Field(None, alias="EvaluationMode")
    evaluation_status: "EvaluationStatus" = pydantic.Field(
        None, alias="EvaluationStatus"
    )
    evaluation_start_timestamp: Date = pydantic.Field(
        None, alias="EvaluationStartTimestamp"
    )
    compliance: ComplianceType = pydantic.Field(None, alias="Compliance")
    evaluation_context: "EvaluationContext" = pydantic.Field(
        None, alias="EvaluationContext"
    )
    resource_details: "ResourceDetails" = pydantic.Field(None, alias="ResourceDetails")


class GetStoredQueryRequest(_ConfigServiceModelBase):
    query_name: QueryName = pydantic.Field(None, alias="QueryName")


class GetStoredQueryResponse(_ConfigServiceModelBase):
    stored_query: "StoredQuery" = pydantic.Field(None, alias="StoredQuery")


class GroupedResourceCount(_ConfigServiceModelBase):
    group_name: StringWithCharLimit256 = pydantic.Field(None, alias="GroupName")
    resource_count: Long = pydantic.Field(None, alias="ResourceCount")


class ListAggregateDiscoveredResourcesRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    filters: "ResourceFilters" = pydantic.Field(None, alias="Filters")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListAggregateDiscoveredResourcesResponse(_ConfigServiceModelBase):
    resource_identifiers: DiscoveredResourceIdentifierList = pydantic.Field(
        None, alias="ResourceIdentifiers"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListConformancePackComplianceScoresRequest(_ConfigServiceModelBase):
    filters: "ConformancePackComplianceScoresFilters" = pydantic.Field(
        None, alias="Filters"
    )
    sort_order: SortOrder = pydantic.Field(None, alias="SortOrder")
    sort_by: SortBy = pydantic.Field(None, alias="SortBy")
    limit: PageSizeLimit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListConformancePackComplianceScoresResponse(_ConfigServiceModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    conformance_pack_compliance_scores: ConformancePackComplianceScores = (
        pydantic.Field(None, alias="ConformancePackComplianceScores")
    )


class ListDiscoveredResourcesRequest(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_ids: ResourceIdList = pydantic.Field(None, alias="resourceIds")
    resource_name: ResourceName = pydantic.Field(None, alias="resourceName")
    limit: Limit = pydantic.Field(None, alias="limit")
    include_deleted_resources: Boolean = pydantic.Field(
        None, alias="includeDeletedResources"
    )
    next_token: NextToken = pydantic.Field(None, alias="nextToken")


class ListDiscoveredResourcesResponse(_ConfigServiceModelBase):
    resource_identifiers: ResourceIdentifierList = pydantic.Field(
        None, alias="resourceIdentifiers"
    )
    next_token: NextToken = pydantic.Field(None, alias="nextToken")


class ListResourceEvaluationsRequest(_ConfigServiceModelBase):
    filters: "ResourceEvaluationFilters" = pydantic.Field(None, alias="Filters")
    limit: ListResourceEvaluationsPageItemLimit = pydantic.Field(None, alias="Limit")
    next_token: String = pydantic.Field(None, alias="NextToken")


class ListResourceEvaluationsResponse(_ConfigServiceModelBase):
    resource_evaluations: ResourceEvaluations = pydantic.Field(
        None, alias="ResourceEvaluations"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class ListStoredQueriesRequest(_ConfigServiceModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: Limit = pydantic.Field(None, alias="MaxResults")


class ListStoredQueriesResponse(_ConfigServiceModelBase):
    stored_query_metadata: StoredQueryMetadataList = pydantic.Field(
        None, alias="StoredQueryMetadata"
    )
    next_token: String = pydantic.Field(None, alias="NextToken")


class ListTagsForResourceRequest(_ConfigServiceModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceArn")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListTagsForResourceResponse(_ConfigServiceModelBase):
    tags: TagList = pydantic.Field(None, alias="Tags")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class MemberAccountStatus(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    config_rule_name: StringWithCharLimit64 = pydantic.Field(
        None, alias="ConfigRuleName"
    )
    member_account_rule_status: MemberAccountRuleStatus = pydantic.Field(
        None, alias="MemberAccountRuleStatus"
    )
    error_code: String = pydantic.Field(None, alias="ErrorCode")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")


class OrganizationAggregationSource(_ConfigServiceModelBase):
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    aws_regions: AggregatorRegionList = pydantic.Field(None, alias="AwsRegions")
    all_aws_regions: Boolean = pydantic.Field(None, alias="AllAwsRegions")


class OrganizationConfigRule(_ConfigServiceModelBase):
    organization_config_rule_name: OrganizationConfigRuleName = pydantic.Field(
        None, alias="OrganizationConfigRuleName"
    )
    organization_config_rule_arn: StringWithCharLimit256 = pydantic.Field(
        None, alias="OrganizationConfigRuleArn"
    )
    organization_managed_rule_metadata: "OrganizationManagedRuleMetadata" = (
        pydantic.Field(None, alias="OrganizationManagedRuleMetadata")
    )
    organization_custom_rule_metadata: "OrganizationCustomRuleMetadata" = (
        pydantic.Field(None, alias="OrganizationCustomRuleMetadata")
    )
    excluded_accounts: ExcludedAccounts = pydantic.Field(None, alias="ExcludedAccounts")
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")
    organization_custom_policy_rule_metadata: "OrganizationCustomPolicyRuleMetadataNoPolicy" = pydantic.Field(
        None, alias="OrganizationCustomPolicyRuleMetadata"
    )


class OrganizationConfigRuleStatus(_ConfigServiceModelBase):
    organization_config_rule_name: OrganizationConfigRuleName = pydantic.Field(
        None, alias="OrganizationConfigRuleName"
    )
    organization_rule_status: OrganizationRuleStatus = pydantic.Field(
        None, alias="OrganizationRuleStatus"
    )
    error_code: String = pydantic.Field(None, alias="ErrorCode")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")


class OrganizationConformancePack(_ConfigServiceModelBase):
    organization_conformance_pack_name: OrganizationConformancePackName = (
        pydantic.Field(None, alias="OrganizationConformancePackName")
    )
    organization_conformance_pack_arn: StringWithCharLimit256 = pydantic.Field(
        None, alias="OrganizationConformancePackArn"
    )
    delivery_s_3_bucket: DeliveryS3Bucket = pydantic.Field(
        None, alias="DeliveryS3Bucket"
    )
    delivery_s_3_key_prefix: DeliveryS3KeyPrefix = pydantic.Field(
        None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: ConformancePackInputParameters = pydantic.Field(
        None, alias="ConformancePackInputParameters"
    )
    excluded_accounts: ExcludedAccounts = pydantic.Field(None, alias="ExcludedAccounts")
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")


class OrganizationConformancePackDetailedStatus(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    conformance_pack_name: StringWithCharLimit256 = pydantic.Field(
        None, alias="ConformancePackName"
    )
    status: OrganizationResourceDetailedStatus = pydantic.Field(None, alias="Status")
    error_code: String = pydantic.Field(None, alias="ErrorCode")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")


class OrganizationConformancePackStatus(_ConfigServiceModelBase):
    organization_conformance_pack_name: OrganizationConformancePackName = (
        pydantic.Field(None, alias="OrganizationConformancePackName")
    )
    status: OrganizationResourceStatus = pydantic.Field(None, alias="Status")
    error_code: String = pydantic.Field(None, alias="ErrorCode")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")
    last_update_time: Date = pydantic.Field(None, alias="LastUpdateTime")


class OrganizationCustomPolicyRuleMetadata(_ConfigServiceModelBase):
    description: StringWithCharLimit256Min0 = pydantic.Field(None, alias="Description")
    organization_config_rule_trigger_types: OrganizationConfigRuleTriggerTypeNoSNs = (
        pydantic.Field(None, alias="OrganizationConfigRuleTriggerTypes")
    )
    input_parameters: StringWithCharLimit2048 = pydantic.Field(
        None, alias="InputParameters"
    )
    maximum_execution_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="MaximumExecutionFrequency"
    )
    resource_types_scope: ResourceTypesScope = pydantic.Field(
        None, alias="ResourceTypesScope"
    )
    resource_id_scope: StringWithCharLimit768 = pydantic.Field(
        None, alias="ResourceIdScope"
    )
    tag_key_scope: StringWithCharLimit128 = pydantic.Field(None, alias="TagKeyScope")
    tag_value_scope: StringWithCharLimit256 = pydantic.Field(
        None, alias="TagValueScope"
    )
    policy_runtime: PolicyRuntime = pydantic.Field(None, alias="PolicyRuntime")
    policy_text: PolicyText = pydantic.Field(None, alias="PolicyText")
    debug_log_delivery_accounts: DebugLogDeliveryAccounts = pydantic.Field(
        None, alias="DebugLogDeliveryAccounts"
    )


class OrganizationCustomPolicyRuleMetadataNoPolicy(_ConfigServiceModelBase):
    description: StringWithCharLimit256Min0 = pydantic.Field(None, alias="Description")
    organization_config_rule_trigger_types: OrganizationConfigRuleTriggerTypeNoSNs = (
        pydantic.Field(None, alias="OrganizationConfigRuleTriggerTypes")
    )
    input_parameters: StringWithCharLimit2048 = pydantic.Field(
        None, alias="InputParameters"
    )
    maximum_execution_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="MaximumExecutionFrequency"
    )
    resource_types_scope: ResourceTypesScope = pydantic.Field(
        None, alias="ResourceTypesScope"
    )
    resource_id_scope: StringWithCharLimit768 = pydantic.Field(
        None, alias="ResourceIdScope"
    )
    tag_key_scope: StringWithCharLimit128 = pydantic.Field(None, alias="TagKeyScope")
    tag_value_scope: StringWithCharLimit256 = pydantic.Field(
        None, alias="TagValueScope"
    )
    policy_runtime: PolicyRuntime = pydantic.Field(None, alias="PolicyRuntime")
    debug_log_delivery_accounts: DebugLogDeliveryAccounts = pydantic.Field(
        None, alias="DebugLogDeliveryAccounts"
    )


class OrganizationCustomRuleMetadata(_ConfigServiceModelBase):
    description: StringWithCharLimit256Min0 = pydantic.Field(None, alias="Description")
    lambda_function_arn: StringWithCharLimit256 = pydantic.Field(
        None, alias="LambdaFunctionArn"
    )
    organization_config_rule_trigger_types: OrganizationConfigRuleTriggerTypes = (
        pydantic.Field(None, alias="OrganizationConfigRuleTriggerTypes")
    )
    input_parameters: StringWithCharLimit2048 = pydantic.Field(
        None, alias="InputParameters"
    )
    maximum_execution_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="MaximumExecutionFrequency"
    )
    resource_types_scope: ResourceTypesScope = pydantic.Field(
        None, alias="ResourceTypesScope"
    )
    resource_id_scope: StringWithCharLimit768 = pydantic.Field(
        None, alias="ResourceIdScope"
    )
    tag_key_scope: StringWithCharLimit128 = pydantic.Field(None, alias="TagKeyScope")
    tag_value_scope: StringWithCharLimit256 = pydantic.Field(
        None, alias="TagValueScope"
    )


class OrganizationManagedRuleMetadata(_ConfigServiceModelBase):
    description: StringWithCharLimit256Min0 = pydantic.Field(None, alias="Description")
    rule_identifier: StringWithCharLimit256 = pydantic.Field(
        None, alias="RuleIdentifier"
    )
    input_parameters: StringWithCharLimit2048 = pydantic.Field(
        None, alias="InputParameters"
    )
    maximum_execution_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="MaximumExecutionFrequency"
    )
    resource_types_scope: ResourceTypesScope = pydantic.Field(
        None, alias="ResourceTypesScope"
    )
    resource_id_scope: StringWithCharLimit768 = pydantic.Field(
        None, alias="ResourceIdScope"
    )
    tag_key_scope: StringWithCharLimit128 = pydantic.Field(None, alias="TagKeyScope")
    tag_value_scope: StringWithCharLimit256 = pydantic.Field(
        None, alias="TagValueScope"
    )


class OrganizationResourceDetailedStatusFilters(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    status: OrganizationResourceDetailedStatus = pydantic.Field(None, alias="Status")


class PendingAggregationRequest(_ConfigServiceModelBase):
    requester_account_id: AccountId = pydantic.Field(None, alias="RequesterAccountId")
    requester_aws_region: AwsRegion = pydantic.Field(None, alias="RequesterAwsRegion")


class PutAggregationAuthorizationRequest(_ConfigServiceModelBase):
    authorized_account_id: AccountId = pydantic.Field(None, alias="AuthorizedAccountId")
    authorized_aws_region: AwsRegion = pydantic.Field(None, alias="AuthorizedAwsRegion")
    tags: TagsList = pydantic.Field(None, alias="Tags")


class PutAggregationAuthorizationResponse(_ConfigServiceModelBase):
    aggregation_authorization: "AggregationAuthorization" = pydantic.Field(
        None, alias="AggregationAuthorization"
    )


class PutConfigRuleRequest(_ConfigServiceModelBase):
    config_rule: "ConfigRule" = pydantic.Field(None, alias="ConfigRule")
    tags: TagsList = pydantic.Field(None, alias="Tags")


class PutConfigurationAggregatorRequest(_ConfigServiceModelBase):
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    account_aggregation_sources: AccountAggregationSourceList = pydantic.Field(
        None, alias="AccountAggregationSources"
    )
    organization_aggregation_source: "OrganizationAggregationSource" = pydantic.Field(
        None, alias="OrganizationAggregationSource"
    )
    tags: TagsList = pydantic.Field(None, alias="Tags")


class PutConfigurationAggregatorResponse(_ConfigServiceModelBase):
    configuration_aggregator: "ConfigurationAggregator" = pydantic.Field(
        None, alias="ConfigurationAggregator"
    )


class PutConfigurationRecorderRequest(_ConfigServiceModelBase):
    configuration_recorder: "ConfigurationRecorder" = pydantic.Field(
        None, alias="ConfigurationRecorder"
    )


class PutConformancePackRequest(_ConfigServiceModelBase):
    conformance_pack_name: ConformancePackName = pydantic.Field(
        None, alias="ConformancePackName"
    )
    template_s_3_uri: TemplateS3Uri = pydantic.Field(None, alias="TemplateS3Uri")
    template_body: TemplateBody = pydantic.Field(None, alias="TemplateBody")
    delivery_s_3_bucket: DeliveryS3Bucket = pydantic.Field(
        None, alias="DeliveryS3Bucket"
    )
    delivery_s_3_key_prefix: DeliveryS3KeyPrefix = pydantic.Field(
        None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: ConformancePackInputParameters = pydantic.Field(
        None, alias="ConformancePackInputParameters"
    )
    template_ssm_document_details: "TemplateSSMDocumentDetails" = pydantic.Field(
        None, alias="TemplateSSMDocumentDetails"
    )


class PutConformancePackResponse(_ConfigServiceModelBase):
    conformance_pack_arn: ConformancePackArn = pydantic.Field(
        None, alias="ConformancePackArn"
    )


class PutDeliveryChannelRequest(_ConfigServiceModelBase):
    delivery_channel: "DeliveryChannel" = pydantic.Field(None, alias="DeliveryChannel")


class PutEvaluationsRequest(_ConfigServiceModelBase):
    evaluations: Evaluations = pydantic.Field(None, alias="Evaluations")
    result_token: String = pydantic.Field(None, alias="ResultToken")
    test_mode: Boolean = pydantic.Field(None, alias="TestMode")


class PutEvaluationsResponse(_ConfigServiceModelBase):
    failed_evaluations: Evaluations = pydantic.Field(None, alias="FailedEvaluations")


class PutExternalEvaluationRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    external_evaluation: "ExternalEvaluation" = pydantic.Field(
        None, alias="ExternalEvaluation"
    )


class PutExternalEvaluationResponse(_ConfigServiceModelBase):
    pass


class PutOrganizationConfigRuleRequest(_ConfigServiceModelBase):
    organization_config_rule_name: OrganizationConfigRuleName = pydantic.Field(
        None, alias="OrganizationConfigRuleName"
    )
    organization_managed_rule_metadata: "OrganizationManagedRuleMetadata" = (
        pydantic.Field(None, alias="OrganizationManagedRuleMetadata")
    )
    organization_custom_rule_metadata: "OrganizationCustomRuleMetadata" = (
        pydantic.Field(None, alias="OrganizationCustomRuleMetadata")
    )
    excluded_accounts: ExcludedAccounts = pydantic.Field(None, alias="ExcludedAccounts")
    organization_custom_policy_rule_metadata: "OrganizationCustomPolicyRuleMetadata" = (
        pydantic.Field(None, alias="OrganizationCustomPolicyRuleMetadata")
    )


class PutOrganizationConfigRuleResponse(_ConfigServiceModelBase):
    organization_config_rule_arn: StringWithCharLimit256 = pydantic.Field(
        None, alias="OrganizationConfigRuleArn"
    )


class PutOrganizationConformancePackRequest(_ConfigServiceModelBase):
    organization_conformance_pack_name: OrganizationConformancePackName = (
        pydantic.Field(None, alias="OrganizationConformancePackName")
    )
    template_s_3_uri: TemplateS3Uri = pydantic.Field(None, alias="TemplateS3Uri")
    template_body: TemplateBody = pydantic.Field(None, alias="TemplateBody")
    delivery_s_3_bucket: DeliveryS3Bucket = pydantic.Field(
        None, alias="DeliveryS3Bucket"
    )
    delivery_s_3_key_prefix: DeliveryS3KeyPrefix = pydantic.Field(
        None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: ConformancePackInputParameters = pydantic.Field(
        None, alias="ConformancePackInputParameters"
    )
    excluded_accounts: ExcludedAccounts = pydantic.Field(None, alias="ExcludedAccounts")


class PutOrganizationConformancePackResponse(_ConfigServiceModelBase):
    organization_conformance_pack_arn: StringWithCharLimit256 = pydantic.Field(
        None, alias="OrganizationConformancePackArn"
    )


class PutRemediationConfigurationsRequest(_ConfigServiceModelBase):
    remediation_configurations: RemediationConfigurations = pydantic.Field(
        None, alias="RemediationConfigurations"
    )


class PutRemediationConfigurationsResponse(_ConfigServiceModelBase):
    failed_batches: FailedRemediationBatches = pydantic.Field(
        None, alias="FailedBatches"
    )


class PutRemediationExceptionsRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_keys: RemediationExceptionResourceKeys = pydantic.Field(
        None, alias="ResourceKeys"
    )
    message: StringWithCharLimit1024 = pydantic.Field(None, alias="Message")
    expiration_time: Date = pydantic.Field(None, alias="ExpirationTime")


class PutRemediationExceptionsResponse(_ConfigServiceModelBase):
    failed_batches: FailedRemediationExceptionBatches = pydantic.Field(
        None, alias="FailedBatches"
    )


class PutResourceConfigRequest(_ConfigServiceModelBase):
    resource_type: ResourceTypeString = pydantic.Field(None, alias="ResourceType")
    schema_version_id: SchemaVersionId = pydantic.Field(None, alias="SchemaVersionId")
    resource_id: ResourceId = pydantic.Field(None, alias="ResourceId")
    resource_name: ResourceName = pydantic.Field(None, alias="ResourceName")
    configuration: Configuration = pydantic.Field(None, alias="Configuration")
    tags: Tags = pydantic.Field(None, alias="Tags")


class PutRetentionConfigurationRequest(_ConfigServiceModelBase):
    retention_period_in_days: RetentionPeriodInDays = pydantic.Field(
        None, alias="RetentionPeriodInDays"
    )


class PutRetentionConfigurationResponse(_ConfigServiceModelBase):
    retention_configuration: "RetentionConfiguration" = pydantic.Field(
        None, alias="RetentionConfiguration"
    )


class PutStoredQueryRequest(_ConfigServiceModelBase):
    stored_query: "StoredQuery" = pydantic.Field(None, alias="StoredQuery")
    tags: TagsList = pydantic.Field(None, alias="Tags")


class PutStoredQueryResponse(_ConfigServiceModelBase):
    query_arn: QueryArn = pydantic.Field(None, alias="QueryArn")


class QueryInfo(_ConfigServiceModelBase):
    select_fields: FieldInfoList = pydantic.Field(None, alias="SelectFields")


class RecordingGroup(_ConfigServiceModelBase):
    all_supported: AllSupported = pydantic.Field(None, alias="allSupported")
    include_global_resource_types: IncludeGlobalResourceTypes = pydantic.Field(
        None, alias="includeGlobalResourceTypes"
    )
    resource_types: ResourceTypeList = pydantic.Field(None, alias="resourceTypes")
    exclusion_by_resource_types: "ExclusionByResourceTypes" = pydantic.Field(
        None, alias="exclusionByResourceTypes"
    )
    recording_strategy: "RecordingStrategy" = pydantic.Field(
        None, alias="recordingStrategy"
    )


class RecordingStrategy(_ConfigServiceModelBase):
    use_only: RecordingStrategyType = pydantic.Field(None, alias="useOnly")


class Relationship(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="resourceId")
    resource_name: ResourceName = pydantic.Field(None, alias="resourceName")
    relationship_name: RelationshipName = pydantic.Field(None, alias="relationshipName")


class RemediationConfiguration(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    target_type: RemediationTargetType = pydantic.Field(None, alias="TargetType")
    target_id: StringWithCharLimit256 = pydantic.Field(None, alias="TargetId")
    target_version: String = pydantic.Field(None, alias="TargetVersion")
    parameters: RemediationParameters = pydantic.Field(None, alias="Parameters")
    resource_type: String = pydantic.Field(None, alias="ResourceType")
    automatic: Boolean = pydantic.Field(None, alias="Automatic")
    execution_controls: "ExecutionControls" = pydantic.Field(
        None, alias="ExecutionControls"
    )
    maximum_automatic_attempts: AutoRemediationAttempts = pydantic.Field(
        None, alias="MaximumAutomaticAttempts"
    )
    retry_attempt_seconds: AutoRemediationAttemptSeconds = pydantic.Field(
        None, alias="RetryAttemptSeconds"
    )
    arn: StringWithCharLimit1024 = pydantic.Field(None, alias="Arn")
    created_by_service: StringWithCharLimit1024 = pydantic.Field(
        None, alias="CreatedByService"
    )


class RemediationException(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_id: StringWithCharLimit1024 = pydantic.Field(None, alias="ResourceId")
    message: StringWithCharLimit1024 = pydantic.Field(None, alias="Message")
    expiration_time: Date = pydantic.Field(None, alias="ExpirationTime")


class RemediationExceptionResourceKey(_ConfigServiceModelBase):
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_id: StringWithCharLimit1024 = pydantic.Field(None, alias="ResourceId")


class RemediationExecutionStatus(_ConfigServiceModelBase):
    resource_key: "ResourceKey" = pydantic.Field(None, alias="ResourceKey")
    state: RemediationExecutionState = pydantic.Field(None, alias="State")
    step_details: RemediationExecutionSteps = pydantic.Field(None, alias="StepDetails")
    invocation_time: Date = pydantic.Field(None, alias="InvocationTime")
    last_updated_time: Date = pydantic.Field(None, alias="LastUpdatedTime")


class RemediationExecutionStep(_ConfigServiceModelBase):
    name: String = pydantic.Field(None, alias="Name")
    state: RemediationExecutionStepState = pydantic.Field(None, alias="State")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")
    start_time: Date = pydantic.Field(None, alias="StartTime")
    stop_time: Date = pydantic.Field(None, alias="StopTime")


class RemediationParameterValue(_ConfigServiceModelBase):
    resource_value: "ResourceValue" = pydantic.Field(None, alias="ResourceValue")
    static_value: "StaticValue" = pydantic.Field(None, alias="StaticValue")


class ResourceCount(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    count: Long = pydantic.Field(None, alias="count")


class ResourceCountFilters(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    region: AwsRegion = pydantic.Field(None, alias="Region")


class ResourceDetails(_ConfigServiceModelBase):
    resource_id: BaseResourceId = pydantic.Field(None, alias="ResourceId")
    resource_type: StringWithCharLimit256 = pydantic.Field(None, alias="ResourceType")
    resource_configuration: ResourceConfiguration = pydantic.Field(
        None, alias="ResourceConfiguration"
    )
    resource_configuration_schema_type: ResourceConfigurationSchemaType = (
        pydantic.Field(None, alias="ResourceConfigurationSchemaType")
    )


class ResourceEvaluation(_ConfigServiceModelBase):
    resource_evaluation_id: ResourceEvaluationId = pydantic.Field(
        None, alias="ResourceEvaluationId"
    )
    evaluation_mode: EvaluationMode = pydantic.Field(None, alias="EvaluationMode")
    evaluation_start_timestamp: Date = pydantic.Field(
        None, alias="EvaluationStartTimestamp"
    )


class ResourceEvaluationFilters(_ConfigServiceModelBase):
    evaluation_mode: EvaluationMode = pydantic.Field(None, alias="EvaluationMode")
    time_window: "TimeWindow" = pydantic.Field(None, alias="TimeWindow")
    evaluation_context_identifier: EvaluationContextIdentifier = pydantic.Field(
        None, alias="EvaluationContextIdentifier"
    )


class ResourceFilters(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    resource_id: ResourceId = pydantic.Field(None, alias="ResourceId")
    resource_name: ResourceName = pydantic.Field(None, alias="ResourceName")
    region: AwsRegion = pydantic.Field(None, alias="Region")


class ResourceIdentifier(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="resourceId")
    resource_name: ResourceName = pydantic.Field(None, alias="resourceName")
    resource_deletion_time: ResourceDeletionTime = pydantic.Field(
        None, alias="resourceDeletionTime"
    )


class ResourceKey(_ConfigServiceModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="resourceType")
    resource_id: ResourceId = pydantic.Field(None, alias="resourceId")


class ResourceValue(_ConfigServiceModelBase):
    value: ResourceValueType = pydantic.Field(None, alias="Value")


class RetentionConfiguration(_ConfigServiceModelBase):
    name: RetentionConfigurationName = pydantic.Field(None, alias="Name")
    retention_period_in_days: RetentionPeriodInDays = pydantic.Field(
        None, alias="RetentionPeriodInDays"
    )


class Scope(_ConfigServiceModelBase):
    compliance_resource_types: ComplianceResourceTypes = pydantic.Field(
        None, alias="ComplianceResourceTypes"
    )
    tag_key: StringWithCharLimit128 = pydantic.Field(None, alias="TagKey")
    tag_value: StringWithCharLimit256 = pydantic.Field(None, alias="TagValue")
    compliance_resource_id: BaseResourceId = pydantic.Field(
        None, alias="ComplianceResourceId"
    )


class SelectAggregateResourceConfigRequest(_ConfigServiceModelBase):
    expression: Expression = pydantic.Field(None, alias="Expression")
    configuration_aggregator_name: ConfigurationAggregatorName = pydantic.Field(
        None, alias="ConfigurationAggregatorName"
    )
    limit: Limit = pydantic.Field(None, alias="Limit")
    max_results: Limit = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class SelectAggregateResourceConfigResponse(_ConfigServiceModelBase):
    results: Results = pydantic.Field(None, alias="Results")
    query_info: "QueryInfo" = pydantic.Field(None, alias="QueryInfo")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class SelectResourceConfigRequest(_ConfigServiceModelBase):
    expression: Expression = pydantic.Field(None, alias="Expression")
    limit: Limit = pydantic.Field(None, alias="Limit")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class SelectResourceConfigResponse(_ConfigServiceModelBase):
    results: Results = pydantic.Field(None, alias="Results")
    query_info: "QueryInfo" = pydantic.Field(None, alias="QueryInfo")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class Source(_ConfigServiceModelBase):
    owner: Owner = pydantic.Field(None, alias="Owner")
    source_identifier: StringWithCharLimit256 = pydantic.Field(
        None, alias="SourceIdentifier"
    )
    source_details: SourceDetails = pydantic.Field(None, alias="SourceDetails")
    custom_policy_details: "CustomPolicyDetails" = pydantic.Field(
        None, alias="CustomPolicyDetails"
    )


class SourceDetail(_ConfigServiceModelBase):
    event_source: EventSource = pydantic.Field(None, alias="EventSource")
    message_type: MessageType = pydantic.Field(None, alias="MessageType")
    maximum_execution_frequency: MaximumExecutionFrequency = pydantic.Field(
        None, alias="MaximumExecutionFrequency"
    )


class SsmControls(_ConfigServiceModelBase):
    concurrent_execution_rate_percentage: Percentage = pydantic.Field(
        None, alias="ConcurrentExecutionRatePercentage"
    )
    error_percentage: Percentage = pydantic.Field(None, alias="ErrorPercentage")


class StartConfigRulesEvaluationRequest(_ConfigServiceModelBase):
    config_rule_names: ReevaluateConfigRuleNames = pydantic.Field(
        None, alias="ConfigRuleNames"
    )


class StartConfigRulesEvaluationResponse(_ConfigServiceModelBase):
    pass


class StartConfigurationRecorderRequest(_ConfigServiceModelBase):
    configuration_recorder_name: RecorderName = pydantic.Field(
        None, alias="ConfigurationRecorderName"
    )


class StartRemediationExecutionRequest(_ConfigServiceModelBase):
    config_rule_name: ConfigRuleName = pydantic.Field(None, alias="ConfigRuleName")
    resource_keys: ResourceKeys = pydantic.Field(None, alias="ResourceKeys")


class StartRemediationExecutionResponse(_ConfigServiceModelBase):
    failure_message: String = pydantic.Field(None, alias="FailureMessage")
    failed_items: ResourceKeys = pydantic.Field(None, alias="FailedItems")


class StartResourceEvaluationRequest(_ConfigServiceModelBase):
    resource_details: "ResourceDetails" = pydantic.Field(None, alias="ResourceDetails")
    evaluation_context: "EvaluationContext" = pydantic.Field(
        None, alias="EvaluationContext"
    )
    evaluation_mode: EvaluationMode = pydantic.Field(None, alias="EvaluationMode")
    evaluation_timeout: EvaluationTimeout = pydantic.Field(
        None, alias="EvaluationTimeout"
    )
    client_token: ClientToken = pydantic.Field(None, alias="ClientToken")


class StartResourceEvaluationResponse(_ConfigServiceModelBase):
    resource_evaluation_id: ResourceEvaluationId = pydantic.Field(
        None, alias="ResourceEvaluationId"
    )


class StaticValue(_ConfigServiceModelBase):
    values: StaticParameterValues = pydantic.Field(None, alias="Values")


class StatusDetailFilters(_ConfigServiceModelBase):
    account_id: AccountId = pydantic.Field(None, alias="AccountId")
    member_account_rule_status: MemberAccountRuleStatus = pydantic.Field(
        None, alias="MemberAccountRuleStatus"
    )


class StopConfigurationRecorderRequest(_ConfigServiceModelBase):
    configuration_recorder_name: RecorderName = pydantic.Field(
        None, alias="ConfigurationRecorderName"
    )


class StoredQuery(_ConfigServiceModelBase):
    query_id: QueryId = pydantic.Field(None, alias="QueryId")
    query_arn: QueryArn = pydantic.Field(None, alias="QueryArn")
    query_name: QueryName = pydantic.Field(None, alias="QueryName")
    description: QueryDescription = pydantic.Field(None, alias="Description")
    expression: QueryExpression = pydantic.Field(None, alias="Expression")


class StoredQueryMetadata(_ConfigServiceModelBase):
    query_id: QueryId = pydantic.Field(None, alias="QueryId")
    query_arn: QueryArn = pydantic.Field(None, alias="QueryArn")
    query_name: QueryName = pydantic.Field(None, alias="QueryName")
    description: QueryDescription = pydantic.Field(None, alias="Description")


class Tag(_ConfigServiceModelBase):
    key: TagKey = pydantic.Field(None, alias="Key")
    value: TagValue = pydantic.Field(None, alias="Value")


class TagResourceRequest(_ConfigServiceModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceArn")
    tags: TagList = pydantic.Field(None, alias="Tags")


class TemplateSSMDocumentDetails(_ConfigServiceModelBase):
    document_name: SSMDocumentName = pydantic.Field(None, alias="DocumentName")
    document_version: SSMDocumentVersion = pydantic.Field(None, alias="DocumentVersion")


class TimeWindow(_ConfigServiceModelBase):
    start_time: Date = pydantic.Field(None, alias="StartTime")
    end_time: Date = pydantic.Field(None, alias="EndTime")


class UntagResourceRequest(_ConfigServiceModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceArn")
    tag_keys: TagKeyList = pydantic.Field(None, alias="TagKeys")


AccountAggregationSource.update_forward_refs()
AggregateComplianceByConfigRule.update_forward_refs()
AggregateComplianceByConformancePack.update_forward_refs()
AggregateComplianceCount.update_forward_refs()
AggregateConformancePackCompliance.update_forward_refs()
AggregateConformancePackComplianceCount.update_forward_refs()
AggregateConformancePackComplianceFilters.update_forward_refs()
AggregateConformancePackComplianceSummary.update_forward_refs()
AggregateConformancePackComplianceSummaryFilters.update_forward_refs()
AggregateEvaluationResult.update_forward_refs()
AggregateResourceIdentifier.update_forward_refs()
AggregatedSourceStatus.update_forward_refs()
AggregationAuthorization.update_forward_refs()
BaseConfigurationItem.update_forward_refs()
BatchGetAggregateResourceConfigRequest.update_forward_refs()
BatchGetAggregateResourceConfigResponse.update_forward_refs()
BatchGetResourceConfigRequest.update_forward_refs()
BatchGetResourceConfigResponse.update_forward_refs()
Compliance.update_forward_refs()
ComplianceByConfigRule.update_forward_refs()
ComplianceByResource.update_forward_refs()
ComplianceContributorCount.update_forward_refs()
ComplianceSummary.update_forward_refs()
ComplianceSummaryByResourceType.update_forward_refs()
ConfigExportDeliveryInfo.update_forward_refs()
ConfigRule.update_forward_refs()
ConfigRuleComplianceFilters.update_forward_refs()
ConfigRuleComplianceSummaryFilters.update_forward_refs()
ConfigRuleEvaluationStatus.update_forward_refs()
ConfigSnapshotDeliveryProperties.update_forward_refs()
ConfigStreamDeliveryInfo.update_forward_refs()
ConfigurationAggregator.update_forward_refs()
ConfigurationItem.update_forward_refs()
ConfigurationRecorder.update_forward_refs()
ConfigurationRecorderStatus.update_forward_refs()
ConformancePackComplianceFilters.update_forward_refs()
ConformancePackComplianceScore.update_forward_refs()
ConformancePackComplianceScoresFilters.update_forward_refs()
ConformancePackComplianceSummary.update_forward_refs()
ConformancePackDetail.update_forward_refs()
ConformancePackEvaluationFilters.update_forward_refs()
ConformancePackEvaluationResult.update_forward_refs()
ConformancePackInputParameter.update_forward_refs()
ConformancePackRuleCompliance.update_forward_refs()
ConformancePackStatusDetail.update_forward_refs()
CustomPolicyDetails.update_forward_refs()
DeleteAggregationAuthorizationRequest.update_forward_refs()
DeleteConfigRuleRequest.update_forward_refs()
DeleteConfigurationAggregatorRequest.update_forward_refs()
DeleteConfigurationRecorderRequest.update_forward_refs()
DeleteConformancePackRequest.update_forward_refs()
DeleteDeliveryChannelRequest.update_forward_refs()
DeleteEvaluationResultsRequest.update_forward_refs()
DeleteEvaluationResultsResponse.update_forward_refs()
DeleteOrganizationConfigRuleRequest.update_forward_refs()
DeleteOrganizationConformancePackRequest.update_forward_refs()
DeletePendingAggregationRequestRequest.update_forward_refs()
DeleteRemediationConfigurationRequest.update_forward_refs()
DeleteRemediationConfigurationResponse.update_forward_refs()
DeleteRemediationExceptionsRequest.update_forward_refs()
DeleteRemediationExceptionsResponse.update_forward_refs()
DeleteResourceConfigRequest.update_forward_refs()
DeleteRetentionConfigurationRequest.update_forward_refs()
DeleteStoredQueryRequest.update_forward_refs()
DeleteStoredQueryResponse.update_forward_refs()
DeliverConfigSnapshotRequest.update_forward_refs()
DeliverConfigSnapshotResponse.update_forward_refs()
DeliveryChannel.update_forward_refs()
DeliveryChannelStatus.update_forward_refs()
DescribeAggregateComplianceByConfigRulesRequest.update_forward_refs()
DescribeAggregateComplianceByConfigRulesResponse.update_forward_refs()
DescribeAggregateComplianceByConformancePacksRequest.update_forward_refs()
DescribeAggregateComplianceByConformancePacksResponse.update_forward_refs()
DescribeAggregationAuthorizationsRequest.update_forward_refs()
DescribeAggregationAuthorizationsResponse.update_forward_refs()
DescribeComplianceByConfigRuleRequest.update_forward_refs()
DescribeComplianceByConfigRuleResponse.update_forward_refs()
DescribeComplianceByResourceRequest.update_forward_refs()
DescribeComplianceByResourceResponse.update_forward_refs()
DescribeConfigRuleEvaluationStatusRequest.update_forward_refs()
DescribeConfigRuleEvaluationStatusResponse.update_forward_refs()
DescribeConfigRulesFilters.update_forward_refs()
DescribeConfigRulesRequest.update_forward_refs()
DescribeConfigRulesResponse.update_forward_refs()
DescribeConfigurationAggregatorSourcesStatusRequest.update_forward_refs()
DescribeConfigurationAggregatorSourcesStatusResponse.update_forward_refs()
DescribeConfigurationAggregatorsRequest.update_forward_refs()
DescribeConfigurationAggregatorsResponse.update_forward_refs()
DescribeConfigurationRecorderStatusRequest.update_forward_refs()
DescribeConfigurationRecorderStatusResponse.update_forward_refs()
DescribeConfigurationRecordersRequest.update_forward_refs()
DescribeConfigurationRecordersResponse.update_forward_refs()
DescribeConformancePackComplianceRequest.update_forward_refs()
DescribeConformancePackComplianceResponse.update_forward_refs()
DescribeConformancePackStatusRequest.update_forward_refs()
DescribeConformancePackStatusResponse.update_forward_refs()
DescribeConformancePacksRequest.update_forward_refs()
DescribeConformancePacksResponse.update_forward_refs()
DescribeDeliveryChannelStatusRequest.update_forward_refs()
DescribeDeliveryChannelStatusResponse.update_forward_refs()
DescribeDeliveryChannelsRequest.update_forward_refs()
DescribeDeliveryChannelsResponse.update_forward_refs()
DescribeOrganizationConfigRuleStatusesRequest.update_forward_refs()
DescribeOrganizationConfigRuleStatusesResponse.update_forward_refs()
DescribeOrganizationConfigRulesRequest.update_forward_refs()
DescribeOrganizationConfigRulesResponse.update_forward_refs()
DescribeOrganizationConformancePackStatusesRequest.update_forward_refs()
DescribeOrganizationConformancePackStatusesResponse.update_forward_refs()
DescribeOrganizationConformancePacksRequest.update_forward_refs()
DescribeOrganizationConformancePacksResponse.update_forward_refs()
DescribePendingAggregationRequestsRequest.update_forward_refs()
DescribePendingAggregationRequestsResponse.update_forward_refs()
DescribeRemediationConfigurationsRequest.update_forward_refs()
DescribeRemediationConfigurationsResponse.update_forward_refs()
DescribeRemediationExceptionsRequest.update_forward_refs()
DescribeRemediationExceptionsResponse.update_forward_refs()
DescribeRemediationExecutionStatusRequest.update_forward_refs()
DescribeRemediationExecutionStatusResponse.update_forward_refs()
DescribeRetentionConfigurationsRequest.update_forward_refs()
DescribeRetentionConfigurationsResponse.update_forward_refs()
Evaluation.update_forward_refs()
EvaluationContext.update_forward_refs()
EvaluationModeConfiguration.update_forward_refs()
EvaluationResult.update_forward_refs()
EvaluationResultIdentifier.update_forward_refs()
EvaluationResultQualifier.update_forward_refs()
EvaluationStatus.update_forward_refs()
ExclusionByResourceTypes.update_forward_refs()
ExecutionControls.update_forward_refs()
ExternalEvaluation.update_forward_refs()
FailedDeleteRemediationExceptionsBatch.update_forward_refs()
FailedRemediationBatch.update_forward_refs()
FailedRemediationExceptionBatch.update_forward_refs()
FieldInfo.update_forward_refs()
GetAggregateComplianceDetailsByConfigRuleRequest.update_forward_refs()
GetAggregateComplianceDetailsByConfigRuleResponse.update_forward_refs()
GetAggregateConfigRuleComplianceSummaryRequest.update_forward_refs()
GetAggregateConfigRuleComplianceSummaryResponse.update_forward_refs()
GetAggregateConformancePackComplianceSummaryRequest.update_forward_refs()
GetAggregateConformancePackComplianceSummaryResponse.update_forward_refs()
GetAggregateDiscoveredResourceCountsRequest.update_forward_refs()
GetAggregateDiscoveredResourceCountsResponse.update_forward_refs()
GetAggregateResourceConfigRequest.update_forward_refs()
GetAggregateResourceConfigResponse.update_forward_refs()
GetComplianceDetailsByConfigRuleRequest.update_forward_refs()
GetComplianceDetailsByConfigRuleResponse.update_forward_refs()
GetComplianceDetailsByResourceRequest.update_forward_refs()
GetComplianceDetailsByResourceResponse.update_forward_refs()
GetComplianceSummaryByConfigRuleResponse.update_forward_refs()
GetComplianceSummaryByResourceTypeRequest.update_forward_refs()
GetComplianceSummaryByResourceTypeResponse.update_forward_refs()
GetConformancePackComplianceDetailsRequest.update_forward_refs()
GetConformancePackComplianceDetailsResponse.update_forward_refs()
GetConformancePackComplianceSummaryRequest.update_forward_refs()
GetConformancePackComplianceSummaryResponse.update_forward_refs()
GetCustomRulePolicyRequest.update_forward_refs()
GetCustomRulePolicyResponse.update_forward_refs()
GetDiscoveredResourceCountsRequest.update_forward_refs()
GetDiscoveredResourceCountsResponse.update_forward_refs()
GetOrganizationConfigRuleDetailedStatusRequest.update_forward_refs()
GetOrganizationConfigRuleDetailedStatusResponse.update_forward_refs()
GetOrganizationConformancePackDetailedStatusRequest.update_forward_refs()
GetOrganizationConformancePackDetailedStatusResponse.update_forward_refs()
GetOrganizationCustomRulePolicyRequest.update_forward_refs()
GetOrganizationCustomRulePolicyResponse.update_forward_refs()
GetResourceConfigHistoryRequest.update_forward_refs()
GetResourceConfigHistoryResponse.update_forward_refs()
GetResourceEvaluationSummaryRequest.update_forward_refs()
GetResourceEvaluationSummaryResponse.update_forward_refs()
GetStoredQueryRequest.update_forward_refs()
GetStoredQueryResponse.update_forward_refs()
GroupedResourceCount.update_forward_refs()
ListAggregateDiscoveredResourcesRequest.update_forward_refs()
ListAggregateDiscoveredResourcesResponse.update_forward_refs()
ListConformancePackComplianceScoresRequest.update_forward_refs()
ListConformancePackComplianceScoresResponse.update_forward_refs()
ListDiscoveredResourcesRequest.update_forward_refs()
ListDiscoveredResourcesResponse.update_forward_refs()
ListResourceEvaluationsRequest.update_forward_refs()
ListResourceEvaluationsResponse.update_forward_refs()
ListStoredQueriesRequest.update_forward_refs()
ListStoredQueriesResponse.update_forward_refs()
ListTagsForResourceRequest.update_forward_refs()
ListTagsForResourceResponse.update_forward_refs()
MemberAccountStatus.update_forward_refs()
OrganizationAggregationSource.update_forward_refs()
OrganizationConfigRule.update_forward_refs()
OrganizationConfigRuleStatus.update_forward_refs()
OrganizationConformancePack.update_forward_refs()
OrganizationConformancePackDetailedStatus.update_forward_refs()
OrganizationConformancePackStatus.update_forward_refs()
OrganizationCustomPolicyRuleMetadata.update_forward_refs()
OrganizationCustomPolicyRuleMetadataNoPolicy.update_forward_refs()
OrganizationCustomRuleMetadata.update_forward_refs()
OrganizationManagedRuleMetadata.update_forward_refs()
OrganizationResourceDetailedStatusFilters.update_forward_refs()
PendingAggregationRequest.update_forward_refs()
PutAggregationAuthorizationRequest.update_forward_refs()
PutAggregationAuthorizationResponse.update_forward_refs()
PutConfigRuleRequest.update_forward_refs()
PutConfigurationAggregatorRequest.update_forward_refs()
PutConfigurationAggregatorResponse.update_forward_refs()
PutConfigurationRecorderRequest.update_forward_refs()
PutConformancePackRequest.update_forward_refs()
PutConformancePackResponse.update_forward_refs()
PutDeliveryChannelRequest.update_forward_refs()
PutEvaluationsRequest.update_forward_refs()
PutEvaluationsResponse.update_forward_refs()
PutExternalEvaluationRequest.update_forward_refs()
PutExternalEvaluationResponse.update_forward_refs()
PutOrganizationConfigRuleRequest.update_forward_refs()
PutOrganizationConfigRuleResponse.update_forward_refs()
PutOrganizationConformancePackRequest.update_forward_refs()
PutOrganizationConformancePackResponse.update_forward_refs()
PutRemediationConfigurationsRequest.update_forward_refs()
PutRemediationConfigurationsResponse.update_forward_refs()
PutRemediationExceptionsRequest.update_forward_refs()
PutRemediationExceptionsResponse.update_forward_refs()
PutResourceConfigRequest.update_forward_refs()
PutRetentionConfigurationRequest.update_forward_refs()
PutRetentionConfigurationResponse.update_forward_refs()
PutStoredQueryRequest.update_forward_refs()
PutStoredQueryResponse.update_forward_refs()
QueryInfo.update_forward_refs()
RecordingGroup.update_forward_refs()
RecordingStrategy.update_forward_refs()
Relationship.update_forward_refs()
RemediationConfiguration.update_forward_refs()
RemediationException.update_forward_refs()
RemediationExceptionResourceKey.update_forward_refs()
RemediationExecutionStatus.update_forward_refs()
RemediationExecutionStep.update_forward_refs()
RemediationParameterValue.update_forward_refs()
ResourceCount.update_forward_refs()
ResourceCountFilters.update_forward_refs()
ResourceDetails.update_forward_refs()
ResourceEvaluation.update_forward_refs()
ResourceEvaluationFilters.update_forward_refs()
ResourceFilters.update_forward_refs()
ResourceIdentifier.update_forward_refs()
ResourceKey.update_forward_refs()
ResourceValue.update_forward_refs()
RetentionConfiguration.update_forward_refs()
Scope.update_forward_refs()
SelectAggregateResourceConfigRequest.update_forward_refs()
SelectAggregateResourceConfigResponse.update_forward_refs()
SelectResourceConfigRequest.update_forward_refs()
SelectResourceConfigResponse.update_forward_refs()
Source.update_forward_refs()
SourceDetail.update_forward_refs()
SsmControls.update_forward_refs()
StartConfigRulesEvaluationRequest.update_forward_refs()
StartConfigRulesEvaluationResponse.update_forward_refs()
StartConfigurationRecorderRequest.update_forward_refs()
StartRemediationExecutionRequest.update_forward_refs()
StartRemediationExecutionResponse.update_forward_refs()
StartResourceEvaluationRequest.update_forward_refs()
StartResourceEvaluationResponse.update_forward_refs()
StaticValue.update_forward_refs()
StatusDetailFilters.update_forward_refs()
StopConfigurationRecorderRequest.update_forward_refs()
StoredQuery.update_forward_refs()
StoredQueryMetadata.update_forward_refs()
Tag.update_forward_refs()
TagResourceRequest.update_forward_refs()
TemplateSSMDocumentDetails.update_forward_refs()
TimeWindow.update_forward_refs()
UntagResourceRequest.update_forward_refs()
