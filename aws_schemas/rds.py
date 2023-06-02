from datetime import datetime
import typing
import enum

import pydantic


class _RDSBase(pydantic.BaseModel, frozen=True, use_enum_values=True, allow_population_by_field_name=True):
    def dict(self, by_alias=True, **kwargs) -> dict:
        return super().dict(by_alias=True, **kwargs)

ActivityStreamMode: str = pydantic.constr()
ActivityStreamPolicyStatus: str = pydantic.constr()
ActivityStreamStatus: str = pydantic.constr()
ApplyMethod: str = pydantic.constr()
AuditPolicyState: str = pydantic.constr()
AuthScheme: str = pydantic.constr()
AutomationMode: str = pydantic.constr()
AwsBackupRecoveryPointArn: str = pydantic.constr(min=43, max=350, pattern=r'^arn:aws[a-z-]*:backup:[-a-z0-9]+:[0-9]{12}:[-a-z]+:([a-z0-9\-]+:)?[a-z][a-z0-9\-]{0,255}$')
BlueGreenDeploymentIdentifier: str = pydantic.constr(min=1, max=255, pattern=r'[A-Za-z][0-9A-Za-z-:._]*')
BlueGreenDeploymentName: str = pydantic.constr(min=1, max=60, pattern=r'[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*')
BlueGreenDeploymentStatus: str = pydantic.constr()
BlueGreenDeploymentStatusDetails: str = pydantic.constr()
BlueGreenDeploymentTaskName: str = pydantic.constr()
BlueGreenDeploymentTaskStatus: str = pydantic.constr()
Boolean: bool = pydantic.conbool()
BooleanOptional: bool = pydantic.conbool()
BucketName: str = pydantic.constr(min=3, max=63, pattern=r'.*')
ClientPasswordAuthType: str = pydantic.constr()
CustomDBEngineVersionManifest: str = pydantic.constr(min=1, max=51000, pattern=r'[\s\S]*')
CustomEngineName: str = pydantic.constr(min=1, max=35, pattern=r'^[A-Za-z0-9-]{1,35}$')
CustomEngineVersion: str = pydantic.constr(min=1, max=60, pattern=r'^[a-z0-9_.-]{1,60}$')
CustomEngineVersionStatus: str = pydantic.constr()
DBClusterIdentifier: str = pydantic.constr(min=1, max=255, pattern=r'[A-Za-z][0-9A-Za-z-:._]*')
DBProxyEndpointName: str = pydantic.constr(min=1, max=63, pattern=r'[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*')
DBProxyEndpointStatus: str = pydantic.constr()
DBProxyEndpointTargetRole: str = pydantic.constr()
DBProxyName: str = pydantic.constr(min=1, max=63, pattern=r'[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*')
DBProxyStatus: str = pydantic.constr()
DatabaseArn: str = pydantic.constr(min=1, max=2048, pattern=r'^arn:[A-Za-z][0-9A-Za-z-:._]*')
Description: str = pydantic.constr(min=1, max=1000, pattern=r'.*')
Double: float = pydantic.confloat()
DoubleOptional: float = pydantic.confloat()
EngineFamily: str = pydantic.constr()
ExportSourceType: str = pydantic.constr()
FailoverStatus: str = pydantic.constr()
GlobalClusterIdentifier: str = pydantic.constr(min=1, max=255, pattern=r'[A-Za-z][0-9A-Za-z-:._]*')
IAMAuthMode: str = pydantic.constr()
Integer: int = pydantic.conint()
IntegerOptional: int = pydantic.conint()
KmsKeyIdOrArn: str = pydantic.constr(min=1, max=2048, pattern=r'[a-zA-Z0-9_:\-\/]+')
Long: int = pydantic.conint()
LongOptional: int = pydantic.conint()
MaxRecords: int = pydantic.conint(min=20, max=100)
ReplicaMode: str = pydantic.constr()
SourceType: str = pydantic.constr()
String: str = pydantic.constr()
String255: str = pydantic.constr(min=1, max=255, pattern=r'.*')
SwitchoverDetailStatus: str = pydantic.constr()
SwitchoverTimeout: int = pydantic.conint(min=30)
TStamp: datetime = pydantic.condate()
TargetDBClusterParameterGroupName: str = pydantic.constr(min=1, max=255, pattern=r'[A-Za-z](?!.*--)[0-9A-Za-z-]*[^-]|^default(?!.*--)(?!.*\.\.)[0-9A-Za-z-.]*[^-]')
TargetDBParameterGroupName: str = pydantic.constr(min=1, max=255, pattern=r'[A-Za-z](?!.*--)[0-9A-Za-z-]*[^-]|^default(?!.*--)(?!.*\.\.)[0-9A-Za-z-.]*[^-]')
TargetEngineVersion: str = pydantic.constr(min=1, max=64, pattern=r'[0-9A-Za-z-_.]+')
TargetHealthReason: str = pydantic.constr()
TargetRole: str = pydantic.constr()
TargetState: str = pydantic.constr()
TargetType: str = pydantic.constr()
WriteForwardingStatus: str = pydantic.constr()

AccountQuotaList = typing.List["AccountQuota"]
ActivityStreamModeList = typing.List["String"]
AttributeValueList = typing.List["String"]
AvailabilityZoneList = typing.List["AvailabilityZone"]
AvailabilityZones = typing.List["String"]
AvailableProcessorFeatureList = typing.List["AvailableProcessorFeature"]
BlueGreenDeploymentList = typing.List["BlueGreenDeployment"]
BlueGreenDeploymentTaskList = typing.List["BlueGreenDeploymentTask"]
CACertificateIdentifiersList = typing.List["String"]
CertificateList = typing.List["Certificate"]
DBClusterBacktrackList = typing.List["DBClusterBacktrack"]
DBClusterEndpointList = typing.List["DBClusterEndpoint"]
DBClusterList = typing.List["DBCluster"]
DBClusterMemberList = typing.List["DBClusterMember"]
DBClusterOptionGroupMemberships = typing.List["DBClusterOptionGroupStatus"]
DBClusterParameterGroupList = typing.List["DBClusterParameterGroup"]
DBClusterRoles = typing.List["DBClusterRole"]
DBClusterSnapshotAttributeList = typing.List["DBClusterSnapshotAttribute"]
DBClusterSnapshotList = typing.List["DBClusterSnapshot"]
DBEngineVersionList = typing.List["DBEngineVersion"]
DBInstanceAutomatedBackupList = typing.List["DBInstanceAutomatedBackup"]
DBInstanceAutomatedBackupsReplicationList = typing.List["DBInstanceAutomatedBackupsReplication"]
DBInstanceList = typing.List["DBInstance"]
DBInstanceRoles = typing.List["DBInstanceRole"]
DBInstanceStatusInfoList = typing.List["DBInstanceStatusInfo"]
DBParameterGroupList = typing.List["DBParameterGroup"]
DBParameterGroupStatusList = typing.List["DBParameterGroupStatus"]
DBProxyEndpointList = typing.List["DBProxyEndpoint"]
DBProxyList = typing.List["DBProxy"]
DBSecurityGroupMembershipList = typing.List["DBSecurityGroupMembership"]
DBSecurityGroupNameList = typing.List["String"]
DBSecurityGroups = typing.List["DBSecurityGroup"]
DBSnapshotAttributeList = typing.List["DBSnapshotAttribute"]
DBSnapshotList = typing.List["DBSnapshot"]
DBSubnetGroups = typing.List["DBSubnetGroup"]
DescribeDBLogFilesList = typing.List["DescribeDBLogFilesDetails"]
DomainMembershipList = typing.List["DomainMembership"]
DoubleRangeList = typing.List["DoubleRange"]
EC2SecurityGroupList = typing.List["EC2SecurityGroup"]
EngineModeList = typing.List["String"]
EventCategoriesList = typing.List["String"]
EventCategoriesMapList = typing.List["EventCategoriesMap"]
EventList = typing.List["Event"]
EventSubscriptionsList = typing.List["EventSubscription"]
ExportTasksList = typing.List["ExportTask"]
FeatureNameList = typing.List["String"]
FilterList = typing.List["Filter"]
FilterValueList = typing.List["String"]
GlobalClusterList = typing.List["GlobalCluster"]
GlobalClusterMemberList = typing.List["GlobalClusterMember"]
IPRangeList = typing.List["IPRange"]
KeyList = typing.List["String"]
LogTypeList = typing.List["String"]
MinimumEngineVersionPerAllowedValueList = typing.List["MinimumEngineVersionPerAllowedValue"]
OptionConfigurationList = typing.List["OptionConfiguration"]
OptionGroupMembershipList = typing.List["OptionGroupMembership"]
OptionGroupOptionSettingsList = typing.List["OptionGroupOptionSetting"]
OptionGroupOptionVersionsList = typing.List["OptionVersion"]
OptionGroupOptionsList = typing.List["OptionGroupOption"]
OptionGroupsList = typing.List["OptionGroup"]
OptionNamesList = typing.List["String"]
OptionSettingConfigurationList = typing.List["OptionSetting"]
OptionSettingsList = typing.List["OptionSetting"]
OptionsConflictsWith = typing.List["String"]
OptionsDependedOn = typing.List["String"]
OptionsList = typing.List["Option"]
OrderableDBInstanceOptionsList = typing.List["OrderableDBInstanceOption"]
ParametersList = typing.List["Parameter"]
PendingMaintenanceActionDetails = typing.List["PendingMaintenanceAction"]
PendingMaintenanceActions = typing.List["ResourcePendingMaintenanceActions"]
ProcessorFeatureList = typing.List["ProcessorFeature"]
RangeList = typing.List["Range"]
ReadReplicaDBClusterIdentifierList = typing.List["String"]
ReadReplicaDBInstanceIdentifierList = typing.List["String"]
ReadReplicaIdentifierList = typing.List["String"]
ReadersArnList = typing.List["String"]
RecurringChargeList = typing.List["RecurringCharge"]
ReservedDBInstanceList = typing.List["ReservedDBInstance"]
ReservedDBInstancesOfferingList = typing.List["ReservedDBInstancesOffering"]
SourceIdsList = typing.List["String"]
SourceRegionList = typing.List["SourceRegion"]
StringList = typing.List["String"]
SubnetIdentifierList = typing.List["String"]
SubnetList = typing.List["Subnet"]
SupportedCharacterSetsList = typing.List["CharacterSet"]
SupportedTimezonesList = typing.List["Timezone"]
SwitchoverDetailList = typing.List["SwitchoverDetail"]
TagList = typing.List["Tag"]
TargetGroupList = typing.List["DBProxyTargetGroup"]
TargetList = typing.List["DBProxyTarget"]
UserAuthConfigInfoList = typing.List["UserAuthConfigInfo"]
UserAuthConfigList = typing.List["UserAuthConfig"]
ValidStorageOptionsList = typing.List["ValidStorageOptions"]
ValidUpgradeTargetList = typing.List["UpgradeTarget"]
VpcSecurityGroupIdList = typing.List["String"]
VpcSecurityGroupMembershipList = typing.List["VpcSecurityGroupMembership"]

class ActivityStreamMode(enum.Enum):
    SYNC = 'sync'
    ASYNC = 'async'

class ActivityStreamPolicyStatus(enum.Enum):
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'
    LOCKING_POLICY = 'locking-policy'
    UNLOCKING_POLICY = 'unlocking-policy'

class ActivityStreamStatus(enum.Enum):
    STOPPED = 'stopped'
    STARTING = 'starting'
    STARTED = 'started'
    STOPPING = 'stopping'

class ApplyMethod(enum.Enum):
    IMMEDIATE = 'immediate'
    PENDING_REBOOT = 'pending-reboot'

class AuditPolicyState(enum.Enum):
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'

class AuthScheme(enum.Enum):
    SECRETS = 'SECRETS'

class AutomationMode(enum.Enum):
    FULL = 'full'
    ALL_PAUSED = 'all-paused'

class ClientPasswordAuthType(enum.Enum):
    MYSQL_NATIVE_PASSWORD = 'MYSQL_NATIVE_PASSWORD'
    POSTGRES_SCRAM_SHA_256 = 'POSTGRES_SCRAM_SHA_256'
    POSTGRES_MD5 = 'POSTGRES_MD5'
    SQL_SERVER_AUTHENTICATION = 'SQL_SERVER_AUTHENTICATION'

class CustomEngineVersionStatus(enum.Enum):
    AVAILABLE = 'available'
    INACTIVE = 'inactive'
    INACTIVE_EXCEPT_RESTORE = 'inactive-except-restore'

class DBProxyEndpointStatus(enum.Enum):
    AVAILABLE = 'available'
    MODIFYING = 'modifying'
    INCOMPATIBLE_NETWORK = 'incompatible-network'
    INSUFFICIENT_RESOURCE_LIMITS = 'insufficient-resource-limits'
    CREATING = 'creating'
    DELETING = 'deleting'

class DBProxyEndpointTargetRole(enum.Enum):
    READ_WRITE = 'READ_WRITE'
    READ_ONLY = 'READ_ONLY'

class DBProxyStatus(enum.Enum):
    AVAILABLE = 'available'
    MODIFYING = 'modifying'
    INCOMPATIBLE_NETWORK = 'incompatible-network'
    INSUFFICIENT_RESOURCE_LIMITS = 'insufficient-resource-limits'
    CREATING = 'creating'
    DELETING = 'deleting'
    SUSPENDED = 'suspended'
    SUSPENDING = 'suspending'
    REACTIVATING = 'reactivating'

class EngineFamily(enum.Enum):
    MYSQL = 'MYSQL'
    POSTGRESQL = 'POSTGRESQL'
    SQLSERVER = 'SQLSERVER'

class ExportSourceType(enum.Enum):
    SNAPSHOT = 'SNAPSHOT'
    CLUSTER = 'CLUSTER'

class FailoverStatus(enum.Enum):
    PENDING = 'pending'
    FAILING_OVER = 'failing-over'
    CANCELLING = 'cancelling'

class IAMAuthMode(enum.Enum):
    DISABLED = 'DISABLED'
    REQUIRED = 'REQUIRED'
    ENABLED = 'ENABLED'

class ReplicaMode(enum.Enum):
    OPEN_READ_ONLY = 'open-read-only'
    MOUNTED = 'mounted'

class SourceType(enum.Enum):
    DB_INSTANCE = 'db-instance'
    DB_PARAMETER_GROUP = 'db-parameter-group'
    DB_SECURITY_GROUP = 'db-security-group'
    DB_SNAPSHOT = 'db-snapshot'
    DB_CLUSTER = 'db-cluster'
    DB_CLUSTER_SNAPSHOT = 'db-cluster-snapshot'
    CUSTOM_ENGINE_VERSION = 'custom-engine-version'
    DB_PROXY = 'db-proxy'
    BLUE_GREEN_DEPLOYMENT = 'blue-green-deployment'

class TargetHealthReason(enum.Enum):
    UNREACHABLE = 'UNREACHABLE'
    CONNECTION_FAILED = 'CONNECTION_FAILED'
    AUTH_FAILURE = 'AUTH_FAILURE'
    PENDING_PROXY_CAPACITY = 'PENDING_PROXY_CAPACITY'
    INVALID_REPLICATION_STATE = 'INVALID_REPLICATION_STATE'

class TargetRole(enum.Enum):
    READ_WRITE = 'READ_WRITE'
    READ_ONLY = 'READ_ONLY'
    UNKNOWN = 'UNKNOWN'

class TargetState(enum.Enum):
    REGISTERING = 'REGISTERING'
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'

class TargetType(enum.Enum):
    RDS_INSTANCE = 'RDS_INSTANCE'
    RDS_SERVERLESS_ENDPOINT = 'RDS_SERVERLESS_ENDPOINT'
    TRACKED_CLUSTER = 'TRACKED_CLUSTER'

