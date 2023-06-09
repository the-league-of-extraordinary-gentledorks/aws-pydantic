from datetime import datetime
import typing
import enum

import pydantic


class _CloudWatchModelBase(
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


AccountId: str = pydantic.constr(min_length=1, max_length=255)
ActionPrefix: str = pydantic.constr(min_length=1, max_length=1024)
ActionsEnabled: bool = pydantic.conbool()
ActionsSuppressedBy: str = pydantic.constr()
ActionsSuppressedReason: str = pydantic.constr(max_length=1024)
AlarmArn: str = pydantic.constr(min_length=1, max_length=1600)
AlarmDescription: str = pydantic.constr(max_length=1024)
AlarmName: str = pydantic.constr(min_length=1, max_length=255)
AlarmNamePrefix: str = pydantic.constr(min_length=1, max_length=255)
AlarmRule: str = pydantic.constr(min_length=1, max_length=10240)
AlarmType: str = pydantic.constr()
AmazonResourceName: str = pydantic.constr(min_length=1, max_length=1024)
AnomalyDetectorMetricStat: str = pydantic.constr(
    max_length=50,
    regex=r"(SampleCount|Average|Sum|Minimum|Maximum|IQM|(p|tc|tm|ts|wm)(\d{1,2}(\.\d{0,10})?|100)|[ou]\d+(\.\d*)?)(_E|_L|_H)?|(TM|TC|TS|WM)\(((((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?:((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%|((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%:(((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?)\)|(TM|TC|TS|WM|PR)\(((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)):((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?|((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?:(\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))\)",
)
AnomalyDetectorMetricTimezone: str = pydantic.constr(max_length=50, regex=r".*")
AnomalyDetectorStateValue: str = pydantic.constr()
AnomalyDetectorType: str = pydantic.constr()
AwsQueryErrorMessage: str = pydantic.constr()
ComparisonOperator: str = pydantic.constr()
DashboardArn: str = pydantic.constr()
DashboardBody: str = pydantic.constr()
DashboardErrorMessage: str = pydantic.constr()
DashboardName: str = pydantic.constr()
DashboardNamePrefix: str = pydantic.constr()
DataPath: str = pydantic.constr()
DatapointValue: float = pydantic.confloat()
DatapointValueMap: dict = pydantic.condict()
DatapointsToAlarm: int = pydantic.conint(ge=1)
DimensionName: str = pydantic.constr(min_length=1, max_length=255)
DimensionValue: str = pydantic.constr(min_length=1, max_length=1024)
ErrorMessage: str = pydantic.constr(min_length=1, max_length=255)
EvaluateLowSampleCountPercentile: str = pydantic.constr(min_length=1, max_length=255)
EvaluationPeriods: int = pydantic.conint(ge=1)
EvaluationState: str = pydantic.constr()
ExceptionType: str = pydantic.constr()
ExtendedStatistic: str = pydantic.constr()
FailureCode: str = pydantic.constr()
FailureDescription: str = pydantic.constr()
FailureResource: str = pydantic.constr()
FaultDescription: str = pydantic.constr()
GetMetricDataLabelTimezone: str = pydantic.constr()
GetMetricDataMaxDatapoints: int = pydantic.conint()
HistoryData: str = pydantic.constr(min_length=1, max_length=4095)
HistoryItemType: str = pydantic.constr()
HistorySummary: str = pydantic.constr(min_length=1, max_length=255)
IncludeLinkedAccounts: bool = pydantic.conbool()
IncludeLinkedAccountsMetrics: bool = pydantic.conbool()
InsightRuleAggregationStatistic: str = pydantic.constr()
InsightRuleContributorKey: str = pydantic.constr()
InsightRuleContributorKeyLabel: str = pydantic.constr()
InsightRuleDefinition: str = pydantic.constr(
    min_length=1, max_length=8192, regex=r"[\x00-\x7F]+"
)
InsightRuleIsManaged: bool = pydantic.conbool()
InsightRuleMaxResults: int = pydantic.conint(ge=1, le=500)
InsightRuleMetricName: str = pydantic.constr(
    min_length=1, max_length=32, regex=r"[\x20-\x7E]+"
)
InsightRuleName: str = pydantic.constr(
    min_length=1, max_length=128, regex=r"[\x20-\x7E]+"
)
InsightRuleOrderBy: str = pydantic.constr(
    min_length=1, max_length=32, regex=r"[\x20-\x7E]+"
)
InsightRuleSchema: str = pydantic.constr()
InsightRuleState: str = pydantic.constr(
    min_length=1, max_length=32, regex=r"[\x20-\x7E]+"
)
InsightRuleUnboundDouble: float = pydantic.confloat()
InsightRuleUnboundInteger: int = pydantic.conint()
InsightRuleUnboundLong: int = pydantic.conint()
LastModified: datetime = pydantic.condate()
ListMetricStreamsMaxResults: int = pydantic.conint(ge=1, le=500)
MaxRecords: int = pydantic.conint(ge=1, le=100)
MaxReturnedResultsCount: int = pydantic.conint(ge=1)
Message: str = pydantic.constr()
MessageDataCode: str = pydantic.constr()
MessageDataValue: str = pydantic.constr()
MetricExpression: str = pydantic.constr(min_length=1, max_length=2048)
MetricId: str = pydantic.constr(min_length=1, max_length=255)
MetricLabel: str = pydantic.constr()
MetricName: str = pydantic.constr(min_length=1, max_length=255)
MetricStreamName: str = pydantic.constr(min_length=1, max_length=255)
MetricStreamOutputFormat: str = pydantic.constr(min_length=1, max_length=255)
MetricStreamState: str = pydantic.constr()
MetricStreamStatistic: str = pydantic.constr()
MetricWidget: str = pydantic.constr()
MetricWidgetImage: bytes = pydantic.conbytes()
Namespace: str = pydantic.constr(min_length=1, max_length=255, regex=r"[^:].*")
NextToken: str = pydantic.constr()
OutputFormat: str = pydantic.constr()
Period: int = pydantic.conint(ge=1)
RecentlyActive: str = pydantic.constr()
ResourceId: str = pydantic.constr()
ResourceName: str = pydantic.constr(min_length=1, max_length=1024)
ResourceType: str = pydantic.constr()
ReturnData: bool = pydantic.conbool()
ScanBy: str = pydantic.constr()
Size: int = pydantic.conint()
StandardUnit: str = pydantic.constr()
Stat: str = pydantic.constr()
StateReason: str = pydantic.constr(max_length=1023)
StateReasonData: str = pydantic.constr(max_length=4000)
StateValue: str = pydantic.constr()
Statistic: str = pydantic.constr()
StatusCode: str = pydantic.constr()
StorageResolution: int = pydantic.conint(ge=1)
SuppressorPeriod: int = pydantic.conint()
TagKey: str = pydantic.constr(min_length=1, max_length=128)
TagValue: str = pydantic.constr(max_length=256)
TemplateName: str = pydantic.constr(
    min_length=1,
    max_length=128,
    regex=r"[0-9A-Za-z][\-\.\_0-9A-Za-z]{0,126}[0-9A-Za-z]",
)
Threshold: float = pydantic.confloat()
Timestamp: datetime = pydantic.condate()
TreatMissingData: str = pydantic.constr(min_length=1, max_length=255)

AlarmHistoryItems = typing.List["AlarmHistoryItem"]
AlarmNames = typing.List["AlarmName"]
AlarmTypes = typing.List["AlarmType"]
AnomalyDetectorExcludedTimeRanges = typing.List["Range"]
AnomalyDetectorTypes = typing.List["AnomalyDetectorType"]
AnomalyDetectors = typing.List["AnomalyDetector"]
BatchFailures = typing.List["PartialFailure"]
CompositeAlarms = typing.List["CompositeAlarm"]
Counts = typing.List["DatapointValue"]
DashboardEntries = typing.List["DashboardEntry"]
DashboardNames = typing.List["DashboardName"]
DashboardValidationMessages = typing.List["DashboardValidationMessage"]
DatapointValues = typing.List["DatapointValue"]
Datapoints = typing.List["Datapoint"]
DimensionFilters = typing.List["DimensionFilter"]
Dimensions = typing.List["Dimension"]
ExtendedStatistics = typing.List["ExtendedStatistic"]
InsightRuleContributorDatapoints = typing.List["InsightRuleContributorDatapoint"]
InsightRuleContributorKeyLabels = typing.List["InsightRuleContributorKeyLabel"]
InsightRuleContributorKeys = typing.List["InsightRuleContributorKey"]
InsightRuleContributors = typing.List["InsightRuleContributor"]
InsightRuleMetricDatapoints = typing.List["InsightRuleMetricDatapoint"]
InsightRuleMetricList = typing.List["InsightRuleMetricName"]
InsightRuleNames = typing.List["InsightRuleName"]
InsightRules = typing.List["InsightRule"]
ManagedRuleDescriptions = typing.List["ManagedRuleDescription"]
ManagedRules = typing.List["ManagedRule"]
MetricAlarms = typing.List["MetricAlarm"]
MetricData = typing.List["MetricDatum"]
MetricDataQueries = typing.List["MetricDataQuery"]
MetricDataResultMessages = typing.List["MessageData"]
MetricDataResults = typing.List["MetricDataResult"]
MetricStreamEntries = typing.List["MetricStreamEntry"]
MetricStreamFilterMetricNames = typing.List["MetricName"]
MetricStreamFilters = typing.List["MetricStreamFilter"]
MetricStreamNames = typing.List["MetricStreamName"]
MetricStreamStatisticsAdditionalStatistics = typing.List["MetricStreamStatistic"]
MetricStreamStatisticsConfigurations = typing.List[
    "MetricStreamStatisticsConfiguration"
]
MetricStreamStatisticsIncludeMetrics = typing.List["MetricStreamStatisticsMetric"]
Metrics = typing.List["Metric"]
OwningAccounts = typing.List["AccountId"]
ResourceList = typing.List["ResourceName"]
Statistics = typing.List["Statistic"]
TagKeyList = typing.List["TagKey"]
TagList = typing.List["Tag"]
Timestamps = typing.List["Timestamp"]
Values = typing.List["DatapointValue"]


class ActionsSuppressedBy(enum.Enum):
    WAITPERIOD = "WaitPeriod"
    EXTENSIONPERIOD = "ExtensionPeriod"
    ALARM = "Alarm"


class AlarmType(enum.Enum):
    COMPOSITEALARM = "CompositeAlarm"
    METRICALARM = "MetricAlarm"


class AnomalyDetectorStateValue(enum.Enum):
    PENDING_TRAINING = "PENDING_TRAINING"
    TRAINED_INSUFFICIENT_DATA = "TRAINED_INSUFFICIENT_DATA"
    TRAINED = "TRAINED"


class AnomalyDetectorType(enum.Enum):
    SINGLE_METRIC = "SINGLE_METRIC"
    METRIC_MATH = "METRIC_MATH"


class ComparisonOperator(enum.Enum):
    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"
    LESSTHANLOWERORGREATERTHANUPPERTHRESHOLD = (
        "LessThanLowerOrGreaterThanUpperThreshold"
    )
    LESSTHANLOWERTHRESHOLD = "LessThanLowerThreshold"
    GREATERTHANUPPERTHRESHOLD = "GreaterThanUpperThreshold"


class EvaluationState(enum.Enum):
    PARTIAL_DATA = "PARTIAL_DATA"


class HistoryItemType(enum.Enum):
    CONFIGURATIONUPDATE = "ConfigurationUpdate"
    STATEUPDATE = "StateUpdate"
    ACTION = "Action"


class MetricStreamOutputFormat(enum.Enum):
    JSON = "json"
    OPENTELEMETRY0_7 = "opentelemetry0.7"


class RecentlyActive(enum.Enum):
    PT3H = "PT3H"


class ScanBy(enum.Enum):
    TIMESTAMPDESCENDING = "TimestampDescending"
    TIMESTAMPASCENDING = "TimestampAscending"


class StandardUnit(enum.Enum):
    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


class StateValue(enum.Enum):
    OK = "OK"
    ALARM = "ALARM"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class Statistic(enum.Enum):
    SAMPLECOUNT = "SampleCount"
    AVERAGE = "Average"
    SUM = "Sum"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"


class StatusCode(enum.Enum):
    COMPLETE = "Complete"
    INTERNALERROR = "InternalError"
    PARTIALDATA = "PartialData"
    FORBIDDEN = "Forbidden"


class AlarmHistoryItem(_CloudWatchModelBase):
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    alarm_type: AlarmType = pydantic.Field(None, alias="AlarmType")
    timestamp: Timestamp = pydantic.Field(None, alias="Timestamp")
    history_item_type: HistoryItemType = pydantic.Field(None, alias="HistoryItemType")
    history_summary: HistorySummary = pydantic.Field(None, alias="HistorySummary")
    history_data: HistoryData = pydantic.Field(None, alias="HistoryData")


class AnomalyDetector(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    stat: AnomalyDetectorMetricStat = pydantic.Field(None, alias="Stat")
    configuration: "AnomalyDetectorConfiguration" = pydantic.Field(
        None, alias="Configuration"
    )
    state_value: AnomalyDetectorStateValue = pydantic.Field(None, alias="StateValue")
    single_metric_anomaly_detector: "SingleMetricAnomalyDetector" = pydantic.Field(
        None, alias="SingleMetricAnomalyDetector"
    )
    metric_math_anomaly_detector: "MetricMathAnomalyDetector" = pydantic.Field(
        None, alias="MetricMathAnomalyDetector"
    )


class AnomalyDetectorConfiguration(_CloudWatchModelBase):
    excluded_time_ranges: AnomalyDetectorExcludedTimeRanges = pydantic.Field(
        None, alias="ExcludedTimeRanges"
    )
    metric_timezone: AnomalyDetectorMetricTimezone = pydantic.Field(
        None, alias="MetricTimezone"
    )


class CompositeAlarm(_CloudWatchModelBase):
    actions_enabled: ActionsEnabled = pydantic.Field(None, alias="ActionsEnabled")
    alarm_actions: ResourceList = pydantic.Field(None, alias="AlarmActions")
    alarm_arn: AlarmArn = pydantic.Field(None, alias="AlarmArn")
    alarm_configuration_updated_timestamp: Timestamp = pydantic.Field(
        None, alias="AlarmConfigurationUpdatedTimestamp"
    )
    alarm_description: AlarmDescription = pydantic.Field(None, alias="AlarmDescription")
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    alarm_rule: AlarmRule = pydantic.Field(None, alias="AlarmRule")
    insufficient_data_actions: ResourceList = pydantic.Field(
        None, alias="InsufficientDataActions"
    )
    ok_actions: ResourceList = pydantic.Field(None, alias="OKActions")
    state_reason: StateReason = pydantic.Field(None, alias="StateReason")
    state_reason_data: StateReasonData = pydantic.Field(None, alias="StateReasonData")
    state_updated_timestamp: Timestamp = pydantic.Field(
        None, alias="StateUpdatedTimestamp"
    )
    state_value: StateValue = pydantic.Field(None, alias="StateValue")
    state_transitioned_timestamp: Timestamp = pydantic.Field(
        None, alias="StateTransitionedTimestamp"
    )
    actions_suppressed_by: ActionsSuppressedBy = pydantic.Field(
        None, alias="ActionsSuppressedBy"
    )
    actions_suppressed_reason: ActionsSuppressedReason = pydantic.Field(
        None, alias="ActionsSuppressedReason"
    )
    actions_suppressor: AlarmArn = pydantic.Field(None, alias="ActionsSuppressor")
    actions_suppressor_wait_period: SuppressorPeriod = pydantic.Field(
        None, alias="ActionsSuppressorWaitPeriod"
    )
    actions_suppressor_extension_period: SuppressorPeriod = pydantic.Field(
        None, alias="ActionsSuppressorExtensionPeriod"
    )


class DashboardEntry(_CloudWatchModelBase):
    dashboard_name: DashboardName = pydantic.Field(None, alias="DashboardName")
    dashboard_arn: DashboardArn = pydantic.Field(None, alias="DashboardArn")
    last_modified: LastModified = pydantic.Field(None, alias="LastModified")
    size: Size = pydantic.Field(None, alias="Size")


class DashboardValidationMessage(_CloudWatchModelBase):
    data_path: DataPath = pydantic.Field(None, alias="DataPath")
    message: Message = pydantic.Field(None, alias="Message")


class Datapoint(_CloudWatchModelBase):
    timestamp: Timestamp = pydantic.Field(None, alias="Timestamp")
    sample_count: DatapointValue = pydantic.Field(None, alias="SampleCount")
    average: DatapointValue = pydantic.Field(None, alias="Average")
    sum: DatapointValue = pydantic.Field(None, alias="Sum")
    minimum: DatapointValue = pydantic.Field(None, alias="Minimum")
    maximum: DatapointValue = pydantic.Field(None, alias="Maximum")
    unit: StandardUnit = pydantic.Field(None, alias="Unit")
    extended_statistics: DatapointValueMap = pydantic.Field(
        None, alias="ExtendedStatistics"
    )


class DeleteAlarmsInput(_CloudWatchModelBase):
    alarm_names: AlarmNames = pydantic.Field(None, alias="AlarmNames")


class DeleteAnomalyDetectorInput(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    stat: AnomalyDetectorMetricStat = pydantic.Field(None, alias="Stat")
    single_metric_anomaly_detector: "SingleMetricAnomalyDetector" = pydantic.Field(
        None, alias="SingleMetricAnomalyDetector"
    )
    metric_math_anomaly_detector: "MetricMathAnomalyDetector" = pydantic.Field(
        None, alias="MetricMathAnomalyDetector"
    )


class DeleteAnomalyDetectorOutput(_CloudWatchModelBase):
    pass


class DeleteDashboardsInput(_CloudWatchModelBase):
    dashboard_names: DashboardNames = pydantic.Field(None, alias="DashboardNames")


class DeleteDashboardsOutput(_CloudWatchModelBase):
    pass


class DeleteInsightRulesInput(_CloudWatchModelBase):
    rule_names: InsightRuleNames = pydantic.Field(None, alias="RuleNames")


class DeleteInsightRulesOutput(_CloudWatchModelBase):
    failures: BatchFailures = pydantic.Field(None, alias="Failures")


class DeleteMetricStreamInput(_CloudWatchModelBase):
    name: MetricStreamName = pydantic.Field(None, alias="Name")


class DeleteMetricStreamOutput(_CloudWatchModelBase):
    pass


class DescribeAlarmHistoryInput(_CloudWatchModelBase):
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    alarm_types: AlarmTypes = pydantic.Field(None, alias="AlarmTypes")
    history_item_type: HistoryItemType = pydantic.Field(None, alias="HistoryItemType")
    start_date: Timestamp = pydantic.Field(None, alias="StartDate")
    end_date: Timestamp = pydantic.Field(None, alias="EndDate")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    scan_by: ScanBy = pydantic.Field(None, alias="ScanBy")


class DescribeAlarmHistoryOutput(_CloudWatchModelBase):
    alarm_history_items: AlarmHistoryItems = pydantic.Field(
        None, alias="AlarmHistoryItems"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAlarmsForMetricInput(_CloudWatchModelBase):
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    statistic: Statistic = pydantic.Field(None, alias="Statistic")
    extended_statistic: ExtendedStatistic = pydantic.Field(
        None, alias="ExtendedStatistic"
    )
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    period: Period = pydantic.Field(None, alias="Period")
    unit: StandardUnit = pydantic.Field(None, alias="Unit")


class DescribeAlarmsForMetricOutput(_CloudWatchModelBase):
    metric_alarms: MetricAlarms = pydantic.Field(None, alias="MetricAlarms")


class DescribeAlarmsInput(_CloudWatchModelBase):
    alarm_names: AlarmNames = pydantic.Field(None, alias="AlarmNames")
    alarm_name_prefix: AlarmNamePrefix = pydantic.Field(None, alias="AlarmNamePrefix")
    alarm_types: AlarmTypes = pydantic.Field(None, alias="AlarmTypes")
    children_of_alarm_name: AlarmName = pydantic.Field(
        None, alias="ChildrenOfAlarmName"
    )
    parents_of_alarm_name: AlarmName = pydantic.Field(None, alias="ParentsOfAlarmName")
    state_value: StateValue = pydantic.Field(None, alias="StateValue")
    action_prefix: ActionPrefix = pydantic.Field(None, alias="ActionPrefix")
    max_records: MaxRecords = pydantic.Field(None, alias="MaxRecords")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAlarmsOutput(_CloudWatchModelBase):
    composite_alarms: CompositeAlarms = pydantic.Field(None, alias="CompositeAlarms")
    metric_alarms: MetricAlarms = pydantic.Field(None, alias="MetricAlarms")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeAnomalyDetectorsInput(_CloudWatchModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: MaxReturnedResultsCount = pydantic.Field(None, alias="MaxResults")
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    anomaly_detector_types: AnomalyDetectorTypes = pydantic.Field(
        None, alias="AnomalyDetectorTypes"
    )


class DescribeAnomalyDetectorsOutput(_CloudWatchModelBase):
    anomaly_detectors: AnomalyDetectors = pydantic.Field(None, alias="AnomalyDetectors")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class DescribeInsightRulesInput(_CloudWatchModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: InsightRuleMaxResults = pydantic.Field(None, alias="MaxResults")


class DescribeInsightRulesOutput(_CloudWatchModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    insight_rules: InsightRules = pydantic.Field(None, alias="InsightRules")


class Dimension(_CloudWatchModelBase):
    name: DimensionName = pydantic.Field(None, alias="Name")
    value: DimensionValue = pydantic.Field(None, alias="Value")


class DimensionFilter(_CloudWatchModelBase):
    name: DimensionName = pydantic.Field(None, alias="Name")
    value: DimensionValue = pydantic.Field(None, alias="Value")


class DisableAlarmActionsInput(_CloudWatchModelBase):
    alarm_names: AlarmNames = pydantic.Field(None, alias="AlarmNames")


class DisableInsightRulesInput(_CloudWatchModelBase):
    rule_names: InsightRuleNames = pydantic.Field(None, alias="RuleNames")


class DisableInsightRulesOutput(_CloudWatchModelBase):
    failures: BatchFailures = pydantic.Field(None, alias="Failures")


class EnableAlarmActionsInput(_CloudWatchModelBase):
    alarm_names: AlarmNames = pydantic.Field(None, alias="AlarmNames")


class EnableInsightRulesInput(_CloudWatchModelBase):
    rule_names: InsightRuleNames = pydantic.Field(None, alias="RuleNames")


class EnableInsightRulesOutput(_CloudWatchModelBase):
    failures: BatchFailures = pydantic.Field(None, alias="Failures")


class GetDashboardInput(_CloudWatchModelBase):
    dashboard_name: DashboardName = pydantic.Field(None, alias="DashboardName")


class GetDashboardOutput(_CloudWatchModelBase):
    dashboard_arn: DashboardArn = pydantic.Field(None, alias="DashboardArn")
    dashboard_body: DashboardBody = pydantic.Field(None, alias="DashboardBody")
    dashboard_name: DashboardName = pydantic.Field(None, alias="DashboardName")


class GetInsightRuleReportInput(_CloudWatchModelBase):
    rule_name: InsightRuleName = pydantic.Field(None, alias="RuleName")
    start_time: Timestamp = pydantic.Field(None, alias="StartTime")
    end_time: Timestamp = pydantic.Field(None, alias="EndTime")
    period: Period = pydantic.Field(None, alias="Period")
    max_contributor_count: InsightRuleUnboundInteger = pydantic.Field(
        None, alias="MaxContributorCount"
    )
    metrics: InsightRuleMetricList = pydantic.Field(None, alias="Metrics")
    order_by: InsightRuleOrderBy = pydantic.Field(None, alias="OrderBy")


class GetInsightRuleReportOutput(_CloudWatchModelBase):
    key_labels: InsightRuleContributorKeyLabels = pydantic.Field(
        None, alias="KeyLabels"
    )
    aggregation_statistic: InsightRuleAggregationStatistic = pydantic.Field(
        None, alias="AggregationStatistic"
    )
    aggregate_value: InsightRuleUnboundDouble = pydantic.Field(
        None, alias="AggregateValue"
    )
    approximate_unique_count: InsightRuleUnboundLong = pydantic.Field(
        None, alias="ApproximateUniqueCount"
    )
    contributors: InsightRuleContributors = pydantic.Field(None, alias="Contributors")
    metric_datapoints: InsightRuleMetricDatapoints = pydantic.Field(
        None, alias="MetricDatapoints"
    )


class GetMetricDataInput(_CloudWatchModelBase):
    metric_data_queries: MetricDataQueries = pydantic.Field(
        None, alias="MetricDataQueries"
    )
    start_time: Timestamp = pydantic.Field(None, alias="StartTime")
    end_time: Timestamp = pydantic.Field(None, alias="EndTime")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    scan_by: ScanBy = pydantic.Field(None, alias="ScanBy")
    max_datapoints: GetMetricDataMaxDatapoints = pydantic.Field(
        None, alias="MaxDatapoints"
    )
    label_options: "LabelOptions" = pydantic.Field(None, alias="LabelOptions")


class GetMetricDataOutput(_CloudWatchModelBase):
    metric_data_results: MetricDataResults = pydantic.Field(
        None, alias="MetricDataResults"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    messages: MetricDataResultMessages = pydantic.Field(None, alias="Messages")


class GetMetricStatisticsInput(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    start_time: Timestamp = pydantic.Field(None, alias="StartTime")
    end_time: Timestamp = pydantic.Field(None, alias="EndTime")
    period: Period = pydantic.Field(None, alias="Period")
    statistics: Statistics = pydantic.Field(None, alias="Statistics")
    extended_statistics: ExtendedStatistics = pydantic.Field(
        None, alias="ExtendedStatistics"
    )
    unit: StandardUnit = pydantic.Field(None, alias="Unit")


class GetMetricStatisticsOutput(_CloudWatchModelBase):
    label: MetricLabel = pydantic.Field(None, alias="Label")
    datapoints: Datapoints = pydantic.Field(None, alias="Datapoints")


class GetMetricStreamInput(_CloudWatchModelBase):
    name: MetricStreamName = pydantic.Field(None, alias="Name")


class GetMetricStreamOutput(_CloudWatchModelBase):
    arn: AmazonResourceName = pydantic.Field(None, alias="Arn")
    name: MetricStreamName = pydantic.Field(None, alias="Name")
    include_filters: MetricStreamFilters = pydantic.Field(None, alias="IncludeFilters")
    exclude_filters: MetricStreamFilters = pydantic.Field(None, alias="ExcludeFilters")
    firehose_arn: AmazonResourceName = pydantic.Field(None, alias="FirehoseArn")
    role_arn: AmazonResourceName = pydantic.Field(None, alias="RoleArn")
    state: MetricStreamState = pydantic.Field(None, alias="State")
    creation_date: Timestamp = pydantic.Field(None, alias="CreationDate")
    last_update_date: Timestamp = pydantic.Field(None, alias="LastUpdateDate")
    output_format: MetricStreamOutputFormat = pydantic.Field(None, alias="OutputFormat")
    statistics_configurations: MetricStreamStatisticsConfigurations = pydantic.Field(
        None, alias="StatisticsConfigurations"
    )
    include_linked_accounts_metrics: IncludeLinkedAccountsMetrics = pydantic.Field(
        None, alias="IncludeLinkedAccountsMetrics"
    )


class GetMetricWidgetImageInput(_CloudWatchModelBase):
    metric_widget: MetricWidget = pydantic.Field(None, alias="MetricWidget")
    output_format: OutputFormat = pydantic.Field(None, alias="OutputFormat")


class GetMetricWidgetImageOutput(_CloudWatchModelBase):
    metric_widget_image: MetricWidgetImage = pydantic.Field(
        None, alias="MetricWidgetImage"
    )


class InsightRule(_CloudWatchModelBase):
    name: InsightRuleName = pydantic.Field(None, alias="Name")
    state: InsightRuleState = pydantic.Field(None, alias="State")
    schema: InsightRuleSchema = pydantic.Field(None, alias="Schema")
    definition: InsightRuleDefinition = pydantic.Field(None, alias="Definition")
    managed_rule: InsightRuleIsManaged = pydantic.Field(None, alias="ManagedRule")


class InsightRuleContributor(_CloudWatchModelBase):
    keys: InsightRuleContributorKeys = pydantic.Field(None, alias="Keys")
    approximate_aggregate_value: InsightRuleUnboundDouble = pydantic.Field(
        None, alias="ApproximateAggregateValue"
    )
    datapoints: InsightRuleContributorDatapoints = pydantic.Field(
        None, alias="Datapoints"
    )


class InsightRuleContributorDatapoint(_CloudWatchModelBase):
    timestamp: Timestamp = pydantic.Field(None, alias="Timestamp")
    approximate_value: InsightRuleUnboundDouble = pydantic.Field(
        None, alias="ApproximateValue"
    )


class InsightRuleMetricDatapoint(_CloudWatchModelBase):
    timestamp: Timestamp = pydantic.Field(None, alias="Timestamp")
    unique_contributors: InsightRuleUnboundDouble = pydantic.Field(
        None, alias="UniqueContributors"
    )
    max_contributor_value: InsightRuleUnboundDouble = pydantic.Field(
        None, alias="MaxContributorValue"
    )
    sample_count: InsightRuleUnboundDouble = pydantic.Field(None, alias="SampleCount")
    average: InsightRuleUnboundDouble = pydantic.Field(None, alias="Average")
    sum: InsightRuleUnboundDouble = pydantic.Field(None, alias="Sum")
    minimum: InsightRuleUnboundDouble = pydantic.Field(None, alias="Minimum")
    maximum: InsightRuleUnboundDouble = pydantic.Field(None, alias="Maximum")


class LabelOptions(_CloudWatchModelBase):
    timezone: GetMetricDataLabelTimezone = pydantic.Field(None, alias="Timezone")


class ListDashboardsInput(_CloudWatchModelBase):
    dashboard_name_prefix: DashboardNamePrefix = pydantic.Field(
        None, alias="DashboardNamePrefix"
    )
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListDashboardsOutput(_CloudWatchModelBase):
    dashboard_entries: DashboardEntries = pydantic.Field(None, alias="DashboardEntries")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListManagedInsightRulesInput(_CloudWatchModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceARN")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: InsightRuleMaxResults = pydantic.Field(None, alias="MaxResults")


class ListManagedInsightRulesOutput(_CloudWatchModelBase):
    managed_rules: ManagedRuleDescriptions = pydantic.Field(None, alias="ManagedRules")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")


class ListMetricStreamsInput(_CloudWatchModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: ListMetricStreamsMaxResults = pydantic.Field(None, alias="MaxResults")


class ListMetricStreamsOutput(_CloudWatchModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    entries: MetricStreamEntries = pydantic.Field(None, alias="Entries")


class ListMetricsInput(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: DimensionFilters = pydantic.Field(None, alias="Dimensions")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    recently_active: RecentlyActive = pydantic.Field(None, alias="RecentlyActive")
    include_linked_accounts: IncludeLinkedAccounts = pydantic.Field(
        None, alias="IncludeLinkedAccounts"
    )
    owning_account: AccountId = pydantic.Field(None, alias="OwningAccount")


class ListMetricsOutput(_CloudWatchModelBase):
    metrics: Metrics = pydantic.Field(None, alias="Metrics")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    owning_accounts: OwningAccounts = pydantic.Field(None, alias="OwningAccounts")


class ListTagsForResourceInput(_CloudWatchModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceARN")


class ListTagsForResourceOutput(_CloudWatchModelBase):
    tags: TagList = pydantic.Field(None, alias="Tags")


class ManagedRule(_CloudWatchModelBase):
    template_name: TemplateName = pydantic.Field(None, alias="TemplateName")
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceARN")
    tags: TagList = pydantic.Field(None, alias="Tags")


class ManagedRuleDescription(_CloudWatchModelBase):
    template_name: TemplateName = pydantic.Field(None, alias="TemplateName")
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceARN")
    rule_state: "ManagedRuleState" = pydantic.Field(None, alias="RuleState")


class ManagedRuleState(_CloudWatchModelBase):
    rule_name: InsightRuleName = pydantic.Field(None, alias="RuleName")
    state: InsightRuleState = pydantic.Field(None, alias="State")


class MessageData(_CloudWatchModelBase):
    code: MessageDataCode = pydantic.Field(None, alias="Code")
    value: MessageDataValue = pydantic.Field(None, alias="Value")


class Metric(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")


class MetricAlarm(_CloudWatchModelBase):
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    alarm_arn: AlarmArn = pydantic.Field(None, alias="AlarmArn")
    alarm_description: AlarmDescription = pydantic.Field(None, alias="AlarmDescription")
    alarm_configuration_updated_timestamp: Timestamp = pydantic.Field(
        None, alias="AlarmConfigurationUpdatedTimestamp"
    )
    actions_enabled: ActionsEnabled = pydantic.Field(None, alias="ActionsEnabled")
    ok_actions: ResourceList = pydantic.Field(None, alias="OKActions")
    alarm_actions: ResourceList = pydantic.Field(None, alias="AlarmActions")
    insufficient_data_actions: ResourceList = pydantic.Field(
        None, alias="InsufficientDataActions"
    )
    state_value: StateValue = pydantic.Field(None, alias="StateValue")
    state_reason: StateReason = pydantic.Field(None, alias="StateReason")
    state_reason_data: StateReasonData = pydantic.Field(None, alias="StateReasonData")
    state_updated_timestamp: Timestamp = pydantic.Field(
        None, alias="StateUpdatedTimestamp"
    )
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    statistic: Statistic = pydantic.Field(None, alias="Statistic")
    extended_statistic: ExtendedStatistic = pydantic.Field(
        None, alias="ExtendedStatistic"
    )
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    period: Period = pydantic.Field(None, alias="Period")
    unit: StandardUnit = pydantic.Field(None, alias="Unit")
    evaluation_periods: EvaluationPeriods = pydantic.Field(
        None, alias="EvaluationPeriods"
    )
    datapoints_to_alarm: DatapointsToAlarm = pydantic.Field(
        None, alias="DatapointsToAlarm"
    )
    threshold: Threshold = pydantic.Field(None, alias="Threshold")
    comparison_operator: ComparisonOperator = pydantic.Field(
        None, alias="ComparisonOperator"
    )
    treat_missing_data: TreatMissingData = pydantic.Field(
        None, alias="TreatMissingData"
    )
    evaluate_low_sample_count_percentile: EvaluateLowSampleCountPercentile = (
        pydantic.Field(None, alias="EvaluateLowSampleCountPercentile")
    )
    metrics: MetricDataQueries = pydantic.Field(None, alias="Metrics")
    threshold_metric_id: MetricId = pydantic.Field(None, alias="ThresholdMetricId")
    evaluation_state: EvaluationState = pydantic.Field(None, alias="EvaluationState")
    state_transitioned_timestamp: Timestamp = pydantic.Field(
        None, alias="StateTransitionedTimestamp"
    )


class MetricDataQuery(_CloudWatchModelBase):
    id: MetricId = pydantic.Field(None, alias="Id")
    metric_stat: "MetricStat" = pydantic.Field(None, alias="MetricStat")
    expression: MetricExpression = pydantic.Field(None, alias="Expression")
    label: MetricLabel = pydantic.Field(None, alias="Label")
    return_data: ReturnData = pydantic.Field(None, alias="ReturnData")
    period: Period = pydantic.Field(None, alias="Period")
    account_id: AccountId = pydantic.Field(None, alias="AccountId")


class MetricDataResult(_CloudWatchModelBase):
    id: MetricId = pydantic.Field(None, alias="Id")
    label: MetricLabel = pydantic.Field(None, alias="Label")
    timestamps: Timestamps = pydantic.Field(None, alias="Timestamps")
    values: DatapointValues = pydantic.Field(None, alias="Values")
    status_code: StatusCode = pydantic.Field(None, alias="StatusCode")
    messages: MetricDataResultMessages = pydantic.Field(None, alias="Messages")


class MetricDatum(_CloudWatchModelBase):
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    timestamp: Timestamp = pydantic.Field(None, alias="Timestamp")
    value: DatapointValue = pydantic.Field(None, alias="Value")
    statistic_values: "StatisticSet" = pydantic.Field(None, alias="StatisticValues")
    values: Values = pydantic.Field(None, alias="Values")
    counts: Counts = pydantic.Field(None, alias="Counts")
    unit: StandardUnit = pydantic.Field(None, alias="Unit")
    storage_resolution: StorageResolution = pydantic.Field(
        None, alias="StorageResolution"
    )


class MetricMathAnomalyDetector(_CloudWatchModelBase):
    metric_data_queries: MetricDataQueries = pydantic.Field(
        None, alias="MetricDataQueries"
    )


class MetricStat(_CloudWatchModelBase):
    metric: "Metric" = pydantic.Field(None, alias="Metric")
    period: Period = pydantic.Field(None, alias="Period")
    stat: Stat = pydantic.Field(None, alias="Stat")
    unit: StandardUnit = pydantic.Field(None, alias="Unit")


class MetricStreamEntry(_CloudWatchModelBase):
    arn: AmazonResourceName = pydantic.Field(None, alias="Arn")
    creation_date: Timestamp = pydantic.Field(None, alias="CreationDate")
    last_update_date: Timestamp = pydantic.Field(None, alias="LastUpdateDate")
    name: MetricStreamName = pydantic.Field(None, alias="Name")
    firehose_arn: AmazonResourceName = pydantic.Field(None, alias="FirehoseArn")
    state: MetricStreamState = pydantic.Field(None, alias="State")
    output_format: MetricStreamOutputFormat = pydantic.Field(None, alias="OutputFormat")


class MetricStreamFilter(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_names: MetricStreamFilterMetricNames = pydantic.Field(
        None, alias="MetricNames"
    )


class MetricStreamStatisticsConfiguration(_CloudWatchModelBase):
    include_metrics: MetricStreamStatisticsIncludeMetrics = pydantic.Field(
        None, alias="IncludeMetrics"
    )
    additional_statistics: MetricStreamStatisticsAdditionalStatistics = pydantic.Field(
        None, alias="AdditionalStatistics"
    )


class MetricStreamStatisticsMetric(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")


class PartialFailure(_CloudWatchModelBase):
    failure_resource: FailureResource = pydantic.Field(None, alias="FailureResource")
    exception_type: ExceptionType = pydantic.Field(None, alias="ExceptionType")
    failure_code: FailureCode = pydantic.Field(None, alias="FailureCode")
    failure_description: FailureDescription = pydantic.Field(
        None, alias="FailureDescription"
    )


class PutAnomalyDetectorInput(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    stat: AnomalyDetectorMetricStat = pydantic.Field(None, alias="Stat")
    configuration: "AnomalyDetectorConfiguration" = pydantic.Field(
        None, alias="Configuration"
    )
    single_metric_anomaly_detector: "SingleMetricAnomalyDetector" = pydantic.Field(
        None, alias="SingleMetricAnomalyDetector"
    )
    metric_math_anomaly_detector: "MetricMathAnomalyDetector" = pydantic.Field(
        None, alias="MetricMathAnomalyDetector"
    )


class PutAnomalyDetectorOutput(_CloudWatchModelBase):
    pass


class PutCompositeAlarmInput(_CloudWatchModelBase):
    actions_enabled: ActionsEnabled = pydantic.Field(None, alias="ActionsEnabled")
    alarm_actions: ResourceList = pydantic.Field(None, alias="AlarmActions")
    alarm_description: AlarmDescription = pydantic.Field(None, alias="AlarmDescription")
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    alarm_rule: AlarmRule = pydantic.Field(None, alias="AlarmRule")
    insufficient_data_actions: ResourceList = pydantic.Field(
        None, alias="InsufficientDataActions"
    )
    ok_actions: ResourceList = pydantic.Field(None, alias="OKActions")
    tags: TagList = pydantic.Field(None, alias="Tags")
    actions_suppressor: AlarmArn = pydantic.Field(None, alias="ActionsSuppressor")
    actions_suppressor_wait_period: SuppressorPeriod = pydantic.Field(
        None, alias="ActionsSuppressorWaitPeriod"
    )
    actions_suppressor_extension_period: SuppressorPeriod = pydantic.Field(
        None, alias="ActionsSuppressorExtensionPeriod"
    )


class PutDashboardInput(_CloudWatchModelBase):
    dashboard_name: DashboardName = pydantic.Field(None, alias="DashboardName")
    dashboard_body: DashboardBody = pydantic.Field(None, alias="DashboardBody")


class PutDashboardOutput(_CloudWatchModelBase):
    dashboard_validation_messages: DashboardValidationMessages = pydantic.Field(
        None, alias="DashboardValidationMessages"
    )


class PutInsightRuleInput(_CloudWatchModelBase):
    rule_name: InsightRuleName = pydantic.Field(None, alias="RuleName")
    rule_state: InsightRuleState = pydantic.Field(None, alias="RuleState")
    rule_definition: InsightRuleDefinition = pydantic.Field(
        None, alias="RuleDefinition"
    )
    tags: TagList = pydantic.Field(None, alias="Tags")


class PutInsightRuleOutput(_CloudWatchModelBase):
    pass


class PutManagedInsightRulesInput(_CloudWatchModelBase):
    managed_rules: ManagedRules = pydantic.Field(None, alias="ManagedRules")


class PutManagedInsightRulesOutput(_CloudWatchModelBase):
    failures: BatchFailures = pydantic.Field(None, alias="Failures")


class PutMetricAlarmInput(_CloudWatchModelBase):
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    alarm_description: AlarmDescription = pydantic.Field(None, alias="AlarmDescription")
    actions_enabled: ActionsEnabled = pydantic.Field(None, alias="ActionsEnabled")
    ok_actions: ResourceList = pydantic.Field(None, alias="OKActions")
    alarm_actions: ResourceList = pydantic.Field(None, alias="AlarmActions")
    insufficient_data_actions: ResourceList = pydantic.Field(
        None, alias="InsufficientDataActions"
    )
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    statistic: Statistic = pydantic.Field(None, alias="Statistic")
    extended_statistic: ExtendedStatistic = pydantic.Field(
        None, alias="ExtendedStatistic"
    )
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    period: Period = pydantic.Field(None, alias="Period")
    unit: StandardUnit = pydantic.Field(None, alias="Unit")
    evaluation_periods: EvaluationPeriods = pydantic.Field(
        None, alias="EvaluationPeriods"
    )
    datapoints_to_alarm: DatapointsToAlarm = pydantic.Field(
        None, alias="DatapointsToAlarm"
    )
    threshold: Threshold = pydantic.Field(None, alias="Threshold")
    comparison_operator: ComparisonOperator = pydantic.Field(
        None, alias="ComparisonOperator"
    )
    treat_missing_data: TreatMissingData = pydantic.Field(
        None, alias="TreatMissingData"
    )
    evaluate_low_sample_count_percentile: EvaluateLowSampleCountPercentile = (
        pydantic.Field(None, alias="EvaluateLowSampleCountPercentile")
    )
    metrics: MetricDataQueries = pydantic.Field(None, alias="Metrics")
    tags: TagList = pydantic.Field(None, alias="Tags")
    threshold_metric_id: MetricId = pydantic.Field(None, alias="ThresholdMetricId")


class PutMetricDataInput(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_data: MetricData = pydantic.Field(None, alias="MetricData")


class PutMetricStreamInput(_CloudWatchModelBase):
    name: MetricStreamName = pydantic.Field(None, alias="Name")
    include_filters: MetricStreamFilters = pydantic.Field(None, alias="IncludeFilters")
    exclude_filters: MetricStreamFilters = pydantic.Field(None, alias="ExcludeFilters")
    firehose_arn: AmazonResourceName = pydantic.Field(None, alias="FirehoseArn")
    role_arn: AmazonResourceName = pydantic.Field(None, alias="RoleArn")
    output_format: MetricStreamOutputFormat = pydantic.Field(None, alias="OutputFormat")
    tags: TagList = pydantic.Field(None, alias="Tags")
    statistics_configurations: MetricStreamStatisticsConfigurations = pydantic.Field(
        None, alias="StatisticsConfigurations"
    )
    include_linked_accounts_metrics: IncludeLinkedAccountsMetrics = pydantic.Field(
        None, alias="IncludeLinkedAccountsMetrics"
    )


class PutMetricStreamOutput(_CloudWatchModelBase):
    arn: AmazonResourceName = pydantic.Field(None, alias="Arn")


class Range(_CloudWatchModelBase):
    start_time: Timestamp = pydantic.Field(None, alias="StartTime")
    end_time: Timestamp = pydantic.Field(None, alias="EndTime")


class SetAlarmStateInput(_CloudWatchModelBase):
    alarm_name: AlarmName = pydantic.Field(None, alias="AlarmName")
    state_value: StateValue = pydantic.Field(None, alias="StateValue")
    state_reason: StateReason = pydantic.Field(None, alias="StateReason")
    state_reason_data: StateReasonData = pydantic.Field(None, alias="StateReasonData")


class SingleMetricAnomalyDetector(_CloudWatchModelBase):
    namespace: Namespace = pydantic.Field(None, alias="Namespace")
    metric_name: MetricName = pydantic.Field(None, alias="MetricName")
    dimensions: Dimensions = pydantic.Field(None, alias="Dimensions")
    stat: AnomalyDetectorMetricStat = pydantic.Field(None, alias="Stat")


class StartMetricStreamsInput(_CloudWatchModelBase):
    names: MetricStreamNames = pydantic.Field(None, alias="Names")


class StartMetricStreamsOutput(_CloudWatchModelBase):
    pass


class StatisticSet(_CloudWatchModelBase):
    sample_count: DatapointValue = pydantic.Field(None, alias="SampleCount")
    sum: DatapointValue = pydantic.Field(None, alias="Sum")
    minimum: DatapointValue = pydantic.Field(None, alias="Minimum")
    maximum: DatapointValue = pydantic.Field(None, alias="Maximum")


class StopMetricStreamsInput(_CloudWatchModelBase):
    names: MetricStreamNames = pydantic.Field(None, alias="Names")


class StopMetricStreamsOutput(_CloudWatchModelBase):
    pass


class Tag(_CloudWatchModelBase):
    key: TagKey = pydantic.Field(None, alias="Key")
    value: TagValue = pydantic.Field(None, alias="Value")


class TagResourceInput(_CloudWatchModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceARN")
    tags: TagList = pydantic.Field(None, alias="Tags")


class TagResourceOutput(_CloudWatchModelBase):
    pass


class UntagResourceInput(_CloudWatchModelBase):
    resource_arn: AmazonResourceName = pydantic.Field(None, alias="ResourceARN")
    tag_keys: TagKeyList = pydantic.Field(None, alias="TagKeys")


class UntagResourceOutput(_CloudWatchModelBase):
    pass


AlarmHistoryItem.update_forward_refs()
AnomalyDetector.update_forward_refs()
AnomalyDetectorConfiguration.update_forward_refs()
CompositeAlarm.update_forward_refs()
DashboardEntry.update_forward_refs()
DashboardValidationMessage.update_forward_refs()
Datapoint.update_forward_refs()
DeleteAlarmsInput.update_forward_refs()
DeleteAnomalyDetectorInput.update_forward_refs()
DeleteAnomalyDetectorOutput.update_forward_refs()
DeleteDashboardsInput.update_forward_refs()
DeleteDashboardsOutput.update_forward_refs()
DeleteInsightRulesInput.update_forward_refs()
DeleteInsightRulesOutput.update_forward_refs()
DeleteMetricStreamInput.update_forward_refs()
DeleteMetricStreamOutput.update_forward_refs()
DescribeAlarmHistoryInput.update_forward_refs()
DescribeAlarmHistoryOutput.update_forward_refs()
DescribeAlarmsForMetricInput.update_forward_refs()
DescribeAlarmsForMetricOutput.update_forward_refs()
DescribeAlarmsInput.update_forward_refs()
DescribeAlarmsOutput.update_forward_refs()
DescribeAnomalyDetectorsInput.update_forward_refs()
DescribeAnomalyDetectorsOutput.update_forward_refs()
DescribeInsightRulesInput.update_forward_refs()
DescribeInsightRulesOutput.update_forward_refs()
Dimension.update_forward_refs()
DimensionFilter.update_forward_refs()
DisableAlarmActionsInput.update_forward_refs()
DisableInsightRulesInput.update_forward_refs()
DisableInsightRulesOutput.update_forward_refs()
EnableAlarmActionsInput.update_forward_refs()
EnableInsightRulesInput.update_forward_refs()
EnableInsightRulesOutput.update_forward_refs()
GetDashboardInput.update_forward_refs()
GetDashboardOutput.update_forward_refs()
GetInsightRuleReportInput.update_forward_refs()
GetInsightRuleReportOutput.update_forward_refs()
GetMetricDataInput.update_forward_refs()
GetMetricDataOutput.update_forward_refs()
GetMetricStatisticsInput.update_forward_refs()
GetMetricStatisticsOutput.update_forward_refs()
GetMetricStreamInput.update_forward_refs()
GetMetricStreamOutput.update_forward_refs()
GetMetricWidgetImageInput.update_forward_refs()
GetMetricWidgetImageOutput.update_forward_refs()
InsightRule.update_forward_refs()
InsightRuleContributor.update_forward_refs()
InsightRuleContributorDatapoint.update_forward_refs()
InsightRuleMetricDatapoint.update_forward_refs()
LabelOptions.update_forward_refs()
ListDashboardsInput.update_forward_refs()
ListDashboardsOutput.update_forward_refs()
ListManagedInsightRulesInput.update_forward_refs()
ListManagedInsightRulesOutput.update_forward_refs()
ListMetricStreamsInput.update_forward_refs()
ListMetricStreamsOutput.update_forward_refs()
ListMetricsInput.update_forward_refs()
ListMetricsOutput.update_forward_refs()
ListTagsForResourceInput.update_forward_refs()
ListTagsForResourceOutput.update_forward_refs()
ManagedRule.update_forward_refs()
ManagedRuleDescription.update_forward_refs()
ManagedRuleState.update_forward_refs()
MessageData.update_forward_refs()
Metric.update_forward_refs()
MetricAlarm.update_forward_refs()
MetricDataQuery.update_forward_refs()
MetricDataResult.update_forward_refs()
MetricDatum.update_forward_refs()
MetricMathAnomalyDetector.update_forward_refs()
MetricStat.update_forward_refs()
MetricStreamEntry.update_forward_refs()
MetricStreamFilter.update_forward_refs()
MetricStreamStatisticsConfiguration.update_forward_refs()
MetricStreamStatisticsMetric.update_forward_refs()
PartialFailure.update_forward_refs()
PutAnomalyDetectorInput.update_forward_refs()
PutAnomalyDetectorOutput.update_forward_refs()
PutCompositeAlarmInput.update_forward_refs()
PutDashboardInput.update_forward_refs()
PutDashboardOutput.update_forward_refs()
PutInsightRuleInput.update_forward_refs()
PutInsightRuleOutput.update_forward_refs()
PutManagedInsightRulesInput.update_forward_refs()
PutManagedInsightRulesOutput.update_forward_refs()
PutMetricAlarmInput.update_forward_refs()
PutMetricDataInput.update_forward_refs()
PutMetricStreamInput.update_forward_refs()
PutMetricStreamOutput.update_forward_refs()
Range.update_forward_refs()
SetAlarmStateInput.update_forward_refs()
SingleMetricAnomalyDetector.update_forward_refs()
StartMetricStreamsInput.update_forward_refs()
StartMetricStreamsOutput.update_forward_refs()
StatisticSet.update_forward_refs()
StopMetricStreamsInput.update_forward_refs()
StopMetricStreamsOutput.update_forward_refs()
Tag.update_forward_refs()
TagResourceInput.update_forward_refs()
TagResourceOutput.update_forward_refs()
UntagResourceInput.update_forward_refs()
UntagResourceOutput.update_forward_refs()