class WriteForwardingStatus(enum.Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    ENABLING = 'enabling'
    DISABLING = 'disabling'
    UNKNOWN = 'unknown'

class AccountAttributesMessage(_RDSBase):
    account_quotas: AccountQuotaList = pydantic.Field(None, alias="AccountQuotas")

class AccountQuota(_RDSBase):
    account_quota_name: String = pydantic.Field(None, alias="AccountQuotaName")
    used: Long = pydantic.Field(None, alias="Used")
    max: Long = pydantic.Field(None, alias="Max")

class AddRoleToDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    feature_name: String = pydantic.Field(None, alias="FeatureName")

class AddRoleToDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    feature_name: String = pydantic.Field(None, alias="FeatureName")

class AddSourceIdentifierToSubscriptionMessage(_RDSBase):
    subscription_name: String = pydantic.Field(None, alias="SubscriptionName")
    source_identifier: String = pydantic.Field(None, alias="SourceIdentifier")

class AddSourceIdentifierToSubscriptionResult(_RDSBase):
    event_subscription: 'EventSubscription' = pydantic.Field(None, alias="EventSubscription")

class AddTagsToResourceMessage(_RDSBase):
    resource_name: String = pydantic.Field(None, alias="ResourceName")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ApplyPendingMaintenanceActionMessage(_RDSBase):
    resource_identifier: String = pydantic.Field(None, alias="ResourceIdentifier")
    apply_action: String = pydantic.Field(None, alias="ApplyAction")
    opt_in_type: String = pydantic.Field(None, alias="OptInType")

class ApplyPendingMaintenanceActionResult(_RDSBase):
    resource_pending_maintenance_actions: 'ResourcePendingMaintenanceActions' = pydantic.Field(None, alias="ResourcePendingMaintenanceActions")

class AuthorizeDBSecurityGroupIngressMessage(_RDSBase):
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")
    cidrip: String = pydantic.Field(None, alias="CIDRIP")
    ec_2_security_group_name: String = pydantic.Field(None, alias="EC2SecurityGroupName")
    ec_2_security_group_id: String = pydantic.Field(None, alias="EC2SecurityGroupId")
    ec_2_security_group_owner_id: String = pydantic.Field(None, alias="EC2SecurityGroupOwnerId")

class AuthorizeDBSecurityGroupIngressResult(_RDSBase):
    db_security_group: 'DBSecurityGroup' = pydantic.Field(None, alias="DBSecurityGroup")

class AvailabilityZone(_RDSBase):
    name: String = pydantic.Field(None, alias="Name")

class AvailableProcessorFeature(_RDSBase):
    name: String = pydantic.Field(None, alias="Name")
    default_value: String = pydantic.Field(None, alias="DefaultValue")
    allowed_values: String = pydantic.Field(None, alias="AllowedValues")

class BacktrackDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    backtrack_to: 'TStamp' = pydantic.Field(None, alias="BacktrackTo")
    force: BooleanOptional = pydantic.Field(None, alias="Force")
    use_earliest_time_on_point_in_time_unavailable: BooleanOptional = pydantic.Field(None, alias="UseEarliestTimeOnPointInTimeUnavailable")

class BlueGreenDeployment(_RDSBase):
    blue_green_deployment_identifier: BlueGreenDeploymentIdentifier = pydantic.Field(None, alias="BlueGreenDeploymentIdentifier")
    blue_green_deployment_name: BlueGreenDeploymentName = pydantic.Field(None, alias="BlueGreenDeploymentName")
    source: DatabaseArn = pydantic.Field(None, alias="Source")
    target: DatabaseArn = pydantic.Field(None, alias="Target")
    switchover_details: SwitchoverDetailList = pydantic.Field(None, alias="SwitchoverDetails")
    tasks: BlueGreenDeploymentTaskList = pydantic.Field(None, alias="Tasks")
    status: BlueGreenDeploymentStatus = pydantic.Field(None, alias="Status")
    status_details: BlueGreenDeploymentStatusDetails = pydantic.Field(None, alias="StatusDetails")
    create_time: 'TStamp' = pydantic.Field(None, alias="CreateTime")
    delete_time: 'TStamp' = pydantic.Field(None, alias="DeleteTime")
    tag_list: TagList = pydantic.Field(None, alias="TagList")

class BlueGreenDeploymentTask(_RDSBase):
    name: BlueGreenDeploymentTaskName = pydantic.Field(None, alias="Name")
    status: BlueGreenDeploymentTaskStatus = pydantic.Field(None, alias="Status")

class CancelExportTaskMessage(_RDSBase):
    export_task_identifier: String = pydantic.Field(None, alias="ExportTaskIdentifier")

class Certificate(_RDSBase):
    certificate_identifier: String = pydantic.Field(None, alias="CertificateIdentifier")
    certificate_type: String = pydantic.Field(None, alias="CertificateType")
    thumbprint: String = pydantic.Field(None, alias="Thumbprint")
    valid_from: 'TStamp' = pydantic.Field(None, alias="ValidFrom")
    valid_till: 'TStamp' = pydantic.Field(None, alias="ValidTill")
    certificate_arn: String = pydantic.Field(None, alias="CertificateArn")
    customer_override: BooleanOptional = pydantic.Field(None, alias="CustomerOverride")
    customer_override_valid_till: 'TStamp' = pydantic.Field(None, alias="CustomerOverrideValidTill")

class CertificateDetails(_RDSBase):
    ca_identifier: String = pydantic.Field(None, alias="CAIdentifier")
    valid_till: 'TStamp' = pydantic.Field(None, alias="ValidTill")

class CertificateMessage(_RDSBase):
    certificates: CertificateList = pydantic.Field(None, alias="Certificates")
    marker: String = pydantic.Field(None, alias="Marker")

class CharacterSet(_RDSBase):
    character_set_name: String = pydantic.Field(None, alias="CharacterSetName")
    character_set_description: String = pydantic.Field(None, alias="CharacterSetDescription")

class CloudwatchLogsExportConfiguration(_RDSBase):
    enable_log_types: LogTypeList = pydantic.Field(None, alias="EnableLogTypes")
    disable_log_types: LogTypeList = pydantic.Field(None, alias="DisableLogTypes")

class ClusterPendingModifiedValues(_RDSBase):
    pending_cloudwatch_logs_exports: 'PendingCloudwatchLogsExports' = pydantic.Field(None, alias="PendingCloudwatchLogsExports")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    iam_database_authentication_enabled: BooleanOptional = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    storage_type: String = pydantic.Field(None, alias="StorageType")

class ConnectionPoolConfiguration(_RDSBase):
    max_connections_percent: IntegerOptional = pydantic.Field(None, alias="MaxConnectionsPercent")
    max_idle_connections_percent: IntegerOptional = pydantic.Field(None, alias="MaxIdleConnectionsPercent")
    connection_borrow_timeout: IntegerOptional = pydantic.Field(None, alias="ConnectionBorrowTimeout")
    session_pinning_filters: StringList = pydantic.Field(None, alias="SessionPinningFilters")
    init_query: String = pydantic.Field(None, alias="InitQuery")

class ConnectionPoolConfigurationInfo(_RDSBase):
    max_connections_percent: Integer = pydantic.Field(None, alias="MaxConnectionsPercent")
    max_idle_connections_percent: Integer = pydantic.Field(None, alias="MaxIdleConnectionsPercent")
    connection_borrow_timeout: Integer = pydantic.Field(None, alias="ConnectionBorrowTimeout")
    session_pinning_filters: StringList = pydantic.Field(None, alias="SessionPinningFilters")
    init_query: String = pydantic.Field(None, alias="InitQuery")

class CopyDBClusterParameterGroupMessage(_RDSBase):
    source_db_cluster_parameter_group_identifier: String = pydantic.Field(None, alias="SourceDBClusterParameterGroupIdentifier")
    target_db_cluster_parameter_group_identifier: String = pydantic.Field(None, alias="TargetDBClusterParameterGroupIdentifier")
    target_db_cluster_parameter_group_description: String = pydantic.Field(None, alias="TargetDBClusterParameterGroupDescription")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CopyDBClusterParameterGroupResult(_RDSBase):
    db_cluster_parameter_group: 'DBClusterParameterGroup' = pydantic.Field(None, alias="DBClusterParameterGroup")

class CopyDBClusterSnapshotMessage(_RDSBase):
    source_db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="SourceDBClusterSnapshotIdentifier")
    target_db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="TargetDBClusterSnapshotIdentifier")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    pre_signed_url: String = pydantic.Field(None, alias="PreSignedUrl")
    copy_tags: BooleanOptional = pydantic.Field(None, alias="CopyTags")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CopyDBClusterSnapshotResult(_RDSBase):
    db_cluster_snapshot: 'DBClusterSnapshot' = pydantic.Field(None, alias="DBClusterSnapshot")

class CopyDBParameterGroupMessage(_RDSBase):
    source_db_parameter_group_identifier: String = pydantic.Field(None, alias="SourceDBParameterGroupIdentifier")
    target_db_parameter_group_identifier: String = pydantic.Field(None, alias="TargetDBParameterGroupIdentifier")
    target_db_parameter_group_description: String = pydantic.Field(None, alias="TargetDBParameterGroupDescription")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CopyDBParameterGroupResult(_RDSBase):
    db_parameter_group: 'DBParameterGroup' = pydantic.Field(None, alias="DBParameterGroup")

class CopyDBSnapshotMessage(_RDSBase):
    source_db_snapshot_identifier: String = pydantic.Field(None, alias="SourceDBSnapshotIdentifier")
    target_db_snapshot_identifier: String = pydantic.Field(None, alias="TargetDBSnapshotIdentifier")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    copy_tags: BooleanOptional = pydantic.Field(None, alias="CopyTags")
    pre_signed_url: String = pydantic.Field(None, alias="PreSignedUrl")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    target_custom_availability_zone: String = pydantic.Field(None, alias="TargetCustomAvailabilityZone")
    copy_option_group: BooleanOptional = pydantic.Field(None, alias="CopyOptionGroup")

class CopyDBSnapshotResult(_RDSBase):
    db_snapshot: 'DBSnapshot' = pydantic.Field(None, alias="DBSnapshot")

class CopyOptionGroupMessage(_RDSBase):
    source_option_group_identifier: String = pydantic.Field(None, alias="SourceOptionGroupIdentifier")
    target_option_group_identifier: String = pydantic.Field(None, alias="TargetOptionGroupIdentifier")
    target_option_group_description: String = pydantic.Field(None, alias="TargetOptionGroupDescription")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CopyOptionGroupResult(_RDSBase):
    option_group: 'OptionGroup' = pydantic.Field(None, alias="OptionGroup")

class CreateBlueGreenDeploymentRequest(_RDSBase):
    blue_green_deployment_name: BlueGreenDeploymentName = pydantic.Field(None, alias="BlueGreenDeploymentName")
    source: DatabaseArn = pydantic.Field(None, alias="Source")
    target_engine_version: TargetEngineVersion = pydantic.Field(None, alias="TargetEngineVersion")
    target_db_parameter_group_name: TargetDBParameterGroupName = pydantic.Field(None, alias="TargetDBParameterGroupName")
    target_db_cluster_parameter_group_name: TargetDBClusterParameterGroupName = pydantic.Field(None, alias="TargetDBClusterParameterGroupName")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateBlueGreenDeploymentResponse(_RDSBase):
    blue_green_deployment: 'BlueGreenDeployment' = pydantic.Field(None, alias="BlueGreenDeployment")

class CreateCustomDBEngineVersionMessage(_RDSBase):
    engine: CustomEngineName = pydantic.Field(None, alias="Engine")
    engine_version: CustomEngineVersion = pydantic.Field(None, alias="EngineVersion")
    database_installation_files_s_3_bucket_name: BucketName = pydantic.Field(None, alias="DatabaseInstallationFilesS3BucketName")
    database_installation_files_s_3_prefix: String255 = pydantic.Field(None, alias="DatabaseInstallationFilesS3Prefix")
    image_id: String255 = pydantic.Field(None, alias="ImageId")
    kms_key_id: KmsKeyIdOrArn = pydantic.Field(None, alias="KMSKeyId")
    description: Description = pydantic.Field(None, alias="Description")
    manifest: CustomDBEngineVersionManifest = pydantic.Field(None, alias="Manifest")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBClusterEndpointMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_endpoint_identifier: String = pydantic.Field(None, alias="DBClusterEndpointIdentifier")
    endpoint_type: String = pydantic.Field(None, alias="EndpointType")
    static_members: StringList = pydantic.Field(None, alias="StaticMembers")
    excluded_members: StringList = pydantic.Field(None, alias="ExcludedMembers")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBClusterMessage(_RDSBase):
    availability_zones: AvailabilityZones = pydantic.Field(None, alias="AvailabilityZones")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    character_set_name: String = pydantic.Field(None, alias="CharacterSetName")
    database_name: String = pydantic.Field(None, alias="DatabaseName")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    replication_source_identifier: String = pydantic.Field(None, alias="ReplicationSourceIdentifier")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_encrypted: BooleanOptional = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    pre_signed_url: String = pydantic.Field(None, alias="PreSignedUrl")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    backtrack_window: LongOptional = pydantic.Field(None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    engine_mode: String = pydantic.Field(None, alias="EngineMode")
    scaling_configuration: 'ScalingConfiguration' = pydantic.Field(None, alias="ScalingConfiguration")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")
    enable_http_endpoint: BooleanOptional = pydantic.Field(None, alias="EnableHttpEndpoint")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    enable_global_write_forwarding: BooleanOptional = pydantic.Field(None, alias="EnableGlobalWriteForwarding")
    db_cluster_instance_class: String = pydantic.Field(None, alias="DBClusterInstanceClass")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    enable_performance_insights: BooleanOptional = pydantic.Field(None, alias="EnablePerformanceInsights")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    serverless_v_2_scaling_configuration: 'ServerlessV2ScalingConfiguration' = pydantic.Field(None, alias="ServerlessV2ScalingConfiguration")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    db_system_id: String = pydantic.Field(None, alias="DBSystemId")
    manage_master_user_password: BooleanOptional = pydantic.Field(None, alias="ManageMasterUserPassword")
    master_user_secret_kms_key_id: String = pydantic.Field(None, alias="MasterUserSecretKmsKeyId")

class CreateDBClusterParameterGroupMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBClusterParameterGroupResult(_RDSBase):
    db_cluster_parameter_group: 'DBClusterParameterGroup' = pydantic.Field(None, alias="DBClusterParameterGroup")

class CreateDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class CreateDBClusterSnapshotMessage(_RDSBase):
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBClusterSnapshotResult(_RDSBase):
    db_cluster_snapshot: 'DBClusterSnapshot' = pydantic.Field(None, alias="DBClusterSnapshot")

class CreateDBInstanceMessage(_RDSBase):
    db_name: String = pydantic.Field(None, alias="DBName")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    engine: String = pydantic.Field(None, alias="Engine")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    db_security_groups: DBSecurityGroupNameList = pydantic.Field(None, alias="DBSecurityGroups")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    character_set_name: String = pydantic.Field(None, alias="CharacterSetName")
    nchar_character_set_name: String = pydantic.Field(None, alias="NcharCharacterSetName")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    tags: TagList = pydantic.Field(None, alias="Tags")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    tde_credential_password: String = pydantic.Field(None, alias="TdeCredentialPassword")
    storage_encrypted: BooleanOptional = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    domain: String = pydantic.Field(None, alias="Domain")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    promotion_tier: IntegerOptional = pydantic.Field(None, alias="PromotionTier")
    timezone: String = pydantic.Field(None, alias="Timezone")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    enable_performance_insights: BooleanOptional = pydantic.Field(None, alias="EnablePerformanceInsights")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    max_allocated_storage: IntegerOptional = pydantic.Field(None, alias="MaxAllocatedStorage")
    enable_customer_owned_ip: BooleanOptional = pydantic.Field(None, alias="EnableCustomerOwnedIp")
    custom_iam_instance_profile: String = pydantic.Field(None, alias="CustomIamInstanceProfile")
    backup_target: String = pydantic.Field(None, alias="BackupTarget")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    manage_master_user_password: BooleanOptional = pydantic.Field(None, alias="ManageMasterUserPassword")
    master_user_secret_kms_key_id: String = pydantic.Field(None, alias="MasterUserSecretKmsKeyId")
    ca_certificate_identifier: String = pydantic.Field(None, alias="CACertificateIdentifier")

class CreateDBInstanceReadReplicaMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    source_db_instance_identifier: String = pydantic.Field(None, alias="SourceDBInstanceIdentifier")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    tags: TagList = pydantic.Field(None, alias="Tags")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    pre_signed_url: String = pydantic.Field(None, alias="PreSignedUrl")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    enable_performance_insights: BooleanOptional = pydantic.Field(None, alias="EnablePerformanceInsights")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    use_default_processor_features: BooleanOptional = pydantic.Field(None, alias="UseDefaultProcessorFeatures")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    replica_mode: ReplicaMode = pydantic.Field(None, alias="ReplicaMode")
    max_allocated_storage: IntegerOptional = pydantic.Field(None, alias="MaxAllocatedStorage")
    custom_iam_instance_profile: String = pydantic.Field(None, alias="CustomIamInstanceProfile")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    enable_customer_owned_ip: BooleanOptional = pydantic.Field(None, alias="EnableCustomerOwnedIp")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    source_db_cluster_identifier: String = pydantic.Field(None, alias="SourceDBClusterIdentifier")

class CreateDBInstanceReadReplicaResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class CreateDBInstanceResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class CreateDBParameterGroupMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBParameterGroupResult(_RDSBase):
    db_parameter_group: 'DBParameterGroup' = pydantic.Field(None, alias="DBParameterGroup")

class CreateDBProxyEndpointRequest(_RDSBase):
    db_proxy_name: DBProxyName = pydantic.Field(None, alias="DBProxyName")
    db_proxy_endpoint_name: DBProxyEndpointName = pydantic.Field(None, alias="DBProxyEndpointName")
    vpc_subnet_ids: StringList = pydantic.Field(None, alias="VpcSubnetIds")
    vpc_security_group_ids: StringList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    target_role: DBProxyEndpointTargetRole = pydantic.Field(None, alias="TargetRole")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBProxyEndpointResponse(_RDSBase):
    db_proxy_endpoint: 'DBProxyEndpoint' = pydantic.Field(None, alias="DBProxyEndpoint")

class CreateDBProxyRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    engine_family: EngineFamily = pydantic.Field(None, alias="EngineFamily")
    auth: UserAuthConfigList = pydantic.Field(None, alias="Auth")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    vpc_subnet_ids: StringList = pydantic.Field(None, alias="VpcSubnetIds")
    vpc_security_group_ids: StringList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    require_tls: Boolean = pydantic.Field(None, alias="RequireTLS")
    idle_client_timeout: IntegerOptional = pydantic.Field(None, alias="IdleClientTimeout")
    debug_logging: Boolean = pydantic.Field(None, alias="DebugLogging")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBProxyResponse(_RDSBase):
    db_proxy: 'DBProxy' = pydantic.Field(None, alias="DBProxy")

class CreateDBSecurityGroupMessage(_RDSBase):
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")
    db_security_group_description: String = pydantic.Field(None, alias="DBSecurityGroupDescription")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBSecurityGroupResult(_RDSBase):
    db_security_group: 'DBSecurityGroup' = pydantic.Field(None, alias="DBSecurityGroup")

class CreateDBSnapshotMessage(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBSnapshotResult(_RDSBase):
    db_snapshot: 'DBSnapshot' = pydantic.Field(None, alias="DBSnapshot")

class CreateDBSubnetGroupMessage(_RDSBase):
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    db_subnet_group_description: String = pydantic.Field(None, alias="DBSubnetGroupDescription")
    subnet_ids: SubnetIdentifierList = pydantic.Field(None, alias="SubnetIds")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateDBSubnetGroupResult(_RDSBase):
    db_subnet_group: 'DBSubnetGroup' = pydantic.Field(None, alias="DBSubnetGroup")

class CreateEventSubscriptionMessage(_RDSBase):
    subscription_name: String = pydantic.Field(None, alias="SubscriptionName")
    sns_topic_arn: String = pydantic.Field(None, alias="SnsTopicArn")
    source_type: String = pydantic.Field(None, alias="SourceType")
    event_categories: EventCategoriesList = pydantic.Field(None, alias="EventCategories")
    source_ids: SourceIdsList = pydantic.Field(None, alias="SourceIds")
    enabled: BooleanOptional = pydantic.Field(None, alias="Enabled")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateEventSubscriptionResult(_RDSBase):
    event_subscription: 'EventSubscription' = pydantic.Field(None, alias="EventSubscription")

class CreateGlobalClusterMessage(_RDSBase):
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")
    source_db_cluster_identifier: String = pydantic.Field(None, alias="SourceDBClusterIdentifier")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    database_name: String = pydantic.Field(None, alias="DatabaseName")
    storage_encrypted: BooleanOptional = pydantic.Field(None, alias="StorageEncrypted")

class CreateGlobalClusterResult(_RDSBase):
    global_cluster: 'GlobalCluster' = pydantic.Field(None, alias="GlobalCluster")

class CreateOptionGroupMessage(_RDSBase):
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    engine_name: String = pydantic.Field(None, alias="EngineName")
    major_engine_version: String = pydantic.Field(None, alias="MajorEngineVersion")
    option_group_description: String = pydantic.Field(None, alias="OptionGroupDescription")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateOptionGroupResult(_RDSBase):
    option_group: 'OptionGroup' = pydantic.Field(None, alias="OptionGroup")

class CustomDBEngineVersionAMI(_RDSBase):
    image_id: String = pydantic.Field(None, alias="ImageId")
    status: String = pydantic.Field(None, alias="Status")

class DBCluster(_RDSBase):
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    availability_zones: AvailabilityZones = pydantic.Field(None, alias="AvailabilityZones")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    character_set_name: String = pydantic.Field(None, alias="CharacterSetName")
    database_name: String = pydantic.Field(None, alias="DatabaseName")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_parameter_group: String = pydantic.Field(None, alias="DBClusterParameterGroup")
    db_subnet_group: String = pydantic.Field(None, alias="DBSubnetGroup")
    status: String = pydantic.Field(None, alias="Status")
    automatic_restart_time: 'TStamp' = pydantic.Field(None, alias="AutomaticRestartTime")
    percent_progress: String = pydantic.Field(None, alias="PercentProgress")
    earliest_restorable_time: 'TStamp' = pydantic.Field(None, alias="EarliestRestorableTime")
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    reader_endpoint: String = pydantic.Field(None, alias="ReaderEndpoint")
    custom_endpoints: StringList = pydantic.Field(None, alias="CustomEndpoints")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    latest_restorable_time: 'TStamp' = pydantic.Field(None, alias="LatestRestorableTime")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    db_cluster_option_group_memberships: DBClusterOptionGroupMemberships = pydantic.Field(None, alias="DBClusterOptionGroupMemberships")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    replication_source_identifier: String = pydantic.Field(None, alias="ReplicationSourceIdentifier")
    read_replica_identifiers: ReadReplicaIdentifierList = pydantic.Field(None, alias="ReadReplicaIdentifiers")
    db_cluster_members: DBClusterMemberList = pydantic.Field(None, alias="DBClusterMembers")
    vpc_security_groups: VpcSecurityGroupMembershipList = pydantic.Field(None, alias="VpcSecurityGroups")
    hosted_zone_id: String = pydantic.Field(None, alias="HostedZoneId")
    storage_encrypted: Boolean = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    db_cluster_resource_id: String = pydantic.Field(None, alias="DbClusterResourceId")
    db_cluster_arn: String = pydantic.Field(None, alias="DBClusterArn")
    associated_roles: DBClusterRoles = pydantic.Field(None, alias="AssociatedRoles")
    iam_database_authentication_enabled: BooleanOptional = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    clone_group_id: String = pydantic.Field(None, alias="CloneGroupId")
    cluster_create_time: 'TStamp' = pydantic.Field(None, alias="ClusterCreateTime")
    earliest_backtrack_time: 'TStamp' = pydantic.Field(None, alias="EarliestBacktrackTime")
    backtrack_window: LongOptional = pydantic.Field(None, alias="BacktrackWindow")
    backtrack_consumed_change_records: LongOptional = pydantic.Field(None, alias="BacktrackConsumedChangeRecords")
    enabled_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnabledCloudwatchLogsExports")
    capacity: IntegerOptional = pydantic.Field(None, alias="Capacity")
    engine_mode: String = pydantic.Field(None, alias="EngineMode")
    scaling_configuration_info: 'ScalingConfigurationInfo' = pydantic.Field(None, alias="ScalingConfigurationInfo")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    http_endpoint_enabled: BooleanOptional = pydantic.Field(None, alias="HttpEndpointEnabled")
    activity_stream_mode: ActivityStreamMode = pydantic.Field(None, alias="ActivityStreamMode")
    activity_stream_status: ActivityStreamStatus = pydantic.Field(None, alias="ActivityStreamStatus")
    activity_stream_kms_key_id: String = pydantic.Field(None, alias="ActivityStreamKmsKeyId")
    activity_stream_kinesis_stream_name: String = pydantic.Field(None, alias="ActivityStreamKinesisStreamName")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    cross_account_clone: BooleanOptional = pydantic.Field(None, alias="CrossAccountClone")
    domain_memberships: DomainMembershipList = pydantic.Field(None, alias="DomainMemberships")
    tag_list: TagList = pydantic.Field(None, alias="TagList")
    global_write_forwarding_status: WriteForwardingStatus = pydantic.Field(None, alias="GlobalWriteForwardingStatus")
    global_write_forwarding_requested: BooleanOptional = pydantic.Field(None, alias="GlobalWriteForwardingRequested")
    pending_modified_values: 'ClusterPendingModifiedValues' = pydantic.Field(None, alias="PendingModifiedValues")
    db_cluster_instance_class: String = pydantic.Field(None, alias="DBClusterInstanceClass")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    auto_minor_version_upgrade: Boolean = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    performance_insights_enabled: BooleanOptional = pydantic.Field(None, alias="PerformanceInsightsEnabled")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    serverless_v_2_scaling_configuration: 'ServerlessV2ScalingConfigurationInfo' = pydantic.Field(None, alias="ServerlessV2ScalingConfiguration")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    db_system_id: String = pydantic.Field(None, alias="DBSystemId")
    master_user_secret: 'MasterUserSecret' = pydantic.Field(None, alias="MasterUserSecret")
    io_optimized_next_allowed_modification_time: 'TStamp' = pydantic.Field(None, alias="IOOptimizedNextAllowedModificationTime")

class DBClusterBacktrack(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    backtrack_identifier: String = pydantic.Field(None, alias="BacktrackIdentifier")
    backtrack_to: 'TStamp' = pydantic.Field(None, alias="BacktrackTo")
    backtracked_from: 'TStamp' = pydantic.Field(None, alias="BacktrackedFrom")
    backtrack_request_creation_time: 'TStamp' = pydantic.Field(None, alias="BacktrackRequestCreationTime")
    status: String = pydantic.Field(None, alias="Status")

class DBClusterBacktrackMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_cluster_backtracks: DBClusterBacktrackList = pydantic.Field(None, alias="DBClusterBacktracks")

class DBClusterCapacityInfo(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    pending_capacity: IntegerOptional = pydantic.Field(None, alias="PendingCapacity")
    current_capacity: IntegerOptional = pydantic.Field(None, alias="CurrentCapacity")
    seconds_before_timeout: IntegerOptional = pydantic.Field(None, alias="SecondsBeforeTimeout")
    timeout_action: String = pydantic.Field(None, alias="TimeoutAction")

class DBClusterEndpoint(_RDSBase):
    db_cluster_endpoint_identifier: String = pydantic.Field(None, alias="DBClusterEndpointIdentifier")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_endpoint_resource_identifier: String = pydantic.Field(None, alias="DBClusterEndpointResourceIdentifier")
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    status: String = pydantic.Field(None, alias="Status")
    endpoint_type: String = pydantic.Field(None, alias="EndpointType")
    custom_endpoint_type: String = pydantic.Field(None, alias="CustomEndpointType")
    static_members: StringList = pydantic.Field(None, alias="StaticMembers")
    excluded_members: StringList = pydantic.Field(None, alias="ExcludedMembers")
    db_cluster_endpoint_arn: String = pydantic.Field(None, alias="DBClusterEndpointArn")

class DBClusterEndpointMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_cluster_endpoints: DBClusterEndpointList = pydantic.Field(None, alias="DBClusterEndpoints")

class DBClusterMember(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    is_cluster_writer: Boolean = pydantic.Field(None, alias="IsClusterWriter")
    db_cluster_parameter_group_status: String = pydantic.Field(None, alias="DBClusterParameterGroupStatus")
    promotion_tier: IntegerOptional = pydantic.Field(None, alias="PromotionTier")

class DBClusterMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_clusters: DBClusterList = pydantic.Field(None, alias="DBClusters")

class DBClusterOptionGroupStatus(_RDSBase):
    db_cluster_option_group_name: String = pydantic.Field(None, alias="DBClusterOptionGroupName")
    status: String = pydantic.Field(None, alias="Status")

class DBClusterParameterGroup(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    description: String = pydantic.Field(None, alias="Description")
    db_cluster_parameter_group_arn: String = pydantic.Field(None, alias="DBClusterParameterGroupArn")

class DBClusterParameterGroupDetails(_RDSBase):
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")
    marker: String = pydantic.Field(None, alias="Marker")

class DBClusterParameterGroupNameMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")

class DBClusterParameterGroupsMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_cluster_parameter_groups: DBClusterParameterGroupList = pydantic.Field(None, alias="DBClusterParameterGroups")

class DBClusterRole(_RDSBase):
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    status: String = pydantic.Field(None, alias="Status")
    feature_name: String = pydantic.Field(None, alias="FeatureName")

class DBClusterSnapshot(_RDSBase):
    availability_zones: AvailabilityZones = pydantic.Field(None, alias="AvailabilityZones")
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    snapshot_create_time: 'TStamp' = pydantic.Field(None, alias="SnapshotCreateTime")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_mode: String = pydantic.Field(None, alias="EngineMode")
    allocated_storage: Integer = pydantic.Field(None, alias="AllocatedStorage")
    status: String = pydantic.Field(None, alias="Status")
    port: Integer = pydantic.Field(None, alias="Port")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    cluster_create_time: 'TStamp' = pydantic.Field(None, alias="ClusterCreateTime")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    snapshot_type: String = pydantic.Field(None, alias="SnapshotType")
    percent_progress: Integer = pydantic.Field(None, alias="PercentProgress")
    storage_encrypted: Boolean = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    db_cluster_snapshot_arn: String = pydantic.Field(None, alias="DBClusterSnapshotArn")
    source_db_cluster_snapshot_arn: String = pydantic.Field(None, alias="SourceDBClusterSnapshotArn")
    iam_database_authentication_enabled: Boolean = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    tag_list: TagList = pydantic.Field(None, alias="TagList")
    db_system_id: String = pydantic.Field(None, alias="DBSystemId")
    storage_type: String = pydantic.Field(None, alias="StorageType")

class DBClusterSnapshotAttribute(_RDSBase):
    attribute_name: String = pydantic.Field(None, alias="AttributeName")
    attribute_values: AttributeValueList = pydantic.Field(None, alias="AttributeValues")

class DBClusterSnapshotAttributesResult(_RDSBase):
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")
    db_cluster_snapshot_attributes: DBClusterSnapshotAttributeList = pydantic.Field(None, alias="DBClusterSnapshotAttributes")

class DBClusterSnapshotMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_cluster_snapshots: DBClusterSnapshotList = pydantic.Field(None, alias="DBClusterSnapshots")

class DBEngineVersion(_RDSBase):
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    db_engine_description: String = pydantic.Field(None, alias="DBEngineDescription")
    db_engine_version_description: String = pydantic.Field(None, alias="DBEngineVersionDescription")
    default_character_set: 'CharacterSet' = pydantic.Field(None, alias="DefaultCharacterSet")
    image: 'CustomDBEngineVersionAMI' = pydantic.Field(None, alias="Image")
    db_engine_media_type: String = pydantic.Field(None, alias="DBEngineMediaType")
    supported_character_sets: SupportedCharacterSetsList = pydantic.Field(None, alias="SupportedCharacterSets")
    supported_nchar_character_sets: SupportedCharacterSetsList = pydantic.Field(None, alias="SupportedNcharCharacterSets")
    valid_upgrade_target: ValidUpgradeTargetList = pydantic.Field(None, alias="ValidUpgradeTarget")
    supported_timezones: SupportedTimezonesList = pydantic.Field(None, alias="SupportedTimezones")
    exportable_log_types: LogTypeList = pydantic.Field(None, alias="ExportableLogTypes")
    supports_log_exports_to_cloudwatch_logs: Boolean = pydantic.Field(None, alias="SupportsLogExportsToCloudwatchLogs")
    supports_read_replica: Boolean = pydantic.Field(None, alias="SupportsReadReplica")
    supported_engine_modes: EngineModeList = pydantic.Field(None, alias="SupportedEngineModes")
    supported_feature_names: FeatureNameList = pydantic.Field(None, alias="SupportedFeatureNames")
    status: String = pydantic.Field(None, alias="Status")
    supports_parallel_query: Boolean = pydantic.Field(None, alias="SupportsParallelQuery")
    supports_global_databases: Boolean = pydantic.Field(None, alias="SupportsGlobalDatabases")
    major_engine_version: String = pydantic.Field(None, alias="MajorEngineVersion")
    database_installation_files_s_3_bucket_name: String = pydantic.Field(None, alias="DatabaseInstallationFilesS3BucketName")
    database_installation_files_s_3_prefix: String = pydantic.Field(None, alias="DatabaseInstallationFilesS3Prefix")
    db_engine_version_arn: String = pydantic.Field(None, alias="DBEngineVersionArn")
    kms_key_id: String = pydantic.Field(None, alias="KMSKeyId")
    create_time: 'TStamp' = pydantic.Field(None, alias="CreateTime")
    tag_list: TagList = pydantic.Field(None, alias="TagList")
    supports_babelfish: Boolean = pydantic.Field(None, alias="SupportsBabelfish")
    custom_db_engine_version_manifest: CustomDBEngineVersionManifest = pydantic.Field(None, alias="CustomDBEngineVersionManifest")
    supports_certificate_rotation_without_restart: BooleanOptional = pydantic.Field(None, alias="SupportsCertificateRotationWithoutRestart")
    supported_ca_certificate_identifiers: CACertificateIdentifiersList = pydantic.Field(None, alias="SupportedCACertificateIdentifiers")

class DBEngineVersionMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_engine_versions: DBEngineVersionList = pydantic.Field(None, alias="DBEngineVersions")

class DBInstance(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    engine: String = pydantic.Field(None, alias="Engine")
    db_instance_status: String = pydantic.Field(None, alias="DBInstanceStatus")
    automatic_restart_time: 'TStamp' = pydantic.Field(None, alias="AutomaticRestartTime")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    db_name: String = pydantic.Field(None, alias="DBName")
    endpoint: 'Endpoint' = pydantic.Field(None, alias="Endpoint")
    allocated_storage: Integer = pydantic.Field(None, alias="AllocatedStorage")
    instance_create_time: 'TStamp' = pydantic.Field(None, alias="InstanceCreateTime")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    backup_retention_period: Integer = pydantic.Field(None, alias="BackupRetentionPeriod")
    db_security_groups: DBSecurityGroupMembershipList = pydantic.Field(None, alias="DBSecurityGroups")
    vpc_security_groups: VpcSecurityGroupMembershipList = pydantic.Field(None, alias="VpcSecurityGroups")
    db_parameter_groups: DBParameterGroupStatusList = pydantic.Field(None, alias="DBParameterGroups")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    db_subnet_group: 'DBSubnetGroup' = pydantic.Field(None, alias="DBSubnetGroup")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    pending_modified_values: 'PendingModifiedValues' = pydantic.Field(None, alias="PendingModifiedValues")
    latest_restorable_time: 'TStamp' = pydantic.Field(None, alias="LatestRestorableTime")
    multi_az: Boolean = pydantic.Field(None, alias="MultiAZ")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    auto_minor_version_upgrade: Boolean = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    read_replica_source_db_instance_identifier: String = pydantic.Field(None, alias="ReadReplicaSourceDBInstanceIdentifier")
    read_replica_db_instance_identifiers: ReadReplicaDBInstanceIdentifierList = pydantic.Field(None, alias="ReadReplicaDBInstanceIdentifiers")
    read_replica_db_cluster_identifiers: ReadReplicaDBClusterIdentifierList = pydantic.Field(None, alias="ReadReplicaDBClusterIdentifiers")
    replica_mode: ReplicaMode = pydantic.Field(None, alias="ReplicaMode")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_memberships: OptionGroupMembershipList = pydantic.Field(None, alias="OptionGroupMemberships")
    character_set_name: String = pydantic.Field(None, alias="CharacterSetName")
    nchar_character_set_name: String = pydantic.Field(None, alias="NcharCharacterSetName")
    secondary_availability_zone: String = pydantic.Field(None, alias="SecondaryAvailabilityZone")
    publicly_accessible: Boolean = pydantic.Field(None, alias="PubliclyAccessible")
    status_infos: DBInstanceStatusInfoList = pydantic.Field(None, alias="StatusInfos")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    db_instance_port: Integer = pydantic.Field(None, alias="DbInstancePort")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    storage_encrypted: Boolean = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    dbi_resource_id: String = pydantic.Field(None, alias="DbiResourceId")
    ca_certificate_identifier: String = pydantic.Field(None, alias="CACertificateIdentifier")
    domain_memberships: DomainMembershipList = pydantic.Field(None, alias="DomainMemberships")
    copy_tags_to_snapshot: Boolean = pydantic.Field(None, alias="CopyTagsToSnapshot")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    enhanced_monitoring_resource_arn: String = pydantic.Field(None, alias="EnhancedMonitoringResourceArn")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    promotion_tier: IntegerOptional = pydantic.Field(None, alias="PromotionTier")
    db_instance_arn: String = pydantic.Field(None, alias="DBInstanceArn")
    timezone: String = pydantic.Field(None, alias="Timezone")
    iam_database_authentication_enabled: Boolean = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    performance_insights_enabled: BooleanOptional = pydantic.Field(None, alias="PerformanceInsightsEnabled")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    enabled_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnabledCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    deletion_protection: Boolean = pydantic.Field(None, alias="DeletionProtection")
    associated_roles: DBInstanceRoles = pydantic.Field(None, alias="AssociatedRoles")
    listener_endpoint: 'Endpoint' = pydantic.Field(None, alias="ListenerEndpoint")
    max_allocated_storage: IntegerOptional = pydantic.Field(None, alias="MaxAllocatedStorage")
    tag_list: TagList = pydantic.Field(None, alias="TagList")
    db_instance_automated_backups_replications: DBInstanceAutomatedBackupsReplicationList = pydantic.Field(None, alias="DBInstanceAutomatedBackupsReplications")
    customer_owned_ip_enabled: BooleanOptional = pydantic.Field(None, alias="CustomerOwnedIpEnabled")
    aws_backup_recovery_point_arn: String = pydantic.Field(None, alias="AwsBackupRecoveryPointArn")
    activity_stream_status: ActivityStreamStatus = pydantic.Field(None, alias="ActivityStreamStatus")
    activity_stream_kms_key_id: String = pydantic.Field(None, alias="ActivityStreamKmsKeyId")
    activity_stream_kinesis_stream_name: String = pydantic.Field(None, alias="ActivityStreamKinesisStreamName")
    activity_stream_mode: ActivityStreamMode = pydantic.Field(None, alias="ActivityStreamMode")
    activity_stream_engine_native_audit_fields_included: BooleanOptional = pydantic.Field(None, alias="ActivityStreamEngineNativeAuditFieldsIncluded")
    automation_mode: AutomationMode = pydantic.Field(None, alias="AutomationMode")
    resume_full_automation_mode_time: 'TStamp' = pydantic.Field(None, alias="ResumeFullAutomationModeTime")
    custom_iam_instance_profile: String = pydantic.Field(None, alias="CustomIamInstanceProfile")
    backup_target: String = pydantic.Field(None, alias="BackupTarget")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    activity_stream_policy_status: ActivityStreamPolicyStatus = pydantic.Field(None, alias="ActivityStreamPolicyStatus")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    db_system_id: String = pydantic.Field(None, alias="DBSystemId")
    master_user_secret: 'MasterUserSecret' = pydantic.Field(None, alias="MasterUserSecret")
    certificate_details: 'CertificateDetails' = pydantic.Field(None, alias="CertificateDetails")
    read_replica_source_db_cluster_identifier: String = pydantic.Field(None, alias="ReadReplicaSourceDBClusterIdentifier")

class DBInstanceAutomatedBackup(_RDSBase):
    db_instance_arn: String = pydantic.Field(None, alias="DBInstanceArn")
    dbi_resource_id: String = pydantic.Field(None, alias="DbiResourceId")
    region: String = pydantic.Field(None, alias="Region")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    restore_window: 'RestoreWindow' = pydantic.Field(None, alias="RestoreWindow")
    allocated_storage: Integer = pydantic.Field(None, alias="AllocatedStorage")
    status: String = pydantic.Field(None, alias="Status")
    port: Integer = pydantic.Field(None, alias="Port")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    instance_create_time: 'TStamp' = pydantic.Field(None, alias="InstanceCreateTime")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    timezone: String = pydantic.Field(None, alias="Timezone")
    iam_database_authentication_enabled: Boolean = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    db_instance_automated_backups_arn: String = pydantic.Field(None, alias="DBInstanceAutomatedBackupsArn")
    db_instance_automated_backups_replications: DBInstanceAutomatedBackupsReplicationList = pydantic.Field(None, alias="DBInstanceAutomatedBackupsReplications")
    backup_target: String = pydantic.Field(None, alias="BackupTarget")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")

class DBInstanceAutomatedBackupMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_instance_automated_backups: DBInstanceAutomatedBackupList = pydantic.Field(None, alias="DBInstanceAutomatedBackups")

class DBInstanceAutomatedBackupsReplication(_RDSBase):
    db_instance_automated_backups_arn: String = pydantic.Field(None, alias="DBInstanceAutomatedBackupsArn")

class DBInstanceMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_instances: DBInstanceList = pydantic.Field(None, alias="DBInstances")

class DBInstanceRole(_RDSBase):
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    feature_name: String = pydantic.Field(None, alias="FeatureName")
    status: String = pydantic.Field(None, alias="Status")

class DBInstanceStatusInfo(_RDSBase):
    status_type: String = pydantic.Field(None, alias="StatusType")
    normal: Boolean = pydantic.Field(None, alias="Normal")
    status: String = pydantic.Field(None, alias="Status")
    message: String = pydantic.Field(None, alias="Message")

class DBParameterGroup(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    description: String = pydantic.Field(None, alias="Description")
    db_parameter_group_arn: String = pydantic.Field(None, alias="DBParameterGroupArn")

class DBParameterGroupDetails(_RDSBase):
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")
    marker: String = pydantic.Field(None, alias="Marker")

class DBParameterGroupNameMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")

class DBParameterGroupStatus(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    parameter_apply_status: String = pydantic.Field(None, alias="ParameterApplyStatus")

class DBParameterGroupsMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_parameter_groups: DBParameterGroupList = pydantic.Field(None, alias="DBParameterGroups")

class DBProxy(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    db_proxy_arn: String = pydantic.Field(None, alias="DBProxyArn")
    status: DBProxyStatus = pydantic.Field(None, alias="Status")
    engine_family: String = pydantic.Field(None, alias="EngineFamily")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    vpc_security_group_ids: StringList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    vpc_subnet_ids: StringList = pydantic.Field(None, alias="VpcSubnetIds")
    auth: UserAuthConfigInfoList = pydantic.Field(None, alias="Auth")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    require_tls: Boolean = pydantic.Field(None, alias="RequireTLS")
    idle_client_timeout: Integer = pydantic.Field(None, alias="IdleClientTimeout")
    debug_logging: Boolean = pydantic.Field(None, alias="DebugLogging")
    created_date: 'TStamp' = pydantic.Field(None, alias="CreatedDate")
    updated_date: 'TStamp' = pydantic.Field(None, alias="UpdatedDate")

class DBProxyEndpoint(_RDSBase):
    db_proxy_endpoint_name: String = pydantic.Field(None, alias="DBProxyEndpointName")
    db_proxy_endpoint_arn: String = pydantic.Field(None, alias="DBProxyEndpointArn")
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    status: DBProxyEndpointStatus = pydantic.Field(None, alias="Status")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    vpc_security_group_ids: StringList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    vpc_subnet_ids: StringList = pydantic.Field(None, alias="VpcSubnetIds")
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    created_date: 'TStamp' = pydantic.Field(None, alias="CreatedDate")
    target_role: DBProxyEndpointTargetRole = pydantic.Field(None, alias="TargetRole")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")

class DBProxyTarget(_RDSBase):
    target_arn: String = pydantic.Field(None, alias="TargetArn")
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    tracked_cluster_id: String = pydantic.Field(None, alias="TrackedClusterId")
    rds_resource_id: String = pydantic.Field(None, alias="RdsResourceId")
    port: Integer = pydantic.Field(None, alias="Port")
    type: TargetType = pydantic.Field(None, alias="Type")
    role: TargetRole = pydantic.Field(None, alias="Role")
    target_health: 'TargetHealth' = pydantic.Field(None, alias="TargetHealth")

class DBProxyTargetGroup(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    target_group_name: String = pydantic.Field(None, alias="TargetGroupName")
    target_group_arn: String = pydantic.Field(None, alias="TargetGroupArn")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")
    status: String = pydantic.Field(None, alias="Status")
    connection_pool_config: 'ConnectionPoolConfigurationInfo' = pydantic.Field(None, alias="ConnectionPoolConfig")
    created_date: 'TStamp' = pydantic.Field(None, alias="CreatedDate")
    updated_date: 'TStamp' = pydantic.Field(None, alias="UpdatedDate")

class DBSecurityGroup(_RDSBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")
    db_security_group_description: String = pydantic.Field(None, alias="DBSecurityGroupDescription")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    ec_2_security_groups: EC2SecurityGroupList = pydantic.Field(None, alias="EC2SecurityGroups")
    ip_ranges: IPRangeList = pydantic.Field(None, alias="IPRanges")
    db_security_group_arn: String = pydantic.Field(None, alias="DBSecurityGroupArn")

class DBSecurityGroupMembership(_RDSBase):
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")
    status: String = pydantic.Field(None, alias="Status")

class DBSecurityGroupMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_security_groups: DBSecurityGroups = pydantic.Field(None, alias="DBSecurityGroups")

class DBSnapshot(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    snapshot_create_time: 'TStamp' = pydantic.Field(None, alias="SnapshotCreateTime")
    engine: String = pydantic.Field(None, alias="Engine")
    allocated_storage: Integer = pydantic.Field(None, alias="AllocatedStorage")
    status: String = pydantic.Field(None, alias="Status")
    port: Integer = pydantic.Field(None, alias="Port")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    instance_create_time: 'TStamp' = pydantic.Field(None, alias="InstanceCreateTime")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    snapshot_type: String = pydantic.Field(None, alias="SnapshotType")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    percent_progress: Integer = pydantic.Field(None, alias="PercentProgress")
    source_region: String = pydantic.Field(None, alias="SourceRegion")
    source_db_snapshot_identifier: String = pydantic.Field(None, alias="SourceDBSnapshotIdentifier")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    db_snapshot_arn: String = pydantic.Field(None, alias="DBSnapshotArn")
    timezone: String = pydantic.Field(None, alias="Timezone")
    iam_database_authentication_enabled: Boolean = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    dbi_resource_id: String = pydantic.Field(None, alias="DbiResourceId")
    tag_list: TagList = pydantic.Field(None, alias="TagList")
    original_snapshot_create_time: 'TStamp' = pydantic.Field(None, alias="OriginalSnapshotCreateTime")
    snapshot_database_time: 'TStamp' = pydantic.Field(None, alias="SnapshotDatabaseTime")
    snapshot_target: String = pydantic.Field(None, alias="SnapshotTarget")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")

class DBSnapshotAttribute(_RDSBase):
    attribute_name: String = pydantic.Field(None, alias="AttributeName")
    attribute_values: AttributeValueList = pydantic.Field(None, alias="AttributeValues")

class DBSnapshotAttributesResult(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    db_snapshot_attributes: DBSnapshotAttributeList = pydantic.Field(None, alias="DBSnapshotAttributes")

class DBSnapshotMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_snapshots: DBSnapshotList = pydantic.Field(None, alias="DBSnapshots")

class DBSubnetGroup(_RDSBase):
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    db_subnet_group_description: String = pydantic.Field(None, alias="DBSubnetGroupDescription")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    subnet_group_status: String = pydantic.Field(None, alias="SubnetGroupStatus")
    subnets: SubnetList = pydantic.Field(None, alias="Subnets")
    db_subnet_group_arn: String = pydantic.Field(None, alias="DBSubnetGroupArn")
    supported_network_types: StringList = pydantic.Field(None, alias="SupportedNetworkTypes")

class DBSubnetGroupMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    db_subnet_groups: DBSubnetGroups = pydantic.Field(None, alias="DBSubnetGroups")

class DeleteBlueGreenDeploymentRequest(_RDSBase):
    blue_green_deployment_identifier: BlueGreenDeploymentIdentifier = pydantic.Field(None, alias="BlueGreenDeploymentIdentifier")
    delete_target: BooleanOptional = pydantic.Field(None, alias="DeleteTarget")

class DeleteBlueGreenDeploymentResponse(_RDSBase):
    blue_green_deployment: 'BlueGreenDeployment' = pydantic.Field(None, alias="BlueGreenDeployment")

class DeleteCustomDBEngineVersionMessage(_RDSBase):
    engine: CustomEngineName = pydantic.Field(None, alias="Engine")
    engine_version: CustomEngineVersion = pydantic.Field(None, alias="EngineVersion")

class DeleteDBClusterEndpointMessage(_RDSBase):
    db_cluster_endpoint_identifier: String = pydantic.Field(None, alias="DBClusterEndpointIdentifier")

class DeleteDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    skip_final_snapshot: Boolean = pydantic.Field(None, alias="SkipFinalSnapshot")
    final_db_snapshot_identifier: String = pydantic.Field(None, alias="FinalDBSnapshotIdentifier")

class DeleteDBClusterParameterGroupMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")

class DeleteDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class DeleteDBClusterSnapshotMessage(_RDSBase):
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")

class DeleteDBClusterSnapshotResult(_RDSBase):
    db_cluster_snapshot: 'DBClusterSnapshot' = pydantic.Field(None, alias="DBClusterSnapshot")

class DeleteDBInstanceAutomatedBackupMessage(_RDSBase):
    dbi_resource_id: String = pydantic.Field(None, alias="DbiResourceId")
    db_instance_automated_backups_arn: String = pydantic.Field(None, alias="DBInstanceAutomatedBackupsArn")

class DeleteDBInstanceAutomatedBackupResult(_RDSBase):
    db_instance_automated_backup: 'DBInstanceAutomatedBackup' = pydantic.Field(None, alias="DBInstanceAutomatedBackup")

class DeleteDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    skip_final_snapshot: Boolean = pydantic.Field(None, alias="SkipFinalSnapshot")
    final_db_snapshot_identifier: String = pydantic.Field(None, alias="FinalDBSnapshotIdentifier")
    delete_automated_backups: BooleanOptional = pydantic.Field(None, alias="DeleteAutomatedBackups")

class DeleteDBInstanceResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class DeleteDBParameterGroupMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")

class DeleteDBProxyEndpointRequest(_RDSBase):
    db_proxy_endpoint_name: DBProxyEndpointName = pydantic.Field(None, alias="DBProxyEndpointName")

class DeleteDBProxyEndpointResponse(_RDSBase):
    db_proxy_endpoint: 'DBProxyEndpoint' = pydantic.Field(None, alias="DBProxyEndpoint")

class DeleteDBProxyRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")

class DeleteDBProxyResponse(_RDSBase):
    db_proxy: 'DBProxy' = pydantic.Field(None, alias="DBProxy")

class DeleteDBSecurityGroupMessage(_RDSBase):
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")

class DeleteDBSnapshotMessage(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")

class DeleteDBSnapshotResult(_RDSBase):
    db_snapshot: 'DBSnapshot' = pydantic.Field(None, alias="DBSnapshot")

class DeleteDBSubnetGroupMessage(_RDSBase):
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")

class DeleteEventSubscriptionMessage(_RDSBase):
    subscription_name: String = pydantic.Field(None, alias="SubscriptionName")

class DeleteEventSubscriptionResult(_RDSBase):
    event_subscription: 'EventSubscription' = pydantic.Field(None, alias="EventSubscription")

class DeleteGlobalClusterMessage(_RDSBase):
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")

class DeleteGlobalClusterResult(_RDSBase):
    global_cluster: 'GlobalCluster' = pydantic.Field(None, alias="GlobalCluster")

class DeleteOptionGroupMessage(_RDSBase):
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")

class DeregisterDBProxyTargetsRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    target_group_name: String = pydantic.Field(None, alias="TargetGroupName")
    db_instance_identifiers: StringList = pydantic.Field(None, alias="DBInstanceIdentifiers")
    db_cluster_identifiers: StringList = pydantic.Field(None, alias="DBClusterIdentifiers")

class DeregisterDBProxyTargetsResponse(_RDSBase):
    pass
class DescribeAccountAttributesMessage(_RDSBase):
    pass
class DescribeBlueGreenDeploymentsRequest(_RDSBase):
    blue_green_deployment_identifier: BlueGreenDeploymentIdentifier = pydantic.Field(None, alias="BlueGreenDeploymentIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")

class DescribeBlueGreenDeploymentsResponse(_RDSBase):
    blue_green_deployments: BlueGreenDeploymentList = pydantic.Field(None, alias="BlueGreenDeployments")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeCertificatesMessage(_RDSBase):
    certificate_identifier: String = pydantic.Field(None, alias="CertificateIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBClusterBacktracksMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    backtrack_identifier: String = pydantic.Field(None, alias="BacktrackIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBClusterEndpointsMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_endpoint_identifier: String = pydantic.Field(None, alias="DBClusterEndpointIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBClusterParameterGroupsMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBClusterParametersMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    source: String = pydantic.Field(None, alias="Source")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBClusterSnapshotAttributesMessage(_RDSBase):
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")

class DescribeDBClusterSnapshotAttributesResult(_RDSBase):
    db_cluster_snapshot_attributes_result: 'DBClusterSnapshotAttributesResult' = pydantic.Field(None, alias="DBClusterSnapshotAttributesResult")

class DescribeDBClusterSnapshotsMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")
    snapshot_type: String = pydantic.Field(None, alias="SnapshotType")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")
    include_shared: Boolean = pydantic.Field(None, alias="IncludeShared")
    include_public: Boolean = pydantic.Field(None, alias="IncludePublic")

class DescribeDBClustersMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")
    include_shared: Boolean = pydantic.Field(None, alias="IncludeShared")

class DescribeDBEngineVersionsMessage(_RDSBase):
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")
    default_only: Boolean = pydantic.Field(None, alias="DefaultOnly")
    list_supported_character_sets: BooleanOptional = pydantic.Field(None, alias="ListSupportedCharacterSets")
    list_supported_timezones: BooleanOptional = pydantic.Field(None, alias="ListSupportedTimezones")
    include_all: BooleanOptional = pydantic.Field(None, alias="IncludeAll")

class DescribeDBInstanceAutomatedBackupsMessage(_RDSBase):
    dbi_resource_id: String = pydantic.Field(None, alias="DbiResourceId")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")
    db_instance_automated_backups_arn: String = pydantic.Field(None, alias="DBInstanceAutomatedBackupsArn")

class DescribeDBInstancesMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBLogFilesDetails(_RDSBase):
    log_file_name: String = pydantic.Field(None, alias="LogFileName")
    last_written: Long = pydantic.Field(None, alias="LastWritten")
    size: Long = pydantic.Field(None, alias="Size")

class DescribeDBLogFilesMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    filename_contains: String = pydantic.Field(None, alias="FilenameContains")
    file_last_written: Long = pydantic.Field(None, alias="FileLastWritten")
    file_size: Long = pydantic.Field(None, alias="FileSize")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBLogFilesResponse(_RDSBase):
    describe_db_log_files: DescribeDBLogFilesList = pydantic.Field(None, alias="DescribeDBLogFiles")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBParameterGroupsMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBParametersMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    source: String = pydantic.Field(None, alias="Source")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBProxiesRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")

class DescribeDBProxiesResponse(_RDSBase):
    db_proxies: DBProxyList = pydantic.Field(None, alias="DBProxies")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBProxyEndpointsRequest(_RDSBase):
    db_proxy_name: DBProxyName = pydantic.Field(None, alias="DBProxyName")
    db_proxy_endpoint_name: DBProxyEndpointName = pydantic.Field(None, alias="DBProxyEndpointName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")

class DescribeDBProxyEndpointsResponse(_RDSBase):
    db_proxy_endpoints: DBProxyEndpointList = pydantic.Field(None, alias="DBProxyEndpoints")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBProxyTargetGroupsRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    target_group_name: String = pydantic.Field(None, alias="TargetGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")

class DescribeDBProxyTargetGroupsResponse(_RDSBase):
    target_groups: TargetGroupList = pydantic.Field(None, alias="TargetGroups")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBProxyTargetsRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    target_group_name: String = pydantic.Field(None, alias="TargetGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")

class DescribeDBProxyTargetsResponse(_RDSBase):
    targets: TargetList = pydantic.Field(None, alias="Targets")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBSecurityGroupsMessage(_RDSBase):
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeDBSnapshotAttributesMessage(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")

class DescribeDBSnapshotAttributesResult(_RDSBase):
    db_snapshot_attributes_result: 'DBSnapshotAttributesResult' = pydantic.Field(None, alias="DBSnapshotAttributesResult")

class DescribeDBSnapshotsMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    snapshot_type: String = pydantic.Field(None, alias="SnapshotType")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")
    include_shared: Boolean = pydantic.Field(None, alias="IncludeShared")
    include_public: Boolean = pydantic.Field(None, alias="IncludePublic")
    dbi_resource_id: String = pydantic.Field(None, alias="DbiResourceId")

class DescribeDBSubnetGroupsMessage(_RDSBase):
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeEngineDefaultClusterParametersMessage(_RDSBase):
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeEngineDefaultClusterParametersResult(_RDSBase):
    engine_defaults: 'EngineDefaults' = pydantic.Field(None, alias="EngineDefaults")

class DescribeEngineDefaultParametersMessage(_RDSBase):
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeEngineDefaultParametersResult(_RDSBase):
    engine_defaults: 'EngineDefaults' = pydantic.Field(None, alias="EngineDefaults")

class DescribeEventCategoriesMessage(_RDSBase):
    source_type: String = pydantic.Field(None, alias="SourceType")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeEventSubscriptionsMessage(_RDSBase):
    subscription_name: String = pydantic.Field(None, alias="SubscriptionName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeEventsMessage(_RDSBase):
    source_identifier: String = pydantic.Field(None, alias="SourceIdentifier")
    source_type: SourceType = pydantic.Field(None, alias="SourceType")
    start_time: 'TStamp' = pydantic.Field(None, alias="StartTime")
    end_time: 'TStamp' = pydantic.Field(None, alias="EndTime")
    duration: IntegerOptional = pydantic.Field(None, alias="Duration")
    event_categories: EventCategoriesList = pydantic.Field(None, alias="EventCategories")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeExportTasksMessage(_RDSBase):
    export_task_identifier: String = pydantic.Field(None, alias="ExportTaskIdentifier")
    source_arn: String = pydantic.Field(None, alias="SourceArn")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")
    source_type: ExportSourceType = pydantic.Field(None, alias="SourceType")

class DescribeGlobalClustersMessage(_RDSBase):
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeOptionGroupOptionsMessage(_RDSBase):
    engine_name: String = pydantic.Field(None, alias="EngineName")
    major_engine_version: String = pydantic.Field(None, alias="MajorEngineVersion")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeOptionGroupsMessage(_RDSBase):
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    engine_name: String = pydantic.Field(None, alias="EngineName")
    major_engine_version: String = pydantic.Field(None, alias="MajorEngineVersion")

class DescribeOrderableDBInstanceOptionsMessage(_RDSBase):
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    availability_zone_group: String = pydantic.Field(None, alias="AvailabilityZoneGroup")
    vpc: BooleanOptional = pydantic.Field(None, alias="Vpc")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribePendingMaintenanceActionsMessage(_RDSBase):
    resource_identifier: String = pydantic.Field(None, alias="ResourceIdentifier")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    marker: String = pydantic.Field(None, alias="Marker")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")

class DescribeReservedDBInstancesMessage(_RDSBase):
    reserved_db_instance_id: String = pydantic.Field(None, alias="ReservedDBInstanceId")
    reserved_db_instances_offering_id: String = pydantic.Field(None, alias="ReservedDBInstancesOfferingId")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    duration: String = pydantic.Field(None, alias="Duration")
    product_description: String = pydantic.Field(None, alias="ProductDescription")
    offering_type: String = pydantic.Field(None, alias="OfferingType")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    lease_id: String = pydantic.Field(None, alias="LeaseId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeReservedDBInstancesOfferingsMessage(_RDSBase):
    reserved_db_instances_offering_id: String = pydantic.Field(None, alias="ReservedDBInstancesOfferingId")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    duration: String = pydantic.Field(None, alias="Duration")
    product_description: String = pydantic.Field(None, alias="ProductDescription")
    offering_type: String = pydantic.Field(None, alias="OfferingType")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")

class DescribeSourceRegionsMessage(_RDSBase):
    region_name: String = pydantic.Field(None, alias="RegionName")
    max_records: IntegerOptional = pydantic.Field(None, alias="MaxRecords")
    marker: String = pydantic.Field(None, alias="Marker")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeValidDBInstanceModificationsMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")

class DescribeValidDBInstanceModificationsResult(_RDSBase):
    valid_db_instance_modifications_message: 'ValidDBInstanceModificationsMessage' = pydantic.Field(None, alias="ValidDBInstanceModificationsMessage")

class DomainMembership(_RDSBase):
    domain: String = pydantic.Field(None, alias="Domain")
    status: String = pydantic.Field(None, alias="Status")
    fqdn: String = pydantic.Field(None, alias="FQDN")
    iam_role_name: String = pydantic.Field(None, alias="IAMRoleName")

class DoubleRange(_RDSBase):
    from: Double = pydantic.Field(None, alias="From")
    to: Double = pydantic.Field(None, alias="To")

class DownloadDBLogFilePortionDetails(_RDSBase):
    log_file_data: String = pydantic.Field(None, alias="LogFileData")
    marker: String = pydantic.Field(None, alias="Marker")
    additional_data_pending: Boolean = pydantic.Field(None, alias="AdditionalDataPending")

class DownloadDBLogFilePortionMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    log_file_name: String = pydantic.Field(None, alias="LogFileName")
    marker: String = pydantic.Field(None, alias="Marker")
    number_of_lines: Integer = pydantic.Field(None, alias="NumberOfLines")

class EC2SecurityGroup(_RDSBase):
    status: String = pydantic.Field(None, alias="Status")
    ec_2_security_group_name: String = pydantic.Field(None, alias="EC2SecurityGroupName")
    ec_2_security_group_id: String = pydantic.Field(None, alias="EC2SecurityGroupId")
    ec_2_security_group_owner_id: String = pydantic.Field(None, alias="EC2SecurityGroupOwnerId")

class Endpoint(_RDSBase):
    address: String = pydantic.Field(None, alias="Address")
    port: Integer = pydantic.Field(None, alias="Port")
    hosted_zone_id: String = pydantic.Field(None, alias="HostedZoneId")

class EngineDefaults(_RDSBase):
    db_parameter_group_family: String = pydantic.Field(None, alias="DBParameterGroupFamily")
    marker: String = pydantic.Field(None, alias="Marker")
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")

class Event(_RDSBase):
    source_identifier: String = pydantic.Field(None, alias="SourceIdentifier")
    source_type: SourceType = pydantic.Field(None, alias="SourceType")
    message: String = pydantic.Field(None, alias="Message")
    event_categories: EventCategoriesList = pydantic.Field(None, alias="EventCategories")
    date: 'TStamp' = pydantic.Field(None, alias="Date")
    source_arn: String = pydantic.Field(None, alias="SourceArn")

class EventCategoriesMap(_RDSBase):
    source_type: String = pydantic.Field(None, alias="SourceType")
    event_categories: EventCategoriesList = pydantic.Field(None, alias="EventCategories")

class EventCategoriesMessage(_RDSBase):
    event_categories_map_list: EventCategoriesMapList = pydantic.Field(None, alias="EventCategoriesMapList")

class EventSubscription(_RDSBase):
    customer_aws_id: String = pydantic.Field(None, alias="CustomerAwsId")
    cust_subscription_id: String = pydantic.Field(None, alias="CustSubscriptionId")
    sns_topic_arn: String = pydantic.Field(None, alias="SnsTopicArn")
    status: String = pydantic.Field(None, alias="Status")
    subscription_creation_time: String = pydantic.Field(None, alias="SubscriptionCreationTime")
    source_type: String = pydantic.Field(None, alias="SourceType")
    source_ids_list: SourceIdsList = pydantic.Field(None, alias="SourceIdsList")
    event_categories_list: EventCategoriesList = pydantic.Field(None, alias="EventCategoriesList")
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    event_subscription_arn: String = pydantic.Field(None, alias="EventSubscriptionArn")

class EventSubscriptionsMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    event_subscriptions_list: EventSubscriptionsList = pydantic.Field(None, alias="EventSubscriptionsList")

class EventsMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    events: EventList = pydantic.Field(None, alias="Events")

class ExportTask(_RDSBase):
    export_task_identifier: String = pydantic.Field(None, alias="ExportTaskIdentifier")
    source_arn: String = pydantic.Field(None, alias="SourceArn")
    export_only: StringList = pydantic.Field(None, alias="ExportOnly")
    snapshot_time: 'TStamp' = pydantic.Field(None, alias="SnapshotTime")
    task_start_time: 'TStamp' = pydantic.Field(None, alias="TaskStartTime")
    task_end_time: 'TStamp' = pydantic.Field(None, alias="TaskEndTime")
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")
    iam_role_arn: String = pydantic.Field(None, alias="IamRoleArn")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    status: String = pydantic.Field(None, alias="Status")
    percent_progress: Integer = pydantic.Field(None, alias="PercentProgress")
    total_extracted_data_in_gb: Integer = pydantic.Field(None, alias="TotalExtractedDataInGB")
    failure_cause: String = pydantic.Field(None, alias="FailureCause")
    warning_message: String = pydantic.Field(None, alias="WarningMessage")
    source_type: ExportSourceType = pydantic.Field(None, alias="SourceType")

class ExportTasksMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    export_tasks: ExportTasksList = pydantic.Field(None, alias="ExportTasks")

class FailoverDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    target_db_instance_identifier: String = pydantic.Field(None, alias="TargetDBInstanceIdentifier")

class FailoverDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class FailoverGlobalClusterMessage(_RDSBase):
    global_cluster_identifier: GlobalClusterIdentifier = pydantic.Field(None, alias="GlobalClusterIdentifier")
    target_db_cluster_identifier: DBClusterIdentifier = pydantic.Field(None, alias="TargetDbClusterIdentifier")

class FailoverGlobalClusterResult(_RDSBase):
    global_cluster: 'GlobalCluster' = pydantic.Field(None, alias="GlobalCluster")

class FailoverState(_RDSBase):
    status: FailoverStatus = pydantic.Field(None, alias="Status")
    from_db_cluster_arn: String = pydantic.Field(None, alias="FromDbClusterArn")
    to_db_cluster_arn: String = pydantic.Field(None, alias="ToDbClusterArn")

class Filter(_RDSBase):
    name: String = pydantic.Field(None, alias="Name")
    values: FilterValueList = pydantic.Field(None, alias="Values")

class GlobalCluster(_RDSBase):
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")
    global_cluster_resource_id: String = pydantic.Field(None, alias="GlobalClusterResourceId")
    global_cluster_arn: String = pydantic.Field(None, alias="GlobalClusterArn")
    status: String = pydantic.Field(None, alias="Status")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    database_name: String = pydantic.Field(None, alias="DatabaseName")
    storage_encrypted: BooleanOptional = pydantic.Field(None, alias="StorageEncrypted")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    global_cluster_members: GlobalClusterMemberList = pydantic.Field(None, alias="GlobalClusterMembers")
    failover_state: 'FailoverState' = pydantic.Field(None, alias="FailoverState")

class GlobalClusterMember(_RDSBase):
    db_cluster_arn: String = pydantic.Field(None, alias="DBClusterArn")
    readers: ReadersArnList = pydantic.Field(None, alias="Readers")
    is_writer: Boolean = pydantic.Field(None, alias="IsWriter")
    global_write_forwarding_status: WriteForwardingStatus = pydantic.Field(None, alias="GlobalWriteForwardingStatus")

class GlobalClustersMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    global_clusters: GlobalClusterList = pydantic.Field(None, alias="GlobalClusters")

class IPRange(_RDSBase):
    status: String = pydantic.Field(None, alias="Status")
    cidrip: String = pydantic.Field(None, alias="CIDRIP")

class ListTagsForResourceMessage(_RDSBase):
    resource_name: String = pydantic.Field(None, alias="ResourceName")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class MasterUserSecret(_RDSBase):
    secret_arn: String = pydantic.Field(None, alias="SecretArn")
    secret_status: String = pydantic.Field(None, alias="SecretStatus")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")

class MinimumEngineVersionPerAllowedValue(_RDSBase):
    allowed_value: String = pydantic.Field(None, alias="AllowedValue")
    minimum_engine_version: String = pydantic.Field(None, alias="MinimumEngineVersion")

class ModifyActivityStreamRequest(_RDSBase):
    resource_arn: String = pydantic.Field(None, alias="ResourceArn")
    audit_policy_state: AuditPolicyState = pydantic.Field(None, alias="AuditPolicyState")

class ModifyActivityStreamResponse(_RDSBase):
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    kinesis_stream_name: String = pydantic.Field(None, alias="KinesisStreamName")
    status: ActivityStreamStatus = pydantic.Field(None, alias="Status")
    mode: ActivityStreamMode = pydantic.Field(None, alias="Mode")
    engine_native_audit_fields_included: BooleanOptional = pydantic.Field(None, alias="EngineNativeAuditFieldsIncluded")
    policy_status: ActivityStreamPolicyStatus = pydantic.Field(None, alias="PolicyStatus")

class ModifyCertificatesMessage(_RDSBase):
    certificate_identifier: String = pydantic.Field(None, alias="CertificateIdentifier")
    remove_customer_override: BooleanOptional = pydantic.Field(None, alias="RemoveCustomerOverride")

class ModifyCertificatesResult(_RDSBase):
    certificate: 'Certificate' = pydantic.Field(None, alias="Certificate")

class ModifyCurrentDBClusterCapacityMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    capacity: IntegerOptional = pydantic.Field(None, alias="Capacity")
    seconds_before_timeout: IntegerOptional = pydantic.Field(None, alias="SecondsBeforeTimeout")
    timeout_action: String = pydantic.Field(None, alias="TimeoutAction")

class ModifyCustomDBEngineVersionMessage(_RDSBase):
    engine: CustomEngineName = pydantic.Field(None, alias="Engine")
    engine_version: CustomEngineVersion = pydantic.Field(None, alias="EngineVersion")
    description: Description = pydantic.Field(None, alias="Description")
    status: CustomEngineVersionStatus = pydantic.Field(None, alias="Status")

class ModifyDBClusterEndpointMessage(_RDSBase):
    db_cluster_endpoint_identifier: String = pydantic.Field(None, alias="DBClusterEndpointIdentifier")
    endpoint_type: String = pydantic.Field(None, alias="EndpointType")
    static_members: StringList = pydantic.Field(None, alias="StaticMembers")
    excluded_members: StringList = pydantic.Field(None, alias="ExcludedMembers")

class ModifyDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    new_db_cluster_identifier: String = pydantic.Field(None, alias="NewDBClusterIdentifier")
    apply_immediately: Boolean = pydantic.Field(None, alias="ApplyImmediately")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    backtrack_window: LongOptional = pydantic.Field(None, alias="BacktrackWindow")
    cloudwatch_logs_export_configuration: 'CloudwatchLogsExportConfiguration' = pydantic.Field(None, alias="CloudwatchLogsExportConfiguration")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    allow_major_version_upgrade: Boolean = pydantic.Field(None, alias="AllowMajorVersionUpgrade")
    db_instance_parameter_group_name: String = pydantic.Field(None, alias="DBInstanceParameterGroupName")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    scaling_configuration: 'ScalingConfiguration' = pydantic.Field(None, alias="ScalingConfiguration")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    enable_http_endpoint: BooleanOptional = pydantic.Field(None, alias="EnableHttpEndpoint")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    enable_global_write_forwarding: BooleanOptional = pydantic.Field(None, alias="EnableGlobalWriteForwarding")
    db_cluster_instance_class: String = pydantic.Field(None, alias="DBClusterInstanceClass")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    enable_performance_insights: BooleanOptional = pydantic.Field(None, alias="EnablePerformanceInsights")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    serverless_v_2_scaling_configuration: 'ServerlessV2ScalingConfiguration' = pydantic.Field(None, alias="ServerlessV2ScalingConfiguration")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    manage_master_user_password: BooleanOptional = pydantic.Field(None, alias="ManageMasterUserPassword")
    rotate_master_user_password: BooleanOptional = pydantic.Field(None, alias="RotateMasterUserPassword")
    master_user_secret_kms_key_id: String = pydantic.Field(None, alias="MasterUserSecretKmsKeyId")
    engine_mode: String = pydantic.Field(None, alias="EngineMode")
    allow_engine_mode_change: Boolean = pydantic.Field(None, alias="AllowEngineModeChange")

class ModifyDBClusterParameterGroupMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")

class ModifyDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class ModifyDBClusterSnapshotAttributeMessage(_RDSBase):
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")
    attribute_name: String = pydantic.Field(None, alias="AttributeName")
    values_to_add: AttributeValueList = pydantic.Field(None, alias="ValuesToAdd")
    values_to_remove: AttributeValueList = pydantic.Field(None, alias="ValuesToRemove")

class ModifyDBClusterSnapshotAttributeResult(_RDSBase):
    db_cluster_snapshot_attributes_result: 'DBClusterSnapshotAttributesResult' = pydantic.Field(None, alias="DBClusterSnapshotAttributesResult")

class ModifyDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    db_security_groups: DBSecurityGroupNameList = pydantic.Field(None, alias="DBSecurityGroups")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    apply_immediately: Boolean = pydantic.Field(None, alias="ApplyImmediately")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    allow_major_version_upgrade: Boolean = pydantic.Field(None, alias="AllowMajorVersionUpgrade")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    new_db_instance_identifier: String = pydantic.Field(None, alias="NewDBInstanceIdentifier")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    tde_credential_password: String = pydantic.Field(None, alias="TdeCredentialPassword")
    ca_certificate_identifier: String = pydantic.Field(None, alias="CACertificateIdentifier")
    domain: String = pydantic.Field(None, alias="Domain")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    db_port_number: IntegerOptional = pydantic.Field(None, alias="DBPortNumber")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    promotion_tier: IntegerOptional = pydantic.Field(None, alias="PromotionTier")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    enable_performance_insights: BooleanOptional = pydantic.Field(None, alias="EnablePerformanceInsights")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    cloudwatch_logs_export_configuration: 'CloudwatchLogsExportConfiguration' = pydantic.Field(None, alias="CloudwatchLogsExportConfiguration")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    use_default_processor_features: BooleanOptional = pydantic.Field(None, alias="UseDefaultProcessorFeatures")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    max_allocated_storage: IntegerOptional = pydantic.Field(None, alias="MaxAllocatedStorage")
    certificate_rotation_restart: BooleanOptional = pydantic.Field(None, alias="CertificateRotationRestart")
    replica_mode: ReplicaMode = pydantic.Field(None, alias="ReplicaMode")
    enable_customer_owned_ip: BooleanOptional = pydantic.Field(None, alias="EnableCustomerOwnedIp")
    aws_backup_recovery_point_arn: AwsBackupRecoveryPointArn = pydantic.Field(None, alias="AwsBackupRecoveryPointArn")
    automation_mode: AutomationMode = pydantic.Field(None, alias="AutomationMode")
    resume_full_automation_mode_minutes: IntegerOptional = pydantic.Field(None, alias="ResumeFullAutomationModeMinutes")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    manage_master_user_password: BooleanOptional = pydantic.Field(None, alias="ManageMasterUserPassword")
    rotate_master_user_password: BooleanOptional = pydantic.Field(None, alias="RotateMasterUserPassword")
    master_user_secret_kms_key_id: String = pydantic.Field(None, alias="MasterUserSecretKmsKeyId")
    engine: String = pydantic.Field(None, alias="Engine")

class ModifyDBInstanceResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class ModifyDBParameterGroupMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")

class ModifyDBProxyEndpointRequest(_RDSBase):
    db_proxy_endpoint_name: DBProxyEndpointName = pydantic.Field(None, alias="DBProxyEndpointName")
    new_db_proxy_endpoint_name: DBProxyEndpointName = pydantic.Field(None, alias="NewDBProxyEndpointName")
    vpc_security_group_ids: StringList = pydantic.Field(None, alias="VpcSecurityGroupIds")

class ModifyDBProxyEndpointResponse(_RDSBase):
    db_proxy_endpoint: 'DBProxyEndpoint' = pydantic.Field(None, alias="DBProxyEndpoint")

class ModifyDBProxyRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    new_db_proxy_name: String = pydantic.Field(None, alias="NewDBProxyName")
    auth: UserAuthConfigList = pydantic.Field(None, alias="Auth")
    require_tls: BooleanOptional = pydantic.Field(None, alias="RequireTLS")
    idle_client_timeout: IntegerOptional = pydantic.Field(None, alias="IdleClientTimeout")
    debug_logging: BooleanOptional = pydantic.Field(None, alias="DebugLogging")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    security_groups: StringList = pydantic.Field(None, alias="SecurityGroups")

class ModifyDBProxyResponse(_RDSBase):
    db_proxy: 'DBProxy' = pydantic.Field(None, alias="DBProxy")

class ModifyDBProxyTargetGroupRequest(_RDSBase):
    target_group_name: String = pydantic.Field(None, alias="TargetGroupName")
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    connection_pool_config: 'ConnectionPoolConfiguration' = pydantic.Field(None, alias="ConnectionPoolConfig")
    new_name: String = pydantic.Field(None, alias="NewName")

class ModifyDBProxyTargetGroupResponse(_RDSBase):
    db_proxy_target_group: 'DBProxyTargetGroup' = pydantic.Field(None, alias="DBProxyTargetGroup")

class ModifyDBSnapshotAttributeMessage(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    attribute_name: String = pydantic.Field(None, alias="AttributeName")
    values_to_add: AttributeValueList = pydantic.Field(None, alias="ValuesToAdd")
    values_to_remove: AttributeValueList = pydantic.Field(None, alias="ValuesToRemove")

class ModifyDBSnapshotAttributeResult(_RDSBase):
    db_snapshot_attributes_result: 'DBSnapshotAttributesResult' = pydantic.Field(None, alias="DBSnapshotAttributesResult")

class ModifyDBSnapshotMessage(_RDSBase):
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")

class ModifyDBSnapshotResult(_RDSBase):
    db_snapshot: 'DBSnapshot' = pydantic.Field(None, alias="DBSnapshot")

class ModifyDBSubnetGroupMessage(_RDSBase):
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    db_subnet_group_description: String = pydantic.Field(None, alias="DBSubnetGroupDescription")
    subnet_ids: SubnetIdentifierList = pydantic.Field(None, alias="SubnetIds")

class ModifyDBSubnetGroupResult(_RDSBase):
    db_subnet_group: 'DBSubnetGroup' = pydantic.Field(None, alias="DBSubnetGroup")

class ModifyEventSubscriptionMessage(_RDSBase):
    subscription_name: String = pydantic.Field(None, alias="SubscriptionName")
    sns_topic_arn: String = pydantic.Field(None, alias="SnsTopicArn")
    source_type: String = pydantic.Field(None, alias="SourceType")
    event_categories: EventCategoriesList = pydantic.Field(None, alias="EventCategories")
    enabled: BooleanOptional = pydantic.Field(None, alias="Enabled")

class ModifyEventSubscriptionResult(_RDSBase):
    event_subscription: 'EventSubscription' = pydantic.Field(None, alias="EventSubscription")

class ModifyGlobalClusterMessage(_RDSBase):
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")
    new_global_cluster_identifier: String = pydantic.Field(None, alias="NewGlobalClusterIdentifier")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    allow_major_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AllowMajorVersionUpgrade")

class ModifyGlobalClusterResult(_RDSBase):
    global_cluster: 'GlobalCluster' = pydantic.Field(None, alias="GlobalCluster")

class ModifyOptionGroupMessage(_RDSBase):
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    options_to_include: OptionConfigurationList = pydantic.Field(None, alias="OptionsToInclude")
    options_to_remove: OptionNamesList = pydantic.Field(None, alias="OptionsToRemove")
    apply_immediately: Boolean = pydantic.Field(None, alias="ApplyImmediately")

class ModifyOptionGroupResult(_RDSBase):
    option_group: 'OptionGroup' = pydantic.Field(None, alias="OptionGroup")

class Option(_RDSBase):
    option_name: String = pydantic.Field(None, alias="OptionName")
    option_description: String = pydantic.Field(None, alias="OptionDescription")
    persistent: Boolean = pydantic.Field(None, alias="Persistent")
    permanent: Boolean = pydantic.Field(None, alias="Permanent")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    option_version: String = pydantic.Field(None, alias="OptionVersion")
    option_settings: OptionSettingConfigurationList = pydantic.Field(None, alias="OptionSettings")
    db_security_group_memberships: DBSecurityGroupMembershipList = pydantic.Field(None, alias="DBSecurityGroupMemberships")
    vpc_security_group_memberships: VpcSecurityGroupMembershipList = pydantic.Field(None, alias="VpcSecurityGroupMemberships")

class OptionConfiguration(_RDSBase):
    option_name: String = pydantic.Field(None, alias="OptionName")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    option_version: String = pydantic.Field(None, alias="OptionVersion")
    db_security_group_memberships: DBSecurityGroupNameList = pydantic.Field(None, alias="DBSecurityGroupMemberships")
    vpc_security_group_memberships: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupMemberships")
    option_settings: OptionSettingsList = pydantic.Field(None, alias="OptionSettings")

class OptionGroup(_RDSBase):
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    option_group_description: String = pydantic.Field(None, alias="OptionGroupDescription")
    engine_name: String = pydantic.Field(None, alias="EngineName")
    major_engine_version: String = pydantic.Field(None, alias="MajorEngineVersion")
    options: OptionsList = pydantic.Field(None, alias="Options")
    allows_vpc_and_non_vpc_instance_memberships: Boolean = pydantic.Field(None, alias="AllowsVpcAndNonVpcInstanceMemberships")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    option_group_arn: String = pydantic.Field(None, alias="OptionGroupArn")
    source_option_group: String = pydantic.Field(None, alias="SourceOptionGroup")
    source_account_id: String = pydantic.Field(None, alias="SourceAccountId")
    copy_timestamp: 'TStamp' = pydantic.Field(None, alias="CopyTimestamp")

class OptionGroupMembership(_RDSBase):
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    status: String = pydantic.Field(None, alias="Status")

class OptionGroupOption(_RDSBase):
    name: String = pydantic.Field(None, alias="Name")
    description: String = pydantic.Field(None, alias="Description")
    engine_name: String = pydantic.Field(None, alias="EngineName")
    major_engine_version: String = pydantic.Field(None, alias="MajorEngineVersion")
    minimum_required_minor_engine_version: String = pydantic.Field(None, alias="MinimumRequiredMinorEngineVersion")
    port_required: Boolean = pydantic.Field(None, alias="PortRequired")
    default_port: IntegerOptional = pydantic.Field(None, alias="DefaultPort")
    options_depended_on: OptionsDependedOn = pydantic.Field(None, alias="OptionsDependedOn")
    options_conflicts_with: OptionsConflictsWith = pydantic.Field(None, alias="OptionsConflictsWith")
    persistent: Boolean = pydantic.Field(None, alias="Persistent")
    permanent: Boolean = pydantic.Field(None, alias="Permanent")
    requires_auto_minor_engine_version_upgrade: Boolean = pydantic.Field(None, alias="RequiresAutoMinorEngineVersionUpgrade")
    vpc_only: Boolean = pydantic.Field(None, alias="VpcOnly")
    supports_option_version_downgrade: BooleanOptional = pydantic.Field(None, alias="SupportsOptionVersionDowngrade")
    option_group_option_settings: OptionGroupOptionSettingsList = pydantic.Field(None, alias="OptionGroupOptionSettings")
    option_group_option_versions: OptionGroupOptionVersionsList = pydantic.Field(None, alias="OptionGroupOptionVersions")
    copyable_cross_account: BooleanOptional = pydantic.Field(None, alias="CopyableCrossAccount")

class OptionGroupOptionSetting(_RDSBase):
    setting_name: String = pydantic.Field(None, alias="SettingName")
    setting_description: String = pydantic.Field(None, alias="SettingDescription")
    default_value: String = pydantic.Field(None, alias="DefaultValue")
    apply_type: String = pydantic.Field(None, alias="ApplyType")
    allowed_values: String = pydantic.Field(None, alias="AllowedValues")
    is_modifiable: Boolean = pydantic.Field(None, alias="IsModifiable")
    is_required: Boolean = pydantic.Field(None, alias="IsRequired")
    minimum_engine_version_per_allowed_value: MinimumEngineVersionPerAllowedValueList = pydantic.Field(None, alias="MinimumEngineVersionPerAllowedValue")

class OptionGroupOptionsMessage(_RDSBase):
    option_group_options: OptionGroupOptionsList = pydantic.Field(None, alias="OptionGroupOptions")
    marker: String = pydantic.Field(None, alias="Marker")

class OptionGroups(_RDSBase):
    option_groups_list: OptionGroupsList = pydantic.Field(None, alias="OptionGroupsList")
    marker: String = pydantic.Field(None, alias="Marker")

class OptionSetting(_RDSBase):
    name: String = pydantic.Field(None, alias="Name")
    value: String = pydantic.Field(None, alias="Value")
    default_value: String = pydantic.Field(None, alias="DefaultValue")
    description: String = pydantic.Field(None, alias="Description")
    apply_type: String = pydantic.Field(None, alias="ApplyType")
    data_type: String = pydantic.Field(None, alias="DataType")
    allowed_values: String = pydantic.Field(None, alias="AllowedValues")
    is_modifiable: Boolean = pydantic.Field(None, alias="IsModifiable")
    is_collection: Boolean = pydantic.Field(None, alias="IsCollection")

class OptionVersion(_RDSBase):
    version: String = pydantic.Field(None, alias="Version")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")

class OrderableDBInstanceOption(_RDSBase):
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    availability_zone_group: String = pydantic.Field(None, alias="AvailabilityZoneGroup")
    availability_zones: AvailabilityZoneList = pydantic.Field(None, alias="AvailabilityZones")
    multi_az_capable: Boolean = pydantic.Field(None, alias="MultiAZCapable")
    read_replica_capable: Boolean = pydantic.Field(None, alias="ReadReplicaCapable")
    vpc: Boolean = pydantic.Field(None, alias="Vpc")
    supports_storage_encryption: Boolean = pydantic.Field(None, alias="SupportsStorageEncryption")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    supports_iops: Boolean = pydantic.Field(None, alias="SupportsIops")
    supports_enhanced_monitoring: Boolean = pydantic.Field(None, alias="SupportsEnhancedMonitoring")
    supports_iam_database_authentication: Boolean = pydantic.Field(None, alias="SupportsIAMDatabaseAuthentication")
    supports_performance_insights: Boolean = pydantic.Field(None, alias="SupportsPerformanceInsights")
    min_storage_size: IntegerOptional = pydantic.Field(None, alias="MinStorageSize")
    max_storage_size: IntegerOptional = pydantic.Field(None, alias="MaxStorageSize")
    min_iops_per_db_instance: IntegerOptional = pydantic.Field(None, alias="MinIopsPerDbInstance")
    max_iops_per_db_instance: IntegerOptional = pydantic.Field(None, alias="MaxIopsPerDbInstance")
    min_iops_per_gib: DoubleOptional = pydantic.Field(None, alias="MinIopsPerGib")
    max_iops_per_gib: DoubleOptional = pydantic.Field(None, alias="MaxIopsPerGib")
    available_processor_features: AvailableProcessorFeatureList = pydantic.Field(None, alias="AvailableProcessorFeatures")
    supported_engine_modes: EngineModeList = pydantic.Field(None, alias="SupportedEngineModes")
    supports_storage_autoscaling: BooleanOptional = pydantic.Field(None, alias="SupportsStorageAutoscaling")
    supports_kerberos_authentication: BooleanOptional = pydantic.Field(None, alias="SupportsKerberosAuthentication")
    outpost_capable: Boolean = pydantic.Field(None, alias="OutpostCapable")
    supported_activity_stream_modes: ActivityStreamModeList = pydantic.Field(None, alias="SupportedActivityStreamModes")
    supports_global_databases: Boolean = pydantic.Field(None, alias="SupportsGlobalDatabases")
    supports_clusters: Boolean = pydantic.Field(None, alias="SupportsClusters")
    supported_network_types: StringList = pydantic.Field(None, alias="SupportedNetworkTypes")
    supports_storage_throughput: Boolean = pydantic.Field(None, alias="SupportsStorageThroughput")
    min_storage_throughput_per_db_instance: IntegerOptional = pydantic.Field(None, alias="MinStorageThroughputPerDbInstance")
    max_storage_throughput_per_db_instance: IntegerOptional = pydantic.Field(None, alias="MaxStorageThroughputPerDbInstance")
    min_storage_throughput_per_iops: DoubleOptional = pydantic.Field(None, alias="MinStorageThroughputPerIops")
    max_storage_throughput_per_iops: DoubleOptional = pydantic.Field(None, alias="MaxStorageThroughputPerIops")

class OrderableDBInstanceOptionsMessage(_RDSBase):
    orderable_db_instance_options: OrderableDBInstanceOptionsList = pydantic.Field(None, alias="OrderableDBInstanceOptions")
    marker: String = pydantic.Field(None, alias="Marker")

class Outpost(_RDSBase):
    arn: String = pydantic.Field(None, alias="Arn")

class Parameter(_RDSBase):
    parameter_name: String = pydantic.Field(None, alias="ParameterName")
    parameter_value: String = pydantic.Field(None, alias="ParameterValue")
    description: String = pydantic.Field(None, alias="Description")
    source: String = pydantic.Field(None, alias="Source")
    apply_type: String = pydantic.Field(None, alias="ApplyType")
    data_type: String = pydantic.Field(None, alias="DataType")
    allowed_values: String = pydantic.Field(None, alias="AllowedValues")
    is_modifiable: Boolean = pydantic.Field(None, alias="IsModifiable")
    minimum_engine_version: String = pydantic.Field(None, alias="MinimumEngineVersion")
    apply_method: ApplyMethod = pydantic.Field(None, alias="ApplyMethod")
    supported_engine_modes: EngineModeList = pydantic.Field(None, alias="SupportedEngineModes")

class PendingCloudwatchLogsExports(_RDSBase):
    log_types_to_enable: LogTypeList = pydantic.Field(None, alias="LogTypesToEnable")
    log_types_to_disable: LogTypeList = pydantic.Field(None, alias="LogTypesToDisable")

class PendingMaintenanceAction(_RDSBase):
    action: String = pydantic.Field(None, alias="Action")
    auto_applied_after_date: 'TStamp' = pydantic.Field(None, alias="AutoAppliedAfterDate")
    forced_apply_date: 'TStamp' = pydantic.Field(None, alias="ForcedApplyDate")
    opt_in_status: String = pydantic.Field(None, alias="OptInStatus")
    current_apply_date: 'TStamp' = pydantic.Field(None, alias="CurrentApplyDate")
    description: String = pydantic.Field(None, alias="Description")

class PendingMaintenanceActionsMessage(_RDSBase):
    pending_maintenance_actions: PendingMaintenanceActions = pydantic.Field(None, alias="PendingMaintenanceActions")
    marker: String = pydantic.Field(None, alias="Marker")

class PendingModifiedValues(_RDSBase):
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    ca_certificate_identifier: String = pydantic.Field(None, alias="CACertificateIdentifier")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    pending_cloudwatch_logs_exports: 'PendingCloudwatchLogsExports' = pydantic.Field(None, alias="PendingCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    iam_database_authentication_enabled: BooleanOptional = pydantic.Field(None, alias="IAMDatabaseAuthenticationEnabled")
    automation_mode: AutomationMode = pydantic.Field(None, alias="AutomationMode")
    resume_full_automation_mode_time: 'TStamp' = pydantic.Field(None, alias="ResumeFullAutomationModeTime")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    engine: String = pydantic.Field(None, alias="Engine")

class ProcessorFeature(_RDSBase):
    name: String = pydantic.Field(None, alias="Name")
    value: String = pydantic.Field(None, alias="Value")

class PromoteReadReplicaDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")

class PromoteReadReplicaDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class PromoteReadReplicaMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")

class PromoteReadReplicaResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class PurchaseReservedDBInstancesOfferingMessage(_RDSBase):
    reserved_db_instances_offering_id: String = pydantic.Field(None, alias="ReservedDBInstancesOfferingId")
    reserved_db_instance_id: String = pydantic.Field(None, alias="ReservedDBInstanceId")
    db_instance_count: IntegerOptional = pydantic.Field(None, alias="DBInstanceCount")
    tags: TagList = pydantic.Field(None, alias="Tags")

class PurchaseReservedDBInstancesOfferingResult(_RDSBase):
    reserved_db_instance: 'ReservedDBInstance' = pydantic.Field(None, alias="ReservedDBInstance")

class Range(_RDSBase):
    from: Integer = pydantic.Field(None, alias="From")
    to: Integer = pydantic.Field(None, alias="To")
    step: IntegerOptional = pydantic.Field(None, alias="Step")

class RebootDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")

class RebootDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class RebootDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    force_failover: BooleanOptional = pydantic.Field(None, alias="ForceFailover")

class RebootDBInstanceResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class RecurringCharge(_RDSBase):
    recurring_charge_amount: Double = pydantic.Field(None, alias="RecurringChargeAmount")
    recurring_charge_frequency: String = pydantic.Field(None, alias="RecurringChargeFrequency")

class RegisterDBProxyTargetsRequest(_RDSBase):
    db_proxy_name: String = pydantic.Field(None, alias="DBProxyName")
    target_group_name: String = pydantic.Field(None, alias="TargetGroupName")
    db_instance_identifiers: StringList = pydantic.Field(None, alias="DBInstanceIdentifiers")
    db_cluster_identifiers: StringList = pydantic.Field(None, alias="DBClusterIdentifiers")

class RegisterDBProxyTargetsResponse(_RDSBase):
    db_proxy_targets: TargetList = pydantic.Field(None, alias="DBProxyTargets")

class RemoveFromGlobalClusterMessage(_RDSBase):
    global_cluster_identifier: String = pydantic.Field(None, alias="GlobalClusterIdentifier")
    db_cluster_identifier: String = pydantic.Field(None, alias="DbClusterIdentifier")

class RemoveFromGlobalClusterResult(_RDSBase):
    global_cluster: 'GlobalCluster' = pydantic.Field(None, alias="GlobalCluster")

class RemoveRoleFromDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    feature_name: String = pydantic.Field(None, alias="FeatureName")

class RemoveRoleFromDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    role_arn: String = pydantic.Field(None, alias="RoleArn")
    feature_name: String = pydantic.Field(None, alias="FeatureName")

class RemoveSourceIdentifierFromSubscriptionMessage(_RDSBase):
    subscription_name: String = pydantic.Field(None, alias="SubscriptionName")
    source_identifier: String = pydantic.Field(None, alias="SourceIdentifier")

class RemoveSourceIdentifierFromSubscriptionResult(_RDSBase):
    event_subscription: 'EventSubscription' = pydantic.Field(None, alias="EventSubscription")

class RemoveTagsFromResourceMessage(_RDSBase):
    resource_name: String = pydantic.Field(None, alias="ResourceName")
    tag_keys: KeyList = pydantic.Field(None, alias="TagKeys")

class ReservedDBInstance(_RDSBase):
    reserved_db_instance_id: String = pydantic.Field(None, alias="ReservedDBInstanceId")
    reserved_db_instances_offering_id: String = pydantic.Field(None, alias="ReservedDBInstancesOfferingId")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    start_time: 'TStamp' = pydantic.Field(None, alias="StartTime")
    duration: Integer = pydantic.Field(None, alias="Duration")
    fixed_price: Double = pydantic.Field(None, alias="FixedPrice")
    usage_price: Double = pydantic.Field(None, alias="UsagePrice")
    currency_code: String = pydantic.Field(None, alias="CurrencyCode")
    db_instance_count: Integer = pydantic.Field(None, alias="DBInstanceCount")
    product_description: String = pydantic.Field(None, alias="ProductDescription")
    offering_type: String = pydantic.Field(None, alias="OfferingType")
    multi_az: Boolean = pydantic.Field(None, alias="MultiAZ")
    state: String = pydantic.Field(None, alias="State")
    recurring_charges: RecurringChargeList = pydantic.Field(None, alias="RecurringCharges")
    reserved_db_instance_arn: String = pydantic.Field(None, alias="ReservedDBInstanceArn")
    lease_id: String = pydantic.Field(None, alias="LeaseId")

class ReservedDBInstanceMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    reserved_db_instances: ReservedDBInstanceList = pydantic.Field(None, alias="ReservedDBInstances")

class ReservedDBInstancesOffering(_RDSBase):
    reserved_db_instances_offering_id: String = pydantic.Field(None, alias="ReservedDBInstancesOfferingId")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    duration: Integer = pydantic.Field(None, alias="Duration")
    fixed_price: Double = pydantic.Field(None, alias="FixedPrice")
    usage_price: Double = pydantic.Field(None, alias="UsagePrice")
    currency_code: String = pydantic.Field(None, alias="CurrencyCode")
    product_description: String = pydantic.Field(None, alias="ProductDescription")
    offering_type: String = pydantic.Field(None, alias="OfferingType")
    multi_az: Boolean = pydantic.Field(None, alias="MultiAZ")
    recurring_charges: RecurringChargeList = pydantic.Field(None, alias="RecurringCharges")

class ReservedDBInstancesOfferingMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    reserved_db_instances_offerings: ReservedDBInstancesOfferingList = pydantic.Field(None, alias="ReservedDBInstancesOfferings")

class ResetDBClusterParameterGroupMessage(_RDSBase):
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    reset_all_parameters: Boolean = pydantic.Field(None, alias="ResetAllParameters")
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")

class ResetDBParameterGroupMessage(_RDSBase):
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    reset_all_parameters: Boolean = pydantic.Field(None, alias="ResetAllParameters")
    parameters: ParametersList = pydantic.Field(None, alias="Parameters")

class ResourcePendingMaintenanceActions(_RDSBase):
    resource_identifier: String = pydantic.Field(None, alias="ResourceIdentifier")
    pending_maintenance_action_details: PendingMaintenanceActionDetails = pydantic.Field(None, alias="PendingMaintenanceActionDetails")

class RestoreDBClusterFromS3Message(_RDSBase):
    availability_zones: AvailabilityZones = pydantic.Field(None, alias="AvailabilityZones")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    character_set_name: String = pydantic.Field(None, alias="CharacterSetName")
    database_name: String = pydantic.Field(None, alias="DatabaseName")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_encrypted: BooleanOptional = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    source_engine: String = pydantic.Field(None, alias="SourceEngine")
    source_engine_version: String = pydantic.Field(None, alias="SourceEngineVersion")
    s_3_bucket_name: String = pydantic.Field(None, alias="S3BucketName")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")
    s_3_ingestion_role_arn: String = pydantic.Field(None, alias="S3IngestionRoleArn")
    backtrack_window: LongOptional = pydantic.Field(None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    serverless_v_2_scaling_configuration: 'ServerlessV2ScalingConfiguration' = pydantic.Field(None, alias="ServerlessV2ScalingConfiguration")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    manage_master_user_password: BooleanOptional = pydantic.Field(None, alias="ManageMasterUserPassword")
    master_user_secret_kms_key_id: String = pydantic.Field(None, alias="MasterUserSecretKmsKeyId")
    storage_type: String = pydantic.Field(None, alias="StorageType")

class RestoreDBClusterFromS3Result(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class RestoreDBClusterFromSnapshotMessage(_RDSBase):
    availability_zones: AvailabilityZones = pydantic.Field(None, alias="AvailabilityZones")
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    snapshot_identifier: String = pydantic.Field(None, alias="SnapshotIdentifier")
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    database_name: String = pydantic.Field(None, alias="DatabaseName")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    tags: TagList = pydantic.Field(None, alias="Tags")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    backtrack_window: LongOptional = pydantic.Field(None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    engine_mode: String = pydantic.Field(None, alias="EngineMode")
    scaling_configuration: 'ScalingConfiguration' = pydantic.Field(None, alias="ScalingConfiguration")
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    db_cluster_instance_class: String = pydantic.Field(None, alias="DBClusterInstanceClass")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    serverless_v_2_scaling_configuration: 'ServerlessV2ScalingConfiguration' = pydantic.Field(None, alias="ServerlessV2ScalingConfiguration")
    network_type: String = pydantic.Field(None, alias="NetworkType")

class RestoreDBClusterFromSnapshotResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class RestoreDBClusterToPointInTimeMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")
    restore_type: String = pydantic.Field(None, alias="RestoreType")
    source_db_cluster_identifier: String = pydantic.Field(None, alias="SourceDBClusterIdentifier")
    restore_to_time: 'TStamp' = pydantic.Field(None, alias="RestoreToTime")
    use_latest_restorable_time: Boolean = pydantic.Field(None, alias="UseLatestRestorableTime")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    tags: TagList = pydantic.Field(None, alias="Tags")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    backtrack_window: LongOptional = pydantic.Field(None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    db_cluster_parameter_group_name: String = pydantic.Field(None, alias="DBClusterParameterGroupName")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    scaling_configuration: 'ScalingConfiguration' = pydantic.Field(None, alias="ScalingConfiguration")
    engine_mode: String = pydantic.Field(None, alias="EngineMode")
    db_cluster_instance_class: String = pydantic.Field(None, alias="DBClusterInstanceClass")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    serverless_v_2_scaling_configuration: 'ServerlessV2ScalingConfiguration' = pydantic.Field(None, alias="ServerlessV2ScalingConfiguration")
    network_type: String = pydantic.Field(None, alias="NetworkType")

class RestoreDBClusterToPointInTimeResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class RestoreDBInstanceFromDBSnapshotMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    db_name: String = pydantic.Field(None, alias="DBName")
    engine: String = pydantic.Field(None, alias="Engine")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    tde_credential_password: String = pydantic.Field(None, alias="TdeCredentialPassword")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    domain: String = pydantic.Field(None, alias="Domain")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    use_default_processor_features: BooleanOptional = pydantic.Field(None, alias="UseDefaultProcessorFeatures")
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    enable_customer_owned_ip: BooleanOptional = pydantic.Field(None, alias="EnableCustomerOwnedIp")
    custom_iam_instance_profile: String = pydantic.Field(None, alias="CustomIamInstanceProfile")
    backup_target: String = pydantic.Field(None, alias="BackupTarget")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    db_cluster_snapshot_identifier: String = pydantic.Field(None, alias="DBClusterSnapshotIdentifier")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")

class RestoreDBInstanceFromDBSnapshotResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class RestoreDBInstanceFromS3Message(_RDSBase):
    db_name: String = pydantic.Field(None, alias="DBName")
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    engine: String = pydantic.Field(None, alias="Engine")
    master_username: String = pydantic.Field(None, alias="MasterUsername")
    master_user_password: String = pydantic.Field(None, alias="MasterUserPassword")
    db_security_groups: DBSecurityGroupNameList = pydantic.Field(None, alias="DBSecurityGroups")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    preferred_maintenance_window: String = pydantic.Field(None, alias="PreferredMaintenanceWindow")
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    preferred_backup_window: String = pydantic.Field(None, alias="PreferredBackupWindow")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    storage_encrypted: BooleanOptional = pydantic.Field(None, alias="StorageEncrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    monitoring_interval: IntegerOptional = pydantic.Field(None, alias="MonitoringInterval")
    monitoring_role_arn: String = pydantic.Field(None, alias="MonitoringRoleArn")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    source_engine: String = pydantic.Field(None, alias="SourceEngine")
    source_engine_version: String = pydantic.Field(None, alias="SourceEngineVersion")
    s_3_bucket_name: String = pydantic.Field(None, alias="S3BucketName")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")
    s_3_ingestion_role_arn: String = pydantic.Field(None, alias="S3IngestionRoleArn")
    enable_performance_insights: BooleanOptional = pydantic.Field(None, alias="EnablePerformanceInsights")
    performance_insights_kms_key_id: String = pydantic.Field(None, alias="PerformanceInsightsKMSKeyId")
    performance_insights_retention_period: IntegerOptional = pydantic.Field(None, alias="PerformanceInsightsRetentionPeriod")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    use_default_processor_features: BooleanOptional = pydantic.Field(None, alias="UseDefaultProcessorFeatures")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    max_allocated_storage: IntegerOptional = pydantic.Field(None, alias="MaxAllocatedStorage")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    manage_master_user_password: BooleanOptional = pydantic.Field(None, alias="ManageMasterUserPassword")
    master_user_secret_kms_key_id: String = pydantic.Field(None, alias="MasterUserSecretKmsKeyId")

class RestoreDBInstanceFromS3Result(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class RestoreDBInstanceToPointInTimeMessage(_RDSBase):
    source_db_instance_identifier: String = pydantic.Field(None, alias="SourceDBInstanceIdentifier")
    target_db_instance_identifier: String = pydantic.Field(None, alias="TargetDBInstanceIdentifier")
    restore_time: 'TStamp' = pydantic.Field(None, alias="RestoreTime")
    use_latest_restorable_time: Boolean = pydantic.Field(None, alias="UseLatestRestorableTime")
    db_instance_class: String = pydantic.Field(None, alias="DBInstanceClass")
    port: IntegerOptional = pydantic.Field(None, alias="Port")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    db_subnet_group_name: String = pydantic.Field(None, alias="DBSubnetGroupName")
    multi_az: BooleanOptional = pydantic.Field(None, alias="MultiAZ")
    publicly_accessible: BooleanOptional = pydantic.Field(None, alias="PubliclyAccessible")
    auto_minor_version_upgrade: BooleanOptional = pydantic.Field(None, alias="AutoMinorVersionUpgrade")
    license_model: String = pydantic.Field(None, alias="LicenseModel")
    db_name: String = pydantic.Field(None, alias="DBName")
    engine: String = pydantic.Field(None, alias="Engine")
    iops: IntegerOptional = pydantic.Field(None, alias="Iops")
    option_group_name: String = pydantic.Field(None, alias="OptionGroupName")
    copy_tags_to_snapshot: BooleanOptional = pydantic.Field(None, alias="CopyTagsToSnapshot")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_type: String = pydantic.Field(None, alias="StorageType")
    tde_credential_arn: String = pydantic.Field(None, alias="TdeCredentialArn")
    tde_credential_password: String = pydantic.Field(None, alias="TdeCredentialPassword")
    vpc_security_group_ids: VpcSecurityGroupIdList = pydantic.Field(None, alias="VpcSecurityGroupIds")
    domain: String = pydantic.Field(None, alias="Domain")
    domain_iam_role_name: String = pydantic.Field(None, alias="DomainIAMRoleName")
    enable_iam_database_authentication: BooleanOptional = pydantic.Field(None, alias="EnableIAMDatabaseAuthentication")
    enable_cloudwatch_logs_exports: LogTypeList = pydantic.Field(None, alias="EnableCloudwatchLogsExports")
    processor_features: ProcessorFeatureList = pydantic.Field(None, alias="ProcessorFeatures")
    use_default_processor_features: BooleanOptional = pydantic.Field(None, alias="UseDefaultProcessorFeatures")
    db_parameter_group_name: String = pydantic.Field(None, alias="DBParameterGroupName")
    deletion_protection: BooleanOptional = pydantic.Field(None, alias="DeletionProtection")
    source_dbi_resource_id: String = pydantic.Field(None, alias="SourceDbiResourceId")
    max_allocated_storage: IntegerOptional = pydantic.Field(None, alias="MaxAllocatedStorage")
    source_db_instance_automated_backups_arn: String = pydantic.Field(None, alias="SourceDBInstanceAutomatedBackupsArn")
    enable_customer_owned_ip: BooleanOptional = pydantic.Field(None, alias="EnableCustomerOwnedIp")
    custom_iam_instance_profile: String = pydantic.Field(None, alias="CustomIamInstanceProfile")
    backup_target: String = pydantic.Field(None, alias="BackupTarget")
    network_type: String = pydantic.Field(None, alias="NetworkType")
    storage_throughput: IntegerOptional = pydantic.Field(None, alias="StorageThroughput")
    allocated_storage: IntegerOptional = pydantic.Field(None, alias="AllocatedStorage")

class RestoreDBInstanceToPointInTimeResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class RestoreWindow(_RDSBase):
    earliest_time: 'TStamp' = pydantic.Field(None, alias="EarliestTime")
    latest_time: 'TStamp' = pydantic.Field(None, alias="LatestTime")

class RevokeDBSecurityGroupIngressMessage(_RDSBase):
    db_security_group_name: String = pydantic.Field(None, alias="DBSecurityGroupName")
    cidrip: String = pydantic.Field(None, alias="CIDRIP")
    ec_2_security_group_name: String = pydantic.Field(None, alias="EC2SecurityGroupName")
    ec_2_security_group_id: String = pydantic.Field(None, alias="EC2SecurityGroupId")
    ec_2_security_group_owner_id: String = pydantic.Field(None, alias="EC2SecurityGroupOwnerId")

class RevokeDBSecurityGroupIngressResult(_RDSBase):
    db_security_group: 'DBSecurityGroup' = pydantic.Field(None, alias="DBSecurityGroup")

class ScalingConfiguration(_RDSBase):
    min_capacity: IntegerOptional = pydantic.Field(None, alias="MinCapacity")
    max_capacity: IntegerOptional = pydantic.Field(None, alias="MaxCapacity")
    auto_pause: BooleanOptional = pydantic.Field(None, alias="AutoPause")
    seconds_until_auto_pause: IntegerOptional = pydantic.Field(None, alias="SecondsUntilAutoPause")
    timeout_action: String = pydantic.Field(None, alias="TimeoutAction")
    seconds_before_timeout: IntegerOptional = pydantic.Field(None, alias="SecondsBeforeTimeout")

class ScalingConfigurationInfo(_RDSBase):
    min_capacity: IntegerOptional = pydantic.Field(None, alias="MinCapacity")
    max_capacity: IntegerOptional = pydantic.Field(None, alias="MaxCapacity")
    auto_pause: BooleanOptional = pydantic.Field(None, alias="AutoPause")
    seconds_until_auto_pause: IntegerOptional = pydantic.Field(None, alias="SecondsUntilAutoPause")
    timeout_action: String = pydantic.Field(None, alias="TimeoutAction")
    seconds_before_timeout: IntegerOptional = pydantic.Field(None, alias="SecondsBeforeTimeout")

class ServerlessV2ScalingConfiguration(_RDSBase):
    min_capacity: DoubleOptional = pydantic.Field(None, alias="MinCapacity")
    max_capacity: DoubleOptional = pydantic.Field(None, alias="MaxCapacity")

class ServerlessV2ScalingConfigurationInfo(_RDSBase):
    min_capacity: DoubleOptional = pydantic.Field(None, alias="MinCapacity")
    max_capacity: DoubleOptional = pydantic.Field(None, alias="MaxCapacity")

class SourceRegion(_RDSBase):
    region_name: String = pydantic.Field(None, alias="RegionName")
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    status: String = pydantic.Field(None, alias="Status")
    supports_db_instance_automated_backups_replication: Boolean = pydantic.Field(None, alias="SupportsDBInstanceAutomatedBackupsReplication")

class SourceRegionMessage(_RDSBase):
    marker: String = pydantic.Field(None, alias="Marker")
    source_regions: SourceRegionList = pydantic.Field(None, alias="SourceRegions")

class StartActivityStreamRequest(_RDSBase):
    resource_arn: String = pydantic.Field(None, alias="ResourceArn")
    mode: ActivityStreamMode = pydantic.Field(None, alias="Mode")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    apply_immediately: BooleanOptional = pydantic.Field(None, alias="ApplyImmediately")
    engine_native_audit_fields_included: BooleanOptional = pydantic.Field(None, alias="EngineNativeAuditFieldsIncluded")

class StartActivityStreamResponse(_RDSBase):
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    kinesis_stream_name: String = pydantic.Field(None, alias="KinesisStreamName")
    status: ActivityStreamStatus = pydantic.Field(None, alias="Status")
    mode: ActivityStreamMode = pydantic.Field(None, alias="Mode")
    apply_immediately: Boolean = pydantic.Field(None, alias="ApplyImmediately")
    engine_native_audit_fields_included: BooleanOptional = pydantic.Field(None, alias="EngineNativeAuditFieldsIncluded")

class StartDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")

class StartDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class StartDBInstanceAutomatedBackupsReplicationMessage(_RDSBase):
    source_db_instance_arn: String = pydantic.Field(None, alias="SourceDBInstanceArn")
    backup_retention_period: IntegerOptional = pydantic.Field(None, alias="BackupRetentionPeriod")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    pre_signed_url: String = pydantic.Field(None, alias="PreSignedUrl")

class StartDBInstanceAutomatedBackupsReplicationResult(_RDSBase):
    db_instance_automated_backup: 'DBInstanceAutomatedBackup' = pydantic.Field(None, alias="DBInstanceAutomatedBackup")

class StartDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")

class StartDBInstanceResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class StartExportTaskMessage(_RDSBase):
    export_task_identifier: String = pydantic.Field(None, alias="ExportTaskIdentifier")
    source_arn: String = pydantic.Field(None, alias="SourceArn")
    s_3_bucket_name: String = pydantic.Field(None, alias="S3BucketName")
    iam_role_arn: String = pydantic.Field(None, alias="IamRoleArn")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")
    export_only: StringList = pydantic.Field(None, alias="ExportOnly")

class StopActivityStreamRequest(_RDSBase):
    resource_arn: String = pydantic.Field(None, alias="ResourceArn")
    apply_immediately: BooleanOptional = pydantic.Field(None, alias="ApplyImmediately")

class StopActivityStreamResponse(_RDSBase):
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    kinesis_stream_name: String = pydantic.Field(None, alias="KinesisStreamName")
    status: ActivityStreamStatus = pydantic.Field(None, alias="Status")

class StopDBClusterMessage(_RDSBase):
    db_cluster_identifier: String = pydantic.Field(None, alias="DBClusterIdentifier")

class StopDBClusterResult(_RDSBase):
    db_cluster: 'DBCluster' = pydantic.Field(None, alias="DBCluster")

class StopDBInstanceAutomatedBackupsReplicationMessage(_RDSBase):
    source_db_instance_arn: String = pydantic.Field(None, alias="SourceDBInstanceArn")

class StopDBInstanceAutomatedBackupsReplicationResult(_RDSBase):
    db_instance_automated_backup: 'DBInstanceAutomatedBackup' = pydantic.Field(None, alias="DBInstanceAutomatedBackup")

class StopDBInstanceMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")
    db_snapshot_identifier: String = pydantic.Field(None, alias="DBSnapshotIdentifier")

class StopDBInstanceResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class Subnet(_RDSBase):
    subnet_identifier: String = pydantic.Field(None, alias="SubnetIdentifier")
    subnet_availability_zone: 'AvailabilityZone' = pydantic.Field(None, alias="SubnetAvailabilityZone")
    subnet_outpost: 'Outpost' = pydantic.Field(None, alias="SubnetOutpost")
    subnet_status: String = pydantic.Field(None, alias="SubnetStatus")

class SwitchoverBlueGreenDeploymentRequest(_RDSBase):
    blue_green_deployment_identifier: BlueGreenDeploymentIdentifier = pydantic.Field(None, alias="BlueGreenDeploymentIdentifier")
    switchover_timeout: SwitchoverTimeout = pydantic.Field(None, alias="SwitchoverTimeout")

class SwitchoverBlueGreenDeploymentResponse(_RDSBase):
    blue_green_deployment: 'BlueGreenDeployment' = pydantic.Field(None, alias="BlueGreenDeployment")

class SwitchoverDetail(_RDSBase):
    source_member: DatabaseArn = pydantic.Field(None, alias="SourceMember")
    target_member: DatabaseArn = pydantic.Field(None, alias="TargetMember")
    status: SwitchoverDetailStatus = pydantic.Field(None, alias="Status")

class SwitchoverReadReplicaMessage(_RDSBase):
    db_instance_identifier: String = pydantic.Field(None, alias="DBInstanceIdentifier")

class SwitchoverReadReplicaResult(_RDSBase):
    db_instance: 'DBInstance' = pydantic.Field(None, alias="DBInstance")

class Tag(_RDSBase):
    key: String = pydantic.Field(None, alias="Key")
    value: String = pydantic.Field(None, alias="Value")

class TagListMessage(_RDSBase):
    tag_list: TagList = pydantic.Field(None, alias="TagList")

class TargetHealth(_RDSBase):
    state: TargetState = pydantic.Field(None, alias="State")
    reason: TargetHealthReason = pydantic.Field(None, alias="Reason")
    description: String = pydantic.Field(None, alias="Description")

class Timezone(_RDSBase):
    timezone_name: String = pydantic.Field(None, alias="TimezoneName")

class UpgradeTarget(_RDSBase):
    engine: String = pydantic.Field(None, alias="Engine")
    engine_version: String = pydantic.Field(None, alias="EngineVersion")
    description: String = pydantic.Field(None, alias="Description")
    auto_upgrade: Boolean = pydantic.Field(None, alias="AutoUpgrade")
    is_major_version_upgrade: Boolean = pydantic.Field(None, alias="IsMajorVersionUpgrade")
    supported_engine_modes: EngineModeList = pydantic.Field(None, alias="SupportedEngineModes")
    supports_parallel_query: BooleanOptional = pydantic.Field(None, alias="SupportsParallelQuery")
    supports_global_databases: BooleanOptional = pydantic.Field(None, alias="SupportsGlobalDatabases")
    supports_babelfish: BooleanOptional = pydantic.Field(None, alias="SupportsBabelfish")

class UserAuthConfig(_RDSBase):
    description: String = pydantic.Field(None, alias="Description")
    user_name: String = pydantic.Field(None, alias="UserName")
    auth_scheme: AuthScheme = pydantic.Field(None, alias="AuthScheme")
    secret_arn: String = pydantic.Field(None, alias="SecretArn")
    iam_auth: IAMAuthMode = pydantic.Field(None, alias="IAMAuth")
    client_password_auth_type: ClientPasswordAuthType = pydantic.Field(None, alias="ClientPasswordAuthType")

class UserAuthConfigInfo(_RDSBase):
    description: String = pydantic.Field(None, alias="Description")
    user_name: String = pydantic.Field(None, alias="UserName")
    auth_scheme: AuthScheme = pydantic.Field(None, alias="AuthScheme")
    secret_arn: String = pydantic.Field(None, alias="SecretArn")
    iam_auth: IAMAuthMode = pydantic.Field(None, alias="IAMAuth")
    client_password_auth_type: ClientPasswordAuthType = pydantic.Field(None, alias="ClientPasswordAuthType")

class ValidDBInstanceModificationsMessage(_RDSBase):
    storage: ValidStorageOptionsList = pydantic.Field(None, alias="Storage")
    valid_processor_features: AvailableProcessorFeatureList = pydantic.Field(None, alias="ValidProcessorFeatures")

class ValidStorageOptions(_RDSBase):
    storage_type: String = pydantic.Field(None, alias="StorageType")
    storage_size: RangeList = pydantic.Field(None, alias="StorageSize")
    provisioned_iops: RangeList = pydantic.Field(None, alias="ProvisionedIops")
    iops_to_storage_ratio: DoubleRangeList = pydantic.Field(None, alias="IopsToStorageRatio")
    supports_storage_autoscaling: Boolean = pydantic.Field(None, alias="SupportsStorageAutoscaling")
    provisioned_storage_throughput: RangeList = pydantic.Field(None, alias="ProvisionedStorageThroughput")
    storage_throughput_to_iops_ratio: DoubleRangeList = pydantic.Field(None, alias="StorageThroughputToIopsRatio")

class VpcSecurityGroupMembership(_RDSBase):
    vpc_security_group_id: String = pydantic.Field(None, alias="VpcSecurityGroupId")
    status: String = pydantic.Field(None, alias="Status")

AccountAttributesMessage.update_forward_refs()
AccountQuota.update_forward_refs()
AddRoleToDBClusterMessage.update_forward_refs()
AddRoleToDBInstanceMessage.update_forward_refs()
AddSourceIdentifierToSubscriptionMessage.update_forward_refs()
AddSourceIdentifierToSubscriptionResult.update_forward_refs()
AddTagsToResourceMessage.update_forward_refs()
ApplyPendingMaintenanceActionMessage.update_forward_refs()
ApplyPendingMaintenanceActionResult.update_forward_refs()
AuthorizeDBSecurityGroupIngressMessage.update_forward_refs()
AuthorizeDBSecurityGroupIngressResult.update_forward_refs()
AvailabilityZone.update_forward_refs()
AvailableProcessorFeature.update_forward_refs()
BacktrackDBClusterMessage.update_forward_refs()
BlueGreenDeployment.update_forward_refs()
BlueGreenDeploymentTask.update_forward_refs()
CancelExportTaskMessage.update_forward_refs()
Certificate.update_forward_refs()
CertificateDetails.update_forward_refs()
CertificateMessage.update_forward_refs()
CharacterSet.update_forward_refs()
CloudwatchLogsExportConfiguration.update_forward_refs()
ClusterPendingModifiedValues.update_forward_refs()
ConnectionPoolConfiguration.update_forward_refs()
ConnectionPoolConfigurationInfo.update_forward_refs()
CopyDBClusterParameterGroupMessage.update_forward_refs()
CopyDBClusterParameterGroupResult.update_forward_refs()
CopyDBClusterSnapshotMessage.update_forward_refs()
CopyDBClusterSnapshotResult.update_forward_refs()
CopyDBParameterGroupMessage.update_forward_refs()
CopyDBParameterGroupResult.update_forward_refs()
CopyDBSnapshotMessage.update_forward_refs()
CopyDBSnapshotResult.update_forward_refs()
CopyOptionGroupMessage.update_forward_refs()
CopyOptionGroupResult.update_forward_refs()
CreateBlueGreenDeploymentRequest.update_forward_refs()
CreateBlueGreenDeploymentResponse.update_forward_refs()
CreateCustomDBEngineVersionMessage.update_forward_refs()
CreateDBClusterEndpointMessage.update_forward_refs()
CreateDBClusterMessage.update_forward_refs()
CreateDBClusterParameterGroupMessage.update_forward_refs()
CreateDBClusterParameterGroupResult.update_forward_refs()
CreateDBClusterResult.update_forward_refs()
CreateDBClusterSnapshotMessage.update_forward_refs()
CreateDBClusterSnapshotResult.update_forward_refs()
CreateDBInstanceMessage.update_forward_refs()
CreateDBInstanceReadReplicaMessage.update_forward_refs()
CreateDBInstanceReadReplicaResult.update_forward_refs()
CreateDBInstanceResult.update_forward_refs()
CreateDBParameterGroupMessage.update_forward_refs()
CreateDBParameterGroupResult.update_forward_refs()
CreateDBProxyEndpointRequest.update_forward_refs()
CreateDBProxyEndpointResponse.update_forward_refs()
CreateDBProxyRequest.update_forward_refs()
CreateDBProxyResponse.update_forward_refs()
CreateDBSecurityGroupMessage.update_forward_refs()
CreateDBSecurityGroupResult.update_forward_refs()
CreateDBSnapshotMessage.update_forward_refs()
CreateDBSnapshotResult.update_forward_refs()
CreateDBSubnetGroupMessage.update_forward_refs()
CreateDBSubnetGroupResult.update_forward_refs()
CreateEventSubscriptionMessage.update_forward_refs()
CreateEventSubscriptionResult.update_forward_refs()
CreateGlobalClusterMessage.update_forward_refs()
CreateGlobalClusterResult.update_forward_refs()
CreateOptionGroupMessage.update_forward_refs()
CreateOptionGroupResult.update_forward_refs()
CustomDBEngineVersionAMI.update_forward_refs()
DBCluster.update_forward_refs()
DBClusterBacktrack.update_forward_refs()
DBClusterBacktrackMessage.update_forward_refs()
DBClusterCapacityInfo.update_forward_refs()
DBClusterEndpoint.update_forward_refs()
DBClusterEndpointMessage.update_forward_refs()
DBClusterMember.update_forward_refs()
DBClusterMessage.update_forward_refs()
DBClusterOptionGroupStatus.update_forward_refs()
DBClusterParameterGroup.update_forward_refs()
DBClusterParameterGroupDetails.update_forward_refs()
DBClusterParameterGroupNameMessage.update_forward_refs()
DBClusterParameterGroupsMessage.update_forward_refs()
DBClusterRole.update_forward_refs()
DBClusterSnapshot.update_forward_refs()
DBClusterSnapshotAttribute.update_forward_refs()
DBClusterSnapshotAttributesResult.update_forward_refs()
DBClusterSnapshotMessage.update_forward_refs()
DBEngineVersion.update_forward_refs()
DBEngineVersionMessage.update_forward_refs()
DBInstance.update_forward_refs()
DBInstanceAutomatedBackup.update_forward_refs()
DBInstanceAutomatedBackupMessage.update_forward_refs()
DBInstanceAutomatedBackupsReplication.update_forward_refs()
DBInstanceMessage.update_forward_refs()
DBInstanceRole.update_forward_refs()
DBInstanceStatusInfo.update_forward_refs()
DBParameterGroup.update_forward_refs()
DBParameterGroupDetails.update_forward_refs()
DBParameterGroupNameMessage.update_forward_refs()
DBParameterGroupStatus.update_forward_refs()
DBParameterGroupsMessage.update_forward_refs()
DBProxy.update_forward_refs()
DBProxyEndpoint.update_forward_refs()
DBProxyTarget.update_forward_refs()
DBProxyTargetGroup.update_forward_refs()
DBSecurityGroup.update_forward_refs()
DBSecurityGroupMembership.update_forward_refs()
DBSecurityGroupMessage.update_forward_refs()
DBSnapshot.update_forward_refs()
DBSnapshotAttribute.update_forward_refs()
DBSnapshotAttributesResult.update_forward_refs()
DBSnapshotMessage.update_forward_refs()
DBSubnetGroup.update_forward_refs()
DBSubnetGroupMessage.update_forward_refs()
DeleteBlueGreenDeploymentRequest.update_forward_refs()
DeleteBlueGreenDeploymentResponse.update_forward_refs()
DeleteCustomDBEngineVersionMessage.update_forward_refs()
DeleteDBClusterEndpointMessage.update_forward_refs()
DeleteDBClusterMessage.update_forward_refs()
DeleteDBClusterParameterGroupMessage.update_forward_refs()
DeleteDBClusterResult.update_forward_refs()
DeleteDBClusterSnapshotMessage.update_forward_refs()
DeleteDBClusterSnapshotResult.update_forward_refs()
DeleteDBInstanceAutomatedBackupMessage.update_forward_refs()
DeleteDBInstanceAutomatedBackupResult.update_forward_refs()
DeleteDBInstanceMessage.update_forward_refs()
DeleteDBInstanceResult.update_forward_refs()
DeleteDBParameterGroupMessage.update_forward_refs()
DeleteDBProxyEndpointRequest.update_forward_refs()
DeleteDBProxyEndpointResponse.update_forward_refs()
DeleteDBProxyRequest.update_forward_refs()
DeleteDBProxyResponse.update_forward_refs()
DeleteDBSecurityGroupMessage.update_forward_refs()
DeleteDBSnapshotMessage.update_forward_refs()
DeleteDBSnapshotResult.update_forward_refs()
DeleteDBSubnetGroupMessage.update_forward_refs()
DeleteEventSubscriptionMessage.update_forward_refs()
DeleteEventSubscriptionResult.update_forward_refs()
DeleteGlobalClusterMessage.update_forward_refs()
DeleteGlobalClusterResult.update_forward_refs()
DeleteOptionGroupMessage.update_forward_refs()
DeregisterDBProxyTargetsRequest.update_forward_refs()
DeregisterDBProxyTargetsResponse.update_forward_refs()
DescribeAccountAttributesMessage.update_forward_refs()
DescribeBlueGreenDeploymentsRequest.update_forward_refs()
DescribeBlueGreenDeploymentsResponse.update_forward_refs()
DescribeCertificatesMessage.update_forward_refs()
DescribeDBClusterBacktracksMessage.update_forward_refs()
DescribeDBClusterEndpointsMessage.update_forward_refs()
DescribeDBClusterParameterGroupsMessage.update_forward_refs()
DescribeDBClusterParametersMessage.update_forward_refs()
DescribeDBClusterSnapshotAttributesMessage.update_forward_refs()
DescribeDBClusterSnapshotAttributesResult.update_forward_refs()
DescribeDBClusterSnapshotsMessage.update_forward_refs()
DescribeDBClustersMessage.update_forward_refs()
DescribeDBEngineVersionsMessage.update_forward_refs()
DescribeDBInstanceAutomatedBackupsMessage.update_forward_refs()
DescribeDBInstancesMessage.update_forward_refs()
DescribeDBLogFilesDetails.update_forward_refs()
DescribeDBLogFilesMessage.update_forward_refs()
DescribeDBLogFilesResponse.update_forward_refs()
DescribeDBParameterGroupsMessage.update_forward_refs()
DescribeDBParametersMessage.update_forward_refs()
DescribeDBProxiesRequest.update_forward_refs()
DescribeDBProxiesResponse.update_forward_refs()
DescribeDBProxyEndpointsRequest.update_forward_refs()
DescribeDBProxyEndpointsResponse.update_forward_refs()
DescribeDBProxyTargetGroupsRequest.update_forward_refs()
DescribeDBProxyTargetGroupsResponse.update_forward_refs()
DescribeDBProxyTargetsRequest.update_forward_refs()
DescribeDBProxyTargetsResponse.update_forward_refs()
DescribeDBSecurityGroupsMessage.update_forward_refs()
DescribeDBSnapshotAttributesMessage.update_forward_refs()
DescribeDBSnapshotAttributesResult.update_forward_refs()
DescribeDBSnapshotsMessage.update_forward_refs()
DescribeDBSubnetGroupsMessage.update_forward_refs()
DescribeEngineDefaultClusterParametersMessage.update_forward_refs()
DescribeEngineDefaultClusterParametersResult.update_forward_refs()
DescribeEngineDefaultParametersMessage.update_forward_refs()
DescribeEngineDefaultParametersResult.update_forward_refs()
DescribeEventCategoriesMessage.update_forward_refs()
DescribeEventSubscriptionsMessage.update_forward_refs()
DescribeEventsMessage.update_forward_refs()
DescribeExportTasksMessage.update_forward_refs()
DescribeGlobalClustersMessage.update_forward_refs()
DescribeOptionGroupOptionsMessage.update_forward_refs()
DescribeOptionGroupsMessage.update_forward_refs()
DescribeOrderableDBInstanceOptionsMessage.update_forward_refs()
DescribePendingMaintenanceActionsMessage.update_forward_refs()
DescribeReservedDBInstancesMessage.update_forward_refs()
DescribeReservedDBInstancesOfferingsMessage.update_forward_refs()
DescribeSourceRegionsMessage.update_forward_refs()
DescribeValidDBInstanceModificationsMessage.update_forward_refs()
DescribeValidDBInstanceModificationsResult.update_forward_refs()
DomainMembership.update_forward_refs()
DoubleRange.update_forward_refs()
DownloadDBLogFilePortionDetails.update_forward_refs()
DownloadDBLogFilePortionMessage.update_forward_refs()
EC2SecurityGroup.update_forward_refs()
Endpoint.update_forward_refs()
EngineDefaults.update_forward_refs()
Event.update_forward_refs()
EventCategoriesMap.update_forward_refs()
EventCategoriesMessage.update_forward_refs()
EventSubscription.update_forward_refs()
EventSubscriptionsMessage.update_forward_refs()
EventsMessage.update_forward_refs()
ExportTask.update_forward_refs()
ExportTasksMessage.update_forward_refs()
FailoverDBClusterMessage.update_forward_refs()
FailoverDBClusterResult.update_forward_refs()
FailoverGlobalClusterMessage.update_forward_refs()
FailoverGlobalClusterResult.update_forward_refs()
FailoverState.update_forward_refs()
Filter.update_forward_refs()
GlobalCluster.update_forward_refs()
GlobalClusterMember.update_forward_refs()
GlobalClustersMessage.update_forward_refs()
IPRange.update_forward_refs()
ListTagsForResourceMessage.update_forward_refs()
MasterUserSecret.update_forward_refs()
MinimumEngineVersionPerAllowedValue.update_forward_refs()
ModifyActivityStreamRequest.update_forward_refs()
ModifyActivityStreamResponse.update_forward_refs()
ModifyCertificatesMessage.update_forward_refs()
ModifyCertificatesResult.update_forward_refs()
ModifyCurrentDBClusterCapacityMessage.update_forward_refs()
ModifyCustomDBEngineVersionMessage.update_forward_refs()
ModifyDBClusterEndpointMessage.update_forward_refs()
ModifyDBClusterMessage.update_forward_refs()
ModifyDBClusterParameterGroupMessage.update_forward_refs()
ModifyDBClusterResult.update_forward_refs()
ModifyDBClusterSnapshotAttributeMessage.update_forward_refs()
ModifyDBClusterSnapshotAttributeResult.update_forward_refs()
ModifyDBInstanceMessage.update_forward_refs()
ModifyDBInstanceResult.update_forward_refs()
ModifyDBParameterGroupMessage.update_forward_refs()
ModifyDBProxyEndpointRequest.update_forward_refs()
ModifyDBProxyEndpointResponse.update_forward_refs()
ModifyDBProxyRequest.update_forward_refs()
ModifyDBProxyResponse.update_forward_refs()
ModifyDBProxyTargetGroupRequest.update_forward_refs()
ModifyDBProxyTargetGroupResponse.update_forward_refs()
ModifyDBSnapshotAttributeMessage.update_forward_refs()
ModifyDBSnapshotAttributeResult.update_forward_refs()
ModifyDBSnapshotMessage.update_forward_refs()
ModifyDBSnapshotResult.update_forward_refs()
ModifyDBSubnetGroupMessage.update_forward_refs()
ModifyDBSubnetGroupResult.update_forward_refs()
ModifyEventSubscriptionMessage.update_forward_refs()
ModifyEventSubscriptionResult.update_forward_refs()
ModifyGlobalClusterMessage.update_forward_refs()
ModifyGlobalClusterResult.update_forward_refs()
ModifyOptionGroupMessage.update_forward_refs()
ModifyOptionGroupResult.update_forward_refs()
Option.update_forward_refs()
OptionConfiguration.update_forward_refs()
OptionGroup.update_forward_refs()
OptionGroupMembership.update_forward_refs()
OptionGroupOption.update_forward_refs()
OptionGroupOptionSetting.update_forward_refs()
OptionGroupOptionsMessage.update_forward_refs()
OptionGroups.update_forward_refs()
OptionSetting.update_forward_refs()
OptionVersion.update_forward_refs()
OrderableDBInstanceOption.update_forward_refs()
OrderableDBInstanceOptionsMessage.update_forward_refs()
Outpost.update_forward_refs()
Parameter.update_forward_refs()
PendingCloudwatchLogsExports.update_forward_refs()
PendingMaintenanceAction.update_forward_refs()
PendingMaintenanceActionsMessage.update_forward_refs()
PendingModifiedValues.update_forward_refs()
ProcessorFeature.update_forward_refs()
PromoteReadReplicaDBClusterMessage.update_forward_refs()
PromoteReadReplicaDBClusterResult.update_forward_refs()
PromoteReadReplicaMessage.update_forward_refs()
PromoteReadReplicaResult.update_forward_refs()
PurchaseReservedDBInstancesOfferingMessage.update_forward_refs()
PurchaseReservedDBInstancesOfferingResult.update_forward_refs()
Range.update_forward_refs()
RebootDBClusterMessage.update_forward_refs()
RebootDBClusterResult.update_forward_refs()
RebootDBInstanceMessage.update_forward_refs()
RebootDBInstanceResult.update_forward_refs()
RecurringCharge.update_forward_refs()
RegisterDBProxyTargetsRequest.update_forward_refs()
RegisterDBProxyTargetsResponse.update_forward_refs()
RemoveFromGlobalClusterMessage.update_forward_refs()
RemoveFromGlobalClusterResult.update_forward_refs()
RemoveRoleFromDBClusterMessage.update_forward_refs()
RemoveRoleFromDBInstanceMessage.update_forward_refs()
RemoveSourceIdentifierFromSubscriptionMessage.update_forward_refs()
RemoveSourceIdentifierFromSubscriptionResult.update_forward_refs()
RemoveTagsFromResourceMessage.update_forward_refs()
ReservedDBInstance.update_forward_refs()
ReservedDBInstanceMessage.update_forward_refs()
ReservedDBInstancesOffering.update_forward_refs()
ReservedDBInstancesOfferingMessage.update_forward_refs()
ResetDBClusterParameterGroupMessage.update_forward_refs()
ResetDBParameterGroupMessage.update_forward_refs()
ResourcePendingMaintenanceActions.update_forward_refs()
RestoreDBClusterFromS3Message.update_forward_refs()
RestoreDBClusterFromS3Result.update_forward_refs()
RestoreDBClusterFromSnapshotMessage.update_forward_refs()
RestoreDBClusterFromSnapshotResult.update_forward_refs()
RestoreDBClusterToPointInTimeMessage.update_forward_refs()
RestoreDBClusterToPointInTimeResult.update_forward_refs()
RestoreDBInstanceFromDBSnapshotMessage.update_forward_refs()
RestoreDBInstanceFromDBSnapshotResult.update_forward_refs()
RestoreDBInstanceFromS3Message.update_forward_refs()
RestoreDBInstanceFromS3Result.update_forward_refs()
RestoreDBInstanceToPointInTimeMessage.update_forward_refs()
RestoreDBInstanceToPointInTimeResult.update_forward_refs()
RestoreWindow.update_forward_refs()
RevokeDBSecurityGroupIngressMessage.update_forward_refs()
RevokeDBSecurityGroupIngressResult.update_forward_refs()
ScalingConfiguration.update_forward_refs()
ScalingConfigurationInfo.update_forward_refs()
ServerlessV2ScalingConfiguration.update_forward_refs()
ServerlessV2ScalingConfigurationInfo.update_forward_refs()
SourceRegion.update_forward_refs()
SourceRegionMessage.update_forward_refs()
StartActivityStreamRequest.update_forward_refs()
StartActivityStreamResponse.update_forward_refs()
StartDBClusterMessage.update_forward_refs()
StartDBClusterResult.update_forward_refs()
StartDBInstanceAutomatedBackupsReplicationMessage.update_forward_refs()
StartDBInstanceAutomatedBackupsReplicationResult.update_forward_refs()
StartDBInstanceMessage.update_forward_refs()
StartDBInstanceResult.update_forward_refs()
StartExportTaskMessage.update_forward_refs()
StopActivityStreamRequest.update_forward_refs()
StopActivityStreamResponse.update_forward_refs()
StopDBClusterMessage.update_forward_refs()
StopDBClusterResult.update_forward_refs()
StopDBInstanceAutomatedBackupsReplicationMessage.update_forward_refs()
StopDBInstanceAutomatedBackupsReplicationResult.update_forward_refs()
StopDBInstanceMessage.update_forward_refs()
StopDBInstanceResult.update_forward_refs()
Subnet.update_forward_refs()
SwitchoverBlueGreenDeploymentRequest.update_forward_refs()
SwitchoverBlueGreenDeploymentResponse.update_forward_refs()
SwitchoverDetail.update_forward_refs()
SwitchoverReadReplicaMessage.update_forward_refs()
SwitchoverReadReplicaResult.update_forward_refs()
Tag.update_forward_refs()
TagListMessage.update_forward_refs()
TargetHealth.update_forward_refs()
Timezone.update_forward_refs()
UpgradeTarget.update_forward_refs()
UserAuthConfig.update_forward_refs()
UserAuthConfigInfo.update_forward_refs()
ValidDBInstanceModificationsMessage.update_forward_refs()
ValidStorageOptions.update_forward_refs()
VpcSecurityGroupMembership.update_forward_refs()
