from datetime import datetime
import typing
import enum

import pydantic


class _EC2ModelBase(pydantic.BaseModel, frozen=True, use_enum_values=True, allow_population_by_field_name=True, extra=pydantic.Extra.allow):
    def dict(self, by_alias=True, **kwargs) -> dict:
        return super().dict(by_alias=True, **kwargs)
    
    def json(self, by_alias=True, **kwargs) -> dict:
        return super().json(by_alias=True, **kwargs)

AcceleratorManufacturer: str = pydantic.constr()
AcceleratorName: str = pydantic.constr()
AcceleratorType: str = pydantic.constr()
AccountAttributeName: str = pydantic.constr()
ActivityStatus: str = pydantic.constr()
AddressAttributeName: str = pydantic.constr()
AddressFamily: str = pydantic.constr()
AddressMaxResults: int = pydantic.conint(ge=1, le=1000)
AddressTransferStatus: str = pydantic.constr()
Affinity: str = pydantic.constr()
AllocationId: str = pydantic.constr()
AllocationState: str = pydantic.constr()
AllocationStrategy: str = pydantic.constr()
AllocationType: str = pydantic.constr()
AllowedInstanceType: str = pydantic.constr(min_length=1, max_length=30, regex=r'[a-zA-Z0-9\.\*]+')
AllowsMultipleInstanceTypes: str = pydantic.constr()
AmdSevSnpSpecification: str = pydantic.constr()
AnalysisStatus: str = pydantic.constr()
ApplianceModeSupportValue: str = pydantic.constr()
ArchitectureType: str = pydantic.constr()
ArchitectureValues: str = pydantic.constr()
AssociatedNetworkType: str = pydantic.constr()
AssociationStatusCode: str = pydantic.constr()
AttachmentStatus: str = pydantic.constr()
AutoAcceptSharedAssociationsValue: str = pydantic.constr()
AutoAcceptSharedAttachmentsValue: str = pydantic.constr()
AutoPlacement: str = pydantic.constr()
AutoRecoveryFlag: bool = pydantic.conbool()
AvailabilityZoneName: str = pydantic.constr()
AvailabilityZoneOptInStatus: str = pydantic.constr()
AvailabilityZoneState: str = pydantic.constr()
BareMetal: str = pydantic.constr()
BareMetalFlag: bool = pydantic.conbool()
BaselineBandwidthInMbps: int = pydantic.conint()
BaselineIops: int = pydantic.conint()
BaselineThroughputInMBps: float = pydantic.confloat()
BatchState: str = pydantic.constr()
BgpStatus: str = pydantic.constr()
Blob: bytes = pydantic.conbytes()
Boolean: bool = pydantic.conbool()
BootModeType: str = pydantic.constr()
BootModeValues: str = pydantic.constr()
BoxedDouble: float = pydantic.confloat()
BundleId: str = pydantic.constr()
BundleTaskState: str = pydantic.constr()
BurstablePerformance: str = pydantic.constr()
BurstablePerformanceFlag: bool = pydantic.conbool()
ByoipCidrState: str = pydantic.constr()
CancelBatchErrorCode: str = pydantic.constr()
CancelCapacityReservationFleetErrorCode: str = pydantic.constr()
CancelCapacityReservationFleetErrorMessage: str = pydantic.constr()
CancelSpotInstanceRequestState: str = pydantic.constr()
CapacityReservationFleetId: str = pydantic.constr()
CapacityReservationFleetState: str = pydantic.constr()
CapacityReservationId: str = pydantic.constr()
CapacityReservationInstancePlatform: str = pydantic.constr()
CapacityReservationPreference: str = pydantic.constr()
CapacityReservationState: str = pydantic.constr()
CapacityReservationTenancy: str = pydantic.constr()
CarrierGatewayId: str = pydantic.constr()
CarrierGatewayMaxResults: int = pydantic.conint(ge=5, le=1000)
CarrierGatewayState: str = pydantic.constr()
CertificateArn: str = pydantic.constr()
CertificateId: str = pydantic.constr()
ClientCertificateRevocationListStatusCode: str = pydantic.constr()
ClientSecretType: str = pydantic.constr()
ClientVpnAssociationId: str = pydantic.constr()
ClientVpnAuthenticationType: str = pydantic.constr()
ClientVpnAuthorizationRuleStatusCode: str = pydantic.constr()
ClientVpnConnectionStatusCode: str = pydantic.constr()
ClientVpnEndpointAttributeStatusCode: str = pydantic.constr()
ClientVpnEndpointId: str = pydantic.constr()
ClientVpnEndpointStatusCode: str = pydantic.constr()
ClientVpnRouteStatusCode: str = pydantic.constr()
CloudWatchLogGroupArn: str = pydantic.constr()
CoipPoolId: str = pydantic.constr()
CoipPoolMaxResults: int = pydantic.conint(ge=5, le=1000)
ComponentAccount: str = pydantic.constr(regex=r'\d{12}')
ComponentRegion: str = pydantic.constr(regex=r'[a-z]{2}-[a-z]+-[1-9]+')
ConnectionNotificationId: str = pydantic.constr()
ConnectionNotificationState: str = pydantic.constr()
ConnectionNotificationType: str = pydantic.constr()
ConnectivityType: str = pydantic.constr()
ContainerFormat: str = pydantic.constr()
ConversionTaskId: str = pydantic.constr()
ConversionTaskState: str = pydantic.constr()
CopySnapshotRequestPSU: str = pydantic.constr()
CopyTagsFromSource: str = pydantic.constr()
CoreCount: int = pydantic.conint()
CoreNetworkArn: str = pydantic.constr()
CpuManufacturer: str = pydantic.constr()
CurrencyCodeValues: str = pydantic.constr()
CurrentGenerationFlag: bool = pydantic.conbool()
CustomerGatewayId: str = pydantic.constr()
DITMaxResults: int = pydantic.conint(ge=5, le=100)
DITOMaxResults: int = pydantic.conint(ge=5, le=1000)
DatafeedSubscriptionState: str = pydantic.constr()
DateTime: datetime = pydantic.condate()
DedicatedHostFlag: bool = pydantic.conbool()
DedicatedHostId: str = pydantic.constr()
DefaultNetworkCardIndex: int = pydantic.conint()
DefaultRouteTableAssociationValue: str = pydantic.constr()
DefaultRouteTablePropagationValue: str = pydantic.constr()
DefaultTargetCapacityType: str = pydantic.constr()
DefaultingDhcpOptionsId: str = pydantic.constr()
DeleteFleetErrorCode: str = pydantic.constr()
DeleteQueuedReservedInstancesErrorCode: str = pydantic.constr()
DescribeAddressTransfersMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeByoipCidrsMaxResults: int = pydantic.conint(ge=1, le=100)
DescribeCapacityReservationFleetsMaxResults: int = pydantic.conint(ge=1, le=100)
DescribeCapacityReservationsMaxResults: int = pydantic.conint(ge=1, le=1000)
DescribeClassicLinkInstancesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeClientVpnAuthorizationRulesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeClientVpnConnectionsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeClientVpnEndpointMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeClientVpnRoutesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeClientVpnTargetNetworksMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeDhcpOptionsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeEgressOnlyInternetGatewaysMaxResults: int = pydantic.conint(ge=5, le=255)
DescribeElasticGpusMaxResults: int = pydantic.conint(ge=10, le=1000)
DescribeExportImageTasksMaxResults: int = pydantic.conint(ge=1, le=500)
DescribeFastLaunchImagesRequestMaxResults: int = pydantic.conint(le=200)
DescribeFastSnapshotRestoresMaxResults: int = pydantic.conint(le=200)
DescribeFpgaImagesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeHostReservationsMaxResults: int = pydantic.conint(ge=5, le=500)
DescribeIamInstanceProfileAssociationsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeInstanceCreditSpecificationsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeInternetGatewaysMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeLaunchTemplatesMaxResults: int = pydantic.conint(ge=1, le=200)
DescribeMovingAddressesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeNatGatewaysMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeNetworkAclsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeNetworkInterfacePermissionsMaxResults: int = pydantic.conint(ge=5, le=255)
DescribeNetworkInterfacesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribePrincipalIdFormatMaxResults: int = pydantic.conint(ge=1, le=1000)
DescribeReplaceRootVolumeTasksMaxResults: int = pydantic.conint(ge=1, le=50)
DescribeRouteTablesMaxResults: int = pydantic.conint(ge=5, le=100)
DescribeScheduledInstanceAvailabilityMaxResults: int = pydantic.conint(ge=5, le=300)
DescribeSecurityGroupRulesMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeSecurityGroupsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeSnapshotTierStatusMaxResults: int = pydantic.conint()
DescribeSpotFleetInstancesMaxResults: int = pydantic.conint(ge=1, le=1000)
DescribeSpotFleetRequestHistoryMaxResults: int = pydantic.conint(ge=1, le=1000)
DescribeStaleSecurityGroupsMaxResults: int = pydantic.conint(ge=5, le=255)
DescribeStaleSecurityGroupsNextToken: str = pydantic.constr(min_length=1, max_length=1024)
DescribeStoreImageTasksRequestMaxResults: int = pydantic.conint(ge=1, le=200)
DescribeSubnetsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeTrunkInterfaceAssociationsMaxResults: int = pydantic.conint(ge=5, le=255)
DescribeVerifiedAccessEndpointsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeVerifiedAccessGroupMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeVerifiedAccessInstanceLoggingConfigurationsMaxResults: int = pydantic.conint(ge=1, le=10)
DescribeVerifiedAccessInstancesMaxResults: int = pydantic.conint(ge=5, le=200)
DescribeVerifiedAccessTrustProvidersMaxResults: int = pydantic.conint(ge=5, le=200)
DescribeVpcClassicLinkDnsSupportMaxResults: int = pydantic.conint(ge=5, le=255)
DescribeVpcClassicLinkDnsSupportNextToken: str = pydantic.constr(min_length=1, max_length=1024)
DescribeVpcPeeringConnectionsMaxResults: int = pydantic.conint(ge=5, le=1000)
DescribeVpcsMaxResults: int = pydantic.conint(ge=5, le=1000)
DestinationFileFormat: str = pydantic.constr()
DeviceTrustProviderType: str = pydantic.constr()
DeviceType: str = pydantic.constr()
DhcpOptionsId: str = pydantic.constr()
DiskCount: int = pydantic.conint()
DiskImageFormat: str = pydantic.constr()
DiskSize: int = pydantic.conint()
DiskType: str = pydantic.constr()
DnsNameState: str = pydantic.constr()
DnsRecordIpType: str = pydantic.constr()
DnsSupportValue: str = pydantic.constr()
DomainType: str = pydantic.constr()
Double: float = pydantic.confloat()
DoubleWithConstraints: float = pydantic.confloat()
DrainSeconds: int = pydantic.conint(ge=1, le=4000)
DynamicRoutingValue: str = pydantic.constr()
EbsEncryptionSupport: str = pydantic.constr()
EbsNvmeSupport: str = pydantic.constr()
EbsOptimizedSupport: str = pydantic.constr()
EfaSupportedFlag: bool = pydantic.conbool()
EgressOnlyInternetGatewayId: str = pydantic.constr()
EipAllocationPublicIp: str = pydantic.constr()
ElasticGpuId: str = pydantic.constr()
ElasticGpuState: str = pydantic.constr()
ElasticGpuStatus: str = pydantic.constr()
ElasticInferenceAcceleratorCount: int = pydantic.conint(ge=1)
ElasticIpAssociationId: str = pydantic.constr()
EnaSrdSupported: bool = pydantic.conbool()
EnaSupport: str = pydantic.constr()
EncryptionInTransitSupported: bool = pydantic.conbool()
EndDateType: str = pydantic.constr()
EphemeralNvmeSupport: str = pydantic.constr()
EventCode: str = pydantic.constr()
EventType: str = pydantic.constr()
ExcessCapacityTerminationPolicy: str = pydantic.constr()
ExcludedInstanceType: str = pydantic.constr(min_length=1, max_length=30, regex=r'[a-zA-Z0-9\.\*]+')
ExportEnvironment: str = pydantic.constr()
ExportImageTaskId: str = pydantic.constr()
ExportTaskId: str = pydantic.constr()
ExportTaskState: str = pydantic.constr()
ExportVmTaskId: str = pydantic.constr()
FastLaunchResourceType: str = pydantic.constr()
FastLaunchStateCode: str = pydantic.constr()
FastSnapshotRestoreStateCode: str = pydantic.constr()
FindingsFound: str = pydantic.constr()
FleetActivityStatus: str = pydantic.constr()
FleetCapacityReservationTenancy: str = pydantic.constr()
FleetCapacityReservationUsageStrategy: str = pydantic.constr()
FleetEventType: str = pydantic.constr()
FleetExcessCapacityTerminationPolicy: str = pydantic.constr()
FleetId: str = pydantic.constr()
FleetInstanceMatchCriteria: str = pydantic.constr()
FleetOnDemandAllocationStrategy: str = pydantic.constr()
FleetReplacementStrategy: str = pydantic.constr()
FleetStateCode: str = pydantic.constr()
FleetType: str = pydantic.constr()
Float: float = pydantic.confloat()
FlowLogResourceId: str = pydantic.constr()
FlowLogsResourceType: str = pydantic.constr()
FpgaDeviceCount: int = pydantic.conint()
FpgaDeviceManufacturerName: str = pydantic.constr()
FpgaDeviceMemorySize: int = pydantic.conint()
FpgaDeviceName: str = pydantic.constr()
FpgaImageAttributeName: str = pydantic.constr()
FpgaImageId: str = pydantic.constr()
FpgaImageStateCode: str = pydantic.constr()
FreeTierEligibleFlag: bool = pydantic.conbool()
GVCDMaxResults: int = pydantic.conint(ge=200, le=1000)
GatewayAssociationState: str = pydantic.constr()
GatewayType: str = pydantic.constr()
GetCapacityReservationUsageRequestMaxResults: int = pydantic.conint(ge=1, le=1000)
GetGroupsForCapacityReservationRequestMaxResults: int = pydantic.conint(ge=1, le=1000)
GetIpamPoolAllocationsMaxResults: int = pydantic.conint(ge=1000, le=100000)
GetManagedPrefixListAssociationsMaxResults: int = pydantic.conint(ge=5, le=255)
GetSubnetCidrReservationsMaxResults: int = pydantic.conint(ge=5, le=1000)
GpuDeviceCount: int = pydantic.conint()
GpuDeviceManufacturerName: str = pydantic.constr()
GpuDeviceMemorySize: int = pydantic.conint()
GpuDeviceName: str = pydantic.constr()
HibernationFlag: bool = pydantic.conbool()
HostMaintenance: str = pydantic.constr()
HostRecovery: str = pydantic.constr()
HostReservationId: str = pydantic.constr()
HostTenancy: str = pydantic.constr()
HostnameType: str = pydantic.constr()
Hour: int = pydantic.conint(le=23)
HttpTokensState: str = pydantic.constr()
HypervisorType: str = pydantic.constr()
IamInstanceProfileAssociationId: str = pydantic.constr()
IamInstanceProfileAssociationState: str = pydantic.constr()
Igmpv2SupportValue: str = pydantic.constr()
ImageAttributeName: str = pydantic.constr()
ImageId: str = pydantic.constr()
ImageState: str = pydantic.constr()
ImageTypeValues: str = pydantic.constr()
ImdsSupportValues: str = pydantic.constr()
ImportImageTaskId: str = pydantic.constr()
ImportManifestUrl: str = pydantic.constr()
ImportSnapshotTaskId: str = pydantic.constr()
ImportTaskId: str = pydantic.constr()
InferenceDeviceCount: int = pydantic.conint()
InferenceDeviceManufacturerName: str = pydantic.constr()
InferenceDeviceName: str = pydantic.constr()
InstanceAttributeName: str = pydantic.constr()
InstanceAutoRecoveryState: str = pydantic.constr()
InstanceBootModeValues: str = pydantic.constr()
InstanceEventId: str = pydantic.constr()
InstanceEventWindowCronExpression: str = pydantic.constr()
InstanceEventWindowId: str = pydantic.constr()
InstanceEventWindowState: str = pydantic.constr()
InstanceGeneration: str = pydantic.constr()
InstanceHealthStatus: str = pydantic.constr()
InstanceId: str = pydantic.constr()
InstanceIdForResolver: str = pydantic.constr()
InstanceIdWithVolumeResolver: str = pydantic.constr()
InstanceInterruptionBehavior: str = pydantic.constr()
InstanceLifecycle: str = pydantic.constr()
InstanceLifecycleType: str = pydantic.constr()
InstanceMatchCriteria: str = pydantic.constr()
InstanceMetadataEndpointState: str = pydantic.constr()
InstanceMetadataOptionsState: str = pydantic.constr()
InstanceMetadataProtocolState: str = pydantic.constr()
InstanceMetadataTagsState: str = pydantic.constr()
InstanceStateName: str = pydantic.constr()
InstanceStorageEncryptionSupport: str = pydantic.constr()
InstanceStorageFlag: bool = pydantic.conbool()
InstanceType: str = pydantic.constr()
InstanceTypeHypervisor: str = pydantic.constr()
Integer: int = pydantic.conint()
IntegerWithConstraints: int = pydantic.conint()
InterfacePermissionType: str = pydantic.constr()
InterfaceProtocolType: str = pydantic.constr()
InternetGatewayId: str = pydantic.constr()
IpAddress: str = pydantic.constr(max_length=15, regex=r'^([0-9]{1,3}.){3}[0-9]{1,3}$')
IpAddressType: str = pydantic.constr()
IpamAddressHistoryMaxResults: int = pydantic.conint(ge=1, le=1000)
IpamAddressHistoryResourceType: str = pydantic.constr()
IpamAssociatedResourceDiscoveryStatus: str = pydantic.constr()
IpamComplianceStatus: str = pydantic.constr()
IpamDiscoveryFailureCode: str = pydantic.constr()
IpamId: str = pydantic.constr()
IpamManagementState: str = pydantic.constr()
IpamMaxResults: int = pydantic.conint(ge=5, le=1000)
IpamNetmaskLength: int = pydantic.conint(le=128)
IpamOverlapStatus: str = pydantic.constr()
IpamPoolAllocationId: str = pydantic.constr()
IpamPoolAllocationResourceType: str = pydantic.constr()
IpamPoolAwsService: str = pydantic.constr()
IpamPoolCidrFailureCode: str = pydantic.constr()
IpamPoolCidrId: str = pydantic.constr()
IpamPoolCidrState: str = pydantic.constr()
IpamPoolId: str = pydantic.constr()
IpamPoolPublicIpSource: str = pydantic.constr()
IpamPoolState: str = pydantic.constr()
IpamResourceDiscoveryAssociationId: str = pydantic.constr()
IpamResourceDiscoveryAssociationState: str = pydantic.constr()
IpamResourceDiscoveryId: str = pydantic.constr()
IpamResourceDiscoveryState: str = pydantic.constr()
IpamResourceType: str = pydantic.constr()
IpamScopeId: str = pydantic.constr()
IpamScopeState: str = pydantic.constr()
IpamScopeType: str = pydantic.constr()
IpamState: str = pydantic.constr()
Ipv4PoolCoipId: str = pydantic.constr()
Ipv4PoolEc2Id: str = pydantic.constr()
Ipv6Address: str = pydantic.constr()
Ipv6Flag: bool = pydantic.conbool()
Ipv6PoolEc2Id: str = pydantic.constr()
Ipv6PoolMaxResults: int = pydantic.conint(ge=1, le=1000)
Ipv6SupportValue: str = pydantic.constr()
KernelId: str = pydantic.constr()
KeyFormat: str = pydantic.constr()
KeyPairId: str = pydantic.constr()
KeyPairName: str = pydantic.constr()
KeyType: str = pydantic.constr()
KmsKeyId: str = pydantic.constr()
LaunchTemplateAutoRecoveryState: str = pydantic.constr()
LaunchTemplateElasticInferenceAcceleratorCount: int = pydantic.conint(ge=1)
LaunchTemplateErrorCode: str = pydantic.constr()
LaunchTemplateHttpTokensState: str = pydantic.constr()
LaunchTemplateId: str = pydantic.constr()
LaunchTemplateInstanceMetadataEndpointState: str = pydantic.constr()
LaunchTemplateInstanceMetadataOptionsState: str = pydantic.constr()
LaunchTemplateInstanceMetadataProtocolIpv6: str = pydantic.constr()
LaunchTemplateInstanceMetadataTagsState: str = pydantic.constr()
LaunchTemplateName: str = pydantic.constr(min_length=3, max_length=128, regex=r'[a-zA-Z0-9\(\)\.\-/_]+')
ListImagesInRecycleBinMaxResults: int = pydantic.conint(ge=1, le=1000)
ListSnapshotsInRecycleBinMaxResults: int = pydantic.conint(ge=5, le=1000)
ListingState: str = pydantic.constr()
ListingStatus: str = pydantic.constr()
LoadBalancerArn: str = pydantic.constr()
LocalGatewayId: str = pydantic.constr()
LocalGatewayMaxResults: int = pydantic.conint(ge=5, le=1000)
LocalGatewayRouteState: str = pydantic.constr()
LocalGatewayRouteTableMode: str = pydantic.constr()
LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str = pydantic.constr()
LocalGatewayRouteTableVpcAssociationId: str = pydantic.constr()
LocalGatewayRouteType: str = pydantic.constr()
LocalGatewayRoutetableId: str = pydantic.constr()
LocalGatewayVirtualInterfaceGroupId: str = pydantic.constr()
LocalGatewayVirtualInterfaceId: str = pydantic.constr()
LocalStorage: str = pydantic.constr()
LocalStorageType: str = pydantic.constr()
Location: str = pydantic.constr()
LocationType: str = pydantic.constr()
LogDestinationType: str = pydantic.constr()
Long: int = pydantic.conint()
MarketType: str = pydantic.constr()
MaxIpv4AddrPerInterface: int = pydantic.conint()
MaxIpv6AddrPerInterface: int = pydantic.conint()
MaxNetworkInterfaces: int = pydantic.conint()
MaxResults: int = pydantic.conint()
MaxResultsParam: int = pydantic.conint(le=100)
MaximumBandwidthInMbps: int = pydantic.conint()
MaximumEfaInterfaces: int = pydantic.conint()
MaximumIops: int = pydantic.conint()
MaximumNetworkCards: int = pydantic.conint()
MaximumThroughputInMBps: float = pydantic.confloat()
MembershipType: str = pydantic.constr()
MemorySize: int = pydantic.conint()
MetricType: str = pydantic.constr()
MillisecondDateTime: datetime = pydantic.condate()
ModifyAvailabilityZoneOptInStatus: str = pydantic.constr()
MonitoringState: str = pydantic.constr()
MoveStatus: str = pydantic.constr()
MulticastSupportValue: str = pydantic.constr()
NatGatewayAddressStatus: str = pydantic.constr()
NatGatewayId: str = pydantic.constr()
NatGatewayState: str = pydantic.constr()
NetmaskLength: int = pydantic.conint()
NetworkAclAssociationId: str = pydantic.constr()
NetworkAclId: str = pydantic.constr()
NetworkCardIndex: int = pydantic.conint()
NetworkInsightsAccessScopeAnalysisId: str = pydantic.constr()
NetworkInsightsAccessScopeId: str = pydantic.constr()
NetworkInsightsAnalysisId: str = pydantic.constr()
NetworkInsightsMaxResults: int = pydantic.conint(ge=1, le=100)
NetworkInsightsPathId: str = pydantic.constr()
NetworkInsightsResourceId: str = pydantic.constr()
NetworkInterfaceAttachmentId: str = pydantic.constr()
NetworkInterfaceAttribute: str = pydantic.constr()
NetworkInterfaceCreationType: str = pydantic.constr()
NetworkInterfaceId: str = pydantic.constr()
NetworkInterfacePermissionId: str = pydantic.constr()
NetworkInterfacePermissionStateCode: str = pydantic.constr()
NetworkInterfaceStatus: str = pydantic.constr()
NetworkInterfaceType: str = pydantic.constr()
NetworkPerformance: str = pydantic.constr()
NextToken: str = pydantic.constr()
OfferingClassType: str = pydantic.constr()
OfferingId: str = pydantic.constr()
OfferingTypeValues: str = pydantic.constr()
OnDemandAllocationStrategy: str = pydantic.constr()
OperationType: str = pydantic.constr()
OutpostArn: str = pydantic.constr(regex=r'^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$')
PartitionLoadFrequency: str = pydantic.constr()
PayerResponsibility: str = pydantic.constr()
PaymentOption: str = pydantic.constr()
PeriodType: str = pydantic.constr()
PermissionGroup: str = pydantic.constr()
PlacementGroupArn: str = pydantic.constr(regex=r'^arn:aws([a-z-]+)?:ec2:[a-z\d-]+:\d{12}:placement-group/([^\s].+[^\s]){1,255}$')
PlacementGroupId: str = pydantic.constr()
PlacementGroupName: str = pydantic.constr()
PlacementGroupState: str = pydantic.constr()
PlacementGroupStrategy: str = pydantic.constr()
PlacementStrategy: str = pydantic.constr()
PlatformValues: str = pydantic.constr()
PoolMaxResults: int = pydantic.conint(ge=1, le=10)
Port: int = pydantic.conint(le=65535)
PrefixListMaxResults: int = pydantic.conint(ge=1, le=100)
PrefixListResourceId: str = pydantic.constr()
PrefixListState: str = pydantic.constr()
PrincipalType: str = pydantic.constr()
Priority: int = pydantic.conint(ge=-1, le=65535)
PrivateIpAddressCount: int = pydantic.conint(ge=1, le=31)
ProcessorSustainedClockSpeed: float = pydantic.confloat()
ProductCodeValues: str = pydantic.constr()
Protocol: str = pydantic.constr()
ProtocolInt: int = pydantic.conint(le=255)
ProtocolValue: str = pydantic.constr()
PublicIpAddress: str = pydantic.constr()
RIProductDescription: str = pydantic.constr()
RamdiskId: str = pydantic.constr()
RecurringChargeFrequency: str = pydantic.constr()
ReplaceRootVolumeTaskId: str = pydantic.constr()
ReplaceRootVolumeTaskState: str = pydantic.constr()
ReplacementStrategy: str = pydantic.constr()
ReportInstanceReasonCodes: str = pydantic.constr()
ReportStatusType: str = pydantic.constr()
ReservationId: str = pydantic.constr()
ReservationState: str = pydantic.constr()
ReservedInstanceState: str = pydantic.constr()
ReservedInstancesListingId: str = pydantic.constr()
ReservedInstancesModificationId: str = pydantic.constr()
ReservedInstancesOfferingId: str = pydantic.constr()
ResetFpgaImageAttributeName: str = pydantic.constr()
ResetImageAttributeName: str = pydantic.constr()
ResourceArn: str = pydantic.constr(min_length=1, max_length=1283)
ResourceType: str = pydantic.constr()
RestoreSnapshotTierRequestTemporaryRestoreDays: int = pydantic.conint()
ResultRange: int = pydantic.conint(ge=20, le=500)
RoleId: str = pydantic.constr()
RootDeviceType: str = pydantic.constr()
RouteGatewayId: str = pydantic.constr()
RouteOrigin: str = pydantic.constr()
RouteState: str = pydantic.constr()
RouteTableAssociationId: str = pydantic.constr()
RouteTableAssociationStateCode: str = pydantic.constr()
RouteTableId: str = pydantic.constr()
RuleAction: str = pydantic.constr()
RunInstancesUserData: str = pydantic.constr()
ScheduledInstanceId: str = pydantic.constr()
SecurityGroupId: str = pydantic.constr()
SecurityGroupName: str = pydantic.constr()
SecurityGroupRuleId: str = pydantic.constr()
SelfServicePortal: str = pydantic.constr()
SensitiveUrl: str = pydantic.constr()
SensitiveUserData: str = pydantic.constr()
ServiceConnectivityType: str = pydantic.constr()
ServiceState: str = pydantic.constr()
ServiceType: str = pydantic.constr()
ShutdownBehavior: str = pydantic.constr()
SnapshotAttributeName: str = pydantic.constr()
SnapshotId: str = pydantic.constr()
SnapshotState: str = pydantic.constr()
SpotAllocationStrategy: str = pydantic.constr()
SpotFleetRequestId: str = pydantic.constr()
SpotInstanceInterruptionBehavior: str = pydantic.constr()
SpotInstanceRequestId: str = pydantic.constr()
SpotInstanceState: str = pydantic.constr()
SpotInstanceType: str = pydantic.constr()
SpotPlacementScoresMaxResults: int = pydantic.conint(ge=10, le=1000)
SpotPlacementScoresTargetCapacity: int = pydantic.conint(ge=1, le=2000000000)
SpreadLevel: str = pydantic.constr()
State: str = pydantic.constr()
StaticSourcesSupportValue: str = pydantic.constr()
StatisticType: str = pydantic.constr()
Status: str = pydantic.constr()
StatusName: str = pydantic.constr()
StatusType: str = pydantic.constr()
StorageTier: str = pydantic.constr()
String: str = pydantic.constr()
StringType: str = pydantic.constr(max_length=64000)
SubnetCidrAssociationId: str = pydantic.constr()
SubnetCidrBlockStateCode: str = pydantic.constr()
SubnetCidrReservationId: str = pydantic.constr()
SubnetCidrReservationType: str = pydantic.constr()
SubnetId: str = pydantic.constr()
SubnetState: str = pydantic.constr()
SummaryStatus: str = pydantic.constr()
SupportedAdditionalProcessorFeature: str = pydantic.constr()
TaggableResourceId: str = pydantic.constr()
TargetCapacityUnitType: str = pydantic.constr()
TargetStorageTier: str = pydantic.constr()
TelemetryStatus: str = pydantic.constr()
Tenancy: str = pydantic.constr()
ThreadsPerCore: int = pydantic.conint()
TieringOperationStatus: str = pydantic.constr()
TpmSupportValues: str = pydantic.constr()
TrafficDirection: str = pydantic.constr()
TrafficMirrorFilterId: str = pydantic.constr()
TrafficMirrorFilterRuleField: str = pydantic.constr()
TrafficMirrorFilterRuleIdWithResolver: str = pydantic.constr()
TrafficMirrorNetworkService: str = pydantic.constr()
TrafficMirrorRuleAction: str = pydantic.constr()
TrafficMirrorSessionField: str = pydantic.constr()
TrafficMirrorSessionId: str = pydantic.constr()
TrafficMirrorTargetId: str = pydantic.constr()
TrafficMirrorTargetType: str = pydantic.constr()
TrafficMirroringMaxResults: int = pydantic.conint(ge=5, le=1000)
TrafficType: str = pydantic.constr()
TransitAssociationGatewayId: str = pydantic.constr()
TransitGatewayAssociationState: str = pydantic.constr()
TransitGatewayAttachmentId: str = pydantic.constr()
TransitGatewayAttachmentResourceType: str = pydantic.constr()
TransitGatewayAttachmentState: str = pydantic.constr()
TransitGatewayConnectPeerId: str = pydantic.constr()
TransitGatewayConnectPeerState: str = pydantic.constr()
TransitGatewayId: str = pydantic.constr()
TransitGatewayMaxResults: int = pydantic.conint(ge=5, le=1000)
TransitGatewayMulitcastDomainAssociationState: str = pydantic.constr()
TransitGatewayMulticastDomainId: str = pydantic.constr()
TransitGatewayMulticastDomainState: str = pydantic.constr()
TransitGatewayPolicyTableId: str = pydantic.constr()
TransitGatewayPolicyTableState: str = pydantic.constr()
TransitGatewayPrefixListReferenceState: str = pydantic.constr()
TransitGatewayPropagationState: str = pydantic.constr()
TransitGatewayRouteState: str = pydantic.constr()
TransitGatewayRouteTableAnnouncementDirection: str = pydantic.constr()
TransitGatewayRouteTableAnnouncementId: str = pydantic.constr()
TransitGatewayRouteTableAnnouncementState: str = pydantic.constr()
TransitGatewayRouteTableId: str = pydantic.constr()
TransitGatewayRouteTableState: str = pydantic.constr()
TransitGatewayRouteType: str = pydantic.constr()
TransitGatewayState: str = pydantic.constr()
TransportProtocol: str = pydantic.constr()
TrunkInterfaceAssociationId: str = pydantic.constr()
TrustProviderType: str = pydantic.constr()
TunnelInsideIpVersion: str = pydantic.constr()
UnlimitedSupportedInstanceFamily: str = pydantic.constr()
UnsuccessfulInstanceCreditSpecificationErrorCode: str = pydantic.constr()
UsageClassType: str = pydantic.constr()
UserTrustProviderType: str = pydantic.constr()
VCpuCount: int = pydantic.conint()
VerifiedAccessEndpointAttachmentType: str = pydantic.constr()
VerifiedAccessEndpointId: str = pydantic.constr()
VerifiedAccessEndpointPortNumber: int = pydantic.conint(ge=1, le=65535)
VerifiedAccessEndpointProtocol: str = pydantic.constr()
VerifiedAccessEndpointStatusCode: str = pydantic.constr()
VerifiedAccessEndpointType: str = pydantic.constr()
VerifiedAccessGroupId: str = pydantic.constr()
VerifiedAccessInstanceId: str = pydantic.constr()
VerifiedAccessLogDeliveryStatusCode: str = pydantic.constr()
VerifiedAccessTrustProviderId: str = pydantic.constr()
VersionDescription: str = pydantic.constr(max_length=255)
VirtualizationType: str = pydantic.constr()
VolumeAttachmentState: str = pydantic.constr()
VolumeAttributeName: str = pydantic.constr()
VolumeId: str = pydantic.constr()
VolumeIdWithResolver: str = pydantic.constr()
VolumeModificationState: str = pydantic.constr()
VolumeState: str = pydantic.constr()
VolumeStatusInfoStatus: str = pydantic.constr()
VolumeStatusName: str = pydantic.constr()
VolumeType: str = pydantic.constr()
VpcAttributeName: str = pydantic.constr()
VpcCidrAssociationId: str = pydantic.constr()
VpcCidrBlockStateCode: str = pydantic.constr()
VpcEndpointId: str = pydantic.constr()
VpcEndpointServiceId: str = pydantic.constr()
VpcEndpointType: str = pydantic.constr()
VpcFlowLogId: str = pydantic.constr()
VpcId: str = pydantic.constr()
VpcPeeringConnectionId: str = pydantic.constr()
VpcPeeringConnectionIdWithResolver: str = pydantic.constr()
VpcPeeringConnectionStateReasonCode: str = pydantic.constr()
VpcState: str = pydantic.constr()
VpcTenancy: str = pydantic.constr()
VpnConnectionDeviceSampleConfiguration: str = pydantic.constr()
VpnConnectionDeviceTypeId: str = pydantic.constr()
VpnConnectionId: str = pydantic.constr()
VpnEcmpSupportValue: str = pydantic.constr()
VpnGatewayId: str = pydantic.constr()
VpnProtocol: str = pydantic.constr()
VpnState: str = pydantic.constr()
VpnStaticRouteSource: str = pydantic.constr()
WeekDay: str = pydantic.constr()
scope: str = pydantic.constr()
totalFpgaMemory: int = pydantic.conint()
totalGpuMemory: int = pydantic.conint()

AcceleratorManufacturerSet = typing.List["AcceleratorManufacturer"]
AcceleratorNameSet = typing.List["AcceleratorName"]
AcceleratorTypeSet = typing.List["AcceleratorType"]
AccessScopeAnalysisFindingList = typing.List["AccessScopeAnalysisFinding"]
AccessScopePathList = typing.List["AccessScopePath"]
AccessScopePathListRequest = typing.List["AccessScopePathRequest"]
AccountAttributeList = typing.List["AccountAttribute"]
AccountAttributeNameStringList = typing.List["AccountAttributeName"]
AccountAttributeValueList = typing.List["AccountAttributeValue"]
ActiveInstanceSet = typing.List["ActiveInstance"]
AddIpamOperatingRegionSet = typing.List["AddIpamOperatingRegion"]
AddPrefixListEntries = typing.List["AddPrefixListEntry"]
AddedPrincipalSet = typing.List["AddedPrincipal"]
AdditionalDetailList = typing.List["AdditionalDetail"]
AddressList = typing.List["Address"]
AddressSet = typing.List["AddressAttribute"]
AddressTransferList = typing.List["AddressTransfer"]
AllocationIdList = typing.List["AllocationId"]
AllocationIds = typing.List["AllocationId"]
AllowedInstanceTypeSet = typing.List["AllowedInstanceType"]
AllowedPrincipalSet = typing.List["AllowedPrincipal"]
AlternatePathHintList = typing.List["AlternatePathHint"]
AnalysisComponentList = typing.List["AnalysisComponent"]
ArchitectureTypeList = typing.List["ArchitectureType"]
ArchitectureTypeSet = typing.List["ArchitectureType"]
ArnList = typing.List["ResourceArn"]
AssignedPrivateIpAddressList = typing.List["AssignedPrivateIpAddress"]
AssociatedRolesList = typing.List["AssociatedRole"]
AssociatedTargetNetworkSet = typing.List["AssociatedTargetNetwork"]
AssociationIdList = typing.List["IamInstanceProfileAssociationId"]
AthenaIntegrationsSet = typing.List["AthenaIntegration"]
AuthorizationRuleSet = typing.List["AuthorizationRule"]
AvailabilityZoneList = typing.List["AvailabilityZone"]
AvailabilityZoneMessageList = typing.List["AvailabilityZoneMessage"]
AvailabilityZoneStringList = typing.List["String"]
AvailableInstanceCapacityList = typing.List["InstanceCapacity"]
BillingProductList = typing.List["String"]
BlockDeviceMappingList = typing.List["BlockDeviceMapping"]
BlockDeviceMappingRequestList = typing.List["BlockDeviceMapping"]
BootModeTypeList = typing.List["BootModeType"]
BundleIdStringList = typing.List["BundleId"]
BundleTaskList = typing.List["BundleTask"]
ByoipCidrSet = typing.List["ByoipCidr"]
CancelSpotFleetRequestsErrorSet = typing.List["CancelSpotFleetRequestsErrorItem"]
CancelSpotFleetRequestsSuccessSet = typing.List["CancelSpotFleetRequestsSuccessItem"]
CancelledSpotInstanceRequestList = typing.List["CancelledSpotInstanceRequest"]
CapacityAllocations = typing.List["CapacityAllocation"]
CapacityReservationFleetCancellationStateSet = typing.List["CapacityReservationFleetCancellationState"]
CapacityReservationFleetIdSet = typing.List["CapacityReservationFleetId"]
CapacityReservationFleetSet = typing.List["CapacityReservationFleet"]
CapacityReservationGroupSet = typing.List["CapacityReservationGroup"]
CapacityReservationIdSet = typing.List["CapacityReservationId"]
CapacityReservationSet = typing.List["CapacityReservation"]
CarrierGatewayIdSet = typing.List["CarrierGatewayId"]
CarrierGatewaySet = typing.List["CarrierGateway"]
CidrBlockSet = typing.List["CidrBlock"]
ClassicLinkDnsSupportList = typing.List["ClassicLinkDnsSupport"]
ClassicLinkInstanceList = typing.List["ClassicLinkInstance"]
ClassicLoadBalancers = typing.List["ClassicLoadBalancer"]
ClientVpnAuthenticationList = typing.List["ClientVpnAuthentication"]
ClientVpnAuthenticationRequestList = typing.List["ClientVpnAuthenticationRequest"]
ClientVpnConnectionSet = typing.List["ClientVpnConnection"]
ClientVpnEndpointIdList = typing.List["ClientVpnEndpointId"]
ClientVpnRouteSet = typing.List["ClientVpnRoute"]
ClientVpnSecurityGroupIdSet = typing.List["SecurityGroupId"]
CoipAddressUsageSet = typing.List["CoipAddressUsage"]
CoipPoolIdSet = typing.List["Ipv4PoolCoipId"]
CoipPoolSet = typing.List["CoipPool"]
ConnectionNotificationIdsList = typing.List["ConnectionNotificationId"]
ConnectionNotificationSet = typing.List["ConnectionNotification"]
ConversionIdStringList = typing.List["ConversionTaskId"]
CoreCountList = typing.List["CoreCount"]
CpuManufacturerSet = typing.List["CpuManufacturer"]
CreateFleetErrorsSet = typing.List["CreateFleetError"]
CreateFleetInstancesSet = typing.List["CreateFleetInstance"]
CreateVerifiedAccessEndpointSubnetIdList = typing.List["SubnetId"]
CreateVolumePermissionList = typing.List["CreateVolumePermission"]
CustomerGatewayIdStringList = typing.List["CustomerGatewayId"]
CustomerGatewayList = typing.List["CustomerGateway"]
DataQueries = typing.List["DataQuery"]
DataResponses = typing.List["DataResponse"]
DedicatedHostIdList = typing.List["DedicatedHostId"]
DeleteFleetErrorSet = typing.List["DeleteFleetErrorItem"]
DeleteFleetSuccessSet = typing.List["DeleteFleetSuccessItem"]
DeleteLaunchTemplateVersionsResponseErrorSet = typing.List["DeleteLaunchTemplateVersionsResponseErrorItem"]
DeleteLaunchTemplateVersionsResponseSuccessSet = typing.List["DeleteLaunchTemplateVersionsResponseSuccessItem"]
DeleteQueuedReservedInstancesIdList = typing.List["ReservationId"]
DeprovisionedAddressSet = typing.List["String"]
DescribeConversionTaskList = typing.List["ConversionTask"]
DescribeFastLaunchImagesSuccessSet = typing.List["DescribeFastLaunchImagesSuccessItem"]
DescribeFastSnapshotRestoreSuccessSet = typing.List["DescribeFastSnapshotRestoreSuccessItem"]
DescribeFleetsErrorSet = typing.List["DescribeFleetError"]
DescribeFleetsInstancesSet = typing.List["DescribeFleetsInstances"]
DhcpConfigurationList = typing.List["DhcpConfiguration"]
DhcpConfigurationValueList = typing.List["AttributeValue"]
DhcpOptionsIdStringList = typing.List["DhcpOptionsId"]
DhcpOptionsList = typing.List["DhcpOptions"]
DisableFastSnapshotRestoreErrorSet = typing.List["DisableFastSnapshotRestoreErrorItem"]
DisableFastSnapshotRestoreStateErrorSet = typing.List["DisableFastSnapshotRestoreStateErrorItem"]
DisableFastSnapshotRestoreSuccessSet = typing.List["DisableFastSnapshotRestoreSuccessItem"]
DiskImageList = typing.List["DiskImage"]
DiskInfoList = typing.List["DiskInfo"]
DnsEntrySet = typing.List["DnsEntry"]
EgressOnlyInternetGatewayIdList = typing.List["EgressOnlyInternetGatewayId"]
EgressOnlyInternetGatewayList = typing.List["EgressOnlyInternetGateway"]
EipAssociationIdList = typing.List["ElasticIpAssociationId"]
ElasticGpuAssociationList = typing.List["ElasticGpuAssociation"]
ElasticGpuIdSet = typing.List["ElasticGpuId"]
ElasticGpuSet = typing.List["ElasticGpus"]
ElasticGpuSpecificationList = typing.List["ElasticGpuSpecification"]
ElasticGpuSpecificationResponseList = typing.List["ElasticGpuSpecificationResponse"]
ElasticGpuSpecifications = typing.List["ElasticGpuSpecification"]
ElasticInferenceAcceleratorAssociationList = typing.List["ElasticInferenceAcceleratorAssociation"]
ElasticInferenceAccelerators = typing.List["ElasticInferenceAccelerator"]
EnableFastSnapshotRestoreErrorSet = typing.List["EnableFastSnapshotRestoreErrorItem"]
EnableFastSnapshotRestoreStateErrorSet = typing.List["EnableFastSnapshotRestoreStateErrorItem"]
EnableFastSnapshotRestoreSuccessSet = typing.List["EnableFastSnapshotRestoreSuccessItem"]
EndpointSet = typing.List["ClientVpnEndpoint"]
ErrorSet = typing.List["ValidationError"]
ExcludedInstanceTypeSet = typing.List["ExcludedInstanceType"]
ExecutableByStringList = typing.List["String"]
ExplanationList = typing.List["Explanation"]
ExportImageTaskIdList = typing.List["ExportImageTaskId"]
ExportImageTaskList = typing.List["ExportImageTask"]
ExportTaskIdStringList = typing.List["ExportTaskId"]
ExportTaskList = typing.List["ExportTask"]
FailedCapacityReservationFleetCancellationResultSet = typing.List["FailedCapacityReservationFleetCancellationResult"]
FailedQueuedPurchaseDeletionSet = typing.List["FailedQueuedPurchaseDeletion"]
FastLaunchImageIdList = typing.List["ImageId"]
FilterList = typing.List["Filter"]
FleetCapacityReservationSet = typing.List["FleetCapacityReservation"]
FleetIdSet = typing.List["FleetId"]
FleetLaunchTemplateConfigList = typing.List["FleetLaunchTemplateConfig"]
FleetLaunchTemplateConfigListRequest = typing.List["FleetLaunchTemplateConfigRequest"]
FleetLaunchTemplateOverridesList = typing.List["FleetLaunchTemplateOverrides"]
FleetLaunchTemplateOverridesListRequest = typing.List["FleetLaunchTemplateOverridesRequest"]
FleetSet = typing.List["FleetData"]
FlowLogIdList = typing.List["VpcFlowLogId"]
FlowLogResourceIds = typing.List["FlowLogResourceId"]
FlowLogSet = typing.List["FlowLog"]
FpgaDeviceInfoList = typing.List["FpgaDeviceInfo"]
FpgaImageIdList = typing.List["FpgaImageId"]
FpgaImageList = typing.List["FpgaImage"]
GpuDeviceInfoList = typing.List["GpuDeviceInfo"]
GroupIdStringList = typing.List["SecurityGroupId"]
GroupIdentifierList = typing.List["GroupIdentifier"]
GroupIdentifierSet = typing.List["SecurityGroupIdentifier"]
GroupIds = typing.List["SecurityGroupId"]
GroupNameStringList = typing.List["SecurityGroupName"]
HistoryRecordSet = typing.List["HistoryRecordEntry"]
HistoryRecords = typing.List["HistoryRecord"]
HostInstanceList = typing.List["HostInstance"]
HostList = typing.List["Host"]
HostOfferingSet = typing.List["HostOffering"]
HostReservationIdSet = typing.List["HostReservationId"]
HostReservationSet = typing.List["HostReservation"]
IKEVersionsList = typing.List["IKEVersionsListValue"]
IKEVersionsRequestList = typing.List["IKEVersionsRequestListValue"]
IamInstanceProfileAssociationSet = typing.List["IamInstanceProfileAssociation"]
IdFormatList = typing.List["IdFormat"]
ImageDiskContainerList = typing.List["ImageDiskContainer"]
ImageIdList = typing.List["ImageId"]
ImageIdStringList = typing.List["ImageId"]
ImageList = typing.List["Image"]
ImageRecycleBinInfoList = typing.List["ImageRecycleBinInfo"]
ImportImageLicenseSpecificationListRequest = typing.List["ImportImageLicenseConfigurationRequest"]
ImportImageLicenseSpecificationListResponse = typing.List["ImportImageLicenseConfigurationResponse"]
ImportImageTaskList = typing.List["ImportImageTask"]
ImportInstanceVolumeDetailSet = typing.List["ImportInstanceVolumeDetailItem"]
ImportSnapshotTaskIdList = typing.List["ImportSnapshotTaskId"]
ImportSnapshotTaskList = typing.List["ImportSnapshotTask"]
ImportTaskIdList = typing.List["ImportImageTaskId"]
InferenceDeviceInfoList = typing.List["InferenceDeviceInfo"]
InsideCidrBlocksStringList = typing.List["String"]
InstanceBlockDeviceMappingList = typing.List["InstanceBlockDeviceMapping"]
InstanceBlockDeviceMappingSpecificationList = typing.List["InstanceBlockDeviceMappingSpecification"]
InstanceCountList = typing.List["InstanceCount"]
InstanceCreditSpecificationList = typing.List["InstanceCreditSpecification"]
InstanceCreditSpecificationListRequest = typing.List["InstanceCreditSpecificationRequest"]
InstanceEventWindowIdSet = typing.List["InstanceEventWindowId"]
InstanceEventWindowSet = typing.List["InstanceEventWindow"]
InstanceEventWindowTimeRangeList = typing.List["InstanceEventWindowTimeRange"]
InstanceEventWindowTimeRangeRequestSet = typing.List["InstanceEventWindowTimeRangeRequest"]
InstanceGenerationSet = typing.List["InstanceGeneration"]
InstanceIdList = typing.List["InstanceId"]
InstanceIdSet = typing.List["InstanceId"]
InstanceIdStringList = typing.List["InstanceId"]
InstanceIdsSet = typing.List["InstanceId"]
InstanceIpv4PrefixList = typing.List["InstanceIpv4Prefix"]
InstanceIpv6AddressList = typing.List["InstanceIpv6Address"]
InstanceIpv6AddressListRequest = typing.List["InstanceIpv6AddressRequest"]
InstanceIpv6PrefixList = typing.List["InstanceIpv6Prefix"]
InstanceList = typing.List["Instance"]
InstanceMonitoringList = typing.List["InstanceMonitoring"]
InstanceNetworkInterfaceList = typing.List["InstanceNetworkInterface"]
InstanceNetworkInterfaceSpecificationList = typing.List["InstanceNetworkInterfaceSpecification"]
InstancePrivateIpAddressList = typing.List["InstancePrivateIpAddress"]
InstanceStateChangeList = typing.List["InstanceStateChange"]
InstanceStatusDetailsList = typing.List["InstanceStatusDetails"]
InstanceStatusEventList = typing.List["InstanceStatusEvent"]
InstanceStatusList = typing.List["InstanceStatus"]
InstanceTagKeySet = typing.List["String"]
InstanceTypeInfoFromInstanceRequirementsSet = typing.List["InstanceTypeInfoFromInstanceRequirements"]
InstanceTypeInfoList = typing.List["InstanceTypeInfo"]
InstanceTypeList = typing.List["InstanceType"]
InstanceTypeOfferingsList = typing.List["InstanceTypeOffering"]
InstanceTypes = typing.List["String"]
InstanceTypesList = typing.List["String"]
InstanceUsageSet = typing.List["InstanceUsage"]
InternetGatewayAttachmentList = typing.List["InternetGatewayAttachment"]
InternetGatewayIdList = typing.List["InternetGatewayId"]
InternetGatewayList = typing.List["InternetGateway"]
IpAddressList = typing.List["IpAddress"]
IpList = typing.List["String"]
IpPermissionList = typing.List["IpPermission"]
IpPrefixList = typing.List["String"]
IpRangeList = typing.List["IpRange"]
IpRanges = typing.List["String"]
IpamAddressHistoryRecordSet = typing.List["IpamAddressHistoryRecord"]
IpamDiscoveredAccountSet = typing.List["IpamDiscoveredAccount"]
IpamDiscoveredResourceCidrSet = typing.List["IpamDiscoveredResourceCidr"]
IpamOperatingRegionSet = typing.List["IpamOperatingRegion"]
IpamPoolAllocationDisallowedCidrs = typing.List["String"]
IpamPoolAllocationSet = typing.List["IpamPoolAllocation"]
IpamPoolCidrSet = typing.List["IpamPoolCidr"]
IpamPoolSet = typing.List["IpamPool"]
IpamResourceCidrSet = typing.List["IpamResourceCidr"]
IpamResourceDiscoveryAssociationSet = typing.List["IpamResourceDiscoveryAssociation"]
IpamResourceDiscoverySet = typing.List["IpamResourceDiscovery"]
IpamResourceTagList = typing.List["IpamResourceTag"]
IpamScopeSet = typing.List["IpamScope"]
IpamSet = typing.List["Ipam"]
Ipv4PrefixList = typing.List["Ipv4PrefixSpecificationRequest"]
Ipv4PrefixListResponse = typing.List["Ipv4PrefixSpecificationResponse"]
Ipv4PrefixesList = typing.List["Ipv4PrefixSpecification"]
Ipv6AddressList = typing.List["String"]
Ipv6CidrAssociationSet = typing.List["Ipv6CidrAssociation"]
Ipv6CidrBlockSet = typing.List["Ipv6CidrBlock"]
Ipv6PoolIdList = typing.List["Ipv6PoolEc2Id"]
Ipv6PoolSet = typing.List["Ipv6Pool"]
Ipv6PrefixList = typing.List["Ipv6PrefixSpecificationRequest"]
Ipv6PrefixListResponse = typing.List["Ipv6PrefixSpecificationResponse"]
Ipv6PrefixesList = typing.List["Ipv6PrefixSpecification"]
Ipv6RangeList = typing.List["Ipv6Range"]
KeyNameStringList = typing.List["KeyPairName"]
KeyPairIdStringList = typing.List["KeyPairId"]
KeyPairList = typing.List["KeyPairInfo"]
LaunchPermissionList = typing.List["LaunchPermission"]
LaunchSpecsList = typing.List["SpotFleetLaunchSpecification"]
LaunchTemplateBlockDeviceMappingList = typing.List["LaunchTemplateBlockDeviceMapping"]
LaunchTemplateBlockDeviceMappingRequestList = typing.List["LaunchTemplateBlockDeviceMappingRequest"]
LaunchTemplateConfigList = typing.List["LaunchTemplateConfig"]
LaunchTemplateElasticInferenceAcceleratorList = typing.List["LaunchTemplateElasticInferenceAccelerator"]
LaunchTemplateElasticInferenceAcceleratorResponseList = typing.List["LaunchTemplateElasticInferenceAcceleratorResponse"]
LaunchTemplateIdStringList = typing.List["LaunchTemplateId"]
LaunchTemplateInstanceNetworkInterfaceSpecificationList = typing.List["LaunchTemplateInstanceNetworkInterfaceSpecification"]
LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList = typing.List["LaunchTemplateInstanceNetworkInterfaceSpecificationRequest"]
LaunchTemplateLicenseList = typing.List["LaunchTemplateLicenseConfiguration"]
LaunchTemplateLicenseSpecificationListRequest = typing.List["LaunchTemplateLicenseConfigurationRequest"]
LaunchTemplateNameStringList = typing.List["LaunchTemplateName"]
LaunchTemplateOverridesList = typing.List["LaunchTemplateOverrides"]
LaunchTemplateSet = typing.List["LaunchTemplate"]
LaunchTemplateTagSpecificationList = typing.List["LaunchTemplateTagSpecification"]
LaunchTemplateTagSpecificationRequestList = typing.List["LaunchTemplateTagSpecificationRequest"]
LaunchTemplateVersionSet = typing.List["LaunchTemplateVersion"]
LicenseList = typing.List["LicenseConfiguration"]
LicenseSpecificationListRequest = typing.List["LicenseConfigurationRequest"]
LoadPermissionList = typing.List["LoadPermission"]
LoadPermissionListRequest = typing.List["LoadPermissionRequest"]
LocalGatewayIdSet = typing.List["LocalGatewayId"]
LocalGatewayRouteList = typing.List["LocalGatewayRoute"]
LocalGatewayRouteTableIdSet = typing.List["LocalGatewayRoutetableId"]
LocalGatewayRouteTableSet = typing.List["LocalGatewayRouteTable"]
LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet = typing.List["LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"]
LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet = typing.List["LocalGatewayRouteTableVirtualInterfaceGroupAssociation"]
LocalGatewayRouteTableVpcAssociationIdSet = typing.List["LocalGatewayRouteTableVpcAssociationId"]
LocalGatewayRouteTableVpcAssociationSet = typing.List["LocalGatewayRouteTableVpcAssociation"]
LocalGatewaySet = typing.List["LocalGateway"]
LocalGatewayVirtualInterfaceGroupIdSet = typing.List["LocalGatewayVirtualInterfaceGroupId"]
LocalGatewayVirtualInterfaceGroupSet = typing.List["LocalGatewayVirtualInterfaceGroup"]
LocalGatewayVirtualInterfaceIdSet = typing.List["LocalGatewayVirtualInterfaceId"]
LocalGatewayVirtualInterfaceSet = typing.List["LocalGatewayVirtualInterface"]
LocalStorageTypeSet = typing.List["LocalStorageType"]
ManagedPrefixListSet = typing.List["ManagedPrefixList"]
MetricPoints = typing.List["MetricPoint"]
ModifyVerifiedAccessEndpointSubnetIdList = typing.List["SubnetId"]
MovingAddressStatusSet = typing.List["MovingAddressStatus"]
NatGatewayAddressList = typing.List["NatGatewayAddress"]
NatGatewayIdStringList = typing.List["NatGatewayId"]
NatGatewayList = typing.List["NatGateway"]
NetworkAclAssociationList = typing.List["NetworkAclAssociation"]
NetworkAclEntryList = typing.List["NetworkAclEntry"]
NetworkAclIdStringList = typing.List["NetworkAclId"]
NetworkAclList = typing.List["NetworkAcl"]
NetworkCardInfoList = typing.List["NetworkCardInfo"]
NetworkInsightsAccessScopeAnalysisIdList = typing.List["NetworkInsightsAccessScopeAnalysisId"]
NetworkInsightsAccessScopeAnalysisList = typing.List["NetworkInsightsAccessScopeAnalysis"]
NetworkInsightsAccessScopeIdList = typing.List["NetworkInsightsAccessScopeId"]
NetworkInsightsAccessScopeList = typing.List["NetworkInsightsAccessScope"]
NetworkInsightsAnalysisIdList = typing.List["NetworkInsightsAnalysisId"]
NetworkInsightsAnalysisList = typing.List["NetworkInsightsAnalysis"]
NetworkInsightsPathIdList = typing.List["NetworkInsightsPathId"]
NetworkInsightsPathList = typing.List["NetworkInsightsPath"]
NetworkInterfaceIdList = typing.List["NetworkInterfaceId"]
NetworkInterfaceIpv6AddressesList = typing.List["NetworkInterfaceIpv6Address"]
NetworkInterfaceList = typing.List["NetworkInterface"]
NetworkInterfacePermissionIdList = typing.List["NetworkInterfacePermissionId"]
NetworkInterfacePermissionList = typing.List["NetworkInterfacePermission"]
NetworkInterfacePrivateIpAddressList = typing.List["NetworkInterfacePrivateIpAddress"]
NewDhcpConfigurationList = typing.List["NewDhcpConfiguration"]
OccurrenceDayRequestSet = typing.List["Integer"]
OccurrenceDaySet = typing.List["Integer"]
OrganizationArnStringList = typing.List["String"]
OrganizationalUnitArnStringList = typing.List["String"]
OwnerStringList = typing.List["String"]
PathComponentList = typing.List["PathComponent"]
Phase1DHGroupNumbersList = typing.List["Phase1DHGroupNumbersListValue"]
Phase1DHGroupNumbersRequestList = typing.List["Phase1DHGroupNumbersRequestListValue"]
Phase1EncryptionAlgorithmsList = typing.List["Phase1EncryptionAlgorithmsListValue"]
Phase1EncryptionAlgorithmsRequestList = typing.List["Phase1EncryptionAlgorithmsRequestListValue"]
Phase1IntegrityAlgorithmsList = typing.List["Phase1IntegrityAlgorithmsListValue"]
Phase1IntegrityAlgorithmsRequestList = typing.List["Phase1IntegrityAlgorithmsRequestListValue"]
Phase2DHGroupNumbersList = typing.List["Phase2DHGroupNumbersListValue"]
Phase2DHGroupNumbersRequestList = typing.List["Phase2DHGroupNumbersRequestListValue"]
Phase2EncryptionAlgorithmsList = typing.List["Phase2EncryptionAlgorithmsListValue"]
Phase2EncryptionAlgorithmsRequestList = typing.List["Phase2EncryptionAlgorithmsRequestListValue"]
Phase2IntegrityAlgorithmsList = typing.List["Phase2IntegrityAlgorithmsListValue"]
Phase2IntegrityAlgorithmsRequestList = typing.List["Phase2IntegrityAlgorithmsRequestListValue"]
PlacementGroupIdStringList = typing.List["PlacementGroupId"]
PlacementGroupList = typing.List["PlacementGroup"]
PlacementGroupStrategyList = typing.List["PlacementGroupStrategy"]
PlacementGroupStringList = typing.List["PlacementGroupName"]
PoolCidrBlocksSet = typing.List["PoolCidrBlock"]
PortRangeList = typing.List["PortRange"]
PrefixListAssociationSet = typing.List["PrefixListAssociation"]
PrefixListEntrySet = typing.List["PrefixListEntry"]
PrefixListIdList = typing.List["PrefixListId"]
PrefixListIdSet = typing.List["String"]
PrefixListResourceIdStringList = typing.List["PrefixListResourceId"]
PrefixListSet = typing.List["PrefixList"]
PriceScheduleList = typing.List["PriceSchedule"]
PriceScheduleSpecificationList = typing.List["PriceScheduleSpecification"]
PricingDetailsList = typing.List["PricingDetail"]
PrincipalIdFormatList = typing.List["PrincipalIdFormat"]
PrivateDnsDetailsSet = typing.List["PrivateDnsDetails"]
PrivateIpAddressConfigSet = typing.List["ScheduledInstancesPrivateIpAddressConfig"]
PrivateIpAddressSpecificationList = typing.List["PrivateIpAddressSpecification"]
PrivateIpAddressStringList = typing.List["String"]
ProductCodeList = typing.List["ProductCode"]
ProductCodeStringList = typing.List["String"]
ProductDescriptionList = typing.List["String"]
PropagatingVgwList = typing.List["PropagatingVgw"]
ProtocolIntList = typing.List["ProtocolInt"]
ProtocolList = typing.List["Protocol"]
PublicIpStringList = typing.List["String"]
PublicIpv4PoolIdStringList = typing.List["Ipv4PoolEc2Id"]
PublicIpv4PoolRangeSet = typing.List["PublicIpv4PoolRange"]
PublicIpv4PoolSet = typing.List["PublicIpv4Pool"]
PurchaseRequestSet = typing.List["PurchaseRequest"]
PurchaseSet = typing.List["Purchase"]
PurchasedScheduledInstanceSet = typing.List["ScheduledInstance"]
ReasonCodesList = typing.List["ReportInstanceReasonCodes"]
RecurringChargesList = typing.List["RecurringCharge"]
RegionList = typing.List["Region"]
RegionNameStringList = typing.List["String"]
RegionNames = typing.List["String"]
RemoveIpamOperatingRegionSet = typing.List["RemoveIpamOperatingRegion"]
RemovePrefixListEntries = typing.List["RemovePrefixListEntry"]
ReplaceRootVolumeTaskIds = typing.List["ReplaceRootVolumeTaskId"]
ReplaceRootVolumeTasks = typing.List["ReplaceRootVolumeTask"]
RequestHostIdList = typing.List["DedicatedHostId"]
RequestHostIdSet = typing.List["DedicatedHostId"]
RequestInstanceTypeList = typing.List["InstanceType"]
RequestIpamResourceTagList = typing.List["RequestIpamResourceTag"]
RequestSpotLaunchSpecificationSecurityGroupIdList = typing.List["SecurityGroupId"]
RequestSpotLaunchSpecificationSecurityGroupList = typing.List["String"]
ReservationFleetInstanceSpecificationList = typing.List["ReservationFleetInstanceSpecification"]
ReservationList = typing.List["Reservation"]
ReservedInstanceIdSet = typing.List["ReservationId"]
ReservedInstanceReservationValueSet = typing.List["ReservedInstanceReservationValue"]
ReservedInstancesConfigurationList = typing.List["ReservedInstancesConfiguration"]
ReservedInstancesIdStringList = typing.List["ReservationId"]
ReservedInstancesList = typing.List["ReservedInstances"]
ReservedInstancesListingList = typing.List["ReservedInstancesListing"]
ReservedInstancesModificationIdStringList = typing.List["ReservedInstancesModificationId"]
ReservedInstancesModificationList = typing.List["ReservedInstancesModification"]
ReservedInstancesModificationResultList = typing.List["ReservedInstancesModificationResult"]
ReservedInstancesOfferingIdStringList = typing.List["ReservedInstancesOfferingId"]
ReservedInstancesOfferingList = typing.List["ReservedInstancesOffering"]
ReservedIntancesIds = typing.List["ReservedInstancesId"]
ResourceIdList = typing.List["TaggableResourceId"]
ResourceList = typing.List["String"]
ResponseHostIdList = typing.List["String"]
ResponseHostIdSet = typing.List["String"]
RestorableByStringList = typing.List["String"]
RootDeviceTypeList = typing.List["RootDeviceType"]
RouteList = typing.List["Route"]
RouteTableAssociationList = typing.List["RouteTableAssociation"]
RouteTableIdStringList = typing.List["RouteTableId"]
RouteTableList = typing.List["RouteTable"]
RuleGroupRuleOptionsPairList = typing.List["RuleGroupRuleOptionsPair"]
RuleGroupTypePairList = typing.List["RuleGroupTypePair"]
RuleOptionList = typing.List["RuleOption"]
S3ObjectTagList = typing.List["S3ObjectTag"]
ScheduledInstanceAvailabilitySet = typing.List["ScheduledInstanceAvailability"]
ScheduledInstanceIdRequestSet = typing.List["ScheduledInstanceId"]
ScheduledInstanceSet = typing.List["ScheduledInstance"]
ScheduledInstancesBlockDeviceMappingSet = typing.List["ScheduledInstancesBlockDeviceMapping"]
ScheduledInstancesIpv6AddressList = typing.List["ScheduledInstancesIpv6Address"]
ScheduledInstancesNetworkInterfaceSet = typing.List["ScheduledInstancesNetworkInterface"]
ScheduledInstancesSecurityGroupIdSet = typing.List["SecurityGroupId"]
SecurityGroupIdList = typing.List["SecurityGroupId"]
SecurityGroupIdStringList = typing.List["SecurityGroupId"]
SecurityGroupList = typing.List["SecurityGroup"]
SecurityGroupReferences = typing.List["SecurityGroupReference"]
SecurityGroupRuleDescriptionList = typing.List["SecurityGroupRuleDescription"]
SecurityGroupRuleIdList = typing.List["String"]
SecurityGroupRuleList = typing.List["SecurityGroupRule"]
SecurityGroupRuleUpdateList = typing.List["SecurityGroupRuleUpdate"]
SecurityGroupStringList = typing.List["SecurityGroupName"]
ServiceConfigurationSet = typing.List["ServiceConfiguration"]
ServiceDetailSet = typing.List["ServiceDetail"]
ServiceTypeDetailSet = typing.List["ServiceTypeDetail"]
SnapshotDetailList = typing.List["SnapshotDetail"]
SnapshotIdStringList = typing.List["SnapshotId"]
SnapshotList = typing.List["Snapshot"]
SnapshotRecycleBinInfoList = typing.List["SnapshotRecycleBinInfo"]
SnapshotSet = typing.List["SnapshotInfo"]
SpotFleetRequestConfigSet = typing.List["SpotFleetRequestConfig"]
SpotFleetRequestIdList = typing.List["SpotFleetRequestId"]
SpotFleetTagSpecificationList = typing.List["SpotFleetTagSpecification"]
SpotInstanceRequestIdList = typing.List["SpotInstanceRequestId"]
SpotInstanceRequestList = typing.List["SpotInstanceRequest"]
SpotPlacementScores = typing.List["SpotPlacementScore"]
SpotPriceHistoryList = typing.List["SpotPrice"]
StaleIpPermissionSet = typing.List["StaleIpPermission"]
StaleSecurityGroupSet = typing.List["StaleSecurityGroup"]
StoreImageTaskResultSet = typing.List["StoreImageTaskResult"]
StringList = typing.List["String"]
SubnetAssociationList = typing.List["SubnetAssociation"]
SubnetCidrReservationList = typing.List["SubnetCidrReservation"]
SubnetIdStringList = typing.List["SubnetId"]
SubnetIpv6CidrBlockAssociationSet = typing.List["SubnetIpv6CidrBlockAssociation"]
SubnetList = typing.List["Subnet"]
SubscriptionList = typing.List["Subscription"]
SuccessfulInstanceCreditSpecificationSet = typing.List["SuccessfulInstanceCreditSpecificationItem"]
SuccessfulQueuedPurchaseDeletionSet = typing.List["SuccessfulQueuedPurchaseDeletion"]
SupportedAdditionalProcessorFeatureList = typing.List["SupportedAdditionalProcessorFeature"]
SupportedIpAddressTypes = typing.List["ServiceConnectivityType"]
TagDescriptionList = typing.List["TagDescription"]
TagList = typing.List["Tag"]
TagSpecificationList = typing.List["TagSpecification"]
TargetConfigurationRequestSet = typing.List["TargetConfigurationRequest"]
TargetGroups = typing.List["TargetGroup"]
TargetNetworkSet = typing.List["TargetNetwork"]
TargetReservationValueSet = typing.List["TargetReservationValue"]
TerminateConnectionStatusSet = typing.List["TerminateConnectionStatus"]
ThreadsPerCoreList = typing.List["ThreadsPerCore"]
ThroughResourcesStatementList = typing.List["ThroughResourcesStatement"]
ThroughResourcesStatementRequestList = typing.List["ThroughResourcesStatementRequest"]
TrafficMirrorFilterIdList = typing.List["TrafficMirrorFilterId"]
TrafficMirrorFilterRuleFieldList = typing.List["TrafficMirrorFilterRuleField"]
TrafficMirrorFilterRuleList = typing.List["TrafficMirrorFilterRule"]
TrafficMirrorFilterSet = typing.List["TrafficMirrorFilter"]
TrafficMirrorNetworkServiceList = typing.List["TrafficMirrorNetworkService"]
TrafficMirrorSessionFieldList = typing.List["TrafficMirrorSessionField"]
TrafficMirrorSessionIdList = typing.List["TrafficMirrorSessionId"]
TrafficMirrorSessionSet = typing.List["TrafficMirrorSession"]
TrafficMirrorTargetIdList = typing.List["TrafficMirrorTargetId"]
TrafficMirrorTargetSet = typing.List["TrafficMirrorTarget"]
TransitGatewayAttachmentBgpConfigurationList = typing.List["TransitGatewayAttachmentBgpConfiguration"]
TransitGatewayAttachmentIdStringList = typing.List["TransitGatewayAttachmentId"]
TransitGatewayAttachmentList = typing.List["TransitGatewayAttachment"]
TransitGatewayAttachmentPropagationList = typing.List["TransitGatewayAttachmentPropagation"]
TransitGatewayCidrBlockStringList = typing.List["String"]
TransitGatewayConnectList = typing.List["TransitGatewayConnect"]
TransitGatewayConnectPeerIdStringList = typing.List["TransitGatewayConnectPeerId"]
TransitGatewayConnectPeerList = typing.List["TransitGatewayConnectPeer"]
TransitGatewayIdStringList = typing.List["TransitGatewayId"]
TransitGatewayList = typing.List["TransitGateway"]
TransitGatewayMulticastDomainAssociationList = typing.List["TransitGatewayMulticastDomainAssociation"]
TransitGatewayMulticastDomainIdStringList = typing.List["TransitGatewayMulticastDomainId"]
TransitGatewayMulticastDomainList = typing.List["TransitGatewayMulticastDomain"]
TransitGatewayMulticastGroupList = typing.List["TransitGatewayMulticastGroup"]
TransitGatewayNetworkInterfaceIdList = typing.List["NetworkInterfaceId"]
TransitGatewayPeeringAttachmentList = typing.List["TransitGatewayPeeringAttachment"]
TransitGatewayPolicyTableAssociationList = typing.List["TransitGatewayPolicyTableAssociation"]
TransitGatewayPolicyTableEntryList = typing.List["TransitGatewayPolicyTableEntry"]
TransitGatewayPolicyTableIdStringList = typing.List["TransitGatewayPolicyTableId"]
TransitGatewayPolicyTableList = typing.List["TransitGatewayPolicyTable"]
TransitGatewayPrefixListReferenceSet = typing.List["TransitGatewayPrefixListReference"]
TransitGatewayRouteAttachmentList = typing.List["TransitGatewayRouteAttachment"]
TransitGatewayRouteList = typing.List["TransitGatewayRoute"]
TransitGatewayRouteTableAnnouncementIdStringList = typing.List["TransitGatewayRouteTableAnnouncementId"]
TransitGatewayRouteTableAnnouncementList = typing.List["TransitGatewayRouteTableAnnouncement"]
TransitGatewayRouteTableAssociationList = typing.List["TransitGatewayRouteTableAssociation"]
TransitGatewayRouteTableIdStringList = typing.List["TransitGatewayRouteTableId"]
TransitGatewayRouteTableList = typing.List["TransitGatewayRouteTable"]
TransitGatewayRouteTablePropagationList = typing.List["TransitGatewayRouteTablePropagation"]
TransitGatewaySubnetIdList = typing.List["SubnetId"]
TransitGatewayVpcAttachmentList = typing.List["TransitGatewayVpcAttachment"]
TrunkInterfaceAssociationIdList = typing.List["TrunkInterfaceAssociationId"]
TrunkInterfaceAssociationList = typing.List["TrunkInterfaceAssociation"]
TunnelOptionsList = typing.List["TunnelOption"]
UnsuccessfulInstanceCreditSpecificationSet = typing.List["UnsuccessfulInstanceCreditSpecificationItem"]
UnsuccessfulItemList = typing.List["UnsuccessfulItem"]
UnsuccessfulItemSet = typing.List["UnsuccessfulItem"]
UsageClassTypeList = typing.List["UsageClassType"]
UserGroupStringList = typing.List["String"]
UserIdGroupPairList = typing.List["UserIdGroupPair"]
UserIdGroupPairSet = typing.List["UserIdGroupPair"]
UserIdStringList = typing.List["String"]
ValueStringList = typing.List["String"]
VerifiedAccessEndpointIdList = typing.List["VerifiedAccessEndpointId"]
VerifiedAccessEndpointList = typing.List["VerifiedAccessEndpoint"]
VerifiedAccessEndpointSubnetIdList = typing.List["SubnetId"]
VerifiedAccessGroupIdList = typing.List["VerifiedAccessGroupId"]
VerifiedAccessGroupList = typing.List["VerifiedAccessGroup"]
VerifiedAccessInstanceIdList = typing.List["VerifiedAccessInstanceId"]
VerifiedAccessInstanceList = typing.List["VerifiedAccessInstance"]
VerifiedAccessInstanceLoggingConfigurationList = typing.List["VerifiedAccessInstanceLoggingConfiguration"]
VerifiedAccessTrustProviderCondensedList = typing.List["VerifiedAccessTrustProviderCondensed"]
VerifiedAccessTrustProviderIdList = typing.List["VerifiedAccessTrustProviderId"]
VerifiedAccessTrustProviderList = typing.List["VerifiedAccessTrustProvider"]
VersionStringList = typing.List["String"]
VgwTelemetryList = typing.List["VgwTelemetry"]
VirtualizationTypeList = typing.List["VirtualizationType"]
VirtualizationTypeSet = typing.List["VirtualizationType"]
VolumeAttachmentList = typing.List["VolumeAttachment"]
VolumeIdStringList = typing.List["VolumeId"]
VolumeList = typing.List["Volume"]
VolumeModificationList = typing.List["VolumeModification"]
VolumeStatusActionsList = typing.List["VolumeStatusAction"]
VolumeStatusAttachmentStatusList = typing.List["VolumeStatusAttachmentStatus"]
VolumeStatusDetailsList = typing.List["VolumeStatusDetails"]
VolumeStatusEventsList = typing.List["VolumeStatusEvent"]
VolumeStatusList = typing.List["VolumeStatusItem"]
VpcAttachmentList = typing.List["VpcAttachment"]
VpcCidrBlockAssociationSet = typing.List["VpcCidrBlockAssociation"]
VpcClassicLinkIdList = typing.List["VpcId"]
VpcClassicLinkList = typing.List["VpcClassicLink"]
VpcEndpointConnectionSet = typing.List["VpcEndpointConnection"]
VpcEndpointIdList = typing.List["VpcEndpointId"]
VpcEndpointRouteTableIdList = typing.List["RouteTableId"]
VpcEndpointSecurityGroupIdList = typing.List["SecurityGroupId"]
VpcEndpointServiceIdList = typing.List["VpcEndpointServiceId"]
VpcEndpointSet = typing.List["VpcEndpoint"]
VpcEndpointSubnetIdList = typing.List["SubnetId"]
VpcIdStringList = typing.List["VpcId"]
VpcIpv6CidrBlockAssociationSet = typing.List["VpcIpv6CidrBlockAssociation"]
VpcList = typing.List["Vpc"]
VpcPeeringConnectionIdList = typing.List["VpcPeeringConnectionId"]
VpcPeeringConnectionList = typing.List["VpcPeeringConnection"]
VpnConnectionDeviceTypeList = typing.List["VpnConnectionDeviceType"]
VpnConnectionIdStringList = typing.List["VpnConnectionId"]
VpnConnectionList = typing.List["VpnConnection"]
VpnGatewayIdStringList = typing.List["VpnGatewayId"]
VpnGatewayList = typing.List["VpnGateway"]
VpnStaticRouteList = typing.List["VpnStaticRoute"]
VpnTunnelOptionsSpecificationsList = typing.List["VpnTunnelOptionsSpecification"]
ZoneIdStringList = typing.List["String"]
ZoneNameStringList = typing.List["String"]
snapshotTierStatusSet = typing.List["SnapshotTierStatus"]

class AcceleratorManufacturer(enum.Enum):
    NVIDIA = 'nvidia'
    AMD = 'amd'
    AMAZON_WEB_SERVICES = 'amazon-web-services'
    XILINX = 'xilinx'

class AcceleratorName(enum.Enum):
    A100 = 'a100'
    V100 = 'v100'
    K80 = 'k80'
    T4 = 't4'
    M60 = 'm60'
    RADEON_PRO_V520 = 'radeon-pro-v520'
    VU9P = 'vu9p'
    INFERENTIA = 'inferentia'
    K520 = 'k520'

class AcceleratorType(enum.Enum):
    GPU = 'gpu'
    FPGA = 'fpga'
    INFERENCE = 'inference'

class AccountAttributeName(enum.Enum):
    SUPPORTED_PLATFORMS = 'supported-platforms'
    DEFAULT_VPC = 'default-vpc'

class ActivityStatus(enum.Enum):
    ERROR = 'error'
    PENDING_FULFILLMENT = 'pending_fulfillment'
    PENDING_TERMINATION = 'pending_termination'
    FULFILLED = 'fulfilled'

class AddressAttributeName(enum.Enum):
    DOMAIN_NAME = 'domain-name'

class AddressFamily(enum.Enum):
    IPV4 = 'ipv4'
    IPV6 = 'ipv6'

class AddressTransferStatus(enum.Enum):
    PENDING = 'pending'
    DISABLED = 'disabled'
    ACCEPTED = 'accepted'

class Affinity(enum.Enum):
    DEFAULT = 'default'
    HOST = 'host'

class AllocationState(enum.Enum):
    AVAILABLE = 'available'
    UNDER_ASSESSMENT = 'under-assessment'
    PERMANENT_FAILURE = 'permanent-failure'
    RELEASED = 'released'
    RELEASED_PERMANENT_FAILURE = 'released-permanent-failure'
    PENDING = 'pending'

class AllocationStrategy(enum.Enum):
    LOWESTPRICE = 'lowestPrice'
    DIVERSIFIED = 'diversified'
    CAPACITYOPTIMIZED = 'capacityOptimized'
    CAPACITYOPTIMIZEDPRIORITIZED = 'capacityOptimizedPrioritized'
    PRICECAPACITYOPTIMIZED = 'priceCapacityOptimized'

class AllocationType(enum.Enum):
    USED = 'used'

class AllowsMultipleInstanceTypes(enum.Enum):
    ON = 'on'
    OFF = 'off'

class AmdSevSnpSpecification(enum.Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class AnalysisStatus(enum.Enum):
    RUNNING = 'running'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'

class ApplianceModeSupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class ArchitectureType(enum.Enum):
    I386 = 'i386'
    X86_64 = 'x86_64'
    ARM64 = 'arm64'
    X86_64_MAC = 'x86_64_mac'
    ARM64_MAC = 'arm64_mac'

class ArchitectureValues(enum.Enum):
    I386 = 'i386'
    X86_64 = 'x86_64'
    ARM64 = 'arm64'
    X86_64_MAC = 'x86_64_mac'
    ARM64_MAC = 'arm64_mac'

class AssociatedNetworkType(enum.Enum):
    VPC = 'vpc'

class AssociationStatusCode(enum.Enum):
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    ASSOCIATION_FAILED = 'association-failed'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'

class AttachmentStatus(enum.Enum):
    ATTACHING = 'attaching'
    ATTACHED = 'attached'
    DETACHING = 'detaching'
    DETACHED = 'detached'

class AutoAcceptSharedAssociationsValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class AutoAcceptSharedAttachmentsValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class AutoPlacement(enum.Enum):
    ON = 'on'
    OFF = 'off'

class AvailabilityZoneOptInStatus(enum.Enum):
    OPT_IN_NOT_REQUIRED = 'opt-in-not-required'
    OPTED_IN = 'opted-in'
    NOT_OPTED_IN = 'not-opted-in'

class AvailabilityZoneState(enum.Enum):
    AVAILABLE = 'available'
    INFORMATION = 'information'
    IMPAIRED = 'impaired'
    UNAVAILABLE = 'unavailable'

class BareMetal(enum.Enum):
    INCLUDED = 'included'
    REQUIRED = 'required'
    EXCLUDED = 'excluded'

class BatchState(enum.Enum):
    SUBMITTED = 'submitted'
    ACTIVE = 'active'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    CANCELLED_RUNNING = 'cancelled_running'
    CANCELLED_TERMINATING = 'cancelled_terminating'
    MODIFYING = 'modifying'

class BgpStatus(enum.Enum):
    UP = 'up'
    DOWN = 'down'

class BootModeType(enum.Enum):
    LEGACY_BIOS = 'legacy-bios'
    UEFI = 'uefi'

class BootModeValues(enum.Enum):
    LEGACY_BIOS = 'legacy-bios'
    UEFI = 'uefi'
    UEFI_PREFERRED = 'uefi-preferred'

class BundleTaskState(enum.Enum):
    PENDING = 'pending'
    WAITING_FOR_SHUTDOWN = 'waiting-for-shutdown'
    BUNDLING = 'bundling'
    STORING = 'storing'
    CANCELLING = 'cancelling'
    COMPLETE = 'complete'
    FAILED = 'failed'

class BurstablePerformance(enum.Enum):
    INCLUDED = 'included'
    REQUIRED = 'required'
    EXCLUDED = 'excluded'

class ByoipCidrState(enum.Enum):
    ADVERTISED = 'advertised'
    DEPROVISIONED = 'deprovisioned'
    FAILED_DEPROVISION = 'failed-deprovision'
    FAILED_PROVISION = 'failed-provision'
    PENDING_DEPROVISION = 'pending-deprovision'
    PENDING_PROVISION = 'pending-provision'
    PROVISIONED = 'provisioned'
    PROVISIONED_NOT_PUBLICLY_ADVERTISABLE = 'provisioned-not-publicly-advertisable'

class CancelBatchErrorCode(enum.Enum):
    FLEETREQUESTIDDOESNOTEXIST = 'fleetRequestIdDoesNotExist'
    FLEETREQUESTIDMALFORMED = 'fleetRequestIdMalformed'
    FLEETREQUESTNOTINCANCELLABLESTATE = 'fleetRequestNotInCancellableState'
    UNEXPECTEDERROR = 'unexpectedError'

class CancelSpotInstanceRequestState(enum.Enum):
    ACTIVE = 'active'
    OPEN = 'open'
    CLOSED = 'closed'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'

class CapacityReservationFleetState(enum.Enum):
    SUBMITTED = 'submitted'
    MODIFYING = 'modifying'
    ACTIVE = 'active'
    PARTIALLY_FULFILLED = 'partially_fulfilled'
    EXPIRING = 'expiring'
    EXPIRED = 'expired'
    CANCELLING = 'cancelling'
    CANCELLED = 'cancelled'
    FAILED = 'failed'

class CapacityReservationInstancePlatform(enum.Enum):
    LINUX_UNIX = 'Linux/UNIX'
    RED_HAT_ENTERPRISE_LINUX = 'Red Hat Enterprise Linux'
    SUSE_LINUX = 'SUSE Linux'
    WINDOWS = 'Windows'
    WINDOWS_WITH_SQL_SERVER = 'Windows with SQL Server'
    WINDOWS_WITH_SQL_SERVER_ENTERPRISE = 'Windows with SQL Server Enterprise'
    WINDOWS_WITH_SQL_SERVER_STANDARD = 'Windows with SQL Server Standard'
    WINDOWS_WITH_SQL_SERVER_WEB = 'Windows with SQL Server Web'
    LINUX_WITH_SQL_SERVER_STANDARD = 'Linux with SQL Server Standard'
    LINUX_WITH_SQL_SERVER_WEB = 'Linux with SQL Server Web'
    LINUX_WITH_SQL_SERVER_ENTERPRISE = 'Linux with SQL Server Enterprise'
    RHEL_WITH_SQL_SERVER_STANDARD = 'RHEL with SQL Server Standard'
    RHEL_WITH_SQL_SERVER_ENTERPRISE = 'RHEL with SQL Server Enterprise'
    RHEL_WITH_SQL_SERVER_WEB = 'RHEL with SQL Server Web'
    RHEL_WITH_HA = 'RHEL with HA'
    RHEL_WITH_HA_AND_SQL_SERVER_STANDARD = 'RHEL with HA and SQL Server Standard'
    RHEL_WITH_HA_AND_SQL_SERVER_ENTERPRISE = 'RHEL with HA and SQL Server Enterprise'

class CapacityReservationPreference(enum.Enum):
    OPEN = 'open'
    NONE = 'none'

class CapacityReservationState(enum.Enum):
    ACTIVE = 'active'
    EXPIRED = 'expired'
    CANCELLED = 'cancelled'
    PENDING = 'pending'
    FAILED = 'failed'

class CapacityReservationTenancy(enum.Enum):
    DEFAULT = 'default'
    DEDICATED = 'dedicated'

class CarrierGatewayState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class ClientCertificateRevocationListStatusCode(enum.Enum):
    PENDING = 'pending'
    ACTIVE = 'active'

class ClientVpnAuthenticationType(enum.Enum):
    CERTIFICATE_AUTHENTICATION = 'certificate-authentication'
    DIRECTORY_SERVICE_AUTHENTICATION = 'directory-service-authentication'
    FEDERATED_AUTHENTICATION = 'federated-authentication'

class ClientVpnAuthorizationRuleStatusCode(enum.Enum):
    AUTHORIZING = 'authorizing'
    ACTIVE = 'active'
    FAILED = 'failed'
    REVOKING = 'revoking'

class ClientVpnConnectionStatusCode(enum.Enum):
    ACTIVE = 'active'
    FAILED_TO_TERMINATE = 'failed-to-terminate'
    TERMINATING = 'terminating'
    TERMINATED = 'terminated'

class ClientVpnEndpointAttributeStatusCode(enum.Enum):
    APPLYING = 'applying'
    APPLIED = 'applied'

class ClientVpnEndpointStatusCode(enum.Enum):
    PENDING_ASSOCIATE = 'pending-associate'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class ClientVpnRouteStatusCode(enum.Enum):
    CREATING = 'creating'
    ACTIVE = 'active'
    FAILED = 'failed'
    DELETING = 'deleting'

class ConnectionNotificationState(enum.Enum):
    ENABLED = 'Enabled'
    DISABLED = 'Disabled'

class ConnectionNotificationType(enum.Enum):
    TOPIC = 'Topic'

class ConnectivityType(enum.Enum):
    PRIVATE = 'private'
    PUBLIC = 'public'

class ContainerFormat(enum.Enum):
    OVA = 'ova'

class ConversionTaskState(enum.Enum):
    ACTIVE = 'active'
    CANCELLING = 'cancelling'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'

class CopyTagsFromSource(enum.Enum):
    VOLUME = 'volume'

class CpuManufacturer(enum.Enum):
    INTEL = 'intel'
    AMD = 'amd'
    AMAZON_WEB_SERVICES = 'amazon-web-services'

class CurrencyCodeValues(enum.Enum):
    USD = 'USD'

class DatafeedSubscriptionState(enum.Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

class DefaultRouteTableAssociationValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class DefaultRouteTablePropagationValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class DefaultTargetCapacityType(enum.Enum):
    SPOT = 'spot'
    ON_DEMAND = 'on-demand'

class DeleteFleetErrorCode(enum.Enum):
    FLEETIDDOESNOTEXIST = 'fleetIdDoesNotExist'
    FLEETIDMALFORMED = 'fleetIdMalformed'
    FLEETNOTINDELETABLESTATE = 'fleetNotInDeletableState'
    UNEXPECTEDERROR = 'unexpectedError'

class DeleteQueuedReservedInstancesErrorCode(enum.Enum):
    RESERVED_INSTANCES_ID_INVALID = 'reserved-instances-id-invalid'
    RESERVED_INSTANCES_NOT_IN_QUEUED_STATE = 'reserved-instances-not-in-queued-state'
    UNEXPECTED_ERROR = 'unexpected-error'

class DestinationFileFormat(enum.Enum):
    PLAIN_TEXT = 'plain-text'
    PARQUET = 'parquet'

class DeviceTrustProviderType(enum.Enum):
    JAMF = 'jamf'
    CROWDSTRIKE = 'crowdstrike'

class DeviceType(enum.Enum):
    EBS = 'ebs'
    INSTANCE_STORE = 'instance-store'

class DiskImageFormat(enum.Enum):
    VMDK = 'VMDK'
    RAW = 'RAW'
    VHD = 'VHD'

class DiskType(enum.Enum):
    HDD = 'hdd'
    SSD = 'ssd'

class DnsNameState(enum.Enum):
    PENDINGVERIFICATION = 'pendingVerification'
    VERIFIED = 'verified'
    FAILED = 'failed'

class DnsRecordIpType(enum.Enum):
    IPV4 = 'ipv4'
    DUALSTACK = 'dualstack'
    IPV6 = 'ipv6'
    SERVICE_DEFINED = 'service-defined'

class DnsSupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class DomainType(enum.Enum):
    VPC = 'vpc'
    STANDARD = 'standard'

class DynamicRoutingValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class EbsEncryptionSupport(enum.Enum):
    UNSUPPORTED = 'unsupported'
    SUPPORTED = 'supported'

class EbsNvmeSupport(enum.Enum):
    UNSUPPORTED = 'unsupported'
    SUPPORTED = 'supported'
    REQUIRED = 'required'

class EbsOptimizedSupport(enum.Enum):
    UNSUPPORTED = 'unsupported'
    SUPPORTED = 'supported'
    DEFAULT = 'default'

class ElasticGpuState(enum.Enum):
    ATTACHED = 'ATTACHED'

class ElasticGpuStatus(enum.Enum):
    OK = 'OK'
    IMPAIRED = 'IMPAIRED'

class EnaSupport(enum.Enum):
    UNSUPPORTED = 'unsupported'
    SUPPORTED = 'supported'
    REQUIRED = 'required'

class EndDateType(enum.Enum):
    UNLIMITED = 'unlimited'
    LIMITED = 'limited'

class EphemeralNvmeSupport(enum.Enum):
    UNSUPPORTED = 'unsupported'
    SUPPORTED = 'supported'
    REQUIRED = 'required'

class EventCode(enum.Enum):
    INSTANCE_REBOOT = 'instance-reboot'
    SYSTEM_REBOOT = 'system-reboot'
    SYSTEM_MAINTENANCE = 'system-maintenance'
    INSTANCE_RETIREMENT = 'instance-retirement'
    INSTANCE_STOP = 'instance-stop'

class EventType(enum.Enum):
    INSTANCECHANGE = 'instanceChange'
    FLEETREQUESTCHANGE = 'fleetRequestChange'
    ERROR = 'error'
    INFORMATION = 'information'

class ExcessCapacityTerminationPolicy(enum.Enum):
    NOTERMINATION = 'noTermination'
    DEFAULT = 'default'

class ExportEnvironment(enum.Enum):
    CITRIX = 'citrix'
    VMWARE = 'vmware'
    MICROSOFT = 'microsoft'

class ExportTaskState(enum.Enum):
    ACTIVE = 'active'
    CANCELLING = 'cancelling'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'

class FastLaunchResourceType(enum.Enum):
    SNAPSHOT = 'snapshot'

class FastLaunchStateCode(enum.Enum):
    ENABLING = 'enabling'
    ENABLING_FAILED = 'enabling-failed'
    ENABLED = 'enabled'
    ENABLED_FAILED = 'enabled-failed'
    DISABLING = 'disabling'
    DISABLING_FAILED = 'disabling-failed'

class FastSnapshotRestoreStateCode(enum.Enum):
    ENABLING = 'enabling'
    OPTIMIZING = 'optimizing'
    ENABLED = 'enabled'
    DISABLING = 'disabling'
    DISABLED = 'disabled'

class FindingsFound(enum.Enum):
    TRUE = 'true'
    FALSE = 'false'
    UNKNOWN = 'unknown'

class FleetActivityStatus(enum.Enum):
    ERROR = 'error'
    PENDING_FULFILLMENT = 'pending_fulfillment'
    PENDING_TERMINATION = 'pending_termination'
    FULFILLED = 'fulfilled'

class FleetCapacityReservationTenancy(enum.Enum):
    DEFAULT = 'default'

class FleetCapacityReservationUsageStrategy(enum.Enum):
    USE_CAPACITY_RESERVATIONS_FIRST = 'use-capacity-reservations-first'

class FleetEventType(enum.Enum):
    INSTANCE_CHANGE = 'instance-change'
    FLEET_CHANGE = 'fleet-change'
    SERVICE_ERROR = 'service-error'

class FleetExcessCapacityTerminationPolicy(enum.Enum):
    NO_TERMINATION = 'no-termination'
    TERMINATION = 'termination'

class FleetInstanceMatchCriteria(enum.Enum):
    OPEN = 'open'

class FleetOnDemandAllocationStrategy(enum.Enum):
    LOWEST_PRICE = 'lowest-price'
    PRIORITIZED = 'prioritized'

class FleetReplacementStrategy(enum.Enum):
    LAUNCH = 'launch'
    LAUNCH_BEFORE_TERMINATE = 'launch-before-terminate'

class FleetStateCode(enum.Enum):
    SUBMITTED = 'submitted'
    ACTIVE = 'active'
    DELETED = 'deleted'
    FAILED = 'failed'
    DELETED_RUNNING = 'deleted_running'
    DELETED_TERMINATING = 'deleted_terminating'
    MODIFYING = 'modifying'

class FleetType(enum.Enum):
    REQUEST = 'request'
    MAINTAIN = 'maintain'
    INSTANT = 'instant'

class FlowLogsResourceType(enum.Enum):
    VPC = 'VPC'
    SUBNET = 'Subnet'
    NETWORKINTERFACE = 'NetworkInterface'
    TRANSITGATEWAY = 'TransitGateway'
    TRANSITGATEWAYATTACHMENT = 'TransitGatewayAttachment'

class FpgaImageAttributeName(enum.Enum):
    DESCRIPTION = 'description'
    NAME = 'name'
    LOADPERMISSION = 'loadPermission'
    PRODUCTCODES = 'productCodes'

class FpgaImageStateCode(enum.Enum):
    PENDING = 'pending'
    FAILED = 'failed'
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'

class GatewayAssociationState(enum.Enum):
    ASSOCIATED = 'associated'
    NOT_ASSOCIATED = 'not-associated'
    ASSOCIATING = 'associating'
    DISASSOCIATING = 'disassociating'

class GatewayType(enum.Enum):
    IPSEC_1 = 'ipsec.1'

class HostMaintenance(enum.Enum):
    ON = 'on'
    OFF = 'off'

class HostRecovery(enum.Enum):
    ON = 'on'
    OFF = 'off'

class HostTenancy(enum.Enum):
    DEDICATED = 'dedicated'
    HOST = 'host'

class HostnameType(enum.Enum):
    IP_NAME = 'ip-name'
    RESOURCE_NAME = 'resource-name'

class HttpTokensState(enum.Enum):
    OPTIONAL = 'optional'
    REQUIRED = 'required'

class HypervisorType(enum.Enum):
    OVM = 'ovm'
    XEN = 'xen'

class IamInstanceProfileAssociationState(enum.Enum):
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'

class Igmpv2SupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class ImageAttributeName(enum.Enum):
    DESCRIPTION = 'description'
    KERNEL = 'kernel'
    RAMDISK = 'ramdisk'
    LAUNCHPERMISSION = 'launchPermission'
    PRODUCTCODES = 'productCodes'
    BLOCKDEVICEMAPPING = 'blockDeviceMapping'
    SRIOVNETSUPPORT = 'sriovNetSupport'
    BOOTMODE = 'bootMode'
    TPMSUPPORT = 'tpmSupport'
    UEFIDATA = 'uefiData'
    LASTLAUNCHEDTIME = 'lastLaunchedTime'
    IMDSSUPPORT = 'imdsSupport'

class ImageState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    INVALID = 'invalid'
    DEREGISTERED = 'deregistered'
    TRANSIENT = 'transient'
    FAILED = 'failed'
    ERROR = 'error'

class ImageTypeValues(enum.Enum):
    MACHINE = 'machine'
    KERNEL = 'kernel'
    RAMDISK = 'ramdisk'

class ImdsSupportValues(enum.Enum):
    V2_0 = 'v2.0'

class InstanceAttributeName(enum.Enum):
    INSTANCETYPE = 'instanceType'
    KERNEL = 'kernel'
    RAMDISK = 'ramdisk'
    USERDATA = 'userData'
    DISABLEAPITERMINATION = 'disableApiTermination'
    INSTANCEINITIATEDSHUTDOWNBEHAVIOR = 'instanceInitiatedShutdownBehavior'
    ROOTDEVICENAME = 'rootDeviceName'
    BLOCKDEVICEMAPPING = 'blockDeviceMapping'
    PRODUCTCODES = 'productCodes'
    SOURCEDESTCHECK = 'sourceDestCheck'
    GROUPSET = 'groupSet'
    EBSOPTIMIZED = 'ebsOptimized'
    SRIOVNETSUPPORT = 'sriovNetSupport'
    ENASUPPORT = 'enaSupport'
    ENCLAVEOPTIONS = 'enclaveOptions'
    DISABLEAPISTOP = 'disableApiStop'

class InstanceAutoRecoveryState(enum.Enum):
    DISABLED = 'disabled'
    DEFAULT = 'default'

class InstanceBootModeValues(enum.Enum):
    LEGACY_BIOS = 'legacy-bios'
    UEFI = 'uefi'

class InstanceEventWindowState(enum.Enum):
    CREATING = 'creating'
    DELETING = 'deleting'
    ACTIVE = 'active'
    DELETED = 'deleted'

class InstanceGeneration(enum.Enum):
    CURRENT = 'current'
    PREVIOUS = 'previous'

class InstanceHealthStatus(enum.Enum):
    HEALTHY = 'healthy'
    UNHEALTHY = 'unhealthy'

class InstanceInterruptionBehavior(enum.Enum):
    HIBERNATE = 'hibernate'
    STOP = 'stop'
    TERMINATE = 'terminate'

class InstanceLifecycle(enum.Enum):
    SPOT = 'spot'
    ON_DEMAND = 'on-demand'

class InstanceLifecycleType(enum.Enum):
    SPOT = 'spot'
    SCHEDULED = 'scheduled'

class InstanceMatchCriteria(enum.Enum):
    OPEN = 'open'
    TARGETED = 'targeted'

class InstanceMetadataEndpointState(enum.Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class InstanceMetadataOptionsState(enum.Enum):
    PENDING = 'pending'
    APPLIED = 'applied'

class InstanceMetadataProtocolState(enum.Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class InstanceMetadataTagsState(enum.Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class InstanceStateName(enum.Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    SHUTTING_DOWN = 'shutting-down'
    TERMINATED = 'terminated'
    STOPPING = 'stopping'
    STOPPED = 'stopped'

class InstanceStorageEncryptionSupport(enum.Enum):
    UNSUPPORTED = 'unsupported'
    REQUIRED = 'required'

class InstanceType(enum.Enum):
    A1_MEDIUM = 'a1.medium'
    A1_LARGE = 'a1.large'
    A1_XLARGE = 'a1.xlarge'
    A1_2XLARGE = 'a1.2xlarge'
    A1_4XLARGE = 'a1.4xlarge'
    A1_METAL = 'a1.metal'
    C1_MEDIUM = 'c1.medium'
    C1_XLARGE = 'c1.xlarge'
    C3_LARGE = 'c3.large'
    C3_XLARGE = 'c3.xlarge'
    C3_2XLARGE = 'c3.2xlarge'
    C3_4XLARGE = 'c3.4xlarge'
    C3_8XLARGE = 'c3.8xlarge'
    C4_LARGE = 'c4.large'
    C4_XLARGE = 'c4.xlarge'
    C4_2XLARGE = 'c4.2xlarge'
    C4_4XLARGE = 'c4.4xlarge'
    C4_8XLARGE = 'c4.8xlarge'
    C5_LARGE = 'c5.large'
    C5_XLARGE = 'c5.xlarge'
    C5_2XLARGE = 'c5.2xlarge'
    C5_4XLARGE = 'c5.4xlarge'
    C5_9XLARGE = 'c5.9xlarge'
    C5_12XLARGE = 'c5.12xlarge'
    C5_18XLARGE = 'c5.18xlarge'
    C5_24XLARGE = 'c5.24xlarge'
    C5_METAL = 'c5.metal'
    C5A_LARGE = 'c5a.large'
    C5A_XLARGE = 'c5a.xlarge'
    C5A_2XLARGE = 'c5a.2xlarge'
    C5A_4XLARGE = 'c5a.4xlarge'
    C5A_8XLARGE = 'c5a.8xlarge'
    C5A_12XLARGE = 'c5a.12xlarge'
    C5A_16XLARGE = 'c5a.16xlarge'
    C5A_24XLARGE = 'c5a.24xlarge'
    C5AD_LARGE = 'c5ad.large'
    C5AD_XLARGE = 'c5ad.xlarge'
    C5AD_2XLARGE = 'c5ad.2xlarge'
    C5AD_4XLARGE = 'c5ad.4xlarge'
    C5AD_8XLARGE = 'c5ad.8xlarge'
    C5AD_12XLARGE = 'c5ad.12xlarge'
    C5AD_16XLARGE = 'c5ad.16xlarge'
    C5AD_24XLARGE = 'c5ad.24xlarge'
    C5D_LARGE = 'c5d.large'
    C5D_XLARGE = 'c5d.xlarge'
    C5D_2XLARGE = 'c5d.2xlarge'
    C5D_4XLARGE = 'c5d.4xlarge'
    C5D_9XLARGE = 'c5d.9xlarge'
    C5D_12XLARGE = 'c5d.12xlarge'
    C5D_18XLARGE = 'c5d.18xlarge'
    C5D_24XLARGE = 'c5d.24xlarge'
    C5D_METAL = 'c5d.metal'
    C5N_LARGE = 'c5n.large'
    C5N_XLARGE = 'c5n.xlarge'
    C5N_2XLARGE = 'c5n.2xlarge'
    C5N_4XLARGE = 'c5n.4xlarge'
    C5N_9XLARGE = 'c5n.9xlarge'
    C5N_18XLARGE = 'c5n.18xlarge'
    C5N_METAL = 'c5n.metal'
    C6G_MEDIUM = 'c6g.medium'
    C6G_LARGE = 'c6g.large'
    C6G_XLARGE = 'c6g.xlarge'
    C6G_2XLARGE = 'c6g.2xlarge'
    C6G_4XLARGE = 'c6g.4xlarge'
    C6G_8XLARGE = 'c6g.8xlarge'
    C6G_12XLARGE = 'c6g.12xlarge'
    C6G_16XLARGE = 'c6g.16xlarge'
    C6G_METAL = 'c6g.metal'
    C6GD_MEDIUM = 'c6gd.medium'
    C6GD_LARGE = 'c6gd.large'
    C6GD_XLARGE = 'c6gd.xlarge'
    C6GD_2XLARGE = 'c6gd.2xlarge'
    C6GD_4XLARGE = 'c6gd.4xlarge'
    C6GD_8XLARGE = 'c6gd.8xlarge'
    C6GD_12XLARGE = 'c6gd.12xlarge'
    C6GD_16XLARGE = 'c6gd.16xlarge'
    C6GD_METAL = 'c6gd.metal'
    C6GN_MEDIUM = 'c6gn.medium'
    C6GN_LARGE = 'c6gn.large'
    C6GN_XLARGE = 'c6gn.xlarge'
    C6GN_2XLARGE = 'c6gn.2xlarge'
    C6GN_4XLARGE = 'c6gn.4xlarge'
    C6GN_8XLARGE = 'c6gn.8xlarge'
    C6GN_12XLARGE = 'c6gn.12xlarge'
    C6GN_16XLARGE = 'c6gn.16xlarge'
    C6I_LARGE = 'c6i.large'
    C6I_XLARGE = 'c6i.xlarge'
    C6I_2XLARGE = 'c6i.2xlarge'
    C6I_4XLARGE = 'c6i.4xlarge'
    C6I_8XLARGE = 'c6i.8xlarge'
    C6I_12XLARGE = 'c6i.12xlarge'
    C6I_16XLARGE = 'c6i.16xlarge'
    C6I_24XLARGE = 'c6i.24xlarge'
    C6I_32XLARGE = 'c6i.32xlarge'
    C6I_METAL = 'c6i.metal'
    CC1_4XLARGE = 'cc1.4xlarge'
    CC2_8XLARGE = 'cc2.8xlarge'
    CG1_4XLARGE = 'cg1.4xlarge'
    CR1_8XLARGE = 'cr1.8xlarge'
    D2_XLARGE = 'd2.xlarge'
    D2_2XLARGE = 'd2.2xlarge'
    D2_4XLARGE = 'd2.4xlarge'
    D2_8XLARGE = 'd2.8xlarge'
    D3_XLARGE = 'd3.xlarge'
    D3_2XLARGE = 'd3.2xlarge'
    D3_4XLARGE = 'd3.4xlarge'
    D3_8XLARGE = 'd3.8xlarge'
    D3EN_XLARGE = 'd3en.xlarge'
    D3EN_2XLARGE = 'd3en.2xlarge'
    D3EN_4XLARGE = 'd3en.4xlarge'
    D3EN_6XLARGE = 'd3en.6xlarge'
    D3EN_8XLARGE = 'd3en.8xlarge'
    D3EN_12XLARGE = 'd3en.12xlarge'
    DL1_24XLARGE = 'dl1.24xlarge'
    F1_2XLARGE = 'f1.2xlarge'
    F1_4XLARGE = 'f1.4xlarge'
    F1_16XLARGE = 'f1.16xlarge'
    G2_2XLARGE = 'g2.2xlarge'
    G2_8XLARGE = 'g2.8xlarge'
    G3_4XLARGE = 'g3.4xlarge'
    G3_8XLARGE = 'g3.8xlarge'
    G3_16XLARGE = 'g3.16xlarge'
    G3S_XLARGE = 'g3s.xlarge'
    G4AD_XLARGE = 'g4ad.xlarge'
    G4AD_2XLARGE = 'g4ad.2xlarge'
    G4AD_4XLARGE = 'g4ad.4xlarge'
    G4AD_8XLARGE = 'g4ad.8xlarge'
    G4AD_16XLARGE = 'g4ad.16xlarge'
    G4DN_XLARGE = 'g4dn.xlarge'
    G4DN_2XLARGE = 'g4dn.2xlarge'
    G4DN_4XLARGE = 'g4dn.4xlarge'
    G4DN_8XLARGE = 'g4dn.8xlarge'
    G4DN_12XLARGE = 'g4dn.12xlarge'
    G4DN_16XLARGE = 'g4dn.16xlarge'
    G4DN_METAL = 'g4dn.metal'
    G5_XLARGE = 'g5.xlarge'
    G5_2XLARGE = 'g5.2xlarge'
    G5_4XLARGE = 'g5.4xlarge'
    G5_8XLARGE = 'g5.8xlarge'
    G5_12XLARGE = 'g5.12xlarge'
    G5_16XLARGE = 'g5.16xlarge'
    G5_24XLARGE = 'g5.24xlarge'
    G5_48XLARGE = 'g5.48xlarge'
    G5G_XLARGE = 'g5g.xlarge'
    G5G_2XLARGE = 'g5g.2xlarge'
    G5G_4XLARGE = 'g5g.4xlarge'
    G5G_8XLARGE = 'g5g.8xlarge'
    G5G_16XLARGE = 'g5g.16xlarge'
    G5G_METAL = 'g5g.metal'
    HI1_4XLARGE = 'hi1.4xlarge'
    HPC6A_48XLARGE = 'hpc6a.48xlarge'
    HS1_8XLARGE = 'hs1.8xlarge'
    H1_2XLARGE = 'h1.2xlarge'
    H1_4XLARGE = 'h1.4xlarge'
    H1_8XLARGE = 'h1.8xlarge'
    H1_16XLARGE = 'h1.16xlarge'
    I2_XLARGE = 'i2.xlarge'
    I2_2XLARGE = 'i2.2xlarge'
    I2_4XLARGE = 'i2.4xlarge'
    I2_8XLARGE = 'i2.8xlarge'
    I3_LARGE = 'i3.large'
    I3_XLARGE = 'i3.xlarge'
    I3_2XLARGE = 'i3.2xlarge'
    I3_4XLARGE = 'i3.4xlarge'
    I3_8XLARGE = 'i3.8xlarge'
    I3_16XLARGE = 'i3.16xlarge'
    I3_METAL = 'i3.metal'
    I3EN_LARGE = 'i3en.large'
    I3EN_XLARGE = 'i3en.xlarge'
    I3EN_2XLARGE = 'i3en.2xlarge'
    I3EN_3XLARGE = 'i3en.3xlarge'
    I3EN_6XLARGE = 'i3en.6xlarge'
    I3EN_12XLARGE = 'i3en.12xlarge'
    I3EN_24XLARGE = 'i3en.24xlarge'
    I3EN_METAL = 'i3en.metal'
    IM4GN_LARGE = 'im4gn.large'
    IM4GN_XLARGE = 'im4gn.xlarge'
    IM4GN_2XLARGE = 'im4gn.2xlarge'
    IM4GN_4XLARGE = 'im4gn.4xlarge'
    IM4GN_8XLARGE = 'im4gn.8xlarge'
    IM4GN_16XLARGE = 'im4gn.16xlarge'
    INF1_XLARGE = 'inf1.xlarge'
    INF1_2XLARGE = 'inf1.2xlarge'
    INF1_6XLARGE = 'inf1.6xlarge'
    INF1_24XLARGE = 'inf1.24xlarge'
    IS4GEN_MEDIUM = 'is4gen.medium'
    IS4GEN_LARGE = 'is4gen.large'
    IS4GEN_XLARGE = 'is4gen.xlarge'
    IS4GEN_2XLARGE = 'is4gen.2xlarge'
    IS4GEN_4XLARGE = 'is4gen.4xlarge'
    IS4GEN_8XLARGE = 'is4gen.8xlarge'
    M1_SMALL = 'm1.small'
    M1_MEDIUM = 'm1.medium'
    M1_LARGE = 'm1.large'
    M1_XLARGE = 'm1.xlarge'
    M2_XLARGE = 'm2.xlarge'
    M2_2XLARGE = 'm2.2xlarge'
    M2_4XLARGE = 'm2.4xlarge'
    M3_MEDIUM = 'm3.medium'
    M3_LARGE = 'm3.large'
    M3_XLARGE = 'm3.xlarge'
    M3_2XLARGE = 'm3.2xlarge'
    M4_LARGE = 'm4.large'
    M4_XLARGE = 'm4.xlarge'
    M4_2XLARGE = 'm4.2xlarge'
    M4_4XLARGE = 'm4.4xlarge'
    M4_10XLARGE = 'm4.10xlarge'
    M4_16XLARGE = 'm4.16xlarge'
    M5_LARGE = 'm5.large'
    M5_XLARGE = 'm5.xlarge'
    M5_2XLARGE = 'm5.2xlarge'
    M5_4XLARGE = 'm5.4xlarge'
    M5_8XLARGE = 'm5.8xlarge'
    M5_12XLARGE = 'm5.12xlarge'
    M5_16XLARGE = 'm5.16xlarge'
    M5_24XLARGE = 'm5.24xlarge'
    M5_METAL = 'm5.metal'
    M5A_LARGE = 'm5a.large'
    M5A_XLARGE = 'm5a.xlarge'
    M5A_2XLARGE = 'm5a.2xlarge'
    M5A_4XLARGE = 'm5a.4xlarge'
    M5A_8XLARGE = 'm5a.8xlarge'
    M5A_12XLARGE = 'm5a.12xlarge'
    M5A_16XLARGE = 'm5a.16xlarge'
    M5A_24XLARGE = 'm5a.24xlarge'
    M5AD_LARGE = 'm5ad.large'
    M5AD_XLARGE = 'm5ad.xlarge'
    M5AD_2XLARGE = 'm5ad.2xlarge'
    M5AD_4XLARGE = 'm5ad.4xlarge'
    M5AD_8XLARGE = 'm5ad.8xlarge'
    M5AD_12XLARGE = 'm5ad.12xlarge'
    M5AD_16XLARGE = 'm5ad.16xlarge'
    M5AD_24XLARGE = 'm5ad.24xlarge'
    M5D_LARGE = 'm5d.large'
    M5D_XLARGE = 'm5d.xlarge'
    M5D_2XLARGE = 'm5d.2xlarge'
    M5D_4XLARGE = 'm5d.4xlarge'
    M5D_8XLARGE = 'm5d.8xlarge'
    M5D_12XLARGE = 'm5d.12xlarge'
    M5D_16XLARGE = 'm5d.16xlarge'
    M5D_24XLARGE = 'm5d.24xlarge'
    M5D_METAL = 'm5d.metal'
    M5DN_LARGE = 'm5dn.large'
    M5DN_XLARGE = 'm5dn.xlarge'
    M5DN_2XLARGE = 'm5dn.2xlarge'
    M5DN_4XLARGE = 'm5dn.4xlarge'
    M5DN_8XLARGE = 'm5dn.8xlarge'
    M5DN_12XLARGE = 'm5dn.12xlarge'
    M5DN_16XLARGE = 'm5dn.16xlarge'
    M5DN_24XLARGE = 'm5dn.24xlarge'
    M5DN_METAL = 'm5dn.metal'
    M5N_LARGE = 'm5n.large'
    M5N_XLARGE = 'm5n.xlarge'
    M5N_2XLARGE = 'm5n.2xlarge'
    M5N_4XLARGE = 'm5n.4xlarge'
    M5N_8XLARGE = 'm5n.8xlarge'
    M5N_12XLARGE = 'm5n.12xlarge'
    M5N_16XLARGE = 'm5n.16xlarge'
    M5N_24XLARGE = 'm5n.24xlarge'
    M5N_METAL = 'm5n.metal'
    M5ZN_LARGE = 'm5zn.large'
    M5ZN_XLARGE = 'm5zn.xlarge'
    M5ZN_2XLARGE = 'm5zn.2xlarge'
    M5ZN_3XLARGE = 'm5zn.3xlarge'
    M5ZN_6XLARGE = 'm5zn.6xlarge'
    M5ZN_12XLARGE = 'm5zn.12xlarge'
    M5ZN_METAL = 'm5zn.metal'
    M6A_LARGE = 'm6a.large'
    M6A_XLARGE = 'm6a.xlarge'
    M6A_2XLARGE = 'm6a.2xlarge'
    M6A_4XLARGE = 'm6a.4xlarge'
    M6A_8XLARGE = 'm6a.8xlarge'
    M6A_12XLARGE = 'm6a.12xlarge'
    M6A_16XLARGE = 'm6a.16xlarge'
    M6A_24XLARGE = 'm6a.24xlarge'
    M6A_32XLARGE = 'm6a.32xlarge'
    M6A_48XLARGE = 'm6a.48xlarge'
    M6G_METAL = 'm6g.metal'
    M6G_MEDIUM = 'm6g.medium'
    M6G_LARGE = 'm6g.large'
    M6G_XLARGE = 'm6g.xlarge'
    M6G_2XLARGE = 'm6g.2xlarge'
    M6G_4XLARGE = 'm6g.4xlarge'
    M6G_8XLARGE = 'm6g.8xlarge'
    M6G_12XLARGE = 'm6g.12xlarge'
    M6G_16XLARGE = 'm6g.16xlarge'
    M6GD_METAL = 'm6gd.metal'
    M6GD_MEDIUM = 'm6gd.medium'
    M6GD_LARGE = 'm6gd.large'
    M6GD_XLARGE = 'm6gd.xlarge'
    M6GD_2XLARGE = 'm6gd.2xlarge'
    M6GD_4XLARGE = 'm6gd.4xlarge'
    M6GD_8XLARGE = 'm6gd.8xlarge'
    M6GD_12XLARGE = 'm6gd.12xlarge'
    M6GD_16XLARGE = 'm6gd.16xlarge'
    M6I_LARGE = 'm6i.large'
    M6I_XLARGE = 'm6i.xlarge'
    M6I_2XLARGE = 'm6i.2xlarge'
    M6I_4XLARGE = 'm6i.4xlarge'
    M6I_8XLARGE = 'm6i.8xlarge'
    M6I_12XLARGE = 'm6i.12xlarge'
    M6I_16XLARGE = 'm6i.16xlarge'
    M6I_24XLARGE = 'm6i.24xlarge'
    M6I_32XLARGE = 'm6i.32xlarge'
    M6I_METAL = 'm6i.metal'
    MAC1_METAL = 'mac1.metal'
    P2_XLARGE = 'p2.xlarge'
    P2_8XLARGE = 'p2.8xlarge'
    P2_16XLARGE = 'p2.16xlarge'
    P3_2XLARGE = 'p3.2xlarge'
    P3_8XLARGE = 'p3.8xlarge'
    P3_16XLARGE = 'p3.16xlarge'
    P3DN_24XLARGE = 'p3dn.24xlarge'
    P4D_24XLARGE = 'p4d.24xlarge'
    R3_LARGE = 'r3.large'
    R3_XLARGE = 'r3.xlarge'
    R3_2XLARGE = 'r3.2xlarge'
    R3_4XLARGE = 'r3.4xlarge'
    R3_8XLARGE = 'r3.8xlarge'
    R4_LARGE = 'r4.large'
    R4_XLARGE = 'r4.xlarge'
    R4_2XLARGE = 'r4.2xlarge'
    R4_4XLARGE = 'r4.4xlarge'
    R4_8XLARGE = 'r4.8xlarge'
    R4_16XLARGE = 'r4.16xlarge'
    R5_LARGE = 'r5.large'
    R5_XLARGE = 'r5.xlarge'
    R5_2XLARGE = 'r5.2xlarge'
    R5_4XLARGE = 'r5.4xlarge'
    R5_8XLARGE = 'r5.8xlarge'
    R5_12XLARGE = 'r5.12xlarge'
    R5_16XLARGE = 'r5.16xlarge'
    R5_24XLARGE = 'r5.24xlarge'
    R5_METAL = 'r5.metal'
    R5A_LARGE = 'r5a.large'
    R5A_XLARGE = 'r5a.xlarge'
    R5A_2XLARGE = 'r5a.2xlarge'
    R5A_4XLARGE = 'r5a.4xlarge'
    R5A_8XLARGE = 'r5a.8xlarge'
    R5A_12XLARGE = 'r5a.12xlarge'
    R5A_16XLARGE = 'r5a.16xlarge'
    R5A_24XLARGE = 'r5a.24xlarge'
    R5AD_LARGE = 'r5ad.large'
    R5AD_XLARGE = 'r5ad.xlarge'
    R5AD_2XLARGE = 'r5ad.2xlarge'
    R5AD_4XLARGE = 'r5ad.4xlarge'
    R5AD_8XLARGE = 'r5ad.8xlarge'
    R5AD_12XLARGE = 'r5ad.12xlarge'
    R5AD_16XLARGE = 'r5ad.16xlarge'
    R5AD_24XLARGE = 'r5ad.24xlarge'
    R5B_LARGE = 'r5b.large'
    R5B_XLARGE = 'r5b.xlarge'
    R5B_2XLARGE = 'r5b.2xlarge'
    R5B_4XLARGE = 'r5b.4xlarge'
    R5B_8XLARGE = 'r5b.8xlarge'
    R5B_12XLARGE = 'r5b.12xlarge'
    R5B_16XLARGE = 'r5b.16xlarge'
    R5B_24XLARGE = 'r5b.24xlarge'
    R5B_METAL = 'r5b.metal'
    R5D_LARGE = 'r5d.large'
    R5D_XLARGE = 'r5d.xlarge'
    R5D_2XLARGE = 'r5d.2xlarge'
    R5D_4XLARGE = 'r5d.4xlarge'
    R5D_8XLARGE = 'r5d.8xlarge'
    R5D_12XLARGE = 'r5d.12xlarge'
    R5D_16XLARGE = 'r5d.16xlarge'
    R5D_24XLARGE = 'r5d.24xlarge'
    R5D_METAL = 'r5d.metal'
    R5DN_LARGE = 'r5dn.large'
    R5DN_XLARGE = 'r5dn.xlarge'
    R5DN_2XLARGE = 'r5dn.2xlarge'
    R5DN_4XLARGE = 'r5dn.4xlarge'
    R5DN_8XLARGE = 'r5dn.8xlarge'
    R5DN_12XLARGE = 'r5dn.12xlarge'
    R5DN_16XLARGE = 'r5dn.16xlarge'
    R5DN_24XLARGE = 'r5dn.24xlarge'
    R5DN_METAL = 'r5dn.metal'
    R5N_LARGE = 'r5n.large'
    R5N_XLARGE = 'r5n.xlarge'
    R5N_2XLARGE = 'r5n.2xlarge'
    R5N_4XLARGE = 'r5n.4xlarge'
    R5N_8XLARGE = 'r5n.8xlarge'
    R5N_12XLARGE = 'r5n.12xlarge'
    R5N_16XLARGE = 'r5n.16xlarge'
    R5N_24XLARGE = 'r5n.24xlarge'
    R5N_METAL = 'r5n.metal'
    R6G_MEDIUM = 'r6g.medium'
    R6G_LARGE = 'r6g.large'
    R6G_XLARGE = 'r6g.xlarge'
    R6G_2XLARGE = 'r6g.2xlarge'
    R6G_4XLARGE = 'r6g.4xlarge'
    R6G_8XLARGE = 'r6g.8xlarge'
    R6G_12XLARGE = 'r6g.12xlarge'
    R6G_16XLARGE = 'r6g.16xlarge'
    R6G_METAL = 'r6g.metal'
    R6GD_MEDIUM = 'r6gd.medium'
    R6GD_LARGE = 'r6gd.large'
    R6GD_XLARGE = 'r6gd.xlarge'
    R6GD_2XLARGE = 'r6gd.2xlarge'
    R6GD_4XLARGE = 'r6gd.4xlarge'
    R6GD_8XLARGE = 'r6gd.8xlarge'
    R6GD_12XLARGE = 'r6gd.12xlarge'
    R6GD_16XLARGE = 'r6gd.16xlarge'
    R6GD_METAL = 'r6gd.metal'
    R6I_LARGE = 'r6i.large'
    R6I_XLARGE = 'r6i.xlarge'
    R6I_2XLARGE = 'r6i.2xlarge'
    R6I_4XLARGE = 'r6i.4xlarge'
    R6I_8XLARGE = 'r6i.8xlarge'
    R6I_12XLARGE = 'r6i.12xlarge'
    R6I_16XLARGE = 'r6i.16xlarge'
    R6I_24XLARGE = 'r6i.24xlarge'
    R6I_32XLARGE = 'r6i.32xlarge'
    R6I_METAL = 'r6i.metal'
    T1_MICRO = 't1.micro'
    T2_NANO = 't2.nano'
    T2_MICRO = 't2.micro'
    T2_SMALL = 't2.small'
    T2_MEDIUM = 't2.medium'
    T2_LARGE = 't2.large'
    T2_XLARGE = 't2.xlarge'
    T2_2XLARGE = 't2.2xlarge'
    T3_NANO = 't3.nano'
    T3_MICRO = 't3.micro'
    T3_SMALL = 't3.small'
    T3_MEDIUM = 't3.medium'
    T3_LARGE = 't3.large'
    T3_XLARGE = 't3.xlarge'
    T3_2XLARGE = 't3.2xlarge'
    T3A_NANO = 't3a.nano'
    T3A_MICRO = 't3a.micro'
    T3A_SMALL = 't3a.small'
    T3A_MEDIUM = 't3a.medium'
    T3A_LARGE = 't3a.large'
    T3A_XLARGE = 't3a.xlarge'
    T3A_2XLARGE = 't3a.2xlarge'
    T4G_NANO = 't4g.nano'
    T4G_MICRO = 't4g.micro'
    T4G_SMALL = 't4g.small'
    T4G_MEDIUM = 't4g.medium'
    T4G_LARGE = 't4g.large'
    T4G_XLARGE = 't4g.xlarge'
    T4G_2XLARGE = 't4g.2xlarge'
    U_6TB1_56XLARGE = 'u-6tb1.56xlarge'
    U_6TB1_112XLARGE = 'u-6tb1.112xlarge'
    U_9TB1_112XLARGE = 'u-9tb1.112xlarge'
    U_12TB1_112XLARGE = 'u-12tb1.112xlarge'
    U_6TB1_METAL = 'u-6tb1.metal'
    U_9TB1_METAL = 'u-9tb1.metal'
    U_12TB1_METAL = 'u-12tb1.metal'
    U_18TB1_METAL = 'u-18tb1.metal'
    U_24TB1_METAL = 'u-24tb1.metal'
    VT1_3XLARGE = 'vt1.3xlarge'
    VT1_6XLARGE = 'vt1.6xlarge'
    VT1_24XLARGE = 'vt1.24xlarge'
    X1_16XLARGE = 'x1.16xlarge'
    X1_32XLARGE = 'x1.32xlarge'
    X1E_XLARGE = 'x1e.xlarge'
    X1E_2XLARGE = 'x1e.2xlarge'
    X1E_4XLARGE = 'x1e.4xlarge'
    X1E_8XLARGE = 'x1e.8xlarge'
    X1E_16XLARGE = 'x1e.16xlarge'
    X1E_32XLARGE = 'x1e.32xlarge'
    X2IEZN_2XLARGE = 'x2iezn.2xlarge'
    X2IEZN_4XLARGE = 'x2iezn.4xlarge'
    X2IEZN_6XLARGE = 'x2iezn.6xlarge'
    X2IEZN_8XLARGE = 'x2iezn.8xlarge'
    X2IEZN_12XLARGE = 'x2iezn.12xlarge'
    X2IEZN_METAL = 'x2iezn.metal'
    X2GD_MEDIUM = 'x2gd.medium'
    X2GD_LARGE = 'x2gd.large'
    X2GD_XLARGE = 'x2gd.xlarge'
    X2GD_2XLARGE = 'x2gd.2xlarge'
    X2GD_4XLARGE = 'x2gd.4xlarge'
    X2GD_8XLARGE = 'x2gd.8xlarge'
    X2GD_12XLARGE = 'x2gd.12xlarge'
    X2GD_16XLARGE = 'x2gd.16xlarge'
    X2GD_METAL = 'x2gd.metal'
    Z1D_LARGE = 'z1d.large'
    Z1D_XLARGE = 'z1d.xlarge'
    Z1D_2XLARGE = 'z1d.2xlarge'
    Z1D_3XLARGE = 'z1d.3xlarge'
    Z1D_6XLARGE = 'z1d.6xlarge'
    Z1D_12XLARGE = 'z1d.12xlarge'
    Z1D_METAL = 'z1d.metal'
    X2IDN_16XLARGE = 'x2idn.16xlarge'
    X2IDN_24XLARGE = 'x2idn.24xlarge'
    X2IDN_32XLARGE = 'x2idn.32xlarge'
    X2IEDN_XLARGE = 'x2iedn.xlarge'
    X2IEDN_2XLARGE = 'x2iedn.2xlarge'
    X2IEDN_4XLARGE = 'x2iedn.4xlarge'
    X2IEDN_8XLARGE = 'x2iedn.8xlarge'
    X2IEDN_16XLARGE = 'x2iedn.16xlarge'
    X2IEDN_24XLARGE = 'x2iedn.24xlarge'
    X2IEDN_32XLARGE = 'x2iedn.32xlarge'
    C6A_LARGE = 'c6a.large'
    C6A_XLARGE = 'c6a.xlarge'
    C6A_2XLARGE = 'c6a.2xlarge'
    C6A_4XLARGE = 'c6a.4xlarge'
    C6A_8XLARGE = 'c6a.8xlarge'
    C6A_12XLARGE = 'c6a.12xlarge'
    C6A_16XLARGE = 'c6a.16xlarge'
    C6A_24XLARGE = 'c6a.24xlarge'
    C6A_32XLARGE = 'c6a.32xlarge'
    C6A_48XLARGE = 'c6a.48xlarge'
    C6A_METAL = 'c6a.metal'
    M6A_METAL = 'm6a.metal'
    I4I_LARGE = 'i4i.large'
    I4I_XLARGE = 'i4i.xlarge'
    I4I_2XLARGE = 'i4i.2xlarge'
    I4I_4XLARGE = 'i4i.4xlarge'
    I4I_8XLARGE = 'i4i.8xlarge'
    I4I_16XLARGE = 'i4i.16xlarge'
    I4I_32XLARGE = 'i4i.32xlarge'
    I4I_METAL = 'i4i.metal'
    X2IDN_METAL = 'x2idn.metal'
    X2IEDN_METAL = 'x2iedn.metal'
    C7G_MEDIUM = 'c7g.medium'
    C7G_LARGE = 'c7g.large'
    C7G_XLARGE = 'c7g.xlarge'
    C7G_2XLARGE = 'c7g.2xlarge'
    C7G_4XLARGE = 'c7g.4xlarge'
    C7G_8XLARGE = 'c7g.8xlarge'
    C7G_12XLARGE = 'c7g.12xlarge'
    C7G_16XLARGE = 'c7g.16xlarge'
    MAC2_METAL = 'mac2.metal'
    C6ID_LARGE = 'c6id.large'
    C6ID_XLARGE = 'c6id.xlarge'
    C6ID_2XLARGE = 'c6id.2xlarge'
    C6ID_4XLARGE = 'c6id.4xlarge'
    C6ID_8XLARGE = 'c6id.8xlarge'
    C6ID_12XLARGE = 'c6id.12xlarge'
    C6ID_16XLARGE = 'c6id.16xlarge'
    C6ID_24XLARGE = 'c6id.24xlarge'
    C6ID_32XLARGE = 'c6id.32xlarge'
    C6ID_METAL = 'c6id.metal'
    M6ID_LARGE = 'm6id.large'
    M6ID_XLARGE = 'm6id.xlarge'
    M6ID_2XLARGE = 'm6id.2xlarge'
    M6ID_4XLARGE = 'm6id.4xlarge'
    M6ID_8XLARGE = 'm6id.8xlarge'
    M6ID_12XLARGE = 'm6id.12xlarge'
    M6ID_16XLARGE = 'm6id.16xlarge'
    M6ID_24XLARGE = 'm6id.24xlarge'
    M6ID_32XLARGE = 'm6id.32xlarge'
    M6ID_METAL = 'm6id.metal'
    R6ID_LARGE = 'r6id.large'
    R6ID_XLARGE = 'r6id.xlarge'
    R6ID_2XLARGE = 'r6id.2xlarge'
    R6ID_4XLARGE = 'r6id.4xlarge'
    R6ID_8XLARGE = 'r6id.8xlarge'
    R6ID_12XLARGE = 'r6id.12xlarge'
    R6ID_16XLARGE = 'r6id.16xlarge'
    R6ID_24XLARGE = 'r6id.24xlarge'
    R6ID_32XLARGE = 'r6id.32xlarge'
    R6ID_METAL = 'r6id.metal'
    R6A_LARGE = 'r6a.large'
    R6A_XLARGE = 'r6a.xlarge'
    R6A_2XLARGE = 'r6a.2xlarge'
    R6A_4XLARGE = 'r6a.4xlarge'
    R6A_8XLARGE = 'r6a.8xlarge'
    R6A_12XLARGE = 'r6a.12xlarge'
    R6A_16XLARGE = 'r6a.16xlarge'
    R6A_24XLARGE = 'r6a.24xlarge'
    R6A_32XLARGE = 'r6a.32xlarge'
    R6A_48XLARGE = 'r6a.48xlarge'
    R6A_METAL = 'r6a.metal'
    P4DE_24XLARGE = 'p4de.24xlarge'
    U_3TB1_56XLARGE = 'u-3tb1.56xlarge'
    U_18TB1_112XLARGE = 'u-18tb1.112xlarge'
    U_24TB1_112XLARGE = 'u-24tb1.112xlarge'
    TRN1_2XLARGE = 'trn1.2xlarge'
    TRN1_32XLARGE = 'trn1.32xlarge'
    HPC6ID_32XLARGE = 'hpc6id.32xlarge'
    C6IN_LARGE = 'c6in.large'
    C6IN_XLARGE = 'c6in.xlarge'
    C6IN_2XLARGE = 'c6in.2xlarge'
    C6IN_4XLARGE = 'c6in.4xlarge'
    C6IN_8XLARGE = 'c6in.8xlarge'
    C6IN_12XLARGE = 'c6in.12xlarge'
    C6IN_16XLARGE = 'c6in.16xlarge'
    C6IN_24XLARGE = 'c6in.24xlarge'
    C6IN_32XLARGE = 'c6in.32xlarge'
    M6IN_LARGE = 'm6in.large'
    M6IN_XLARGE = 'm6in.xlarge'
    M6IN_2XLARGE = 'm6in.2xlarge'
    M6IN_4XLARGE = 'm6in.4xlarge'
    M6IN_8XLARGE = 'm6in.8xlarge'
    M6IN_12XLARGE = 'm6in.12xlarge'
    M6IN_16XLARGE = 'm6in.16xlarge'
    M6IN_24XLARGE = 'm6in.24xlarge'
    M6IN_32XLARGE = 'm6in.32xlarge'
    M6IDN_LARGE = 'm6idn.large'
    M6IDN_XLARGE = 'm6idn.xlarge'
    M6IDN_2XLARGE = 'm6idn.2xlarge'
    M6IDN_4XLARGE = 'm6idn.4xlarge'
    M6IDN_8XLARGE = 'm6idn.8xlarge'
    M6IDN_12XLARGE = 'm6idn.12xlarge'
    M6IDN_16XLARGE = 'm6idn.16xlarge'
    M6IDN_24XLARGE = 'm6idn.24xlarge'
    M6IDN_32XLARGE = 'm6idn.32xlarge'
    R6IN_LARGE = 'r6in.large'
    R6IN_XLARGE = 'r6in.xlarge'
    R6IN_2XLARGE = 'r6in.2xlarge'
    R6IN_4XLARGE = 'r6in.4xlarge'
    R6IN_8XLARGE = 'r6in.8xlarge'
    R6IN_12XLARGE = 'r6in.12xlarge'
    R6IN_16XLARGE = 'r6in.16xlarge'
    R6IN_24XLARGE = 'r6in.24xlarge'
    R6IN_32XLARGE = 'r6in.32xlarge'
    R6IDN_LARGE = 'r6idn.large'
    R6IDN_XLARGE = 'r6idn.xlarge'
    R6IDN_2XLARGE = 'r6idn.2xlarge'
    R6IDN_4XLARGE = 'r6idn.4xlarge'
    R6IDN_8XLARGE = 'r6idn.8xlarge'
    R6IDN_12XLARGE = 'r6idn.12xlarge'
    R6IDN_16XLARGE = 'r6idn.16xlarge'
    R6IDN_24XLARGE = 'r6idn.24xlarge'
    R6IDN_32XLARGE = 'r6idn.32xlarge'
    C7G_METAL = 'c7g.metal'
    M7G_MEDIUM = 'm7g.medium'
    M7G_LARGE = 'm7g.large'
    M7G_XLARGE = 'm7g.xlarge'
    M7G_2XLARGE = 'm7g.2xlarge'
    M7G_4XLARGE = 'm7g.4xlarge'
    M7G_8XLARGE = 'm7g.8xlarge'
    M7G_12XLARGE = 'm7g.12xlarge'
    M7G_16XLARGE = 'm7g.16xlarge'
    M7G_METAL = 'm7g.metal'
    R7G_MEDIUM = 'r7g.medium'
    R7G_LARGE = 'r7g.large'
    R7G_XLARGE = 'r7g.xlarge'
    R7G_2XLARGE = 'r7g.2xlarge'
    R7G_4XLARGE = 'r7g.4xlarge'
    R7G_8XLARGE = 'r7g.8xlarge'
    R7G_12XLARGE = 'r7g.12xlarge'
    R7G_16XLARGE = 'r7g.16xlarge'
    R7G_METAL = 'r7g.metal'
    C6IN_METAL = 'c6in.metal'
    M6IN_METAL = 'm6in.metal'
    M6IDN_METAL = 'm6idn.metal'
    R6IN_METAL = 'r6in.metal'
    R6IDN_METAL = 'r6idn.metal'
    INF2_XLARGE = 'inf2.xlarge'
    INF2_8XLARGE = 'inf2.8xlarge'
    INF2_24XLARGE = 'inf2.24xlarge'
    INF2_48XLARGE = 'inf2.48xlarge'
    TRN1N_32XLARGE = 'trn1n.32xlarge'
    I4G_LARGE = 'i4g.large'
    I4G_XLARGE = 'i4g.xlarge'
    I4G_2XLARGE = 'i4g.2xlarge'
    I4G_4XLARGE = 'i4g.4xlarge'
    I4G_8XLARGE = 'i4g.8xlarge'
    I4G_16XLARGE = 'i4g.16xlarge'

class InstanceTypeHypervisor(enum.Enum):
    NITRO = 'nitro'
    XEN = 'xen'

class InterfacePermissionType(enum.Enum):
    INSTANCE_ATTACH = 'INSTANCE-ATTACH'
    EIP_ASSOCIATE = 'EIP-ASSOCIATE'

class InterfaceProtocolType(enum.Enum):
    VLAN = 'VLAN'
    GRE = 'GRE'

class IpAddressType(enum.Enum):
    IPV4 = 'ipv4'
    DUALSTACK = 'dualstack'
    IPV6 = 'ipv6'

class IpamAddressHistoryResourceType(enum.Enum):
    EIP = 'eip'
    VPC = 'vpc'
    SUBNET = 'subnet'
    NETWORK_INTERFACE = 'network-interface'
    INSTANCE = 'instance'

class IpamAssociatedResourceDiscoveryStatus(enum.Enum):
    ACTIVE = 'active'
    NOT_FOUND = 'not-found'

class IpamComplianceStatus(enum.Enum):
    COMPLIANT = 'compliant'
    NONCOMPLIANT = 'noncompliant'
    UNMANAGED = 'unmanaged'
    IGNORED = 'ignored'

class IpamDiscoveryFailureCode(enum.Enum):
    ASSUME_ROLE_FAILURE = 'assume-role-failure'
    THROTTLING_FAILURE = 'throttling-failure'
    UNAUTHORIZED_FAILURE = 'unauthorized-failure'

class IpamManagementState(enum.Enum):
    MANAGED = 'managed'
    UNMANAGED = 'unmanaged'
    IGNORED = 'ignored'

class IpamOverlapStatus(enum.Enum):
    OVERLAPPING = 'overlapping'
    NONOVERLAPPING = 'nonoverlapping'
    IGNORED = 'ignored'

class IpamPoolAllocationResourceType(enum.Enum):
    IPAM_POOL = 'ipam-pool'
    VPC = 'vpc'
    EC2_PUBLIC_IPV4_POOL = 'ec2-public-ipv4-pool'
    CUSTOM = 'custom'

class IpamPoolAwsService(enum.Enum):
    EC2 = 'ec2'

class IpamPoolCidrFailureCode(enum.Enum):
    CIDR_NOT_AVAILABLE = 'cidr-not-available'
    LIMIT_EXCEEDED = 'limit-exceeded'

class IpamPoolCidrState(enum.Enum):
    PENDING_PROVISION = 'pending-provision'
    PROVISIONED = 'provisioned'
    FAILED_PROVISION = 'failed-provision'
    PENDING_DEPROVISION = 'pending-deprovision'
    DEPROVISIONED = 'deprovisioned'
    FAILED_DEPROVISION = 'failed-deprovision'
    PENDING_IMPORT = 'pending-import'
    FAILED_IMPORT = 'failed-import'

class IpamPoolPublicIpSource(enum.Enum):
    AMAZON = 'amazon'
    BYOIP = 'byoip'

class IpamPoolState(enum.Enum):
    CREATE_IN_PROGRESS = 'create-in-progress'
    CREATE_COMPLETE = 'create-complete'
    CREATE_FAILED = 'create-failed'
    MODIFY_IN_PROGRESS = 'modify-in-progress'
    MODIFY_COMPLETE = 'modify-complete'
    MODIFY_FAILED = 'modify-failed'
    DELETE_IN_PROGRESS = 'delete-in-progress'
    DELETE_COMPLETE = 'delete-complete'
    DELETE_FAILED = 'delete-failed'
    ISOLATE_IN_PROGRESS = 'isolate-in-progress'
    ISOLATE_COMPLETE = 'isolate-complete'
    RESTORE_IN_PROGRESS = 'restore-in-progress'

class IpamResourceDiscoveryAssociationState(enum.Enum):
    ASSOCIATE_IN_PROGRESS = 'associate-in-progress'
    ASSOCIATE_COMPLETE = 'associate-complete'
    ASSOCIATE_FAILED = 'associate-failed'
    DISASSOCIATE_IN_PROGRESS = 'disassociate-in-progress'
    DISASSOCIATE_COMPLETE = 'disassociate-complete'
    DISASSOCIATE_FAILED = 'disassociate-failed'
    ISOLATE_IN_PROGRESS = 'isolate-in-progress'
    ISOLATE_COMPLETE = 'isolate-complete'
    RESTORE_IN_PROGRESS = 'restore-in-progress'

class IpamResourceDiscoveryState(enum.Enum):
    CREATE_IN_PROGRESS = 'create-in-progress'
    CREATE_COMPLETE = 'create-complete'
    CREATE_FAILED = 'create-failed'
    MODIFY_IN_PROGRESS = 'modify-in-progress'
    MODIFY_COMPLETE = 'modify-complete'
    MODIFY_FAILED = 'modify-failed'
    DELETE_IN_PROGRESS = 'delete-in-progress'
    DELETE_COMPLETE = 'delete-complete'
    DELETE_FAILED = 'delete-failed'
    ISOLATE_IN_PROGRESS = 'isolate-in-progress'
    ISOLATE_COMPLETE = 'isolate-complete'
    RESTORE_IN_PROGRESS = 'restore-in-progress'

class IpamResourceType(enum.Enum):
    VPC = 'vpc'
    SUBNET = 'subnet'
    EIP = 'eip'
    PUBLIC_IPV4_POOL = 'public-ipv4-pool'
    IPV6_POOL = 'ipv6-pool'

class IpamScopeState(enum.Enum):
    CREATE_IN_PROGRESS = 'create-in-progress'
    CREATE_COMPLETE = 'create-complete'
    CREATE_FAILED = 'create-failed'
    MODIFY_IN_PROGRESS = 'modify-in-progress'
    MODIFY_COMPLETE = 'modify-complete'
    MODIFY_FAILED = 'modify-failed'
    DELETE_IN_PROGRESS = 'delete-in-progress'
    DELETE_COMPLETE = 'delete-complete'
    DELETE_FAILED = 'delete-failed'
    ISOLATE_IN_PROGRESS = 'isolate-in-progress'
    ISOLATE_COMPLETE = 'isolate-complete'
    RESTORE_IN_PROGRESS = 'restore-in-progress'

class IpamScopeType(enum.Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'

class IpamState(enum.Enum):
    CREATE_IN_PROGRESS = 'create-in-progress'
    CREATE_COMPLETE = 'create-complete'
    CREATE_FAILED = 'create-failed'
    MODIFY_IN_PROGRESS = 'modify-in-progress'
    MODIFY_COMPLETE = 'modify-complete'
    MODIFY_FAILED = 'modify-failed'
    DELETE_IN_PROGRESS = 'delete-in-progress'
    DELETE_COMPLETE = 'delete-complete'
    DELETE_FAILED = 'delete-failed'
    ISOLATE_IN_PROGRESS = 'isolate-in-progress'
    ISOLATE_COMPLETE = 'isolate-complete'
    RESTORE_IN_PROGRESS = 'restore-in-progress'

class Ipv6SupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class KeyFormat(enum.Enum):
    PEM = 'pem'
    PPK = 'ppk'

class KeyType(enum.Enum):
    RSA = 'rsa'
    ED25519 = 'ed25519'

class LaunchTemplateAutoRecoveryState(enum.Enum):
    DEFAULT = 'default'
    DISABLED = 'disabled'

class LaunchTemplateErrorCode(enum.Enum):
    LAUNCHTEMPLATEIDDOESNOTEXIST = 'launchTemplateIdDoesNotExist'
    LAUNCHTEMPLATEIDMALFORMED = 'launchTemplateIdMalformed'
    LAUNCHTEMPLATENAMEDOESNOTEXIST = 'launchTemplateNameDoesNotExist'
    LAUNCHTEMPLATENAMEMALFORMED = 'launchTemplateNameMalformed'
    LAUNCHTEMPLATEVERSIONDOESNOTEXIST = 'launchTemplateVersionDoesNotExist'
    UNEXPECTEDERROR = 'unexpectedError'

class LaunchTemplateHttpTokensState(enum.Enum):
    OPTIONAL = 'optional'
    REQUIRED = 'required'

class LaunchTemplateInstanceMetadataEndpointState(enum.Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class LaunchTemplateInstanceMetadataOptionsState(enum.Enum):
    PENDING = 'pending'
    APPLIED = 'applied'

class LaunchTemplateInstanceMetadataProtocolIpv6(enum.Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class LaunchTemplateInstanceMetadataTagsState(enum.Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class ListingState(enum.Enum):
    AVAILABLE = 'available'
    SOLD = 'sold'
    CANCELLED = 'cancelled'
    PENDING = 'pending'

class ListingStatus(enum.Enum):
    ACTIVE = 'active'
    PENDING = 'pending'
    CANCELLED = 'cancelled'
    CLOSED = 'closed'

class LocalGatewayRouteState(enum.Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    BLACKHOLE = 'blackhole'
    DELETING = 'deleting'
    DELETED = 'deleted'

class LocalGatewayRouteTableMode(enum.Enum):
    DIRECT_VPC_ROUTING = 'direct-vpc-routing'
    COIP = 'coip'

class LocalGatewayRouteType(enum.Enum):
    STATIC = 'static'
    PROPAGATED = 'propagated'

class LocalStorage(enum.Enum):
    INCLUDED = 'included'
    REQUIRED = 'required'
    EXCLUDED = 'excluded'

class LocalStorageType(enum.Enum):
    HDD = 'hdd'
    SSD = 'ssd'

class LocationType(enum.Enum):
    REGION = 'region'
    AVAILABILITY_ZONE = 'availability-zone'
    AVAILABILITY_ZONE_ID = 'availability-zone-id'

class LogDestinationType(enum.Enum):
    CLOUD_WATCH_LOGS = 'cloud-watch-logs'
    S3 = 's3'
    KINESIS_DATA_FIREHOSE = 'kinesis-data-firehose'

class MarketType(enum.Enum):
    SPOT = 'spot'

class MembershipType(enum.Enum):
    STATIC = 'static'
    IGMP = 'igmp'

class MetricType(enum.Enum):
    AGGREGATE_LATENCY = 'aggregate-latency'

class ModifyAvailabilityZoneOptInStatus(enum.Enum):
    OPTED_IN = 'opted-in'
    NOT_OPTED_IN = 'not-opted-in'

class MonitoringState(enum.Enum):
    DISABLED = 'disabled'
    DISABLING = 'disabling'
    ENABLED = 'enabled'
    PENDING = 'pending'

class MoveStatus(enum.Enum):
    MOVINGTOVPC = 'movingToVpc'
    RESTORINGTOCLASSIC = 'restoringToClassic'

class MulticastSupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class NatGatewayAddressStatus(enum.Enum):
    ASSIGNING = 'assigning'
    UNASSIGNING = 'unassigning'
    ASSOCIATING = 'associating'
    DISASSOCIATING = 'disassociating'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'

class NatGatewayState(enum.Enum):
    PENDING = 'pending'
    FAILED = 'failed'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class NetworkInterfaceAttribute(enum.Enum):
    DESCRIPTION = 'description'
    GROUPSET = 'groupSet'
    SOURCEDESTCHECK = 'sourceDestCheck'
    ATTACHMENT = 'attachment'

class NetworkInterfaceCreationType(enum.Enum):
    EFA = 'efa'
    BRANCH = 'branch'
    TRUNK = 'trunk'

class NetworkInterfacePermissionStateCode(enum.Enum):
    PENDING = 'pending'
    GRANTED = 'granted'
    REVOKING = 'revoking'
    REVOKED = 'revoked'

class NetworkInterfaceStatus(enum.Enum):
    AVAILABLE = 'available'
    ASSOCIATED = 'associated'
    ATTACHING = 'attaching'
    IN_USE = 'in-use'
    DETACHING = 'detaching'

class NetworkInterfaceType(enum.Enum):
    INTERFACE = 'interface'
    NATGATEWAY = 'natGateway'
    EFA = 'efa'
    TRUNK = 'trunk'
    LOAD_BALANCER = 'load_balancer'
    NETWORK_LOAD_BALANCER = 'network_load_balancer'
    VPC_ENDPOINT = 'vpc_endpoint'
    BRANCH = 'branch'
    TRANSIT_GATEWAY = 'transit_gateway'
    LAMBDA = 'lambda'
    QUICKSIGHT = 'quicksight'
    GLOBAL_ACCELERATOR_MANAGED = 'global_accelerator_managed'
    API_GATEWAY_MANAGED = 'api_gateway_managed'
    GATEWAY_LOAD_BALANCER = 'gateway_load_balancer'
    GATEWAY_LOAD_BALANCER_ENDPOINT = 'gateway_load_balancer_endpoint'
    IOT_RULES_MANAGED = 'iot_rules_managed'
    AWS_CODESTAR_CONNECTIONS_MANAGED = 'aws_codestar_connections_managed'

class OfferingClassType(enum.Enum):
    STANDARD = 'standard'
    CONVERTIBLE = 'convertible'

class OfferingTypeValues(enum.Enum):
    HEAVY_UTILIZATION = 'Heavy Utilization'
    MEDIUM_UTILIZATION = 'Medium Utilization'
    LIGHT_UTILIZATION = 'Light Utilization'
    NO_UPFRONT = 'No Upfront'
    PARTIAL_UPFRONT = 'Partial Upfront'
    ALL_UPFRONT = 'All Upfront'

class OnDemandAllocationStrategy(enum.Enum):
    LOWESTPRICE = 'lowestPrice'
    PRIORITIZED = 'prioritized'

class OperationType(enum.Enum):
    ADD = 'add'
    REMOVE = 'remove'

class PartitionLoadFrequency(enum.Enum):
    NONE = 'none'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

class PayerResponsibility(enum.Enum):
    SERVICEOWNER = 'ServiceOwner'

class PaymentOption(enum.Enum):
    ALLUPFRONT = 'AllUpfront'
    PARTIALUPFRONT = 'PartialUpfront'
    NOUPFRONT = 'NoUpfront'

class PeriodType(enum.Enum):
    FIVE_MINUTES = 'five-minutes'
    FIFTEEN_MINUTES = 'fifteen-minutes'
    ONE_HOUR = 'one-hour'
    THREE_HOURS = 'three-hours'
    ONE_DAY = 'one-day'
    ONE_WEEK = 'one-week'

class PermissionGroup(enum.Enum):
    ALL = 'all'

class PlacementGroupState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class PlacementGroupStrategy(enum.Enum):
    CLUSTER = 'cluster'
    PARTITION = 'partition'
    SPREAD = 'spread'

class PlacementStrategy(enum.Enum):
    CLUSTER = 'cluster'
    SPREAD = 'spread'
    PARTITION = 'partition'

class PlatformValues(enum.Enum):
    WINDOWS = 'Windows'

class PrefixListState(enum.Enum):
    CREATE_IN_PROGRESS = 'create-in-progress'
    CREATE_COMPLETE = 'create-complete'
    CREATE_FAILED = 'create-failed'
    MODIFY_IN_PROGRESS = 'modify-in-progress'
    MODIFY_COMPLETE = 'modify-complete'
    MODIFY_FAILED = 'modify-failed'
    RESTORE_IN_PROGRESS = 'restore-in-progress'
    RESTORE_COMPLETE = 'restore-complete'
    RESTORE_FAILED = 'restore-failed'
    DELETE_IN_PROGRESS = 'delete-in-progress'
    DELETE_COMPLETE = 'delete-complete'
    DELETE_FAILED = 'delete-failed'

class PrincipalType(enum.Enum):
    ALL = 'All'
    SERVICE = 'Service'
    ORGANIZATIONUNIT = 'OrganizationUnit'
    ACCOUNT = 'Account'
    USER = 'User'
    ROLE = 'Role'

class ProductCodeValues(enum.Enum):
    DEVPAY = 'devpay'
    MARKETPLACE = 'marketplace'

class Protocol(enum.Enum):
    TCP = 'tcp'
    UDP = 'udp'

class ProtocolValue(enum.Enum):
    GRE = 'gre'

class RIProductDescription(enum.Enum):
    LINUX_UNIX = 'Linux/UNIX'
    LINUX_UNIX_AMAZON_VPC = 'Linux/UNIX (Amazon VPC)'
    WINDOWS = 'Windows'
    WINDOWS_AMAZON_VPC = 'Windows (Amazon VPC)'

class RecurringChargeFrequency(enum.Enum):
    HOURLY = 'Hourly'

class ReplaceRootVolumeTaskState(enum.Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in-progress'
    FAILING = 'failing'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'
    FAILED_DETACHED = 'failed-detached'

class ReplacementStrategy(enum.Enum):
    LAUNCH = 'launch'
    LAUNCH_BEFORE_TERMINATE = 'launch-before-terminate'

class ReportInstanceReasonCodes(enum.Enum):
    INSTANCE_STUCK_IN_STATE = 'instance-stuck-in-state'
    UNRESPONSIVE = 'unresponsive'
    NOT_ACCEPTING_CREDENTIALS = 'not-accepting-credentials'
    PASSWORD_NOT_AVAILABLE = 'password-not-available'
    PERFORMANCE_NETWORK = 'performance-network'
    PERFORMANCE_INSTANCE_STORE = 'performance-instance-store'
    PERFORMANCE_EBS_VOLUME = 'performance-ebs-volume'
    PERFORMANCE_OTHER = 'performance-other'
    OTHER = 'other'

class ReportStatusType(enum.Enum):
    OK = 'ok'
    IMPAIRED = 'impaired'

class ReservationState(enum.Enum):
    PAYMENT_PENDING = 'payment-pending'
    PAYMENT_FAILED = 'payment-failed'
    ACTIVE = 'active'
    RETIRED = 'retired'

class ReservedInstanceState(enum.Enum):
    PAYMENT_PENDING = 'payment-pending'
    ACTIVE = 'active'
    PAYMENT_FAILED = 'payment-failed'
    RETIRED = 'retired'
    QUEUED = 'queued'
    QUEUED_DELETED = 'queued-deleted'

class ResetFpgaImageAttributeName(enum.Enum):
    LOADPERMISSION = 'loadPermission'

class ResetImageAttributeName(enum.Enum):
    LAUNCHPERMISSION = 'launchPermission'

class ResourceType(enum.Enum):
    CAPACITY_RESERVATION = 'capacity-reservation'
    CLIENT_VPN_ENDPOINT = 'client-vpn-endpoint'
    CUSTOMER_GATEWAY = 'customer-gateway'
    CARRIER_GATEWAY = 'carrier-gateway'
    COIP_POOL = 'coip-pool'
    DEDICATED_HOST = 'dedicated-host'
    DHCP_OPTIONS = 'dhcp-options'
    EGRESS_ONLY_INTERNET_GATEWAY = 'egress-only-internet-gateway'
    ELASTIC_IP = 'elastic-ip'
    ELASTIC_GPU = 'elastic-gpu'
    EXPORT_IMAGE_TASK = 'export-image-task'
    EXPORT_INSTANCE_TASK = 'export-instance-task'
    FLEET = 'fleet'
    FPGA_IMAGE = 'fpga-image'
    HOST_RESERVATION = 'host-reservation'
    IMAGE = 'image'
    IMPORT_IMAGE_TASK = 'import-image-task'
    IMPORT_SNAPSHOT_TASK = 'import-snapshot-task'
    INSTANCE = 'instance'
    INSTANCE_EVENT_WINDOW = 'instance-event-window'
    INTERNET_GATEWAY = 'internet-gateway'
    IPAM = 'ipam'
    IPAM_POOL = 'ipam-pool'
    IPAM_SCOPE = 'ipam-scope'
    IPV4POOL_EC2 = 'ipv4pool-ec2'
    IPV6POOL_EC2 = 'ipv6pool-ec2'
    KEY_PAIR = 'key-pair'
    LAUNCH_TEMPLATE = 'launch-template'
    LOCAL_GATEWAY = 'local-gateway'
    LOCAL_GATEWAY_ROUTE_TABLE = 'local-gateway-route-table'
    LOCAL_GATEWAY_VIRTUAL_INTERFACE = 'local-gateway-virtual-interface'
    LOCAL_GATEWAY_VIRTUAL_INTERFACE_GROUP = 'local-gateway-virtual-interface-group'
    LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = 'local-gateway-route-table-vpc-association'
    LOCAL_GATEWAY_ROUTE_TABLE_VIRTUAL_INTERFACE_GROUP_ASSOCIATION = 'local-gateway-route-table-virtual-interface-group-association'
    NATGATEWAY = 'natgateway'
    NETWORK_ACL = 'network-acl'
    NETWORK_INTERFACE = 'network-interface'
    NETWORK_INSIGHTS_ANALYSIS = 'network-insights-analysis'
    NETWORK_INSIGHTS_PATH = 'network-insights-path'
    NETWORK_INSIGHTS_ACCESS_SCOPE = 'network-insights-access-scope'
    NETWORK_INSIGHTS_ACCESS_SCOPE_ANALYSIS = 'network-insights-access-scope-analysis'
    PLACEMENT_GROUP = 'placement-group'
    PREFIX_LIST = 'prefix-list'
    REPLACE_ROOT_VOLUME_TASK = 'replace-root-volume-task'
    RESERVED_INSTANCES = 'reserved-instances'
    ROUTE_TABLE = 'route-table'
    SECURITY_GROUP = 'security-group'
    SECURITY_GROUP_RULE = 'security-group-rule'
    SNAPSHOT = 'snapshot'
    SPOT_FLEET_REQUEST = 'spot-fleet-request'
    SPOT_INSTANCES_REQUEST = 'spot-instances-request'
    SUBNET = 'subnet'
    SUBNET_CIDR_RESERVATION = 'subnet-cidr-reservation'
    TRAFFIC_MIRROR_FILTER = 'traffic-mirror-filter'
    TRAFFIC_MIRROR_SESSION = 'traffic-mirror-session'
    TRAFFIC_MIRROR_TARGET = 'traffic-mirror-target'
    TRANSIT_GATEWAY = 'transit-gateway'
    TRANSIT_GATEWAY_ATTACHMENT = 'transit-gateway-attachment'
    TRANSIT_GATEWAY_CONNECT_PEER = 'transit-gateway-connect-peer'
    TRANSIT_GATEWAY_MULTICAST_DOMAIN = 'transit-gateway-multicast-domain'
    TRANSIT_GATEWAY_POLICY_TABLE = 'transit-gateway-policy-table'
    TRANSIT_GATEWAY_ROUTE_TABLE = 'transit-gateway-route-table'
    TRANSIT_GATEWAY_ROUTE_TABLE_ANNOUNCEMENT = 'transit-gateway-route-table-announcement'
    VOLUME = 'volume'
    VPC = 'vpc'
    VPC_ENDPOINT = 'vpc-endpoint'
    VPC_ENDPOINT_CONNECTION = 'vpc-endpoint-connection'
    VPC_ENDPOINT_SERVICE = 'vpc-endpoint-service'
    VPC_ENDPOINT_SERVICE_PERMISSION = 'vpc-endpoint-service-permission'
    VPC_PEERING_CONNECTION = 'vpc-peering-connection'
    VPN_CONNECTION = 'vpn-connection'
    VPN_GATEWAY = 'vpn-gateway'
    VPC_FLOW_LOG = 'vpc-flow-log'
    CAPACITY_RESERVATION_FLEET = 'capacity-reservation-fleet'
    TRAFFIC_MIRROR_FILTER_RULE = 'traffic-mirror-filter-rule'
    VPC_ENDPOINT_CONNECTION_DEVICE_TYPE = 'vpc-endpoint-connection-device-type'
    VERIFIED_ACCESS_INSTANCE = 'verified-access-instance'
    VERIFIED_ACCESS_GROUP = 'verified-access-group'
    VERIFIED_ACCESS_ENDPOINT = 'verified-access-endpoint'
    VERIFIED_ACCESS_POLICY = 'verified-access-policy'
    VERIFIED_ACCESS_TRUST_PROVIDER = 'verified-access-trust-provider'
    VPN_CONNECTION_DEVICE_TYPE = 'vpn-connection-device-type'
    VPC_BLOCK_PUBLIC_ACCESS_EXCLUSION = 'vpc-block-public-access-exclusion'
    IPAM_RESOURCE_DISCOVERY = 'ipam-resource-discovery'
    IPAM_RESOURCE_DISCOVERY_ASSOCIATION = 'ipam-resource-discovery-association'

class RootDeviceType(enum.Enum):
    EBS = 'ebs'
    INSTANCE_STORE = 'instance-store'

class RouteOrigin(enum.Enum):
    CREATEROUTETABLE = 'CreateRouteTable'
    CREATEROUTE = 'CreateRoute'
    ENABLEVGWROUTEPROPAGATION = 'EnableVgwRoutePropagation'

class RouteState(enum.Enum):
    ACTIVE = 'active'
    BLACKHOLE = 'blackhole'

class RouteTableAssociationStateCode(enum.Enum):
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'
    FAILED = 'failed'

class RuleAction(enum.Enum):
    ALLOW = 'allow'
    DENY = 'deny'

class SelfServicePortal(enum.Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class ServiceConnectivityType(enum.Enum):
    IPV4 = 'ipv4'
    IPV6 = 'ipv6'

class ServiceState(enum.Enum):
    PENDING = 'Pending'
    AVAILABLE = 'Available'
    DELETING = 'Deleting'
    DELETED = 'Deleted'
    FAILED = 'Failed'

class ServiceType(enum.Enum):
    INTERFACE = 'Interface'
    GATEWAY = 'Gateway'
    GATEWAYLOADBALANCER = 'GatewayLoadBalancer'

class ShutdownBehavior(enum.Enum):
    STOP = 'stop'
    TERMINATE = 'terminate'

class SnapshotAttributeName(enum.Enum):
    PRODUCTCODES = 'productCodes'
    CREATEVOLUMEPERMISSION = 'createVolumePermission'

class SnapshotState(enum.Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    ERROR = 'error'
    RECOVERABLE = 'recoverable'
    RECOVERING = 'recovering'

class SpotAllocationStrategy(enum.Enum):
    LOWEST_PRICE = 'lowest-price'
    DIVERSIFIED = 'diversified'
    CAPACITY_OPTIMIZED = 'capacity-optimized'
    CAPACITY_OPTIMIZED_PRIORITIZED = 'capacity-optimized-prioritized'
    PRICE_CAPACITY_OPTIMIZED = 'price-capacity-optimized'

class SpotInstanceInterruptionBehavior(enum.Enum):
    HIBERNATE = 'hibernate'
    STOP = 'stop'
    TERMINATE = 'terminate'

class SpotInstanceState(enum.Enum):
    OPEN = 'open'
    ACTIVE = 'active'
    CLOSED = 'closed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'

class SpotInstanceType(enum.Enum):
    ONE_TIME = 'one-time'
    PERSISTENT = 'persistent'

class SpreadLevel(enum.Enum):
    HOST = 'host'
    RACK = 'rack'

class State(enum.Enum):
    PENDINGACCEPTANCE = 'PendingAcceptance'
    PENDING = 'Pending'
    AVAILABLE = 'Available'
    DELETING = 'Deleting'
    DELETED = 'Deleted'
    REJECTED = 'Rejected'
    FAILED = 'Failed'
    EXPIRED = 'Expired'

class StaticSourcesSupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class StatisticType(enum.Enum):
    P50 = 'p50'

class Status(enum.Enum):
    MOVEINPROGRESS = 'MoveInProgress'
    INVPC = 'InVpc'
    INCLASSIC = 'InClassic'

class StatusName(enum.Enum):
    REACHABILITY = 'reachability'

class StatusType(enum.Enum):
    PASSED = 'passed'
    FAILED = 'failed'
    INSUFFICIENT_DATA = 'insufficient-data'
    INITIALIZING = 'initializing'

class StorageTier(enum.Enum):
    ARCHIVE = 'archive'
    STANDARD = 'standard'

class SubnetCidrBlockStateCode(enum.Enum):
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'
    FAILING = 'failing'
    FAILED = 'failed'

class SubnetCidrReservationType(enum.Enum):
    PREFIX = 'prefix'
    EXPLICIT = 'explicit'

class SubnetState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'

class SummaryStatus(enum.Enum):
    OK = 'ok'
    IMPAIRED = 'impaired'
    INSUFFICIENT_DATA = 'insufficient-data'
    NOT_APPLICABLE = 'not-applicable'
    INITIALIZING = 'initializing'

class SupportedAdditionalProcessorFeature(enum.Enum):
    AMD_SEV_SNP = 'amd-sev-snp'

class TargetCapacityUnitType(enum.Enum):
    VCPU = 'vcpu'
    MEMORY_MIB = 'memory-mib'
    UNITS = 'units'

class TargetStorageTier(enum.Enum):
    ARCHIVE = 'archive'

class TelemetryStatus(enum.Enum):
    UP = 'UP'
    DOWN = 'DOWN'

class Tenancy(enum.Enum):
    DEFAULT = 'default'
    DEDICATED = 'dedicated'
    HOST = 'host'

class TieringOperationStatus(enum.Enum):
    ARCHIVAL_IN_PROGRESS = 'archival-in-progress'
    ARCHIVAL_COMPLETED = 'archival-completed'
    ARCHIVAL_FAILED = 'archival-failed'
    TEMPORARY_RESTORE_IN_PROGRESS = 'temporary-restore-in-progress'
    TEMPORARY_RESTORE_COMPLETED = 'temporary-restore-completed'
    TEMPORARY_RESTORE_FAILED = 'temporary-restore-failed'
    PERMANENT_RESTORE_IN_PROGRESS = 'permanent-restore-in-progress'
    PERMANENT_RESTORE_COMPLETED = 'permanent-restore-completed'
    PERMANENT_RESTORE_FAILED = 'permanent-restore-failed'

class TpmSupportValues(enum.Enum):
    V2_0 = 'v2.0'

class TrafficDirection(enum.Enum):
    INGRESS = 'ingress'
    EGRESS = 'egress'

class TrafficMirrorFilterRuleField(enum.Enum):
    DESTINATION_PORT_RANGE = 'destination-port-range'
    SOURCE_PORT_RANGE = 'source-port-range'
    PROTOCOL = 'protocol'
    DESCRIPTION = 'description'

class TrafficMirrorNetworkService(enum.Enum):
    AMAZON_DNS = 'amazon-dns'

class TrafficMirrorRuleAction(enum.Enum):
    ACCEPT = 'accept'
    REJECT = 'reject'

class TrafficMirrorSessionField(enum.Enum):
    PACKET_LENGTH = 'packet-length'
    DESCRIPTION = 'description'
    VIRTUAL_NETWORK_ID = 'virtual-network-id'

class TrafficMirrorTargetType(enum.Enum):
    NETWORK_INTERFACE = 'network-interface'
    NETWORK_LOAD_BALANCER = 'network-load-balancer'
    GATEWAY_LOAD_BALANCER_ENDPOINT = 'gateway-load-balancer-endpoint'

class TrafficType(enum.Enum):
    ACCEPT = 'ACCEPT'
    REJECT = 'REJECT'
    ALL = 'ALL'

class TransitGatewayAssociationState(enum.Enum):
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'

class TransitGatewayAttachmentResourceType(enum.Enum):
    VPC = 'vpc'
    VPN = 'vpn'
    DIRECT_CONNECT_GATEWAY = 'direct-connect-gateway'
    CONNECT = 'connect'
    PEERING = 'peering'
    TGW_PEERING = 'tgw-peering'

class TransitGatewayAttachmentState(enum.Enum):
    INITIATING = 'initiating'
    INITIATINGREQUEST = 'initiatingRequest'
    PENDINGACCEPTANCE = 'pendingAcceptance'
    ROLLINGBACK = 'rollingBack'
    PENDING = 'pending'
    AVAILABLE = 'available'
    MODIFYING = 'modifying'
    DELETING = 'deleting'
    DELETED = 'deleted'
    FAILED = 'failed'
    REJECTED = 'rejected'
    REJECTING = 'rejecting'
    FAILING = 'failing'

class TransitGatewayConnectPeerState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransitGatewayMulitcastDomainAssociationState(enum.Enum):
    PENDINGACCEPTANCE = 'pendingAcceptance'
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'
    REJECTED = 'rejected'
    FAILED = 'failed'

class TransitGatewayMulticastDomainState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransitGatewayPolicyTableState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransitGatewayPrefixListReferenceState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    MODIFYING = 'modifying'
    DELETING = 'deleting'

class TransitGatewayPropagationState(enum.Enum):
    ENABLING = 'enabling'
    ENABLED = 'enabled'
    DISABLING = 'disabling'
    DISABLED = 'disabled'

class TransitGatewayRouteState(enum.Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    BLACKHOLE = 'blackhole'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransitGatewayRouteTableAnnouncementDirection(enum.Enum):
    OUTGOING = 'outgoing'
    INCOMING = 'incoming'

class TransitGatewayRouteTableAnnouncementState(enum.Enum):
    AVAILABLE = 'available'
    PENDING = 'pending'
    FAILING = 'failing'
    FAILED = 'failed'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransitGatewayRouteTableState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransitGatewayRouteType(enum.Enum):
    STATIC = 'static'
    PROPAGATED = 'propagated'

class TransitGatewayState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    MODIFYING = 'modifying'
    DELETING = 'deleting'
    DELETED = 'deleted'

class TransportProtocol(enum.Enum):
    TCP = 'tcp'
    UDP = 'udp'

class TrustProviderType(enum.Enum):
    USER = 'user'
    DEVICE = 'device'

class TunnelInsideIpVersion(enum.Enum):
    IPV4 = 'ipv4'
    IPV6 = 'ipv6'

class UnlimitedSupportedInstanceFamily(enum.Enum):
    T2 = 't2'
    T3 = 't3'
    T3A = 't3a'
    T4G = 't4g'

class UnsuccessfulInstanceCreditSpecificationErrorCode(enum.Enum):
    INVALIDINSTANCEID_MALFORMED = 'InvalidInstanceID.Malformed'
    INVALIDINSTANCEID_NOTFOUND = 'InvalidInstanceID.NotFound'
    INCORRECTINSTANCESTATE = 'IncorrectInstanceState'
    INSTANCECREDITSPECIFICATION_NOTSUPPORTED = 'InstanceCreditSpecification.NotSupported'

class UsageClassType(enum.Enum):
    SPOT = 'spot'
    ON_DEMAND = 'on-demand'

class UserTrustProviderType(enum.Enum):
    IAM_IDENTITY_CENTER = 'iam-identity-center'
    OIDC = 'oidc'

class VerifiedAccessEndpointAttachmentType(enum.Enum):
    VPC = 'vpc'

class VerifiedAccessEndpointProtocol(enum.Enum):
    HTTP = 'http'
    HTTPS = 'https'

class VerifiedAccessEndpointStatusCode(enum.Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    UPDATING = 'updating'
    DELETING = 'deleting'
    DELETED = 'deleted'

class VerifiedAccessEndpointType(enum.Enum):
    LOAD_BALANCER = 'load-balancer'
    NETWORK_INTERFACE = 'network-interface'

class VerifiedAccessLogDeliveryStatusCode(enum.Enum):
    SUCCESS = 'success'
    FAILED = 'failed'

class VirtualizationType(enum.Enum):
    HVM = 'hvm'
    PARAVIRTUAL = 'paravirtual'

class VolumeAttachmentState(enum.Enum):
    ATTACHING = 'attaching'
    ATTACHED = 'attached'
    DETACHING = 'detaching'
    DETACHED = 'detached'
    BUSY = 'busy'

class VolumeAttributeName(enum.Enum):
    AUTOENABLEIO = 'autoEnableIO'
    PRODUCTCODES = 'productCodes'

class VolumeModificationState(enum.Enum):
    MODIFYING = 'modifying'
    OPTIMIZING = 'optimizing'
    COMPLETED = 'completed'
    FAILED = 'failed'

class VolumeState(enum.Enum):
    CREATING = 'creating'
    AVAILABLE = 'available'
    IN_USE = 'in-use'
    DELETING = 'deleting'
    DELETED = 'deleted'
    ERROR = 'error'

class VolumeStatusInfoStatus(enum.Enum):
    OK = 'ok'
    IMPAIRED = 'impaired'
    INSUFFICIENT_DATA = 'insufficient-data'

class VolumeStatusName(enum.Enum):
    IO_ENABLED = 'io-enabled'
    IO_PERFORMANCE = 'io-performance'

class VolumeType(enum.Enum):
    STANDARD = 'standard'
    IO1 = 'io1'
    IO2 = 'io2'
    GP2 = 'gp2'
    SC1 = 'sc1'
    ST1 = 'st1'
    GP3 = 'gp3'

class VpcAttributeName(enum.Enum):
    ENABLEDNSSUPPORT = 'enableDnsSupport'
    ENABLEDNSHOSTNAMES = 'enableDnsHostnames'
    ENABLENETWORKADDRESSUSAGEMETRICS = 'enableNetworkAddressUsageMetrics'

class VpcCidrBlockStateCode(enum.Enum):
    ASSOCIATING = 'associating'
    ASSOCIATED = 'associated'
    DISASSOCIATING = 'disassociating'
    DISASSOCIATED = 'disassociated'
    FAILING = 'failing'
    FAILED = 'failed'

class VpcEndpointType(enum.Enum):
    INTERFACE = 'Interface'
    GATEWAY = 'Gateway'
    GATEWAYLOADBALANCER = 'GatewayLoadBalancer'

class VpcPeeringConnectionStateReasonCode(enum.Enum):
    INITIATING_REQUEST = 'initiating-request'
    PENDING_ACCEPTANCE = 'pending-acceptance'
    ACTIVE = 'active'
    DELETED = 'deleted'
    REJECTED = 'rejected'
    FAILED = 'failed'
    EXPIRED = 'expired'
    PROVISIONING = 'provisioning'
    DELETING = 'deleting'

class VpcState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'

class VpcTenancy(enum.Enum):
    DEFAULT = 'default'

class VpnEcmpSupportValue(enum.Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class VpnProtocol(enum.Enum):
    OPENVPN = 'openvpn'

class VpnState(enum.Enum):
    PENDING = 'pending'
    AVAILABLE = 'available'
    DELETING = 'deleting'
    DELETED = 'deleted'

class VpnStaticRouteSource(enum.Enum):
    STATIC = 'Static'

class WeekDay(enum.Enum):
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'

class scope(enum.Enum):
    AVAILABILITY_ZONE = 'Availability Zone'
    REGION = 'Region'

class AcceleratorCount(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class AcceleratorCountRequest(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class AcceleratorTotalMemoryMiB(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class AcceleratorTotalMemoryMiBRequest(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class AcceptAddressTransferRequest(_EC2ModelBase):
    address: String = pydantic.Field(None, alias="Address")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AcceptAddressTransferResult(_EC2ModelBase):
    address_transfer: 'AddressTransfer' = pydantic.Field(None, alias="AddressTransfer")

class AcceptReservedInstancesExchangeQuoteRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    reserved_instance_ids: ReservedInstanceIdSet = pydantic.Field(None, alias="ReservedInstanceIds")
    target_configurations: TargetConfigurationRequestSet = pydantic.Field(None, alias="TargetConfigurations")

class AcceptReservedInstancesExchangeQuoteResult(_EC2ModelBase):
    exchange_id: String = pydantic.Field(None, alias="ExchangeId")

class AcceptTransitGatewayMulticastDomainAssociationsRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    subnet_ids: ValueStringList = pydantic.Field(None, alias="SubnetIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AcceptTransitGatewayMulticastDomainAssociationsResult(_EC2ModelBase):
    associations: 'TransitGatewayMulticastDomainAssociations' = pydantic.Field(None, alias="Associations")

class AcceptTransitGatewayPeeringAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AcceptTransitGatewayPeeringAttachmentResult(_EC2ModelBase):
    transit_gateway_peering_attachment: 'TransitGatewayPeeringAttachment' = pydantic.Field(None, alias="TransitGatewayPeeringAttachment")

class AcceptTransitGatewayVpcAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AcceptTransitGatewayVpcAttachmentResult(_EC2ModelBase):
    transit_gateway_vpc_attachment: 'TransitGatewayVpcAttachment' = pydantic.Field(None, alias="TransitGatewayVpcAttachment")

class AcceptVpcEndpointConnectionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    vpc_endpoint_ids: VpcEndpointIdList = pydantic.Field(None, alias="VpcEndpointIds")

class AcceptVpcEndpointConnectionsResult(_EC2ModelBase):
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class AcceptVpcPeeringConnectionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_peering_connection_id: VpcPeeringConnectionIdWithResolver = pydantic.Field(None, alias="VpcPeeringConnectionId")

class AcceptVpcPeeringConnectionResult(_EC2ModelBase):
    vpc_peering_connection: 'VpcPeeringConnection' = pydantic.Field(None, alias="VpcPeeringConnection")

class AccessScopeAnalysisFinding(_EC2ModelBase):
    network_insights_access_scope_analysis_id: NetworkInsightsAccessScopeAnalysisId = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisId")
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    finding_id: String = pydantic.Field(None, alias="FindingId")
    finding_components: PathComponentList = pydantic.Field(None, alias="FindingComponents")

class AccessScopePath(_EC2ModelBase):
    source: 'PathStatement' = pydantic.Field(None, alias="Source")
    destination: 'PathStatement' = pydantic.Field(None, alias="Destination")
    through_resources: ThroughResourcesStatementList = pydantic.Field(None, alias="ThroughResources")

class AccessScopePathRequest(_EC2ModelBase):
    source: 'PathStatementRequest' = pydantic.Field(None, alias="Source")
    destination: 'PathStatementRequest' = pydantic.Field(None, alias="Destination")
    through_resources: ThroughResourcesStatementRequestList = pydantic.Field(None, alias="ThroughResources")

class AccountAttribute(_EC2ModelBase):
    attribute_name: String = pydantic.Field(None, alias="AttributeName")
    attribute_values: AccountAttributeValueList = pydantic.Field(None, alias="AttributeValues")

class AccountAttributeValue(_EC2ModelBase):
    attribute_value: String = pydantic.Field(None, alias="AttributeValue")

class ActiveInstance(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    spot_instance_request_id: String = pydantic.Field(None, alias="SpotInstanceRequestId")
    instance_health: InstanceHealthStatus = pydantic.Field(None, alias="InstanceHealth")

class AddIpamOperatingRegion(_EC2ModelBase):
    region_name: String = pydantic.Field(None, alias="RegionName")

class AddPrefixListEntry(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    description: String = pydantic.Field(None, alias="Description")

class AddedPrincipal(_EC2ModelBase):
    principal_type: PrincipalType = pydantic.Field(None, alias="PrincipalType")
    principal: String = pydantic.Field(None, alias="Principal")
    service_permission_id: String = pydantic.Field(None, alias="ServicePermissionId")
    service_id: String = pydantic.Field(None, alias="ServiceId")

class AdditionalDetail(_EC2ModelBase):
    additional_detail_type: String = pydantic.Field(None, alias="AdditionalDetailType")
    component: 'AnalysisComponent' = pydantic.Field(None, alias="Component")
    vpc_endpoint_service: 'AnalysisComponent' = pydantic.Field(None, alias="VpcEndpointService")
    rule_options: RuleOptionList = pydantic.Field(None, alias="RuleOptions")
    rule_group_type_pairs: RuleGroupTypePairList = pydantic.Field(None, alias="RuleGroupTypePairs")
    rule_group_rule_options_pairs: RuleGroupRuleOptionsPairList = pydantic.Field(None, alias="RuleGroupRuleOptionsPairs")
    service_name: String = pydantic.Field(None, alias="ServiceName")
    load_balancers: AnalysisComponentList = pydantic.Field(None, alias="LoadBalancers")

class Address(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    association_id: String = pydantic.Field(None, alias="AssociationId")
    domain: DomainType = pydantic.Field(None, alias="Domain")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    network_interface_owner_id: String = pydantic.Field(None, alias="NetworkInterfaceOwnerId")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    tags: TagList = pydantic.Field(None, alias="Tags")
    public_ipv_4_pool: String = pydantic.Field(None, alias="PublicIpv4Pool")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    customer_owned_ip: String = pydantic.Field(None, alias="CustomerOwnedIp")
    customer_owned_ipv_4_pool: String = pydantic.Field(None, alias="CustomerOwnedIpv4Pool")
    carrier_ip: String = pydantic.Field(None, alias="CarrierIp")

class AddressAttribute(_EC2ModelBase):
    public_ip: PublicIpAddress = pydantic.Field(None, alias="PublicIp")
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    ptr_record: String = pydantic.Field(None, alias="PtrRecord")
    ptr_record_update: 'PtrUpdateStatus' = pydantic.Field(None, alias="PtrRecordUpdate")

class AddressTransfer(_EC2ModelBase):
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    transfer_account_id: String = pydantic.Field(None, alias="TransferAccountId")
    transfer_offer_expiration_timestamp: MillisecondDateTime = pydantic.Field(None, alias="TransferOfferExpirationTimestamp")
    transfer_offer_accepted_timestamp: MillisecondDateTime = pydantic.Field(None, alias="TransferOfferAcceptedTimestamp")
    address_transfer_status: AddressTransferStatus = pydantic.Field(None, alias="AddressTransferStatus")

class AdvertiseByoipCidrRequest(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AdvertiseByoipCidrResult(_EC2ModelBase):
    byoip_cidr: 'ByoipCidr' = pydantic.Field(None, alias="ByoipCidr")

class AllocateAddressRequest(_EC2ModelBase):
    domain: DomainType = pydantic.Field(None, alias="Domain")
    address: PublicIpAddress = pydantic.Field(None, alias="Address")
    public_ipv_4_pool: Ipv4PoolEc2Id = pydantic.Field(None, alias="PublicIpv4Pool")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    customer_owned_ipv_4_pool: String = pydantic.Field(None, alias="CustomerOwnedIpv4Pool")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class AllocateAddressResult(_EC2ModelBase):
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    public_ipv_4_pool: String = pydantic.Field(None, alias="PublicIpv4Pool")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    domain: DomainType = pydantic.Field(None, alias="Domain")
    customer_owned_ip: String = pydantic.Field(None, alias="CustomerOwnedIp")
    customer_owned_ipv_4_pool: String = pydantic.Field(None, alias="CustomerOwnedIpv4Pool")
    carrier_ip: String = pydantic.Field(None, alias="CarrierIp")

class AllocateHostsRequest(_EC2ModelBase):
    auto_placement: AutoPlacement = pydantic.Field(None, alias="AutoPlacement")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    instance_family: String = pydantic.Field(None, alias="InstanceFamily")
    quantity: Integer = pydantic.Field(None, alias="Quantity")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    host_recovery: HostRecovery = pydantic.Field(None, alias="HostRecovery")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    host_maintenance: HostMaintenance = pydantic.Field(None, alias="HostMaintenance")

class AllocateHostsResult(_EC2ModelBase):
    host_ids: ResponseHostIdList = pydantic.Field(None, alias="HostIds")

class AllocateIpamPoolCidrRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    cidr: String = pydantic.Field(None, alias="Cidr")
    netmask_length: Integer = pydantic.Field(None, alias="NetmaskLength")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    description: String = pydantic.Field(None, alias="Description")
    preview_next_cidr: Boolean = pydantic.Field(None, alias="PreviewNextCidr")
    disallowed_cidrs: IpamPoolAllocationDisallowedCidrs = pydantic.Field(None, alias="DisallowedCidrs")

class AllocateIpamPoolCidrResult(_EC2ModelBase):
    ipam_pool_allocation: 'IpamPoolAllocation' = pydantic.Field(None, alias="IpamPoolAllocation")

class AllowedPrincipal(_EC2ModelBase):
    principal_type: PrincipalType = pydantic.Field(None, alias="PrincipalType")
    principal: String = pydantic.Field(None, alias="Principal")
    service_permission_id: String = pydantic.Field(None, alias="ServicePermissionId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    service_id: String = pydantic.Field(None, alias="ServiceId")

class AlternatePathHint(_EC2ModelBase):
    component_id: String = pydantic.Field(None, alias="ComponentId")
    component_arn: String = pydantic.Field(None, alias="ComponentArn")

class AnalysisAclRule(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    egress: Boolean = pydantic.Field(None, alias="Egress")
    port_range: 'PortRange' = pydantic.Field(None, alias="PortRange")
    protocol: String = pydantic.Field(None, alias="Protocol")
    rule_action: String = pydantic.Field(None, alias="RuleAction")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")

class AnalysisComponent(_EC2ModelBase):
    id: String = pydantic.Field(None, alias="Id")
    arn: String = pydantic.Field(None, alias="Arn")
    name: String = pydantic.Field(None, alias="Name")

class AnalysisLoadBalancerListener(_EC2ModelBase):
    load_balancer_port: Port = pydantic.Field(None, alias="LoadBalancerPort")
    instance_port: Port = pydantic.Field(None, alias="InstancePort")

class AnalysisLoadBalancerTarget(_EC2ModelBase):
    address: IpAddress = pydantic.Field(None, alias="Address")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    instance: 'AnalysisComponent' = pydantic.Field(None, alias="Instance")
    port: Port = pydantic.Field(None, alias="Port")

class AnalysisPacketHeader(_EC2ModelBase):
    destination_addresses: IpAddressList = pydantic.Field(None, alias="DestinationAddresses")
    destination_port_ranges: PortRangeList = pydantic.Field(None, alias="DestinationPortRanges")
    protocol: String = pydantic.Field(None, alias="Protocol")
    source_addresses: IpAddressList = pydantic.Field(None, alias="SourceAddresses")
    source_port_ranges: PortRangeList = pydantic.Field(None, alias="SourcePortRanges")

class AnalysisRouteTableRoute(_EC2ModelBase):
    destination_cidr: String = pydantic.Field(None, alias="DestinationCidr")
    destination_prefix_list_id: String = pydantic.Field(None, alias="DestinationPrefixListId")
    egress_only_internet_gateway_id: String = pydantic.Field(None, alias="EgressOnlyInternetGatewayId")
    gateway_id: String = pydantic.Field(None, alias="GatewayId")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    nat_gateway_id: String = pydantic.Field(None, alias="NatGatewayId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    origin: String = pydantic.Field(None, alias="Origin")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    vpc_peering_connection_id: String = pydantic.Field(None, alias="VpcPeeringConnectionId")
    state: String = pydantic.Field(None, alias="State")
    carrier_gateway_id: String = pydantic.Field(None, alias="CarrierGatewayId")
    core_network_arn: ResourceArn = pydantic.Field(None, alias="CoreNetworkArn")
    local_gateway_id: String = pydantic.Field(None, alias="LocalGatewayId")

class AnalysisSecurityGroupRule(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    direction: String = pydantic.Field(None, alias="Direction")
    security_group_id: String = pydantic.Field(None, alias="SecurityGroupId")
    port_range: 'PortRange' = pydantic.Field(None, alias="PortRange")
    prefix_list_id: String = pydantic.Field(None, alias="PrefixListId")
    protocol: String = pydantic.Field(None, alias="Protocol")

class ApplySecurityGroupsToClientVpnTargetNetworkRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    security_group_ids: ClientVpnSecurityGroupIdSet = pydantic.Field(None, alias="SecurityGroupIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ApplySecurityGroupsToClientVpnTargetNetworkResult(_EC2ModelBase):
    security_group_ids: ClientVpnSecurityGroupIdSet = pydantic.Field(None, alias="SecurityGroupIds")

class AssignIpv6AddressesRequest(_EC2ModelBase):
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: Ipv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    ipv_6_prefix_count: Integer = pydantic.Field(None, alias="Ipv6PrefixCount")
    ipv_6_prefixes: IpPrefixList = pydantic.Field(None, alias="Ipv6Prefixes")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")

class AssignIpv6AddressesResult(_EC2ModelBase):
    assigned_ipv_6_addresses: Ipv6AddressList = pydantic.Field(None, alias="AssignedIpv6Addresses")
    assigned_ipv_6_prefixes: IpPrefixList = pydantic.Field(None, alias="AssignedIpv6Prefixes")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")

class AssignPrivateIpAddressesRequest(_EC2ModelBase):
    allow_reassignment: Boolean = pydantic.Field(None, alias="AllowReassignment")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_addresses: PrivateIpAddressStringList = pydantic.Field(None, alias="PrivateIpAddresses")
    secondary_private_ip_address_count: Integer = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")
    ipv_4_prefixes: IpPrefixList = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_4_prefix_count: Integer = pydantic.Field(None, alias="Ipv4PrefixCount")

class AssignPrivateIpAddressesResult(_EC2ModelBase):
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    assigned_private_ip_addresses: AssignedPrivateIpAddressList = pydantic.Field(None, alias="AssignedPrivateIpAddresses")
    assigned_ipv_4_prefixes: Ipv4PrefixesList = pydantic.Field(None, alias="AssignedIpv4Prefixes")

class AssignPrivateNatGatewayAddressRequest(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    private_ip_addresses: IpList = pydantic.Field(None, alias="PrivateIpAddresses")
    private_ip_address_count: PrivateIpAddressCount = pydantic.Field(None, alias="PrivateIpAddressCount")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssignPrivateNatGatewayAddressResult(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    nat_gateway_addresses: NatGatewayAddressList = pydantic.Field(None, alias="NatGatewayAddresses")

class AssignedPrivateIpAddress(_EC2ModelBase):
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")

class AssociateAddressRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    public_ip: EipAllocationPublicIp = pydantic.Field(None, alias="PublicIp")
    allow_reassociation: Boolean = pydantic.Field(None, alias="AllowReassociation")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")

class AssociateAddressResult(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")

class AssociateClientVpnTargetNetworkRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateClientVpnTargetNetworkResult(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    status: 'AssociationStatus' = pydantic.Field(None, alias="Status")

class AssociateDhcpOptionsRequest(_EC2ModelBase):
    dhcp_options_id: DefaultingDhcpOptionsId = pydantic.Field(None, alias="DhcpOptionsId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateEnclaveCertificateIamRoleRequest(_EC2ModelBase):
    certificate_arn: CertificateId = pydantic.Field(None, alias="CertificateArn")
    role_arn: RoleId = pydantic.Field(None, alias="RoleArn")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateEnclaveCertificateIamRoleResult(_EC2ModelBase):
    certificate_s_3_bucket_name: String = pydantic.Field(None, alias="CertificateS3BucketName")
    certificate_s_3_object_key: String = pydantic.Field(None, alias="CertificateS3ObjectKey")
    encryption_kms_key_id: String = pydantic.Field(None, alias="EncryptionKmsKeyId")

class AssociateIamInstanceProfileRequest(_EC2ModelBase):
    iam_instance_profile: 'IamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")

class AssociateIamInstanceProfileResult(_EC2ModelBase):
    iam_instance_profile_association: 'IamInstanceProfileAssociation' = pydantic.Field(None, alias="IamInstanceProfileAssociation")

class AssociateInstanceEventWindowRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_event_window_id: InstanceEventWindowId = pydantic.Field(None, alias="InstanceEventWindowId")
    association_target: 'InstanceEventWindowAssociationRequest' = pydantic.Field(None, alias="AssociationTarget")

class AssociateInstanceEventWindowResult(_EC2ModelBase):
    instance_event_window: 'InstanceEventWindow' = pydantic.Field(None, alias="InstanceEventWindow")

class AssociateIpamResourceDiscoveryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class AssociateIpamResourceDiscoveryResult(_EC2ModelBase):
    ipam_resource_discovery_association: 'IpamResourceDiscoveryAssociation' = pydantic.Field(None, alias="IpamResourceDiscoveryAssociation")

class AssociateNatGatewayAddressRequest(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    allocation_ids: AllocationIdList = pydantic.Field(None, alias="AllocationIds")
    private_ip_addresses: IpList = pydantic.Field(None, alias="PrivateIpAddresses")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateNatGatewayAddressResult(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    nat_gateway_addresses: NatGatewayAddressList = pydantic.Field(None, alias="NatGatewayAddresses")

class AssociateRouteTableRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    gateway_id: RouteGatewayId = pydantic.Field(None, alias="GatewayId")

class AssociateRouteTableResult(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    association_state: 'RouteTableAssociationState' = pydantic.Field(None, alias="AssociationState")

class AssociateSubnetCidrBlockRequest(_EC2ModelBase):
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")

class AssociateSubnetCidrBlockResult(_EC2ModelBase):
    ipv_6_cidr_block_association: 'SubnetIpv6CidrBlockAssociation' = pydantic.Field(None, alias="Ipv6CidrBlockAssociation")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")

class AssociateTransitGatewayMulticastDomainRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    subnet_ids: TransitGatewaySubnetIdList = pydantic.Field(None, alias="SubnetIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateTransitGatewayMulticastDomainResult(_EC2ModelBase):
    associations: 'TransitGatewayMulticastDomainAssociations' = pydantic.Field(None, alias="Associations")

class AssociateTransitGatewayPolicyTableRequest(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateTransitGatewayPolicyTableResult(_EC2ModelBase):
    association: 'TransitGatewayPolicyTableAssociation' = pydantic.Field(None, alias="Association")

class AssociateTransitGatewayRouteTableRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateTransitGatewayRouteTableResult(_EC2ModelBase):
    association: 'TransitGatewayAssociation' = pydantic.Field(None, alias="Association")

class AssociateTrunkInterfaceRequest(_EC2ModelBase):
    branch_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="BranchInterfaceId")
    trunk_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="TrunkInterfaceId")
    vlan_id: Integer = pydantic.Field(None, alias="VlanId")
    gre_key: Integer = pydantic.Field(None, alias="GreKey")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AssociateTrunkInterfaceResult(_EC2ModelBase):
    interface_association: 'TrunkInterfaceAssociation' = pydantic.Field(None, alias="InterfaceAssociation")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class AssociateVpcCidrBlockRequest(_EC2ModelBase):
    amazon_provided_ipv_6_cidr_block: Boolean = pydantic.Field(None, alias="AmazonProvidedIpv6CidrBlock")
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    ipv_6_cidr_block_network_border_group: String = pydantic.Field(None, alias="Ipv6CidrBlockNetworkBorderGroup")
    ipv_6_pool: Ipv6PoolEc2Id = pydantic.Field(None, alias="Ipv6Pool")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    ipv_4_ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="Ipv4IpamPoolId")
    ipv_4_netmask_length: NetmaskLength = pydantic.Field(None, alias="Ipv4NetmaskLength")
    ipv_6_ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="Ipv6IpamPoolId")
    ipv_6_netmask_length: NetmaskLength = pydantic.Field(None, alias="Ipv6NetmaskLength")

class AssociateVpcCidrBlockResult(_EC2ModelBase):
    ipv_6_cidr_block_association: 'VpcIpv6CidrBlockAssociation' = pydantic.Field(None, alias="Ipv6CidrBlockAssociation")
    cidr_block_association: 'VpcCidrBlockAssociation' = pydantic.Field(None, alias="CidrBlockAssociation")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class AssociatedRole(_EC2ModelBase):
    associated_role_arn: ResourceArn = pydantic.Field(None, alias="AssociatedRoleArn")
    certificate_s_3_bucket_name: String = pydantic.Field(None, alias="CertificateS3BucketName")
    certificate_s_3_object_key: String = pydantic.Field(None, alias="CertificateS3ObjectKey")
    encryption_kms_key_id: String = pydantic.Field(None, alias="EncryptionKmsKeyId")

class AssociatedTargetNetwork(_EC2ModelBase):
    network_id: String = pydantic.Field(None, alias="NetworkId")
    network_type: AssociatedNetworkType = pydantic.Field(None, alias="NetworkType")

class AssociationStatus(_EC2ModelBase):
    code: AssociationStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class AthenaIntegration(_EC2ModelBase):
    integration_result_s_3_destination_arn: String = pydantic.Field(None, alias="IntegrationResultS3DestinationArn")
    partition_load_frequency: PartitionLoadFrequency = pydantic.Field(None, alias="PartitionLoadFrequency")
    partition_start_date: MillisecondDateTime = pydantic.Field(None, alias="PartitionStartDate")
    partition_end_date: MillisecondDateTime = pydantic.Field(None, alias="PartitionEndDate")

class AttachClassicLinkVpcRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    groups: GroupIdStringList = pydantic.Field(None, alias="Groups")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class AttachClassicLinkVpcResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class AttachInternetGatewayRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    internet_gateway_id: InternetGatewayId = pydantic.Field(None, alias="InternetGatewayId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class AttachNetworkInterfaceRequest(_EC2ModelBase):
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")
    ena_srd_specification: 'EnaSrdSpecification' = pydantic.Field(None, alias="EnaSrdSpecification")

class AttachNetworkInterfaceResult(_EC2ModelBase):
    attachment_id: String = pydantic.Field(None, alias="AttachmentId")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")

class AttachVerifiedAccessTrustProviderRequest(_EC2ModelBase):
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    verified_access_trust_provider_id: VerifiedAccessTrustProviderId = pydantic.Field(None, alias="VerifiedAccessTrustProviderId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AttachVerifiedAccessTrustProviderResult(_EC2ModelBase):
    verified_access_trust_provider: 'VerifiedAccessTrustProvider' = pydantic.Field(None, alias="VerifiedAccessTrustProvider")
    verified_access_instance: 'VerifiedAccessInstance' = pydantic.Field(None, alias="VerifiedAccessInstance")

class AttachVolumeRequest(_EC2ModelBase):
    device: String = pydantic.Field(None, alias="Device")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AttachVpnGatewayRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    vpn_gateway_id: VpnGatewayId = pydantic.Field(None, alias="VpnGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AttachVpnGatewayResult(_EC2ModelBase):
    vpc_attachment: 'VpcAttachment' = pydantic.Field(None, alias="VpcAttachment")

class AttachmentEnaSrdSpecification(_EC2ModelBase):
    ena_srd_enabled: Boolean = pydantic.Field(None, alias="EnaSrdEnabled")
    ena_srd_udp_specification: 'AttachmentEnaSrdUdpSpecification' = pydantic.Field(None, alias="EnaSrdUdpSpecification")

class AttachmentEnaSrdUdpSpecification(_EC2ModelBase):
    ena_srd_udp_enabled: Boolean = pydantic.Field(None, alias="EnaSrdUdpEnabled")

class AttributeBooleanValue(_EC2ModelBase):
    value: Boolean = pydantic.Field(None, alias="Value")

class AttributeValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class AuthorizationRule(_EC2ModelBase):
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    description: String = pydantic.Field(None, alias="Description")
    group_id: String = pydantic.Field(None, alias="GroupId")
    access_all: Boolean = pydantic.Field(None, alias="AccessAll")
    destination_cidr: String = pydantic.Field(None, alias="DestinationCidr")
    status: 'ClientVpnAuthorizationRuleStatus' = pydantic.Field(None, alias="Status")

class AuthorizeClientVpnIngressRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    target_network_cidr: String = pydantic.Field(None, alias="TargetNetworkCidr")
    access_group_id: String = pydantic.Field(None, alias="AccessGroupId")
    authorize_all_groups: Boolean = pydantic.Field(None, alias="AuthorizeAllGroups")
    description: String = pydantic.Field(None, alias="Description")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class AuthorizeClientVpnIngressResult(_EC2ModelBase):
    status: 'ClientVpnAuthorizationRuleStatus' = pydantic.Field(None, alias="Status")

class AuthorizeSecurityGroupEgressRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    cidr_ip: String = pydantic.Field(None, alias="CidrIp")
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    source_security_group_name: String = pydantic.Field(None, alias="SourceSecurityGroupName")
    source_security_group_owner_id: String = pydantic.Field(None, alias="SourceSecurityGroupOwnerId")

class AuthorizeSecurityGroupEgressResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")
    security_group_rules: SecurityGroupRuleList = pydantic.Field(None, alias="SecurityGroupRules")

class AuthorizeSecurityGroupIngressRequest(_EC2ModelBase):
    cidr_ip: String = pydantic.Field(None, alias="CidrIp")
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    group_name: SecurityGroupName = pydantic.Field(None, alias="GroupName")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    source_security_group_name: String = pydantic.Field(None, alias="SourceSecurityGroupName")
    source_security_group_owner_id: String = pydantic.Field(None, alias="SourceSecurityGroupOwnerId")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class AuthorizeSecurityGroupIngressResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")
    security_group_rules: SecurityGroupRuleList = pydantic.Field(None, alias="SecurityGroupRules")

class AvailabilityZone(_EC2ModelBase):
    state: AvailabilityZoneState = pydantic.Field(None, alias="State")
    opt_in_status: AvailabilityZoneOptInStatus = pydantic.Field(None, alias="OptInStatus")
    messages: AvailabilityZoneMessageList = pydantic.Field(None, alias="Messages")
    region_name: String = pydantic.Field(None, alias="RegionName")
    zone_name: String = pydantic.Field(None, alias="ZoneName")
    zone_id: String = pydantic.Field(None, alias="ZoneId")
    group_name: String = pydantic.Field(None, alias="GroupName")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    zone_type: String = pydantic.Field(None, alias="ZoneType")
    parent_zone_name: String = pydantic.Field(None, alias="ParentZoneName")
    parent_zone_id: String = pydantic.Field(None, alias="ParentZoneId")

class AvailabilityZoneMessage(_EC2ModelBase):
    message: String = pydantic.Field(None, alias="Message")

class AvailableCapacity(_EC2ModelBase):
    available_instance_capacity: AvailableInstanceCapacityList = pydantic.Field(None, alias="AvailableInstanceCapacity")
    available_v_cpus: Integer = pydantic.Field(None, alias="AvailableVCpus")

class BaselineEbsBandwidthMbps(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class BaselineEbsBandwidthMbpsRequest(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class BlobAttributeValue(_EC2ModelBase):
    value: Blob = pydantic.Field(None, alias="Value")

class BlockDeviceMapping(_EC2ModelBase):
    device_name: String = pydantic.Field(None, alias="DeviceName")
    virtual_name: String = pydantic.Field(None, alias="VirtualName")
    ebs: 'EbsBlockDevice' = pydantic.Field(None, alias="Ebs")
    no_device: String = pydantic.Field(None, alias="NoDevice")

class BundleInstanceRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    storage: 'Storage' = pydantic.Field(None, alias="Storage")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class BundleInstanceResult(_EC2ModelBase):
    bundle_task: 'BundleTask' = pydantic.Field(None, alias="BundleTask")

class BundleTask(_EC2ModelBase):
    bundle_id: String = pydantic.Field(None, alias="BundleId")
    bundle_task_error: 'BundleTaskError' = pydantic.Field(None, alias="BundleTaskError")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    progress: String = pydantic.Field(None, alias="Progress")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")
    state: BundleTaskState = pydantic.Field(None, alias="State")
    storage: 'Storage' = pydantic.Field(None, alias="Storage")
    update_time: DateTime = pydantic.Field(None, alias="UpdateTime")

class BundleTaskError(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ByoipCidr(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    description: String = pydantic.Field(None, alias="Description")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    state: ByoipCidrState = pydantic.Field(None, alias="State")

class CancelBundleTaskRequest(_EC2ModelBase):
    bundle_id: BundleId = pydantic.Field(None, alias="BundleId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CancelBundleTaskResult(_EC2ModelBase):
    bundle_task: 'BundleTask' = pydantic.Field(None, alias="BundleTask")

class CancelCapacityReservationFleetError(_EC2ModelBase):
    code: CancelCapacityReservationFleetErrorCode = pydantic.Field(None, alias="Code")
    message: CancelCapacityReservationFleetErrorMessage = pydantic.Field(None, alias="Message")

class CancelCapacityReservationFleetsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    capacity_reservation_fleet_ids: CapacityReservationFleetIdSet = pydantic.Field(None, alias="CapacityReservationFleetIds")

class CancelCapacityReservationFleetsResult(_EC2ModelBase):
    successful_fleet_cancellations: CapacityReservationFleetCancellationStateSet = pydantic.Field(None, alias="SuccessfulFleetCancellations")
    failed_fleet_cancellations: FailedCapacityReservationFleetCancellationResultSet = pydantic.Field(None, alias="FailedFleetCancellations")

class CancelCapacityReservationRequest(_EC2ModelBase):
    capacity_reservation_id: CapacityReservationId = pydantic.Field(None, alias="CapacityReservationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CancelCapacityReservationResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class CancelConversionRequest(_EC2ModelBase):
    conversion_task_id: ConversionTaskId = pydantic.Field(None, alias="ConversionTaskId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    reason_message: String = pydantic.Field(None, alias="ReasonMessage")

class CancelExportTaskRequest(_EC2ModelBase):
    export_task_id: ExportVmTaskId = pydantic.Field(None, alias="ExportTaskId")

class CancelImageLaunchPermissionRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CancelImageLaunchPermissionResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class CancelImportTaskRequest(_EC2ModelBase):
    cancel_reason: String = pydantic.Field(None, alias="CancelReason")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    import_task_id: ImportTaskId = pydantic.Field(None, alias="ImportTaskId")

class CancelImportTaskResult(_EC2ModelBase):
    import_task_id: String = pydantic.Field(None, alias="ImportTaskId")
    previous_state: String = pydantic.Field(None, alias="PreviousState")
    state: String = pydantic.Field(None, alias="State")

class CancelReservedInstancesListingRequest(_EC2ModelBase):
    reserved_instances_listing_id: ReservedInstancesListingId = pydantic.Field(None, alias="ReservedInstancesListingId")

class CancelReservedInstancesListingResult(_EC2ModelBase):
    reserved_instances_listings: ReservedInstancesListingList = pydantic.Field(None, alias="ReservedInstancesListings")

class CancelSpotFleetRequestsError(_EC2ModelBase):
    code: CancelBatchErrorCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class CancelSpotFleetRequestsErrorItem(_EC2ModelBase):
    error: 'CancelSpotFleetRequestsError' = pydantic.Field(None, alias="Error")
    spot_fleet_request_id: String = pydantic.Field(None, alias="SpotFleetRequestId")

class CancelSpotFleetRequestsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    spot_fleet_request_ids: SpotFleetRequestIdList = pydantic.Field(None, alias="SpotFleetRequestIds")
    terminate_instances: Boolean = pydantic.Field(None, alias="TerminateInstances")

class CancelSpotFleetRequestsResponse(_EC2ModelBase):
    successful_fleet_requests: CancelSpotFleetRequestsSuccessSet = pydantic.Field(None, alias="SuccessfulFleetRequests")
    unsuccessful_fleet_requests: CancelSpotFleetRequestsErrorSet = pydantic.Field(None, alias="UnsuccessfulFleetRequests")

class CancelSpotFleetRequestsSuccessItem(_EC2ModelBase):
    current_spot_fleet_request_state: BatchState = pydantic.Field(None, alias="CurrentSpotFleetRequestState")
    previous_spot_fleet_request_state: BatchState = pydantic.Field(None, alias="PreviousSpotFleetRequestState")
    spot_fleet_request_id: String = pydantic.Field(None, alias="SpotFleetRequestId")

class CancelSpotInstanceRequestsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    spot_instance_request_ids: SpotInstanceRequestIdList = pydantic.Field(None, alias="SpotInstanceRequestIds")

class CancelSpotInstanceRequestsResult(_EC2ModelBase):
    cancelled_spot_instance_requests: CancelledSpotInstanceRequestList = pydantic.Field(None, alias="CancelledSpotInstanceRequests")

class CancelledSpotInstanceRequest(_EC2ModelBase):
    spot_instance_request_id: String = pydantic.Field(None, alias="SpotInstanceRequestId")
    state: CancelSpotInstanceRequestState = pydantic.Field(None, alias="State")

class CapacityAllocation(_EC2ModelBase):
    allocation_type: AllocationType = pydantic.Field(None, alias="AllocationType")
    count: Integer = pydantic.Field(None, alias="Count")

class CapacityReservation(_EC2ModelBase):
    capacity_reservation_id: String = pydantic.Field(None, alias="CapacityReservationId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    capacity_reservation_arn: String = pydantic.Field(None, alias="CapacityReservationArn")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    instance_platform: CapacityReservationInstancePlatform = pydantic.Field(None, alias="InstancePlatform")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    tenancy: CapacityReservationTenancy = pydantic.Field(None, alias="Tenancy")
    total_instance_count: Integer = pydantic.Field(None, alias="TotalInstanceCount")
    available_instance_count: Integer = pydantic.Field(None, alias="AvailableInstanceCount")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    ephemeral_storage: Boolean = pydantic.Field(None, alias="EphemeralStorage")
    state: CapacityReservationState = pydantic.Field(None, alias="State")
    start_date: MillisecondDateTime = pydantic.Field(None, alias="StartDate")
    end_date: DateTime = pydantic.Field(None, alias="EndDate")
    end_date_type: EndDateType = pydantic.Field(None, alias="EndDateType")
    instance_match_criteria: InstanceMatchCriteria = pydantic.Field(None, alias="InstanceMatchCriteria")
    create_date: DateTime = pydantic.Field(None, alias="CreateDate")
    tags: TagList = pydantic.Field(None, alias="Tags")
    outpost_arn: OutpostArn = pydantic.Field(None, alias="OutpostArn")
    capacity_reservation_fleet_id: String = pydantic.Field(None, alias="CapacityReservationFleetId")
    placement_group_arn: PlacementGroupArn = pydantic.Field(None, alias="PlacementGroupArn")
    capacity_allocations: CapacityAllocations = pydantic.Field(None, alias="CapacityAllocations")

class CapacityReservationFleet(_EC2ModelBase):
    capacity_reservation_fleet_id: CapacityReservationFleetId = pydantic.Field(None, alias="CapacityReservationFleetId")
    capacity_reservation_fleet_arn: String = pydantic.Field(None, alias="CapacityReservationFleetArn")
    state: CapacityReservationFleetState = pydantic.Field(None, alias="State")
    total_target_capacity: Integer = pydantic.Field(None, alias="TotalTargetCapacity")
    total_fulfilled_capacity: Double = pydantic.Field(None, alias="TotalFulfilledCapacity")
    tenancy: FleetCapacityReservationTenancy = pydantic.Field(None, alias="Tenancy")
    end_date: MillisecondDateTime = pydantic.Field(None, alias="EndDate")
    create_time: MillisecondDateTime = pydantic.Field(None, alias="CreateTime")
    instance_match_criteria: FleetInstanceMatchCriteria = pydantic.Field(None, alias="InstanceMatchCriteria")
    allocation_strategy: String = pydantic.Field(None, alias="AllocationStrategy")
    instance_type_specifications: FleetCapacityReservationSet = pydantic.Field(None, alias="InstanceTypeSpecifications")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CapacityReservationFleetCancellationState(_EC2ModelBase):
    current_fleet_state: CapacityReservationFleetState = pydantic.Field(None, alias="CurrentFleetState")
    previous_fleet_state: CapacityReservationFleetState = pydantic.Field(None, alias="PreviousFleetState")
    capacity_reservation_fleet_id: CapacityReservationFleetId = pydantic.Field(None, alias="CapacityReservationFleetId")

class CapacityReservationGroup(_EC2ModelBase):
    group_arn: String = pydantic.Field(None, alias="GroupArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")

class CapacityReservationOptions(_EC2ModelBase):
    usage_strategy: FleetCapacityReservationUsageStrategy = pydantic.Field(None, alias="UsageStrategy")

class CapacityReservationOptionsRequest(_EC2ModelBase):
    usage_strategy: FleetCapacityReservationUsageStrategy = pydantic.Field(None, alias="UsageStrategy")

class CapacityReservationSpecification(_EC2ModelBase):
    capacity_reservation_preference: CapacityReservationPreference = pydantic.Field(None, alias="CapacityReservationPreference")
    capacity_reservation_target: 'CapacityReservationTarget' = pydantic.Field(None, alias="CapacityReservationTarget")

class CapacityReservationSpecificationResponse(_EC2ModelBase):
    capacity_reservation_preference: CapacityReservationPreference = pydantic.Field(None, alias="CapacityReservationPreference")
    capacity_reservation_target: 'CapacityReservationTargetResponse' = pydantic.Field(None, alias="CapacityReservationTarget")

class CapacityReservationTarget(_EC2ModelBase):
    capacity_reservation_id: CapacityReservationId = pydantic.Field(None, alias="CapacityReservationId")
    capacity_reservation_resource_group_arn: String = pydantic.Field(None, alias="CapacityReservationResourceGroupArn")

class CapacityReservationTargetResponse(_EC2ModelBase):
    capacity_reservation_id: String = pydantic.Field(None, alias="CapacityReservationId")
    capacity_reservation_resource_group_arn: String = pydantic.Field(None, alias="CapacityReservationResourceGroupArn")

class CarrierGateway(_EC2ModelBase):
    carrier_gateway_id: CarrierGatewayId = pydantic.Field(None, alias="CarrierGatewayId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    state: CarrierGatewayState = pydantic.Field(None, alias="State")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CertificateAuthentication(_EC2ModelBase):
    client_root_certificate_chain: String = pydantic.Field(None, alias="ClientRootCertificateChain")

class CertificateAuthenticationRequest(_EC2ModelBase):
    client_root_certificate_chain_arn: String = pydantic.Field(None, alias="ClientRootCertificateChainArn")

class CidrAuthorizationContext(_EC2ModelBase):
    message: String = pydantic.Field(None, alias="Message")
    signature: String = pydantic.Field(None, alias="Signature")

class CidrBlock(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")

class ClassicLinkDnsSupport(_EC2ModelBase):
    classic_link_dns_supported: Boolean = pydantic.Field(None, alias="ClassicLinkDnsSupported")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class ClassicLinkInstance(_EC2ModelBase):
    groups: GroupIdentifierList = pydantic.Field(None, alias="Groups")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class ClassicLoadBalancer(_EC2ModelBase):
    name: String = pydantic.Field(None, alias="Name")

class ClassicLoadBalancersConfig(_EC2ModelBase):
    classic_load_balancers: ClassicLoadBalancers = pydantic.Field(None, alias="ClassicLoadBalancers")

class ClientCertificateRevocationListStatus(_EC2ModelBase):
    code: ClientCertificateRevocationListStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ClientConnectOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    lambda_function_arn: String = pydantic.Field(None, alias="LambdaFunctionArn")

class ClientConnectResponseOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    lambda_function_arn: String = pydantic.Field(None, alias="LambdaFunctionArn")
    status: 'ClientVpnEndpointAttributeStatus' = pydantic.Field(None, alias="Status")

class ClientData(_EC2ModelBase):
    comment: String = pydantic.Field(None, alias="Comment")
    upload_end: DateTime = pydantic.Field(None, alias="UploadEnd")
    upload_size: Double = pydantic.Field(None, alias="UploadSize")
    upload_start: DateTime = pydantic.Field(None, alias="UploadStart")

class ClientLoginBannerOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    banner_text: String = pydantic.Field(None, alias="BannerText")

class ClientLoginBannerResponseOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    banner_text: String = pydantic.Field(None, alias="BannerText")

class ClientVpnAuthentication(_EC2ModelBase):
    type: ClientVpnAuthenticationType = pydantic.Field(None, alias="Type")
    active_directory: 'DirectoryServiceAuthentication' = pydantic.Field(None, alias="ActiveDirectory")
    mutual_authentication: 'CertificateAuthentication' = pydantic.Field(None, alias="MutualAuthentication")
    federated_authentication: 'FederatedAuthentication' = pydantic.Field(None, alias="FederatedAuthentication")

class ClientVpnAuthenticationRequest(_EC2ModelBase):
    type: ClientVpnAuthenticationType = pydantic.Field(None, alias="Type")
    active_directory: 'DirectoryServiceAuthenticationRequest' = pydantic.Field(None, alias="ActiveDirectory")
    mutual_authentication: 'CertificateAuthenticationRequest' = pydantic.Field(None, alias="MutualAuthentication")
    federated_authentication: 'FederatedAuthenticationRequest' = pydantic.Field(None, alias="FederatedAuthentication")

class ClientVpnAuthorizationRuleStatus(_EC2ModelBase):
    code: ClientVpnAuthorizationRuleStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ClientVpnConnection(_EC2ModelBase):
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    timestamp: String = pydantic.Field(None, alias="Timestamp")
    connection_id: String = pydantic.Field(None, alias="ConnectionId")
    username: String = pydantic.Field(None, alias="Username")
    connection_established_time: String = pydantic.Field(None, alias="ConnectionEstablishedTime")
    ingress_bytes: String = pydantic.Field(None, alias="IngressBytes")
    egress_bytes: String = pydantic.Field(None, alias="EgressBytes")
    ingress_packets: String = pydantic.Field(None, alias="IngressPackets")
    egress_packets: String = pydantic.Field(None, alias="EgressPackets")
    client_ip: String = pydantic.Field(None, alias="ClientIp")
    common_name: String = pydantic.Field(None, alias="CommonName")
    status: 'ClientVpnConnectionStatus' = pydantic.Field(None, alias="Status")
    connection_end_time: String = pydantic.Field(None, alias="ConnectionEndTime")
    posture_compliance_statuses: ValueStringList = pydantic.Field(None, alias="PostureComplianceStatuses")

class ClientVpnConnectionStatus(_EC2ModelBase):
    code: ClientVpnConnectionStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ClientVpnEndpoint(_EC2ModelBase):
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    description: String = pydantic.Field(None, alias="Description")
    status: 'ClientVpnEndpointStatus' = pydantic.Field(None, alias="Status")
    creation_time: String = pydantic.Field(None, alias="CreationTime")
    deletion_time: String = pydantic.Field(None, alias="DeletionTime")
    dns_name: String = pydantic.Field(None, alias="DnsName")
    client_cidr_block: String = pydantic.Field(None, alias="ClientCidrBlock")
    dns_servers: ValueStringList = pydantic.Field(None, alias="DnsServers")
    split_tunnel: Boolean = pydantic.Field(None, alias="SplitTunnel")
    vpn_protocol: VpnProtocol = pydantic.Field(None, alias="VpnProtocol")
    transport_protocol: TransportProtocol = pydantic.Field(None, alias="TransportProtocol")
    vpn_port: Integer = pydantic.Field(None, alias="VpnPort")
    associated_target_networks: AssociatedTargetNetworkSet = pydantic.Field(None, alias="AssociatedTargetNetworks")
    server_certificate_arn: String = pydantic.Field(None, alias="ServerCertificateArn")
    authentication_options: ClientVpnAuthenticationList = pydantic.Field(None, alias="AuthenticationOptions")
    connection_log_options: 'ConnectionLogResponseOptions' = pydantic.Field(None, alias="ConnectionLogOptions")
    tags: TagList = pydantic.Field(None, alias="Tags")
    security_group_ids: ClientVpnSecurityGroupIdSet = pydantic.Field(None, alias="SecurityGroupIds")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    self_service_portal_url: String = pydantic.Field(None, alias="SelfServicePortalUrl")
    client_connect_options: 'ClientConnectResponseOptions' = pydantic.Field(None, alias="ClientConnectOptions")
    session_timeout_hours: Integer = pydantic.Field(None, alias="SessionTimeoutHours")
    client_login_banner_options: 'ClientLoginBannerResponseOptions' = pydantic.Field(None, alias="ClientLoginBannerOptions")

class ClientVpnEndpointAttributeStatus(_EC2ModelBase):
    code: ClientVpnEndpointAttributeStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ClientVpnEndpointStatus(_EC2ModelBase):
    code: ClientVpnEndpointStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ClientVpnRoute(_EC2ModelBase):
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    destination_cidr: String = pydantic.Field(None, alias="DestinationCidr")
    target_subnet: String = pydantic.Field(None, alias="TargetSubnet")
    type: String = pydantic.Field(None, alias="Type")
    origin: String = pydantic.Field(None, alias="Origin")
    status: 'ClientVpnRouteStatus' = pydantic.Field(None, alias="Status")
    description: String = pydantic.Field(None, alias="Description")

class ClientVpnRouteStatus(_EC2ModelBase):
    code: ClientVpnRouteStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class CloudWatchLogOptions(_EC2ModelBase):
    log_enabled: Boolean = pydantic.Field(None, alias="LogEnabled")
    log_group_arn: String = pydantic.Field(None, alias="LogGroupArn")
    log_output_format: String = pydantic.Field(None, alias="LogOutputFormat")

class CloudWatchLogOptionsSpecification(_EC2ModelBase):
    log_enabled: Boolean = pydantic.Field(None, alias="LogEnabled")
    log_group_arn: CloudWatchLogGroupArn = pydantic.Field(None, alias="LogGroupArn")
    log_output_format: String = pydantic.Field(None, alias="LogOutputFormat")

class CoipAddressUsage(_EC2ModelBase):
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    aws_account_id: String = pydantic.Field(None, alias="AwsAccountId")
    aws_service: String = pydantic.Field(None, alias="AwsService")
    co_ip: String = pydantic.Field(None, alias="CoIp")

class CoipCidr(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    coip_pool_id: Ipv4PoolCoipId = pydantic.Field(None, alias="CoipPoolId")
    local_gateway_route_table_id: String = pydantic.Field(None, alias="LocalGatewayRouteTableId")

class CoipPool(_EC2ModelBase):
    pool_id: Ipv4PoolCoipId = pydantic.Field(None, alias="PoolId")
    pool_cidrs: ValueStringList = pydantic.Field(None, alias="PoolCidrs")
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    pool_arn: ResourceArn = pydantic.Field(None, alias="PoolArn")

class ConfirmProductInstanceRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    product_code: String = pydantic.Field(None, alias="ProductCode")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ConfirmProductInstanceResult(_EC2ModelBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ConnectionLogOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    cloudwatch_log_group: String = pydantic.Field(None, alias="CloudwatchLogGroup")
    cloudwatch_log_stream: String = pydantic.Field(None, alias="CloudwatchLogStream")

class ConnectionLogResponseOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    cloudwatch_log_group: String = pydantic.Field(None, alias="CloudwatchLogGroup")
    cloudwatch_log_stream: String = pydantic.Field(None, alias="CloudwatchLogStream")

class ConnectionNotification(_EC2ModelBase):
    connection_notification_id: String = pydantic.Field(None, alias="ConnectionNotificationId")
    service_id: String = pydantic.Field(None, alias="ServiceId")
    vpc_endpoint_id: String = pydantic.Field(None, alias="VpcEndpointId")
    connection_notification_type: ConnectionNotificationType = pydantic.Field(None, alias="ConnectionNotificationType")
    connection_notification_arn: String = pydantic.Field(None, alias="ConnectionNotificationArn")
    connection_events: ValueStringList = pydantic.Field(None, alias="ConnectionEvents")
    connection_notification_state: ConnectionNotificationState = pydantic.Field(None, alias="ConnectionNotificationState")

class ConversionTask(_EC2ModelBase):
    conversion_task_id: String = pydantic.Field(None, alias="ConversionTaskId")
    expiration_time: String = pydantic.Field(None, alias="ExpirationTime")
    import_instance: 'ImportInstanceTaskDetails' = pydantic.Field(None, alias="ImportInstance")
    import_volume: 'ImportVolumeTaskDetails' = pydantic.Field(None, alias="ImportVolume")
    state: ConversionTaskState = pydantic.Field(None, alias="State")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CopyFpgaImageRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    source_fpga_image_id: String = pydantic.Field(None, alias="SourceFpgaImageId")
    description: String = pydantic.Field(None, alias="Description")
    name: String = pydantic.Field(None, alias="Name")
    source_region: String = pydantic.Field(None, alias="SourceRegion")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CopyFpgaImageResult(_EC2ModelBase):
    fpga_image_id: String = pydantic.Field(None, alias="FpgaImageId")

class CopyImageRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    description: String = pydantic.Field(None, alias="Description")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    name: String = pydantic.Field(None, alias="Name")
    source_image_id: String = pydantic.Field(None, alias="SourceImageId")
    source_region: String = pydantic.Field(None, alias="SourceRegion")
    destination_outpost_arn: String = pydantic.Field(None, alias="DestinationOutpostArn")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    copy_image_tags: Boolean = pydantic.Field(None, alias="CopyImageTags")

class CopyImageResult(_EC2ModelBase):
    image_id: String = pydantic.Field(None, alias="ImageId")

class CopySnapshotRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    destination_outpost_arn: String = pydantic.Field(None, alias="DestinationOutpostArn")
    destination_region: String = pydantic.Field(None, alias="DestinationRegion")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    presigned_url: CopySnapshotRequestPSU = pydantic.Field(None, alias="PresignedUrl")
    source_region: String = pydantic.Field(None, alias="SourceRegion")
    source_snapshot_id: String = pydantic.Field(None, alias="SourceSnapshotId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CopySnapshotResult(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CpuOptions(_EC2ModelBase):
    core_count: Integer = pydantic.Field(None, alias="CoreCount")
    threads_per_core: Integer = pydantic.Field(None, alias="ThreadsPerCore")
    amd_sev_snp: AmdSevSnpSpecification = pydantic.Field(None, alias="AmdSevSnp")

class CpuOptionsRequest(_EC2ModelBase):
    core_count: Integer = pydantic.Field(None, alias="CoreCount")
    threads_per_core: Integer = pydantic.Field(None, alias="ThreadsPerCore")
    amd_sev_snp: AmdSevSnpSpecification = pydantic.Field(None, alias="AmdSevSnp")

class CreateCapacityReservationFleetRequest(_EC2ModelBase):
    allocation_strategy: String = pydantic.Field(None, alias="AllocationStrategy")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    instance_type_specifications: ReservationFleetInstanceSpecificationList = pydantic.Field(None, alias="InstanceTypeSpecifications")
    tenancy: FleetCapacityReservationTenancy = pydantic.Field(None, alias="Tenancy")
    total_target_capacity: Integer = pydantic.Field(None, alias="TotalTargetCapacity")
    end_date: MillisecondDateTime = pydantic.Field(None, alias="EndDate")
    instance_match_criteria: FleetInstanceMatchCriteria = pydantic.Field(None, alias="InstanceMatchCriteria")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateCapacityReservationFleetResult(_EC2ModelBase):
    capacity_reservation_fleet_id: CapacityReservationFleetId = pydantic.Field(None, alias="CapacityReservationFleetId")
    state: CapacityReservationFleetState = pydantic.Field(None, alias="State")
    total_target_capacity: Integer = pydantic.Field(None, alias="TotalTargetCapacity")
    total_fulfilled_capacity: Double = pydantic.Field(None, alias="TotalFulfilledCapacity")
    instance_match_criteria: FleetInstanceMatchCriteria = pydantic.Field(None, alias="InstanceMatchCriteria")
    allocation_strategy: String = pydantic.Field(None, alias="AllocationStrategy")
    create_time: MillisecondDateTime = pydantic.Field(None, alias="CreateTime")
    end_date: MillisecondDateTime = pydantic.Field(None, alias="EndDate")
    tenancy: FleetCapacityReservationTenancy = pydantic.Field(None, alias="Tenancy")
    fleet_capacity_reservations: FleetCapacityReservationSet = pydantic.Field(None, alias="FleetCapacityReservations")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateCapacityReservationRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    instance_platform: CapacityReservationInstancePlatform = pydantic.Field(None, alias="InstancePlatform")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    tenancy: CapacityReservationTenancy = pydantic.Field(None, alias="Tenancy")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    ephemeral_storage: Boolean = pydantic.Field(None, alias="EphemeralStorage")
    end_date: DateTime = pydantic.Field(None, alias="EndDate")
    end_date_type: EndDateType = pydantic.Field(None, alias="EndDateType")
    instance_match_criteria: InstanceMatchCriteria = pydantic.Field(None, alias="InstanceMatchCriteria")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    outpost_arn: OutpostArn = pydantic.Field(None, alias="OutpostArn")
    placement_group_arn: PlacementGroupArn = pydantic.Field(None, alias="PlacementGroupArn")

class CreateCapacityReservationResult(_EC2ModelBase):
    capacity_reservation: 'CapacityReservation' = pydantic.Field(None, alias="CapacityReservation")

class CreateCarrierGatewayRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateCarrierGatewayResult(_EC2ModelBase):
    carrier_gateway: 'CarrierGateway' = pydantic.Field(None, alias="CarrierGateway")

class CreateClientVpnEndpointRequest(_EC2ModelBase):
    client_cidr_block: String = pydantic.Field(None, alias="ClientCidrBlock")
    server_certificate_arn: String = pydantic.Field(None, alias="ServerCertificateArn")
    authentication_options: ClientVpnAuthenticationRequestList = pydantic.Field(None, alias="AuthenticationOptions")
    connection_log_options: 'ConnectionLogOptions' = pydantic.Field(None, alias="ConnectionLogOptions")
    dns_servers: ValueStringList = pydantic.Field(None, alias="DnsServers")
    transport_protocol: TransportProtocol = pydantic.Field(None, alias="TransportProtocol")
    vpn_port: Integer = pydantic.Field(None, alias="VpnPort")
    description: String = pydantic.Field(None, alias="Description")
    split_tunnel: Boolean = pydantic.Field(None, alias="SplitTunnel")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    security_group_ids: ClientVpnSecurityGroupIdSet = pydantic.Field(None, alias="SecurityGroupIds")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    self_service_portal: SelfServicePortal = pydantic.Field(None, alias="SelfServicePortal")
    client_connect_options: 'ClientConnectOptions' = pydantic.Field(None, alias="ClientConnectOptions")
    session_timeout_hours: Integer = pydantic.Field(None, alias="SessionTimeoutHours")
    client_login_banner_options: 'ClientLoginBannerOptions' = pydantic.Field(None, alias="ClientLoginBannerOptions")

class CreateClientVpnEndpointResult(_EC2ModelBase):
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    status: 'ClientVpnEndpointStatus' = pydantic.Field(None, alias="Status")
    dns_name: String = pydantic.Field(None, alias="DnsName")

class CreateClientVpnRouteRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    target_vpc_subnet_id: SubnetId = pydantic.Field(None, alias="TargetVpcSubnetId")
    description: String = pydantic.Field(None, alias="Description")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateClientVpnRouteResult(_EC2ModelBase):
    status: 'ClientVpnRouteStatus' = pydantic.Field(None, alias="Status")

class CreateCoipCidrRequest(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    coip_pool_id: Ipv4PoolCoipId = pydantic.Field(None, alias="CoipPoolId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateCoipCidrResult(_EC2ModelBase):
    coip_cidr: 'CoipCidr' = pydantic.Field(None, alias="CoipCidr")

class CreateCoipPoolRequest(_EC2ModelBase):
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateCoipPoolResult(_EC2ModelBase):
    coip_pool: 'CoipPool' = pydantic.Field(None, alias="CoipPool")

class CreateCustomerGatewayRequest(_EC2ModelBase):
    bgp_asn: Integer = pydantic.Field(None, alias="BgpAsn")
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    certificate_arn: String = pydantic.Field(None, alias="CertificateArn")
    type: GatewayType = pydantic.Field(None, alias="Type")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    device_name: String = pydantic.Field(None, alias="DeviceName")
    ip_address: String = pydantic.Field(None, alias="IpAddress")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateCustomerGatewayResult(_EC2ModelBase):
    customer_gateway: 'CustomerGateway' = pydantic.Field(None, alias="CustomerGateway")

class CreateDefaultSubnetRequest(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipv_6_native: Boolean = pydantic.Field(None, alias="Ipv6Native")

class CreateDefaultSubnetResult(_EC2ModelBase):
    subnet: 'Subnet' = pydantic.Field(None, alias="Subnet")

class CreateDefaultVpcRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateDefaultVpcResult(_EC2ModelBase):
    vpc: 'Vpc' = pydantic.Field(None, alias="Vpc")

class CreateDhcpOptionsRequest(_EC2ModelBase):
    dhcp_configurations: NewDhcpConfigurationList = pydantic.Field(None, alias="DhcpConfigurations")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateDhcpOptionsResult(_EC2ModelBase):
    dhcp_options: 'DhcpOptions' = pydantic.Field(None, alias="DhcpOptions")

class CreateEgressOnlyInternetGatewayRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateEgressOnlyInternetGatewayResult(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    egress_only_internet_gateway: 'EgressOnlyInternetGateway' = pydantic.Field(None, alias="EgressOnlyInternetGateway")

class CreateFleetError(_EC2ModelBase):
    launch_template_and_overrides: 'LaunchTemplateAndOverridesResponse' = pydantic.Field(None, alias="LaunchTemplateAndOverrides")
    lifecycle: InstanceLifecycle = pydantic.Field(None, alias="Lifecycle")
    error_code: String = pydantic.Field(None, alias="ErrorCode")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")

class CreateFleetInstance(_EC2ModelBase):
    launch_template_and_overrides: 'LaunchTemplateAndOverridesResponse' = pydantic.Field(None, alias="LaunchTemplateAndOverrides")
    lifecycle: InstanceLifecycle = pydantic.Field(None, alias="Lifecycle")
    instance_ids: InstanceIdsSet = pydantic.Field(None, alias="InstanceIds")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    platform: PlatformValues = pydantic.Field(None, alias="Platform")

class CreateFleetRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    spot_options: 'SpotOptionsRequest' = pydantic.Field(None, alias="SpotOptions")
    on_demand_options: 'OnDemandOptionsRequest' = pydantic.Field(None, alias="OnDemandOptions")
    excess_capacity_termination_policy: FleetExcessCapacityTerminationPolicy = pydantic.Field(None, alias="ExcessCapacityTerminationPolicy")
    launch_template_configs: FleetLaunchTemplateConfigListRequest = pydantic.Field(None, alias="LaunchTemplateConfigs")
    target_capacity_specification: 'TargetCapacitySpecificationRequest' = pydantic.Field(None, alias="TargetCapacitySpecification")
    terminate_instances_with_expiration: Boolean = pydantic.Field(None, alias="TerminateInstancesWithExpiration")
    type: FleetType = pydantic.Field(None, alias="Type")
    valid_from: DateTime = pydantic.Field(None, alias="ValidFrom")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    replace_unhealthy_instances: Boolean = pydantic.Field(None, alias="ReplaceUnhealthyInstances")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    context: String = pydantic.Field(None, alias="Context")

class CreateFleetResult(_EC2ModelBase):
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")
    errors: CreateFleetErrorsSet = pydantic.Field(None, alias="Errors")
    instances: CreateFleetInstancesSet = pydantic.Field(None, alias="Instances")

class CreateFlowLogsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    deliver_logs_permission_arn: String = pydantic.Field(None, alias="DeliverLogsPermissionArn")
    deliver_cross_account_role: String = pydantic.Field(None, alias="DeliverCrossAccountRole")
    log_group_name: String = pydantic.Field(None, alias="LogGroupName")
    resource_ids: FlowLogResourceIds = pydantic.Field(None, alias="ResourceIds")
    resource_type: FlowLogsResourceType = pydantic.Field(None, alias="ResourceType")
    traffic_type: TrafficType = pydantic.Field(None, alias="TrafficType")
    log_destination_type: LogDestinationType = pydantic.Field(None, alias="LogDestinationType")
    log_destination: String = pydantic.Field(None, alias="LogDestination")
    log_format: String = pydantic.Field(None, alias="LogFormat")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    max_aggregation_interval: Integer = pydantic.Field(None, alias="MaxAggregationInterval")
    destination_options: 'DestinationOptionsRequest' = pydantic.Field(None, alias="DestinationOptions")

class CreateFlowLogsResult(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    flow_log_ids: ValueStringList = pydantic.Field(None, alias="FlowLogIds")
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class CreateFpgaImageRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    input_storage_location: 'StorageLocation' = pydantic.Field(None, alias="InputStorageLocation")
    logs_storage_location: 'StorageLocation' = pydantic.Field(None, alias="LogsStorageLocation")
    description: String = pydantic.Field(None, alias="Description")
    name: String = pydantic.Field(None, alias="Name")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateFpgaImageResult(_EC2ModelBase):
    fpga_image_id: String = pydantic.Field(None, alias="FpgaImageId")
    fpga_image_global_id: String = pydantic.Field(None, alias="FpgaImageGlobalId")

class CreateImageRequest(_EC2ModelBase):
    block_device_mappings: BlockDeviceMappingRequestList = pydantic.Field(None, alias="BlockDeviceMappings")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    name: String = pydantic.Field(None, alias="Name")
    no_reboot: Boolean = pydantic.Field(None, alias="NoReboot")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateImageResult(_EC2ModelBase):
    image_id: String = pydantic.Field(None, alias="ImageId")

class CreateInstanceEventWindowRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    name: String = pydantic.Field(None, alias="Name")
    time_ranges: InstanceEventWindowTimeRangeRequestSet = pydantic.Field(None, alias="TimeRanges")
    cron_expression: InstanceEventWindowCronExpression = pydantic.Field(None, alias="CronExpression")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateInstanceEventWindowResult(_EC2ModelBase):
    instance_event_window: 'InstanceEventWindow' = pydantic.Field(None, alias="InstanceEventWindow")

class CreateInstanceExportTaskRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    export_to_s_3_task: 'ExportToS3TaskSpecification' = pydantic.Field(None, alias="ExportToS3Task")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    target_environment: ExportEnvironment = pydantic.Field(None, alias="TargetEnvironment")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateInstanceExportTaskResult(_EC2ModelBase):
    export_task: 'ExportTask' = pydantic.Field(None, alias="ExportTask")

class CreateInternetGatewayRequest(_EC2ModelBase):
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateInternetGatewayResult(_EC2ModelBase):
    internet_gateway: 'InternetGateway' = pydantic.Field(None, alias="InternetGateway")

class CreateIpamPoolRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")
    locale: String = pydantic.Field(None, alias="Locale")
    source_ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="SourceIpamPoolId")
    description: String = pydantic.Field(None, alias="Description")
    address_family: AddressFamily = pydantic.Field(None, alias="AddressFamily")
    auto_import: Boolean = pydantic.Field(None, alias="AutoImport")
    publicly_advertisable: Boolean = pydantic.Field(None, alias="PubliclyAdvertisable")
    allocation_min_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationMinNetmaskLength")
    allocation_max_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationMaxNetmaskLength")
    allocation_default_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationDefaultNetmaskLength")
    allocation_resource_tags: RequestIpamResourceTagList = pydantic.Field(None, alias="AllocationResourceTags")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    aws_service: IpamPoolAwsService = pydantic.Field(None, alias="AwsService")
    public_ip_source: IpamPoolPublicIpSource = pydantic.Field(None, alias="PublicIpSource")

class CreateIpamPoolResult(_EC2ModelBase):
    ipam_pool: 'IpamPool' = pydantic.Field(None, alias="IpamPool")

class CreateIpamRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    description: String = pydantic.Field(None, alias="Description")
    operating_regions: AddIpamOperatingRegionSet = pydantic.Field(None, alias="OperatingRegions")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateIpamResourceDiscoveryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    description: String = pydantic.Field(None, alias="Description")
    operating_regions: AddIpamOperatingRegionSet = pydantic.Field(None, alias="OperatingRegions")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateIpamResourceDiscoveryResult(_EC2ModelBase):
    ipam_resource_discovery: 'IpamResourceDiscovery' = pydantic.Field(None, alias="IpamResourceDiscovery")

class CreateIpamResult(_EC2ModelBase):
    ipam: 'Ipam' = pydantic.Field(None, alias="Ipam")

class CreateIpamScopeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    description: String = pydantic.Field(None, alias="Description")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateIpamScopeResult(_EC2ModelBase):
    ipam_scope: 'IpamScope' = pydantic.Field(None, alias="IpamScope")

class CreateKeyPairRequest(_EC2ModelBase):
    key_name: String = pydantic.Field(None, alias="KeyName")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    key_type: KeyType = pydantic.Field(None, alias="KeyType")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    key_format: KeyFormat = pydantic.Field(None, alias="KeyFormat")

class CreateLaunchTemplateRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    version_description: VersionDescription = pydantic.Field(None, alias="VersionDescription")
    launch_template_data: 'RequestLaunchTemplateData' = pydantic.Field(None, alias="LaunchTemplateData")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateLaunchTemplateResult(_EC2ModelBase):
    launch_template: 'LaunchTemplate' = pydantic.Field(None, alias="LaunchTemplate")
    warning: 'ValidationWarning' = pydantic.Field(None, alias="Warning")

class CreateLaunchTemplateVersionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    source_version: String = pydantic.Field(None, alias="SourceVersion")
    version_description: VersionDescription = pydantic.Field(None, alias="VersionDescription")
    launch_template_data: 'RequestLaunchTemplateData' = pydantic.Field(None, alias="LaunchTemplateData")
    resolve_alias: Boolean = pydantic.Field(None, alias="ResolveAlias")

class CreateLaunchTemplateVersionResult(_EC2ModelBase):
    launch_template_version: 'LaunchTemplateVersion' = pydantic.Field(None, alias="LaunchTemplateVersion")
    warning: 'ValidationWarning' = pydantic.Field(None, alias="Warning")

class CreateLocalGatewayRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_virtual_interface_group_id: LocalGatewayVirtualInterfaceGroupId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")

class CreateLocalGatewayRouteResult(_EC2ModelBase):
    route: 'LocalGatewayRoute' = pydantic.Field(None, alias="Route")

class CreateLocalGatewayRouteTableRequest(_EC2ModelBase):
    local_gateway_id: LocalGatewayId = pydantic.Field(None, alias="LocalGatewayId")
    mode: LocalGatewayRouteTableMode = pydantic.Field(None, alias="Mode")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateLocalGatewayRouteTableResult(_EC2ModelBase):
    local_gateway_route_table: 'LocalGatewayRouteTable' = pydantic.Field(None, alias="LocalGatewayRouteTable")

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest(_EC2ModelBase):
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_virtual_interface_group_id: LocalGatewayVirtualInterfaceGroupId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(_EC2ModelBase):
    local_gateway_route_table_virtual_interface_group_association: 'LocalGatewayRouteTableVirtualInterfaceGroupAssociation' = pydantic.Field(None, alias="LocalGatewayRouteTableVirtualInterfaceGroupAssociation")

class CreateLocalGatewayRouteTableVpcAssociationRequest(_EC2ModelBase):
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateLocalGatewayRouteTableVpcAssociationResult(_EC2ModelBase):
    local_gateway_route_table_vpc_association: 'LocalGatewayRouteTableVpcAssociation' = pydantic.Field(None, alias="LocalGatewayRouteTableVpcAssociation")

class CreateManagedPrefixListRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix_list_name: String = pydantic.Field(None, alias="PrefixListName")
    entries: AddPrefixListEntries = pydantic.Field(None, alias="Entries")
    max_entries: Integer = pydantic.Field(None, alias="MaxEntries")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    address_family: String = pydantic.Field(None, alias="AddressFamily")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateManagedPrefixListResult(_EC2ModelBase):
    prefix_list: 'ManagedPrefixList' = pydantic.Field(None, alias="PrefixList")

class CreateNatGatewayRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    connectivity_type: ConnectivityType = pydantic.Field(None, alias="ConnectivityType")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    secondary_allocation_ids: AllocationIdList = pydantic.Field(None, alias="SecondaryAllocationIds")
    secondary_private_ip_addresses: IpList = pydantic.Field(None, alias="SecondaryPrivateIpAddresses")
    secondary_private_ip_address_count: PrivateIpAddressCount = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")

class CreateNatGatewayResult(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    nat_gateway: 'NatGateway' = pydantic.Field(None, alias="NatGateway")

class CreateNetworkAclEntryRequest(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    egress: Boolean = pydantic.Field(None, alias="Egress")
    icmp_type_code: 'IcmpTypeCode' = pydantic.Field(None, alias="IcmpTypeCode")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    network_acl_id: NetworkAclId = pydantic.Field(None, alias="NetworkAclId")
    port_range: 'PortRange' = pydantic.Field(None, alias="PortRange")
    protocol: String = pydantic.Field(None, alias="Protocol")
    rule_action: RuleAction = pydantic.Field(None, alias="RuleAction")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")

class CreateNetworkAclRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateNetworkAclResult(_EC2ModelBase):
    network_acl: 'NetworkAcl' = pydantic.Field(None, alias="NetworkAcl")

class CreateNetworkInsightsAccessScopeRequest(_EC2ModelBase):
    match_paths: AccessScopePathListRequest = pydantic.Field(None, alias="MatchPaths")
    exclude_paths: AccessScopePathListRequest = pydantic.Field(None, alias="ExcludePaths")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateNetworkInsightsAccessScopeResult(_EC2ModelBase):
    network_insights_access_scope: 'NetworkInsightsAccessScope' = pydantic.Field(None, alias="NetworkInsightsAccessScope")
    network_insights_access_scope_content: 'NetworkInsightsAccessScopeContent' = pydantic.Field(None, alias="NetworkInsightsAccessScopeContent")

class CreateNetworkInsightsPathRequest(_EC2ModelBase):
    source_ip: IpAddress = pydantic.Field(None, alias="SourceIp")
    destination_ip: IpAddress = pydantic.Field(None, alias="DestinationIp")
    source: NetworkInsightsResourceId = pydantic.Field(None, alias="Source")
    destination: NetworkInsightsResourceId = pydantic.Field(None, alias="Destination")
    protocol: Protocol = pydantic.Field(None, alias="Protocol")
    destination_port: Port = pydantic.Field(None, alias="DestinationPort")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    filter_at_source: 'PathRequestFilter' = pydantic.Field(None, alias="FilterAtSource")
    filter_at_destination: 'PathRequestFilter' = pydantic.Field(None, alias="FilterAtDestination")

class CreateNetworkInsightsPathResult(_EC2ModelBase):
    network_insights_path: 'NetworkInsightsPath' = pydantic.Field(None, alias="NetworkInsightsPath")

class CreateNetworkInterfacePermissionRequest(_EC2ModelBase):
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    aws_account_id: String = pydantic.Field(None, alias="AwsAccountId")
    aws_service: String = pydantic.Field(None, alias="AwsService")
    permission: InterfacePermissionType = pydantic.Field(None, alias="Permission")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateNetworkInterfacePermissionResult(_EC2ModelBase):
    interface_permission: 'NetworkInterfacePermission' = pydantic.Field(None, alias="InterfacePermission")

class CreateNetworkInterfaceRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    groups: SecurityGroupIdStringList = pydantic.Field(None, alias="Groups")
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: InstanceIpv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_addresses: PrivateIpAddressSpecificationList = pydantic.Field(None, alias="PrivateIpAddresses")
    secondary_private_ip_address_count: Integer = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")
    ipv_4_prefixes: Ipv4PrefixList = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_4_prefix_count: Integer = pydantic.Field(None, alias="Ipv4PrefixCount")
    ipv_6_prefixes: Ipv6PrefixList = pydantic.Field(None, alias="Ipv6Prefixes")
    ipv_6_prefix_count: Integer = pydantic.Field(None, alias="Ipv6PrefixCount")
    interface_type: NetworkInterfaceCreationType = pydantic.Field(None, alias="InterfaceType")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateNetworkInterfaceResult(_EC2ModelBase):
    network_interface: 'NetworkInterface' = pydantic.Field(None, alias="NetworkInterface")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreatePlacementGroupRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_name: String = pydantic.Field(None, alias="GroupName")
    strategy: PlacementStrategy = pydantic.Field(None, alias="Strategy")
    partition_count: Integer = pydantic.Field(None, alias="PartitionCount")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    spread_level: SpreadLevel = pydantic.Field(None, alias="SpreadLevel")

class CreatePlacementGroupResult(_EC2ModelBase):
    placement_group: 'PlacementGroup' = pydantic.Field(None, alias="PlacementGroup")

class CreatePublicIpv4PoolRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreatePublicIpv4PoolResult(_EC2ModelBase):
    pool_id: Ipv4PoolEc2Id = pydantic.Field(None, alias="PoolId")

class CreateReplaceRootVolumeTaskRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    delete_replaced_root_volume: Boolean = pydantic.Field(None, alias="DeleteReplacedRootVolume")

class CreateReplaceRootVolumeTaskResult(_EC2ModelBase):
    replace_root_volume_task: 'ReplaceRootVolumeTask' = pydantic.Field(None, alias="ReplaceRootVolumeTask")

class CreateReservedInstancesListingRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    price_schedules: PriceScheduleSpecificationList = pydantic.Field(None, alias="PriceSchedules")
    reserved_instances_id: ReservationId = pydantic.Field(None, alias="ReservedInstancesId")

class CreateReservedInstancesListingResult(_EC2ModelBase):
    reserved_instances_listings: ReservedInstancesListingList = pydantic.Field(None, alias="ReservedInstancesListings")

class CreateRestoreImageTaskRequest(_EC2ModelBase):
    bucket: String = pydantic.Field(None, alias="Bucket")
    object_key: String = pydantic.Field(None, alias="ObjectKey")
    name: String = pydantic.Field(None, alias="Name")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateRestoreImageTaskResult(_EC2ModelBase):
    image_id: String = pydantic.Field(None, alias="ImageId")

class CreateRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    destination_ipv_6_cidr_block: String = pydantic.Field(None, alias="DestinationIpv6CidrBlock")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_endpoint_id: VpcEndpointId = pydantic.Field(None, alias="VpcEndpointId")
    egress_only_internet_gateway_id: EgressOnlyInternetGatewayId = pydantic.Field(None, alias="EgressOnlyInternetGatewayId")
    gateway_id: RouteGatewayId = pydantic.Field(None, alias="GatewayId")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    local_gateway_id: LocalGatewayId = pydantic.Field(None, alias="LocalGatewayId")
    carrier_gateway_id: CarrierGatewayId = pydantic.Field(None, alias="CarrierGatewayId")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")
    vpc_peering_connection_id: VpcPeeringConnectionId = pydantic.Field(None, alias="VpcPeeringConnectionId")
    core_network_arn: CoreNetworkArn = pydantic.Field(None, alias="CoreNetworkArn")

class CreateRouteResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class CreateRouteTableRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateRouteTableResult(_EC2ModelBase):
    route_table: 'RouteTable' = pydantic.Field(None, alias="RouteTable")

class CreateSecurityGroupRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    group_name: String = pydantic.Field(None, alias="GroupName")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateSecurityGroupResult(_EC2ModelBase):
    group_id: String = pydantic.Field(None, alias="GroupId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateSnapshotRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateSnapshotsRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    instance_specification: 'InstanceSpecification' = pydantic.Field(None, alias="InstanceSpecification")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    copy_tags_from_source: CopyTagsFromSource = pydantic.Field(None, alias="CopyTagsFromSource")

class CreateSnapshotsResult(_EC2ModelBase):
    snapshots: SnapshotSet = pydantic.Field(None, alias="Snapshots")

class CreateSpotDatafeedSubscriptionRequest(_EC2ModelBase):
    bucket: String = pydantic.Field(None, alias="Bucket")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix: String = pydantic.Field(None, alias="Prefix")

class CreateSpotDatafeedSubscriptionResult(_EC2ModelBase):
    spot_datafeed_subscription: 'SpotDatafeedSubscription' = pydantic.Field(None, alias="SpotDatafeedSubscription")

class CreateStoreImageTaskRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    bucket: String = pydantic.Field(None, alias="Bucket")
    s_3_object_tags: S3ObjectTagList = pydantic.Field(None, alias="S3ObjectTags")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateStoreImageTaskResult(_EC2ModelBase):
    object_key: String = pydantic.Field(None, alias="ObjectKey")

class CreateSubnetCidrReservationRequest(_EC2ModelBase):
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    cidr: String = pydantic.Field(None, alias="Cidr")
    reservation_type: SubnetCidrReservationType = pydantic.Field(None, alias="ReservationType")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateSubnetCidrReservationResult(_EC2ModelBase):
    subnet_cidr_reservation: 'SubnetCidrReservation' = pydantic.Field(None, alias="SubnetCidrReservation")

class CreateSubnetRequest(_EC2ModelBase):
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipv_6_native: Boolean = pydantic.Field(None, alias="Ipv6Native")

class CreateSubnetResult(_EC2ModelBase):
    subnet: 'Subnet' = pydantic.Field(None, alias="Subnet")

class CreateTagsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    resources: ResourceIdList = pydantic.Field(None, alias="Resources")
    tags: TagList = pydantic.Field(None, alias="Tags")

class CreateTrafficMirrorFilterRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTrafficMirrorFilterResult(_EC2ModelBase):
    traffic_mirror_filter: 'TrafficMirrorFilter' = pydantic.Field(None, alias="TrafficMirrorFilter")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTrafficMirrorFilterRuleRequest(_EC2ModelBase):
    traffic_mirror_filter_id: TrafficMirrorFilterId = pydantic.Field(None, alias="TrafficMirrorFilterId")
    traffic_direction: TrafficDirection = pydantic.Field(None, alias="TrafficDirection")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")
    rule_action: TrafficMirrorRuleAction = pydantic.Field(None, alias="RuleAction")
    destination_port_range: 'TrafficMirrorPortRangeRequest' = pydantic.Field(None, alias="DestinationPortRange")
    source_port_range: 'TrafficMirrorPortRangeRequest' = pydantic.Field(None, alias="SourcePortRange")
    protocol: Integer = pydantic.Field(None, alias="Protocol")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    source_cidr_block: String = pydantic.Field(None, alias="SourceCidrBlock")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTrafficMirrorFilterRuleResult(_EC2ModelBase):
    traffic_mirror_filter_rule: 'TrafficMirrorFilterRule' = pydantic.Field(None, alias="TrafficMirrorFilterRule")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTrafficMirrorSessionRequest(_EC2ModelBase):
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    traffic_mirror_target_id: TrafficMirrorTargetId = pydantic.Field(None, alias="TrafficMirrorTargetId")
    traffic_mirror_filter_id: TrafficMirrorFilterId = pydantic.Field(None, alias="TrafficMirrorFilterId")
    packet_length: Integer = pydantic.Field(None, alias="PacketLength")
    session_number: Integer = pydantic.Field(None, alias="SessionNumber")
    virtual_network_id: Integer = pydantic.Field(None, alias="VirtualNetworkId")
    description: String = pydantic.Field(None, alias="Description")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTrafficMirrorSessionResult(_EC2ModelBase):
    traffic_mirror_session: 'TrafficMirrorSession' = pydantic.Field(None, alias="TrafficMirrorSession")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTrafficMirrorTargetRequest(_EC2ModelBase):
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    network_load_balancer_arn: String = pydantic.Field(None, alias="NetworkLoadBalancerArn")
    description: String = pydantic.Field(None, alias="Description")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    gateway_load_balancer_endpoint_id: VpcEndpointId = pydantic.Field(None, alias="GatewayLoadBalancerEndpointId")

class CreateTrafficMirrorTargetResult(_EC2ModelBase):
    traffic_mirror_target: 'TrafficMirrorTarget' = pydantic.Field(None, alias="TrafficMirrorTarget")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateTransitGatewayConnectPeerRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    transit_gateway_address: String = pydantic.Field(None, alias="TransitGatewayAddress")
    peer_address: String = pydantic.Field(None, alias="PeerAddress")
    bgp_options: 'TransitGatewayConnectRequestBgpOptions' = pydantic.Field(None, alias="BgpOptions")
    inside_cidr_blocks: InsideCidrBlocksStringList = pydantic.Field(None, alias="InsideCidrBlocks")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayConnectPeerResult(_EC2ModelBase):
    transit_gateway_connect_peer: 'TransitGatewayConnectPeer' = pydantic.Field(None, alias="TransitGatewayConnectPeer")

class CreateTransitGatewayConnectRequest(_EC2ModelBase):
    transport_transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransportTransitGatewayAttachmentId")
    options: 'CreateTransitGatewayConnectRequestOptions' = pydantic.Field(None, alias="Options")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayConnectRequestOptions(_EC2ModelBase):
    protocol: ProtocolValue = pydantic.Field(None, alias="Protocol")

class CreateTransitGatewayConnectResult(_EC2ModelBase):
    transit_gateway_connect: 'TransitGatewayConnect' = pydantic.Field(None, alias="TransitGatewayConnect")

class CreateTransitGatewayMulticastDomainRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    options: 'CreateTransitGatewayMulticastDomainRequestOptions' = pydantic.Field(None, alias="Options")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayMulticastDomainRequestOptions(_EC2ModelBase):
    igmpv_2_support: Igmpv2SupportValue = pydantic.Field(None, alias="Igmpv2Support")
    static_sources_support: StaticSourcesSupportValue = pydantic.Field(None, alias="StaticSourcesSupport")
    auto_accept_shared_associations: AutoAcceptSharedAssociationsValue = pydantic.Field(None, alias="AutoAcceptSharedAssociations")

class CreateTransitGatewayMulticastDomainResult(_EC2ModelBase):
    transit_gateway_multicast_domain: 'TransitGatewayMulticastDomain' = pydantic.Field(None, alias="TransitGatewayMulticastDomain")

class CreateTransitGatewayPeeringAttachmentRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    peer_transit_gateway_id: TransitAssociationGatewayId = pydantic.Field(None, alias="PeerTransitGatewayId")
    peer_account_id: String = pydantic.Field(None, alias="PeerAccountId")
    peer_region: String = pydantic.Field(None, alias="PeerRegion")
    options: 'CreateTransitGatewayPeeringAttachmentRequestOptions' = pydantic.Field(None, alias="Options")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayPeeringAttachmentRequestOptions(_EC2ModelBase):
    dynamic_routing: DynamicRoutingValue = pydantic.Field(None, alias="DynamicRouting")

class CreateTransitGatewayPeeringAttachmentResult(_EC2ModelBase):
    transit_gateway_peering_attachment: 'TransitGatewayPeeringAttachment' = pydantic.Field(None, alias="TransitGatewayPeeringAttachment")

class CreateTransitGatewayPolicyTableRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayPolicyTableResult(_EC2ModelBase):
    transit_gateway_policy_table: 'TransitGatewayPolicyTable' = pydantic.Field(None, alias="TransitGatewayPolicyTable")

class CreateTransitGatewayPrefixListReferenceRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    blackhole: Boolean = pydantic.Field(None, alias="Blackhole")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayPrefixListReferenceResult(_EC2ModelBase):
    transit_gateway_prefix_list_reference: 'TransitGatewayPrefixListReference' = pydantic.Field(None, alias="TransitGatewayPrefixListReference")

class CreateTransitGatewayRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    options: 'TransitGatewayRequestOptions' = pydantic.Field(None, alias="Options")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayResult(_EC2ModelBase):
    transit_gateway: 'TransitGateway' = pydantic.Field(None, alias="TransitGateway")

class CreateTransitGatewayRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    blackhole: Boolean = pydantic.Field(None, alias="Blackhole")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayRouteResult(_EC2ModelBase):
    route: 'TransitGatewayRoute' = pydantic.Field(None, alias="Route")

class CreateTransitGatewayRouteTableAnnouncementRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    peering_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="PeeringAttachmentId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayRouteTableAnnouncementResult(_EC2ModelBase):
    transit_gateway_route_table_announcement: 'TransitGatewayRouteTableAnnouncement' = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncement")

class CreateTransitGatewayRouteTableRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayRouteTableResult(_EC2ModelBase):
    transit_gateway_route_table: 'TransitGatewayRouteTable' = pydantic.Field(None, alias="TransitGatewayRouteTable")

class CreateTransitGatewayVpcAttachmentRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    subnet_ids: TransitGatewaySubnetIdList = pydantic.Field(None, alias="SubnetIds")
    options: 'CreateTransitGatewayVpcAttachmentRequestOptions' = pydantic.Field(None, alias="Options")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateTransitGatewayVpcAttachmentRequestOptions(_EC2ModelBase):
    dns_support: DnsSupportValue = pydantic.Field(None, alias="DnsSupport")
    ipv_6_support: Ipv6SupportValue = pydantic.Field(None, alias="Ipv6Support")
    appliance_mode_support: ApplianceModeSupportValue = pydantic.Field(None, alias="ApplianceModeSupport")

class CreateTransitGatewayVpcAttachmentResult(_EC2ModelBase):
    transit_gateway_vpc_attachment: 'TransitGatewayVpcAttachment' = pydantic.Field(None, alias="TransitGatewayVpcAttachment")

class CreateVerifiedAccessEndpointEniOptions(_EC2ModelBase):
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    protocol: VerifiedAccessEndpointProtocol = pydantic.Field(None, alias="Protocol")
    port: VerifiedAccessEndpointPortNumber = pydantic.Field(None, alias="Port")

class CreateVerifiedAccessEndpointLoadBalancerOptions(_EC2ModelBase):
    protocol: VerifiedAccessEndpointProtocol = pydantic.Field(None, alias="Protocol")
    port: VerifiedAccessEndpointPortNumber = pydantic.Field(None, alias="Port")
    load_balancer_arn: LoadBalancerArn = pydantic.Field(None, alias="LoadBalancerArn")
    subnet_ids: CreateVerifiedAccessEndpointSubnetIdList = pydantic.Field(None, alias="SubnetIds")

class CreateVerifiedAccessEndpointRequest(_EC2ModelBase):
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    endpoint_type: VerifiedAccessEndpointType = pydantic.Field(None, alias="EndpointType")
    attachment_type: VerifiedAccessEndpointAttachmentType = pydantic.Field(None, alias="AttachmentType")
    domain_certificate_arn: CertificateArn = pydantic.Field(None, alias="DomainCertificateArn")
    application_domain: String = pydantic.Field(None, alias="ApplicationDomain")
    endpoint_domain_prefix: String = pydantic.Field(None, alias="EndpointDomainPrefix")
    security_group_ids: SecurityGroupIdList = pydantic.Field(None, alias="SecurityGroupIds")
    load_balancer_options: 'CreateVerifiedAccessEndpointLoadBalancerOptions' = pydantic.Field(None, alias="LoadBalancerOptions")
    network_interface_options: 'CreateVerifiedAccessEndpointEniOptions' = pydantic.Field(None, alias="NetworkInterfaceOptions")
    description: String = pydantic.Field(None, alias="Description")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateVerifiedAccessEndpointResult(_EC2ModelBase):
    verified_access_endpoint: 'VerifiedAccessEndpoint' = pydantic.Field(None, alias="VerifiedAccessEndpoint")

class CreateVerifiedAccessGroupRequest(_EC2ModelBase):
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    description: String = pydantic.Field(None, alias="Description")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateVerifiedAccessGroupResult(_EC2ModelBase):
    verified_access_group: 'VerifiedAccessGroup' = pydantic.Field(None, alias="VerifiedAccessGroup")

class CreateVerifiedAccessInstanceRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateVerifiedAccessInstanceResult(_EC2ModelBase):
    verified_access_instance: 'VerifiedAccessInstance' = pydantic.Field(None, alias="VerifiedAccessInstance")

class CreateVerifiedAccessTrustProviderDeviceOptions(_EC2ModelBase):
    tenant_id: String = pydantic.Field(None, alias="TenantId")

class CreateVerifiedAccessTrustProviderOidcOptions(_EC2ModelBase):
    issuer: String = pydantic.Field(None, alias="Issuer")
    authorization_endpoint: String = pydantic.Field(None, alias="AuthorizationEndpoint")
    token_endpoint: String = pydantic.Field(None, alias="TokenEndpoint")
    user_info_endpoint: String = pydantic.Field(None, alias="UserInfoEndpoint")
    client_id: String = pydantic.Field(None, alias="ClientId")
    client_secret: ClientSecretType = pydantic.Field(None, alias="ClientSecret")
    scope: String = pydantic.Field(None, alias="Scope")

class CreateVerifiedAccessTrustProviderRequest(_EC2ModelBase):
    trust_provider_type: TrustProviderType = pydantic.Field(None, alias="TrustProviderType")
    user_trust_provider_type: UserTrustProviderType = pydantic.Field(None, alias="UserTrustProviderType")
    device_trust_provider_type: DeviceTrustProviderType = pydantic.Field(None, alias="DeviceTrustProviderType")
    oidc_options: 'CreateVerifiedAccessTrustProviderOidcOptions' = pydantic.Field(None, alias="OidcOptions")
    device_options: 'CreateVerifiedAccessTrustProviderDeviceOptions' = pydantic.Field(None, alias="DeviceOptions")
    policy_reference_name: String = pydantic.Field(None, alias="PolicyReferenceName")
    description: String = pydantic.Field(None, alias="Description")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateVerifiedAccessTrustProviderResult(_EC2ModelBase):
    verified_access_trust_provider: 'VerifiedAccessTrustProvider' = pydantic.Field(None, alias="VerifiedAccessTrustProvider")

class CreateVolumePermission(_EC2ModelBase):
    group: PermissionGroup = pydantic.Field(None, alias="Group")
    user_id: String = pydantic.Field(None, alias="UserId")

class CreateVolumePermissionModifications(_EC2ModelBase):
    add: CreateVolumePermissionList = pydantic.Field(None, alias="Add")
    remove: CreateVolumePermissionList = pydantic.Field(None, alias="Remove")

class CreateVolumeRequest(_EC2ModelBase):
    availability_zone: AvailabilityZoneName = pydantic.Field(None, alias="AvailabilityZone")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    iops: Integer = pydantic.Field(None, alias="Iops")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    size: Integer = pydantic.Field(None, alias="Size")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    volume_type: VolumeType = pydantic.Field(None, alias="VolumeType")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    multi_attach_enabled: Boolean = pydantic.Field(None, alias="MultiAttachEnabled")
    throughput: Integer = pydantic.Field(None, alias="Throughput")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateVpcEndpointConnectionNotificationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    vpc_endpoint_id: VpcEndpointId = pydantic.Field(None, alias="VpcEndpointId")
    connection_notification_arn: String = pydantic.Field(None, alias="ConnectionNotificationArn")
    connection_events: ValueStringList = pydantic.Field(None, alias="ConnectionEvents")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateVpcEndpointConnectionNotificationResult(_EC2ModelBase):
    connection_notification: 'ConnectionNotification' = pydantic.Field(None, alias="ConnectionNotification")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateVpcEndpointRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_endpoint_type: VpcEndpointType = pydantic.Field(None, alias="VpcEndpointType")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    service_name: String = pydantic.Field(None, alias="ServiceName")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    route_table_ids: VpcEndpointRouteTableIdList = pydantic.Field(None, alias="RouteTableIds")
    subnet_ids: VpcEndpointSubnetIdList = pydantic.Field(None, alias="SubnetIds")
    security_group_ids: VpcEndpointSecurityGroupIdList = pydantic.Field(None, alias="SecurityGroupIds")
    ip_address_type: IpAddressType = pydantic.Field(None, alias="IpAddressType")
    dns_options: 'DnsOptionsSpecification' = pydantic.Field(None, alias="DnsOptions")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    private_dns_enabled: Boolean = pydantic.Field(None, alias="PrivateDnsEnabled")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateVpcEndpointResult(_EC2ModelBase):
    vpc_endpoint: 'VpcEndpoint' = pydantic.Field(None, alias="VpcEndpoint")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateVpcEndpointServiceConfigurationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    acceptance_required: Boolean = pydantic.Field(None, alias="AcceptanceRequired")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    network_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="NetworkLoadBalancerArns")
    gateway_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="GatewayLoadBalancerArns")
    supported_ip_address_types: ValueStringList = pydantic.Field(None, alias="SupportedIpAddressTypes")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateVpcEndpointServiceConfigurationResult(_EC2ModelBase):
    service_configuration: 'ServiceConfiguration' = pydantic.Field(None, alias="ServiceConfiguration")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class CreateVpcPeeringConnectionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    peer_owner_id: String = pydantic.Field(None, alias="PeerOwnerId")
    peer_vpc_id: String = pydantic.Field(None, alias="PeerVpcId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    peer_region: String = pydantic.Field(None, alias="PeerRegion")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateVpcPeeringConnectionResult(_EC2ModelBase):
    vpc_peering_connection: 'VpcPeeringConnection' = pydantic.Field(None, alias="VpcPeeringConnection")

class CreateVpcRequest(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    amazon_provided_ipv_6_cidr_block: Boolean = pydantic.Field(None, alias="AmazonProvidedIpv6CidrBlock")
    ipv_6_pool: Ipv6PoolEc2Id = pydantic.Field(None, alias="Ipv6Pool")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    ipv_4_ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="Ipv4IpamPoolId")
    ipv_4_netmask_length: NetmaskLength = pydantic.Field(None, alias="Ipv4NetmaskLength")
    ipv_6_ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="Ipv6IpamPoolId")
    ipv_6_netmask_length: NetmaskLength = pydantic.Field(None, alias="Ipv6NetmaskLength")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_tenancy: Tenancy = pydantic.Field(None, alias="InstanceTenancy")
    ipv_6_cidr_block_network_border_group: String = pydantic.Field(None, alias="Ipv6CidrBlockNetworkBorderGroup")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateVpcResult(_EC2ModelBase):
    vpc: 'Vpc' = pydantic.Field(None, alias="Vpc")

class CreateVpnConnectionRequest(_EC2ModelBase):
    customer_gateway_id: CustomerGatewayId = pydantic.Field(None, alias="CustomerGatewayId")
    type: String = pydantic.Field(None, alias="Type")
    vpn_gateway_id: VpnGatewayId = pydantic.Field(None, alias="VpnGatewayId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    options: 'VpnConnectionOptionsSpecification' = pydantic.Field(None, alias="Options")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class CreateVpnConnectionResult(_EC2ModelBase):
    vpn_connection: 'VpnConnection' = pydantic.Field(None, alias="VpnConnection")

class CreateVpnConnectionRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")

class CreateVpnGatewayRequest(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    type: GatewayType = pydantic.Field(None, alias="Type")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    amazon_side_asn: Long = pydantic.Field(None, alias="AmazonSideAsn")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class CreateVpnGatewayResult(_EC2ModelBase):
    vpn_gateway: 'VpnGateway' = pydantic.Field(None, alias="VpnGateway")

class CreditSpecification(_EC2ModelBase):
    cpu_credits: String = pydantic.Field(None, alias="CpuCredits")

class CreditSpecificationRequest(_EC2ModelBase):
    cpu_credits: String = pydantic.Field(None, alias="CpuCredits")

class CustomerGateway(_EC2ModelBase):
    bgp_asn: String = pydantic.Field(None, alias="BgpAsn")
    customer_gateway_id: String = pydantic.Field(None, alias="CustomerGatewayId")
    ip_address: String = pydantic.Field(None, alias="IpAddress")
    certificate_arn: String = pydantic.Field(None, alias="CertificateArn")
    state: String = pydantic.Field(None, alias="State")
    type: String = pydantic.Field(None, alias="Type")
    device_name: String = pydantic.Field(None, alias="DeviceName")
    tags: TagList = pydantic.Field(None, alias="Tags")

class DataQuery(_EC2ModelBase):
    id: String = pydantic.Field(None, alias="Id")
    source: String = pydantic.Field(None, alias="Source")
    destination: String = pydantic.Field(None, alias="Destination")
    metric: MetricType = pydantic.Field(None, alias="Metric")
    statistic: StatisticType = pydantic.Field(None, alias="Statistic")
    period: PeriodType = pydantic.Field(None, alias="Period")

class DataResponse(_EC2ModelBase):
    id: String = pydantic.Field(None, alias="Id")
    source: String = pydantic.Field(None, alias="Source")
    destination: String = pydantic.Field(None, alias="Destination")
    metric: MetricType = pydantic.Field(None, alias="Metric")
    statistic: StatisticType = pydantic.Field(None, alias="Statistic")
    period: PeriodType = pydantic.Field(None, alias="Period")
    metric_points: MetricPoints = pydantic.Field(None, alias="MetricPoints")

class DeleteCarrierGatewayRequest(_EC2ModelBase):
    carrier_gateway_id: CarrierGatewayId = pydantic.Field(None, alias="CarrierGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteCarrierGatewayResult(_EC2ModelBase):
    carrier_gateway: 'CarrierGateway' = pydantic.Field(None, alias="CarrierGateway")

class DeleteClientVpnEndpointRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteClientVpnEndpointResult(_EC2ModelBase):
    status: 'ClientVpnEndpointStatus' = pydantic.Field(None, alias="Status")

class DeleteClientVpnRouteRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    target_vpc_subnet_id: SubnetId = pydantic.Field(None, alias="TargetVpcSubnetId")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteClientVpnRouteResult(_EC2ModelBase):
    status: 'ClientVpnRouteStatus' = pydantic.Field(None, alias="Status")

class DeleteCoipCidrRequest(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    coip_pool_id: Ipv4PoolCoipId = pydantic.Field(None, alias="CoipPoolId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteCoipCidrResult(_EC2ModelBase):
    coip_cidr: 'CoipCidr' = pydantic.Field(None, alias="CoipCidr")

class DeleteCoipPoolRequest(_EC2ModelBase):
    coip_pool_id: Ipv4PoolCoipId = pydantic.Field(None, alias="CoipPoolId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteCoipPoolResult(_EC2ModelBase):
    coip_pool: 'CoipPool' = pydantic.Field(None, alias="CoipPool")

class DeleteCustomerGatewayRequest(_EC2ModelBase):
    customer_gateway_id: CustomerGatewayId = pydantic.Field(None, alias="CustomerGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteDhcpOptionsRequest(_EC2ModelBase):
    dhcp_options_id: DhcpOptionsId = pydantic.Field(None, alias="DhcpOptionsId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteEgressOnlyInternetGatewayRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    egress_only_internet_gateway_id: EgressOnlyInternetGatewayId = pydantic.Field(None, alias="EgressOnlyInternetGatewayId")

class DeleteEgressOnlyInternetGatewayResult(_EC2ModelBase):
    return_code: Boolean = pydantic.Field(None, alias="ReturnCode")

class DeleteFleetError(_EC2ModelBase):
    code: DeleteFleetErrorCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class DeleteFleetErrorItem(_EC2ModelBase):
    error: 'DeleteFleetError' = pydantic.Field(None, alias="Error")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")

class DeleteFleetSuccessItem(_EC2ModelBase):
    current_fleet_state: FleetStateCode = pydantic.Field(None, alias="CurrentFleetState")
    previous_fleet_state: FleetStateCode = pydantic.Field(None, alias="PreviousFleetState")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")

class DeleteFleetsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    fleet_ids: FleetIdSet = pydantic.Field(None, alias="FleetIds")
    terminate_instances: Boolean = pydantic.Field(None, alias="TerminateInstances")

class DeleteFleetsResult(_EC2ModelBase):
    successful_fleet_deletions: DeleteFleetSuccessSet = pydantic.Field(None, alias="SuccessfulFleetDeletions")
    unsuccessful_fleet_deletions: DeleteFleetErrorSet = pydantic.Field(None, alias="UnsuccessfulFleetDeletions")

class DeleteFlowLogsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    flow_log_ids: FlowLogIdList = pydantic.Field(None, alias="FlowLogIds")

class DeleteFlowLogsResult(_EC2ModelBase):
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class DeleteFpgaImageRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    fpga_image_id: FpgaImageId = pydantic.Field(None, alias="FpgaImageId")

class DeleteFpgaImageResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DeleteInstanceEventWindowRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    force_delete: Boolean = pydantic.Field(None, alias="ForceDelete")
    instance_event_window_id: InstanceEventWindowId = pydantic.Field(None, alias="InstanceEventWindowId")

class DeleteInstanceEventWindowResult(_EC2ModelBase):
    instance_event_window_state: 'InstanceEventWindowStateChange' = pydantic.Field(None, alias="InstanceEventWindowState")

class DeleteInternetGatewayRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    internet_gateway_id: InternetGatewayId = pydantic.Field(None, alias="InternetGatewayId")

class DeleteIpamPoolRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")

class DeleteIpamPoolResult(_EC2ModelBase):
    ipam_pool: 'IpamPool' = pydantic.Field(None, alias="IpamPool")

class DeleteIpamRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    cascade: Boolean = pydantic.Field(None, alias="Cascade")

class DeleteIpamResourceDiscoveryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")

class DeleteIpamResourceDiscoveryResult(_EC2ModelBase):
    ipam_resource_discovery: 'IpamResourceDiscovery' = pydantic.Field(None, alias="IpamResourceDiscovery")

class DeleteIpamResult(_EC2ModelBase):
    ipam: 'Ipam' = pydantic.Field(None, alias="Ipam")

class DeleteIpamScopeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")

class DeleteIpamScopeResult(_EC2ModelBase):
    ipam_scope: 'IpamScope' = pydantic.Field(None, alias="IpamScope")

class DeleteKeyPairRequest(_EC2ModelBase):
    key_name: KeyPairName = pydantic.Field(None, alias="KeyName")
    key_pair_id: KeyPairId = pydantic.Field(None, alias="KeyPairId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteLaunchTemplateRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")

class DeleteLaunchTemplateResult(_EC2ModelBase):
    launch_template: 'LaunchTemplate' = pydantic.Field(None, alias="LaunchTemplate")

class DeleteLaunchTemplateVersionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    versions: VersionStringList = pydantic.Field(None, alias="Versions")

class DeleteLaunchTemplateVersionsResponseErrorItem(_EC2ModelBase):
    launch_template_id: String = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: String = pydantic.Field(None, alias="LaunchTemplateName")
    version_number: Long = pydantic.Field(None, alias="VersionNumber")
    response_error: 'ResponseError' = pydantic.Field(None, alias="ResponseError")

class DeleteLaunchTemplateVersionsResponseSuccessItem(_EC2ModelBase):
    launch_template_id: String = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: String = pydantic.Field(None, alias="LaunchTemplateName")
    version_number: Long = pydantic.Field(None, alias="VersionNumber")

class DeleteLaunchTemplateVersionsResult(_EC2ModelBase):
    successfully_deleted_launch_template_versions: DeleteLaunchTemplateVersionsResponseSuccessSet = pydantic.Field(None, alias="SuccessfullyDeletedLaunchTemplateVersions")
    unsuccessfully_deleted_launch_template_versions: DeleteLaunchTemplateVersionsResponseErrorSet = pydantic.Field(None, alias="UnsuccessfullyDeletedLaunchTemplateVersions")

class DeleteLocalGatewayRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")

class DeleteLocalGatewayRouteResult(_EC2ModelBase):
    route: 'LocalGatewayRoute' = pydantic.Field(None, alias="Route")

class DeleteLocalGatewayRouteTableRequest(_EC2ModelBase):
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteLocalGatewayRouteTableResult(_EC2ModelBase):
    local_gateway_route_table: 'LocalGatewayRouteTable' = pydantic.Field(None, alias="LocalGatewayRouteTable")

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest(_EC2ModelBase):
    local_gateway_route_table_virtual_interface_group_association_id: LocalGatewayRouteTableVirtualInterfaceGroupAssociationId = pydantic.Field(None, alias="LocalGatewayRouteTableVirtualInterfaceGroupAssociationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(_EC2ModelBase):
    local_gateway_route_table_virtual_interface_group_association: 'LocalGatewayRouteTableVirtualInterfaceGroupAssociation' = pydantic.Field(None, alias="LocalGatewayRouteTableVirtualInterfaceGroupAssociation")

class DeleteLocalGatewayRouteTableVpcAssociationRequest(_EC2ModelBase):
    local_gateway_route_table_vpc_association_id: LocalGatewayRouteTableVpcAssociationId = pydantic.Field(None, alias="LocalGatewayRouteTableVpcAssociationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteLocalGatewayRouteTableVpcAssociationResult(_EC2ModelBase):
    local_gateway_route_table_vpc_association: 'LocalGatewayRouteTableVpcAssociation' = pydantic.Field(None, alias="LocalGatewayRouteTableVpcAssociation")

class DeleteManagedPrefixListRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")

class DeleteManagedPrefixListResult(_EC2ModelBase):
    prefix_list: 'ManagedPrefixList' = pydantic.Field(None, alias="PrefixList")

class DeleteNatGatewayRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")

class DeleteNatGatewayResult(_EC2ModelBase):
    nat_gateway_id: String = pydantic.Field(None, alias="NatGatewayId")

class DeleteNetworkAclEntryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    egress: Boolean = pydantic.Field(None, alias="Egress")
    network_acl_id: NetworkAclId = pydantic.Field(None, alias="NetworkAclId")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")

class DeleteNetworkAclRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_acl_id: NetworkAclId = pydantic.Field(None, alias="NetworkAclId")

class DeleteNetworkInsightsAccessScopeAnalysisRequest(_EC2ModelBase):
    network_insights_access_scope_analysis_id: NetworkInsightsAccessScopeAnalysisId = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteNetworkInsightsAccessScopeAnalysisResult(_EC2ModelBase):
    network_insights_access_scope_analysis_id: NetworkInsightsAccessScopeAnalysisId = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisId")

class DeleteNetworkInsightsAccessScopeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")

class DeleteNetworkInsightsAccessScopeResult(_EC2ModelBase):
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")

class DeleteNetworkInsightsAnalysisRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_insights_analysis_id: NetworkInsightsAnalysisId = pydantic.Field(None, alias="NetworkInsightsAnalysisId")

class DeleteNetworkInsightsAnalysisResult(_EC2ModelBase):
    network_insights_analysis_id: NetworkInsightsAnalysisId = pydantic.Field(None, alias="NetworkInsightsAnalysisId")

class DeleteNetworkInsightsPathRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_insights_path_id: NetworkInsightsPathId = pydantic.Field(None, alias="NetworkInsightsPathId")

class DeleteNetworkInsightsPathResult(_EC2ModelBase):
    network_insights_path_id: NetworkInsightsPathId = pydantic.Field(None, alias="NetworkInsightsPathId")

class DeleteNetworkInterfacePermissionRequest(_EC2ModelBase):
    network_interface_permission_id: NetworkInterfacePermissionId = pydantic.Field(None, alias="NetworkInterfacePermissionId")
    force: Boolean = pydantic.Field(None, alias="Force")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteNetworkInterfacePermissionResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DeleteNetworkInterfaceRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")

class DeletePlacementGroupRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")

class DeletePublicIpv4PoolRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    pool_id: Ipv4PoolEc2Id = pydantic.Field(None, alias="PoolId")

class DeletePublicIpv4PoolResult(_EC2ModelBase):
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class DeleteQueuedReservedInstancesError(_EC2ModelBase):
    code: DeleteQueuedReservedInstancesErrorCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class DeleteQueuedReservedInstancesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    reserved_instances_ids: DeleteQueuedReservedInstancesIdList = pydantic.Field(None, alias="ReservedInstancesIds")

class DeleteQueuedReservedInstancesResult(_EC2ModelBase):
    successful_queued_purchase_deletions: SuccessfulQueuedPurchaseDeletionSet = pydantic.Field(None, alias="SuccessfulQueuedPurchaseDeletions")
    failed_queued_purchase_deletions: FailedQueuedPurchaseDeletionSet = pydantic.Field(None, alias="FailedQueuedPurchaseDeletions")

class DeleteRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    destination_ipv_6_cidr_block: String = pydantic.Field(None, alias="DestinationIpv6CidrBlock")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")

class DeleteRouteTableRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")

class DeleteSecurityGroupRequest(_EC2ModelBase):
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    group_name: SecurityGroupName = pydantic.Field(None, alias="GroupName")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteSnapshotRequest(_EC2ModelBase):
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteSpotDatafeedSubscriptionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteSubnetCidrReservationRequest(_EC2ModelBase):
    subnet_cidr_reservation_id: SubnetCidrReservationId = pydantic.Field(None, alias="SubnetCidrReservationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteSubnetCidrReservationResult(_EC2ModelBase):
    deleted_subnet_cidr_reservation: 'SubnetCidrReservation' = pydantic.Field(None, alias="DeletedSubnetCidrReservation")

class DeleteSubnetRequest(_EC2ModelBase):
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTagsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    resources: ResourceIdList = pydantic.Field(None, alias="Resources")
    tags: TagList = pydantic.Field(None, alias="Tags")

class DeleteTrafficMirrorFilterRequest(_EC2ModelBase):
    traffic_mirror_filter_id: TrafficMirrorFilterId = pydantic.Field(None, alias="TrafficMirrorFilterId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTrafficMirrorFilterResult(_EC2ModelBase):
    traffic_mirror_filter_id: String = pydantic.Field(None, alias="TrafficMirrorFilterId")

class DeleteTrafficMirrorFilterRuleRequest(_EC2ModelBase):
    traffic_mirror_filter_rule_id: TrafficMirrorFilterRuleIdWithResolver = pydantic.Field(None, alias="TrafficMirrorFilterRuleId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTrafficMirrorFilterRuleResult(_EC2ModelBase):
    traffic_mirror_filter_rule_id: String = pydantic.Field(None, alias="TrafficMirrorFilterRuleId")

class DeleteTrafficMirrorSessionRequest(_EC2ModelBase):
    traffic_mirror_session_id: TrafficMirrorSessionId = pydantic.Field(None, alias="TrafficMirrorSessionId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTrafficMirrorSessionResult(_EC2ModelBase):
    traffic_mirror_session_id: String = pydantic.Field(None, alias="TrafficMirrorSessionId")

class DeleteTrafficMirrorTargetRequest(_EC2ModelBase):
    traffic_mirror_target_id: TrafficMirrorTargetId = pydantic.Field(None, alias="TrafficMirrorTargetId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTrafficMirrorTargetResult(_EC2ModelBase):
    traffic_mirror_target_id: String = pydantic.Field(None, alias="TrafficMirrorTargetId")

class DeleteTransitGatewayConnectPeerRequest(_EC2ModelBase):
    transit_gateway_connect_peer_id: TransitGatewayConnectPeerId = pydantic.Field(None, alias="TransitGatewayConnectPeerId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayConnectPeerResult(_EC2ModelBase):
    transit_gateway_connect_peer: 'TransitGatewayConnectPeer' = pydantic.Field(None, alias="TransitGatewayConnectPeer")

class DeleteTransitGatewayConnectRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayConnectResult(_EC2ModelBase):
    transit_gateway_connect: 'TransitGatewayConnect' = pydantic.Field(None, alias="TransitGatewayConnect")

class DeleteTransitGatewayMulticastDomainRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayMulticastDomainResult(_EC2ModelBase):
    transit_gateway_multicast_domain: 'TransitGatewayMulticastDomain' = pydantic.Field(None, alias="TransitGatewayMulticastDomain")

class DeleteTransitGatewayPeeringAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayPeeringAttachmentResult(_EC2ModelBase):
    transit_gateway_peering_attachment: 'TransitGatewayPeeringAttachment' = pydantic.Field(None, alias="TransitGatewayPeeringAttachment")

class DeleteTransitGatewayPolicyTableRequest(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayPolicyTableResult(_EC2ModelBase):
    transit_gateway_policy_table: 'TransitGatewayPolicyTable' = pydantic.Field(None, alias="TransitGatewayPolicyTable")

class DeleteTransitGatewayPrefixListReferenceRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayPrefixListReferenceResult(_EC2ModelBase):
    transit_gateway_prefix_list_reference: 'TransitGatewayPrefixListReference' = pydantic.Field(None, alias="TransitGatewayPrefixListReference")

class DeleteTransitGatewayRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayResult(_EC2ModelBase):
    transit_gateway: 'TransitGateway' = pydantic.Field(None, alias="TransitGateway")

class DeleteTransitGatewayRouteRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayRouteResult(_EC2ModelBase):
    route: 'TransitGatewayRoute' = pydantic.Field(None, alias="Route")

class DeleteTransitGatewayRouteTableAnnouncementRequest(_EC2ModelBase):
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayRouteTableAnnouncementResult(_EC2ModelBase):
    transit_gateway_route_table_announcement: 'TransitGatewayRouteTableAnnouncement' = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncement")

class DeleteTransitGatewayRouteTableRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayRouteTableResult(_EC2ModelBase):
    transit_gateway_route_table: 'TransitGatewayRouteTable' = pydantic.Field(None, alias="TransitGatewayRouteTable")

class DeleteTransitGatewayVpcAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteTransitGatewayVpcAttachmentResult(_EC2ModelBase):
    transit_gateway_vpc_attachment: 'TransitGatewayVpcAttachment' = pydantic.Field(None, alias="TransitGatewayVpcAttachment")

class DeleteVerifiedAccessEndpointRequest(_EC2ModelBase):
    verified_access_endpoint_id: VerifiedAccessEndpointId = pydantic.Field(None, alias="VerifiedAccessEndpointId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteVerifiedAccessEndpointResult(_EC2ModelBase):
    verified_access_endpoint: 'VerifiedAccessEndpoint' = pydantic.Field(None, alias="VerifiedAccessEndpoint")

class DeleteVerifiedAccessGroupRequest(_EC2ModelBase):
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteVerifiedAccessGroupResult(_EC2ModelBase):
    verified_access_group: 'VerifiedAccessGroup' = pydantic.Field(None, alias="VerifiedAccessGroup")

class DeleteVerifiedAccessInstanceRequest(_EC2ModelBase):
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class DeleteVerifiedAccessInstanceResult(_EC2ModelBase):
    verified_access_instance: 'VerifiedAccessInstance' = pydantic.Field(None, alias="VerifiedAccessInstance")

class DeleteVerifiedAccessTrustProviderRequest(_EC2ModelBase):
    verified_access_trust_provider_id: VerifiedAccessTrustProviderId = pydantic.Field(None, alias="VerifiedAccessTrustProviderId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class DeleteVerifiedAccessTrustProviderResult(_EC2ModelBase):
    verified_access_trust_provider: 'VerifiedAccessTrustProvider' = pydantic.Field(None, alias="VerifiedAccessTrustProvider")

class DeleteVolumeRequest(_EC2ModelBase):
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteVpcEndpointConnectionNotificationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    connection_notification_ids: ConnectionNotificationIdsList = pydantic.Field(None, alias="ConnectionNotificationIds")

class DeleteVpcEndpointConnectionNotificationsResult(_EC2ModelBase):
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class DeleteVpcEndpointServiceConfigurationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_ids: VpcEndpointServiceIdList = pydantic.Field(None, alias="ServiceIds")

class DeleteVpcEndpointServiceConfigurationsResult(_EC2ModelBase):
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class DeleteVpcEndpointsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_endpoint_ids: VpcEndpointIdList = pydantic.Field(None, alias="VpcEndpointIds")

class DeleteVpcEndpointsResult(_EC2ModelBase):
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class DeleteVpcPeeringConnectionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_peering_connection_id: VpcPeeringConnectionId = pydantic.Field(None, alias="VpcPeeringConnectionId")

class DeleteVpcPeeringConnectionResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DeleteVpcRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteVpnConnectionRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeleteVpnConnectionRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")

class DeleteVpnGatewayRequest(_EC2ModelBase):
    vpn_gateway_id: VpnGatewayId = pydantic.Field(None, alias="VpnGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeprovisionByoipCidrRequest(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeprovisionByoipCidrResult(_EC2ModelBase):
    byoip_cidr: 'ByoipCidr' = pydantic.Field(None, alias="ByoipCidr")

class DeprovisionIpamPoolCidrRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    cidr: String = pydantic.Field(None, alias="Cidr")

class DeprovisionIpamPoolCidrResult(_EC2ModelBase):
    ipam_pool_cidr: 'IpamPoolCidr' = pydantic.Field(None, alias="IpamPoolCidr")

class DeprovisionPublicIpv4PoolCidrRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    pool_id: Ipv4PoolEc2Id = pydantic.Field(None, alias="PoolId")
    cidr: String = pydantic.Field(None, alias="Cidr")

class DeprovisionPublicIpv4PoolCidrResult(_EC2ModelBase):
    pool_id: Ipv4PoolEc2Id = pydantic.Field(None, alias="PoolId")
    deprovisioned_addresses: DeprovisionedAddressSet = pydantic.Field(None, alias="DeprovisionedAddresses")

class DeregisterImageRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeregisterInstanceEventNotificationAttributesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_tag_attribute: 'DeregisterInstanceTagAttributeRequest' = pydantic.Field(None, alias="InstanceTagAttribute")

class DeregisterInstanceEventNotificationAttributesResult(_EC2ModelBase):
    instance_tag_attribute: 'InstanceTagNotificationAttribute' = pydantic.Field(None, alias="InstanceTagAttribute")

class DeregisterInstanceTagAttributeRequest(_EC2ModelBase):
    include_all_tags_of_instance: Boolean = pydantic.Field(None, alias="IncludeAllTagsOfInstance")
    instance_tag_keys: InstanceTagKeySet = pydantic.Field(None, alias="InstanceTagKeys")

class DeregisterTransitGatewayMulticastGroupMembersRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")
    network_interface_ids: TransitGatewayNetworkInterfaceIdList = pydantic.Field(None, alias="NetworkInterfaceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeregisterTransitGatewayMulticastGroupMembersResult(_EC2ModelBase):
    deregistered_multicast_group_members: 'TransitGatewayMulticastDeregisteredGroupMembers' = pydantic.Field(None, alias="DeregisteredMulticastGroupMembers")

class DeregisterTransitGatewayMulticastGroupSourcesRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")
    network_interface_ids: TransitGatewayNetworkInterfaceIdList = pydantic.Field(None, alias="NetworkInterfaceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeregisterTransitGatewayMulticastGroupSourcesResult(_EC2ModelBase):
    deregistered_multicast_group_sources: 'TransitGatewayMulticastDeregisteredGroupSources' = pydantic.Field(None, alias="DeregisteredMulticastGroupSources")

class DescribeAccountAttributesRequest(_EC2ModelBase):
    attribute_names: AccountAttributeNameStringList = pydantic.Field(None, alias="AttributeNames")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAccountAttributesResult(_EC2ModelBase):
    account_attributes: AccountAttributeList = pydantic.Field(None, alias="AccountAttributes")

class DescribeAddressTransfersRequest(_EC2ModelBase):
    allocation_ids: AllocationIdList = pydantic.Field(None, alias="AllocationIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeAddressTransfersMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAddressTransfersResult(_EC2ModelBase):
    address_transfers: AddressTransferList = pydantic.Field(None, alias="AddressTransfers")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeAddressesAttributeRequest(_EC2ModelBase):
    allocation_ids: AllocationIds = pydantic.Field(None, alias="AllocationIds")
    attribute: AddressAttributeName = pydantic.Field(None, alias="Attribute")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: AddressMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAddressesAttributeResult(_EC2ModelBase):
    addresses: AddressSet = pydantic.Field(None, alias="Addresses")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeAddressesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    public_ips: PublicIpStringList = pydantic.Field(None, alias="PublicIps")
    allocation_ids: AllocationIdList = pydantic.Field(None, alias="AllocationIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAddressesResult(_EC2ModelBase):
    addresses: AddressList = pydantic.Field(None, alias="Addresses")

class DescribeAggregateIdFormatRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAggregateIdFormatResult(_EC2ModelBase):
    use_long_ids_aggregated: Boolean = pydantic.Field(None, alias="UseLongIdsAggregated")
    statuses: IdFormatList = pydantic.Field(None, alias="Statuses")

class DescribeAvailabilityZonesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    zone_names: ZoneNameStringList = pydantic.Field(None, alias="ZoneNames")
    zone_ids: ZoneIdStringList = pydantic.Field(None, alias="ZoneIds")
    all_availability_zones: Boolean = pydantic.Field(None, alias="AllAvailabilityZones")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAvailabilityZonesResult(_EC2ModelBase):
    availability_zones: AvailabilityZoneList = pydantic.Field(None, alias="AvailabilityZones")

class DescribeAwsNetworkPerformanceMetricSubscriptionsRequest(_EC2ModelBase):
    max_results: MaxResultsParam = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeAwsNetworkPerformanceMetricSubscriptionsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    subscriptions: SubscriptionList = pydantic.Field(None, alias="Subscriptions")

class DescribeBundleTasksRequest(_EC2ModelBase):
    bundle_ids: BundleIdStringList = pydantic.Field(None, alias="BundleIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeBundleTasksResult(_EC2ModelBase):
    bundle_tasks: BundleTaskList = pydantic.Field(None, alias="BundleTasks")

class DescribeByoipCidrsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: DescribeByoipCidrsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeByoipCidrsResult(_EC2ModelBase):
    byoip_cidrs: ByoipCidrSet = pydantic.Field(None, alias="ByoipCidrs")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeCapacityReservationFleetsRequest(_EC2ModelBase):
    capacity_reservation_fleet_ids: CapacityReservationFleetIdSet = pydantic.Field(None, alias="CapacityReservationFleetIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeCapacityReservationFleetsMaxResults = pydantic.Field(None, alias="MaxResults")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeCapacityReservationFleetsResult(_EC2ModelBase):
    capacity_reservation_fleets: CapacityReservationFleetSet = pydantic.Field(None, alias="CapacityReservationFleets")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeCapacityReservationsRequest(_EC2ModelBase):
    capacity_reservation_ids: CapacityReservationIdSet = pydantic.Field(None, alias="CapacityReservationIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeCapacityReservationsMaxResults = pydantic.Field(None, alias="MaxResults")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeCapacityReservationsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    capacity_reservations: CapacityReservationSet = pydantic.Field(None, alias="CapacityReservations")

class DescribeCarrierGatewaysRequest(_EC2ModelBase):
    carrier_gateway_ids: CarrierGatewayIdSet = pydantic.Field(None, alias="CarrierGatewayIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: CarrierGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeCarrierGatewaysResult(_EC2ModelBase):
    carrier_gateways: CarrierGatewaySet = pydantic.Field(None, alias="CarrierGateways")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeClassicLinkInstancesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    max_results: DescribeClassicLinkInstancesMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeClassicLinkInstancesResult(_EC2ModelBase):
    instances: ClassicLinkInstanceList = pydantic.Field(None, alias="Instances")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeClientVpnAuthorizationRulesRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeClientVpnAuthorizationRulesMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeClientVpnAuthorizationRulesResult(_EC2ModelBase):
    authorization_rules: AuthorizationRuleSet = pydantic.Field(None, alias="AuthorizationRules")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeClientVpnConnectionsRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: DescribeClientVpnConnectionsMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeClientVpnConnectionsResult(_EC2ModelBase):
    connections: ClientVpnConnectionSet = pydantic.Field(None, alias="Connections")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeClientVpnEndpointsRequest(_EC2ModelBase):
    client_vpn_endpoint_ids: ClientVpnEndpointIdList = pydantic.Field(None, alias="ClientVpnEndpointIds")
    max_results: DescribeClientVpnEndpointMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeClientVpnEndpointsResult(_EC2ModelBase):
    client_vpn_endpoints: EndpointSet = pydantic.Field(None, alias="ClientVpnEndpoints")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeClientVpnRoutesRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeClientVpnRoutesMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeClientVpnRoutesResult(_EC2ModelBase):
    routes: ClientVpnRouteSet = pydantic.Field(None, alias="Routes")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeClientVpnTargetNetworksRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    association_ids: ValueStringList = pydantic.Field(None, alias="AssociationIds")
    max_results: DescribeClientVpnTargetNetworksMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeClientVpnTargetNetworksResult(_EC2ModelBase):
    client_vpn_target_networks: TargetNetworkSet = pydantic.Field(None, alias="ClientVpnTargetNetworks")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeCoipPoolsRequest(_EC2ModelBase):
    pool_ids: CoipPoolIdSet = pydantic.Field(None, alias="PoolIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: CoipPoolMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeCoipPoolsResult(_EC2ModelBase):
    coip_pools: CoipPoolSet = pydantic.Field(None, alias="CoipPools")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeConversionTasksRequest(_EC2ModelBase):
    conversion_task_ids: ConversionIdStringList = pydantic.Field(None, alias="ConversionTaskIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeConversionTasksResult(_EC2ModelBase):
    conversion_tasks: DescribeConversionTaskList = pydantic.Field(None, alias="ConversionTasks")

class DescribeCustomerGatewaysRequest(_EC2ModelBase):
    customer_gateway_ids: CustomerGatewayIdStringList = pydantic.Field(None, alias="CustomerGatewayIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeCustomerGatewaysResult(_EC2ModelBase):
    customer_gateways: CustomerGatewayList = pydantic.Field(None, alias="CustomerGateways")

class DescribeDhcpOptionsRequest(_EC2ModelBase):
    dhcp_options_ids: DhcpOptionsIdStringList = pydantic.Field(None, alias="DhcpOptionsIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeDhcpOptionsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeDhcpOptionsResult(_EC2ModelBase):
    dhcp_options: DhcpOptionsList = pydantic.Field(None, alias="DhcpOptions")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeEgressOnlyInternetGatewaysRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    egress_only_internet_gateway_ids: EgressOnlyInternetGatewayIdList = pydantic.Field(None, alias="EgressOnlyInternetGatewayIds")
    max_results: DescribeEgressOnlyInternetGatewaysMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeEgressOnlyInternetGatewaysResult(_EC2ModelBase):
    egress_only_internet_gateways: EgressOnlyInternetGatewayList = pydantic.Field(None, alias="EgressOnlyInternetGateways")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeElasticGpusRequest(_EC2ModelBase):
    elastic_gpu_ids: ElasticGpuIdSet = pydantic.Field(None, alias="ElasticGpuIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeElasticGpusMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeElasticGpusResult(_EC2ModelBase):
    elastic_gpu_set: ElasticGpuSet = pydantic.Field(None, alias="ElasticGpuSet")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeExportImageTasksRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    export_image_task_ids: ExportImageTaskIdList = pydantic.Field(None, alias="ExportImageTaskIds")
    max_results: DescribeExportImageTasksMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeExportImageTasksResult(_EC2ModelBase):
    export_image_tasks: ExportImageTaskList = pydantic.Field(None, alias="ExportImageTasks")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeExportTasksRequest(_EC2ModelBase):
    export_task_ids: ExportTaskIdStringList = pydantic.Field(None, alias="ExportTaskIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeExportTasksResult(_EC2ModelBase):
    export_tasks: ExportTaskList = pydantic.Field(None, alias="ExportTasks")

class DescribeFastLaunchImagesRequest(_EC2ModelBase):
    image_ids: FastLaunchImageIdList = pydantic.Field(None, alias="ImageIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeFastLaunchImagesRequestMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeFastLaunchImagesResult(_EC2ModelBase):
    fast_launch_images: DescribeFastLaunchImagesSuccessSet = pydantic.Field(None, alias="FastLaunchImages")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeFastLaunchImagesSuccessItem(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    resource_type: FastLaunchResourceType = pydantic.Field(None, alias="ResourceType")
    snapshot_configuration: 'FastLaunchSnapshotConfigurationResponse' = pydantic.Field(None, alias="SnapshotConfiguration")
    launch_template: 'FastLaunchLaunchTemplateSpecificationResponse' = pydantic.Field(None, alias="LaunchTemplate")
    max_parallel_launches: Integer = pydantic.Field(None, alias="MaxParallelLaunches")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: FastLaunchStateCode = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    state_transition_time: MillisecondDateTime = pydantic.Field(None, alias="StateTransitionTime")

class DescribeFastSnapshotRestoreSuccessItem(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    state: FastSnapshotRestoreStateCode = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    owner_alias: String = pydantic.Field(None, alias="OwnerAlias")
    enabling_time: MillisecondDateTime = pydantic.Field(None, alias="EnablingTime")
    optimizing_time: MillisecondDateTime = pydantic.Field(None, alias="OptimizingTime")
    enabled_time: MillisecondDateTime = pydantic.Field(None, alias="EnabledTime")
    disabling_time: MillisecondDateTime = pydantic.Field(None, alias="DisablingTime")
    disabled_time: MillisecondDateTime = pydantic.Field(None, alias="DisabledTime")

class DescribeFastSnapshotRestoresRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeFastSnapshotRestoresMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeFastSnapshotRestoresResult(_EC2ModelBase):
    fast_snapshot_restores: DescribeFastSnapshotRestoreSuccessSet = pydantic.Field(None, alias="FastSnapshotRestores")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeFleetError(_EC2ModelBase):
    launch_template_and_overrides: 'LaunchTemplateAndOverridesResponse' = pydantic.Field(None, alias="LaunchTemplateAndOverrides")
    lifecycle: InstanceLifecycle = pydantic.Field(None, alias="Lifecycle")
    error_code: String = pydantic.Field(None, alias="ErrorCode")
    error_message: String = pydantic.Field(None, alias="ErrorMessage")

class DescribeFleetHistoryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    event_type: FleetEventType = pydantic.Field(None, alias="EventType")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")

class DescribeFleetHistoryResult(_EC2ModelBase):
    history_records: HistoryRecordSet = pydantic.Field(None, alias="HistoryRecords")
    last_evaluated_time: DateTime = pydantic.Field(None, alias="LastEvaluatedTime")
    next_token: String = pydantic.Field(None, alias="NextToken")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")

class DescribeFleetInstancesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeFleetInstancesResult(_EC2ModelBase):
    active_instances: ActiveInstanceSet = pydantic.Field(None, alias="ActiveInstances")
    next_token: String = pydantic.Field(None, alias="NextToken")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")

class DescribeFleetsInstances(_EC2ModelBase):
    launch_template_and_overrides: 'LaunchTemplateAndOverridesResponse' = pydantic.Field(None, alias="LaunchTemplateAndOverrides")
    lifecycle: InstanceLifecycle = pydantic.Field(None, alias="Lifecycle")
    instance_ids: InstanceIdsSet = pydantic.Field(None, alias="InstanceIds")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    platform: PlatformValues = pydantic.Field(None, alias="Platform")

class DescribeFleetsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    fleet_ids: FleetIdSet = pydantic.Field(None, alias="FleetIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeFleetsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    fleets: FleetSet = pydantic.Field(None, alias="Fleets")

class DescribeFlowLogsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filter: FilterList = pydantic.Field(None, alias="Filter")
    flow_log_ids: FlowLogIdList = pydantic.Field(None, alias="FlowLogIds")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeFlowLogsResult(_EC2ModelBase):
    flow_logs: FlowLogSet = pydantic.Field(None, alias="FlowLogs")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeFpgaImageAttributeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    fpga_image_id: FpgaImageId = pydantic.Field(None, alias="FpgaImageId")
    attribute: FpgaImageAttributeName = pydantic.Field(None, alias="Attribute")

class DescribeFpgaImageAttributeResult(_EC2ModelBase):
    fpga_image_attribute: 'FpgaImageAttribute' = pydantic.Field(None, alias="FpgaImageAttribute")

class DescribeFpgaImagesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    fpga_image_ids: FpgaImageIdList = pydantic.Field(None, alias="FpgaImageIds")
    owners: OwnerStringList = pydantic.Field(None, alias="Owners")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: DescribeFpgaImagesMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeFpgaImagesResult(_EC2ModelBase):
    fpga_images: FpgaImageList = pydantic.Field(None, alias="FpgaImages")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeHostReservationOfferingsRequest(_EC2ModelBase):
    filter: FilterList = pydantic.Field(None, alias="Filter")
    max_duration: Integer = pydantic.Field(None, alias="MaxDuration")
    max_results: DescribeHostReservationsMaxResults = pydantic.Field(None, alias="MaxResults")
    min_duration: Integer = pydantic.Field(None, alias="MinDuration")
    next_token: String = pydantic.Field(None, alias="NextToken")
    offering_id: OfferingId = pydantic.Field(None, alias="OfferingId")

class DescribeHostReservationOfferingsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    offering_set: HostOfferingSet = pydantic.Field(None, alias="OfferingSet")

class DescribeHostReservationsRequest(_EC2ModelBase):
    filter: FilterList = pydantic.Field(None, alias="Filter")
    host_reservation_id_set: HostReservationIdSet = pydantic.Field(None, alias="HostReservationIdSet")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeHostReservationsResult(_EC2ModelBase):
    host_reservation_set: HostReservationSet = pydantic.Field(None, alias="HostReservationSet")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeHostsRequest(_EC2ModelBase):
    filter: FilterList = pydantic.Field(None, alias="Filter")
    host_ids: RequestHostIdList = pydantic.Field(None, alias="HostIds")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeHostsResult(_EC2ModelBase):
    hosts: HostList = pydantic.Field(None, alias="Hosts")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeIamInstanceProfileAssociationsRequest(_EC2ModelBase):
    association_ids: AssociationIdList = pydantic.Field(None, alias="AssociationIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeIamInstanceProfileAssociationsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeIamInstanceProfileAssociationsResult(_EC2ModelBase):
    iam_instance_profile_associations: IamInstanceProfileAssociationSet = pydantic.Field(None, alias="IamInstanceProfileAssociations")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeIdFormatRequest(_EC2ModelBase):
    resource: String = pydantic.Field(None, alias="Resource")

class DescribeIdFormatResult(_EC2ModelBase):
    statuses: IdFormatList = pydantic.Field(None, alias="Statuses")

class DescribeIdentityIdFormatRequest(_EC2ModelBase):
    principal_arn: String = pydantic.Field(None, alias="PrincipalArn")
    resource: String = pydantic.Field(None, alias="Resource")

class DescribeIdentityIdFormatResult(_EC2ModelBase):
    statuses: IdFormatList = pydantic.Field(None, alias="Statuses")

class DescribeImageAttributeRequest(_EC2ModelBase):
    attribute: ImageAttributeName = pydantic.Field(None, alias="Attribute")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeImagesRequest(_EC2ModelBase):
    executable_users: ExecutableByStringList = pydantic.Field(None, alias="ExecutableUsers")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    image_ids: ImageIdStringList = pydantic.Field(None, alias="ImageIds")
    owners: OwnerStringList = pydantic.Field(None, alias="Owners")
    include_deprecated: Boolean = pydantic.Field(None, alias="IncludeDeprecated")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeImagesResult(_EC2ModelBase):
    images: ImageList = pydantic.Field(None, alias="Images")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeImportImageTasksRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    import_task_ids: ImportTaskIdList = pydantic.Field(None, alias="ImportTaskIds")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeImportImageTasksResult(_EC2ModelBase):
    import_image_tasks: ImportImageTaskList = pydantic.Field(None, alias="ImportImageTasks")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeImportSnapshotTasksRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    import_task_ids: ImportSnapshotTaskIdList = pydantic.Field(None, alias="ImportTaskIds")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeImportSnapshotTasksResult(_EC2ModelBase):
    import_snapshot_tasks: ImportSnapshotTaskList = pydantic.Field(None, alias="ImportSnapshotTasks")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstanceAttributeRequest(_EC2ModelBase):
    attribute: InstanceAttributeName = pydantic.Field(None, alias="Attribute")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")

class DescribeInstanceCreditSpecificationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    max_results: DescribeInstanceCreditSpecificationsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstanceCreditSpecificationsResult(_EC2ModelBase):
    instance_credit_specifications: InstanceCreditSpecificationList = pydantic.Field(None, alias="InstanceCreditSpecifications")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstanceEventNotificationAttributesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeInstanceEventNotificationAttributesResult(_EC2ModelBase):
    instance_tag_attribute: 'InstanceTagNotificationAttribute' = pydantic.Field(None, alias="InstanceTagAttribute")

class DescribeInstanceEventWindowsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_event_window_ids: InstanceEventWindowIdSet = pydantic.Field(None, alias="InstanceEventWindowIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: ResultRange = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstanceEventWindowsResult(_EC2ModelBase):
    instance_event_windows: InstanceEventWindowSet = pydantic.Field(None, alias="InstanceEventWindows")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstanceStatusRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    include_all_instances: Boolean = pydantic.Field(None, alias="IncludeAllInstances")

class DescribeInstanceStatusResult(_EC2ModelBase):
    instance_statuses: InstanceStatusList = pydantic.Field(None, alias="InstanceStatuses")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstanceTypeOfferingsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    location_type: LocationType = pydantic.Field(None, alias="LocationType")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DITOMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeInstanceTypeOfferingsResult(_EC2ModelBase):
    instance_type_offerings: InstanceTypeOfferingsList = pydantic.Field(None, alias="InstanceTypeOfferings")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeInstanceTypesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_types: RequestInstanceTypeList = pydantic.Field(None, alias="InstanceTypes")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DITMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeInstanceTypesResult(_EC2ModelBase):
    instance_types: InstanceTypeInfoList = pydantic.Field(None, alias="InstanceTypes")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeInstancesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInstancesResult(_EC2ModelBase):
    reservations: ReservationList = pydantic.Field(None, alias="Reservations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeInternetGatewaysRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    internet_gateway_ids: InternetGatewayIdList = pydantic.Field(None, alias="InternetGatewayIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeInternetGatewaysMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeInternetGatewaysResult(_EC2ModelBase):
    internet_gateways: InternetGatewayList = pydantic.Field(None, alias="InternetGateways")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeIpamPoolsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_pool_ids: ValueStringList = pydantic.Field(None, alias="IpamPoolIds")

class DescribeIpamPoolsResult(_EC2ModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_pools: IpamPoolSet = pydantic.Field(None, alias="IpamPools")

class DescribeIpamResourceDiscoveriesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_ids: ValueStringList = pydantic.Field(None, alias="IpamResourceDiscoveryIds")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeIpamResourceDiscoveriesResult(_EC2ModelBase):
    ipam_resource_discoveries: IpamResourceDiscoverySet = pydantic.Field(None, alias="IpamResourceDiscoveries")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeIpamResourceDiscoveryAssociationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_association_ids: ValueStringList = pydantic.Field(None, alias="IpamResourceDiscoveryAssociationIds")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeIpamResourceDiscoveryAssociationsResult(_EC2ModelBase):
    ipam_resource_discovery_associations: IpamResourceDiscoveryAssociationSet = pydantic.Field(None, alias="IpamResourceDiscoveryAssociations")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeIpamScopesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_scope_ids: ValueStringList = pydantic.Field(None, alias="IpamScopeIds")

class DescribeIpamScopesResult(_EC2ModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_scopes: IpamScopeSet = pydantic.Field(None, alias="IpamScopes")

class DescribeIpamsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_ids: ValueStringList = pydantic.Field(None, alias="IpamIds")

class DescribeIpamsResult(_EC2ModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipams: IpamSet = pydantic.Field(None, alias="Ipams")

class DescribeIpv6PoolsRequest(_EC2ModelBase):
    pool_ids: Ipv6PoolIdList = pydantic.Field(None, alias="PoolIds")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: Ipv6PoolMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribeIpv6PoolsResult(_EC2ModelBase):
    ipv_6_pools: Ipv6PoolSet = pydantic.Field(None, alias="Ipv6Pools")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeKeyPairsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    key_names: KeyNameStringList = pydantic.Field(None, alias="KeyNames")
    key_pair_ids: KeyPairIdStringList = pydantic.Field(None, alias="KeyPairIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    include_public_key: Boolean = pydantic.Field(None, alias="IncludePublicKey")

class DescribeKeyPairsResult(_EC2ModelBase):
    key_pairs: KeyPairList = pydantic.Field(None, alias="KeyPairs")

class DescribeLaunchTemplateVersionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    versions: VersionStringList = pydantic.Field(None, alias="Versions")
    min_version: String = pydantic.Field(None, alias="MinVersion")
    max_version: String = pydantic.Field(None, alias="MaxVersion")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    resolve_alias: Boolean = pydantic.Field(None, alias="ResolveAlias")

class DescribeLaunchTemplateVersionsResult(_EC2ModelBase):
    launch_template_versions: LaunchTemplateVersionSet = pydantic.Field(None, alias="LaunchTemplateVersions")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLaunchTemplatesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    launch_template_ids: LaunchTemplateIdStringList = pydantic.Field(None, alias="LaunchTemplateIds")
    launch_template_names: LaunchTemplateNameStringList = pydantic.Field(None, alias="LaunchTemplateNames")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeLaunchTemplatesMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeLaunchTemplatesResult(_EC2ModelBase):
    launch_templates: LaunchTemplateSet = pydantic.Field(None, alias="LaunchTemplates")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest(_EC2ModelBase):
    local_gateway_route_table_virtual_interface_group_association_ids: LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet = pydantic.Field(None, alias="LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: LocalGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult(_EC2ModelBase):
    local_gateway_route_table_virtual_interface_group_associations: LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet = pydantic.Field(None, alias="LocalGatewayRouteTableVirtualInterfaceGroupAssociations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLocalGatewayRouteTableVpcAssociationsRequest(_EC2ModelBase):
    local_gateway_route_table_vpc_association_ids: LocalGatewayRouteTableVpcAssociationIdSet = pydantic.Field(None, alias="LocalGatewayRouteTableVpcAssociationIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: LocalGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeLocalGatewayRouteTableVpcAssociationsResult(_EC2ModelBase):
    local_gateway_route_table_vpc_associations: LocalGatewayRouteTableVpcAssociationSet = pydantic.Field(None, alias="LocalGatewayRouteTableVpcAssociations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLocalGatewayRouteTablesRequest(_EC2ModelBase):
    local_gateway_route_table_ids: LocalGatewayRouteTableIdSet = pydantic.Field(None, alias="LocalGatewayRouteTableIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: LocalGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeLocalGatewayRouteTablesResult(_EC2ModelBase):
    local_gateway_route_tables: LocalGatewayRouteTableSet = pydantic.Field(None, alias="LocalGatewayRouteTables")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLocalGatewayVirtualInterfaceGroupsRequest(_EC2ModelBase):
    local_gateway_virtual_interface_group_ids: LocalGatewayVirtualInterfaceGroupIdSet = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: LocalGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeLocalGatewayVirtualInterfaceGroupsResult(_EC2ModelBase):
    local_gateway_virtual_interface_groups: LocalGatewayVirtualInterfaceGroupSet = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroups")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLocalGatewayVirtualInterfacesRequest(_EC2ModelBase):
    local_gateway_virtual_interface_ids: LocalGatewayVirtualInterfaceIdSet = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: LocalGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeLocalGatewayVirtualInterfacesResult(_EC2ModelBase):
    local_gateway_virtual_interfaces: LocalGatewayVirtualInterfaceSet = pydantic.Field(None, alias="LocalGatewayVirtualInterfaces")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeLocalGatewaysRequest(_EC2ModelBase):
    local_gateway_ids: LocalGatewayIdSet = pydantic.Field(None, alias="LocalGatewayIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: LocalGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeLocalGatewaysResult(_EC2ModelBase):
    local_gateways: LocalGatewaySet = pydantic.Field(None, alias="LocalGateways")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeManagedPrefixListsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: PrefixListMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    prefix_list_ids: ValueStringList = pydantic.Field(None, alias="PrefixListIds")

class DescribeManagedPrefixListsResult(_EC2ModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    prefix_lists: ManagedPrefixListSet = pydantic.Field(None, alias="PrefixLists")

class DescribeMovingAddressesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: DescribeMovingAddressesMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    public_ips: ValueStringList = pydantic.Field(None, alias="PublicIps")

class DescribeMovingAddressesResult(_EC2ModelBase):
    moving_address_statuses: MovingAddressStatusSet = pydantic.Field(None, alias="MovingAddressStatuses")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNatGatewaysRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filter: FilterList = pydantic.Field(None, alias="Filter")
    max_results: DescribeNatGatewaysMaxResults = pydantic.Field(None, alias="MaxResults")
    nat_gateway_ids: NatGatewayIdStringList = pydantic.Field(None, alias="NatGatewayIds")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNatGatewaysResult(_EC2ModelBase):
    nat_gateways: NatGatewayList = pydantic.Field(None, alias="NatGateways")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkAclsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_acl_ids: NetworkAclIdStringList = pydantic.Field(None, alias="NetworkAclIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeNetworkAclsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeNetworkAclsResult(_EC2ModelBase):
    network_acls: NetworkAclList = pydantic.Field(None, alias="NetworkAcls")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsAccessScopeAnalysesRequest(_EC2ModelBase):
    network_insights_access_scope_analysis_ids: NetworkInsightsAccessScopeAnalysisIdList = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisIds")
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    analysis_start_time_begin: MillisecondDateTime = pydantic.Field(None, alias="AnalysisStartTimeBegin")
    analysis_start_time_end: MillisecondDateTime = pydantic.Field(None, alias="AnalysisStartTimeEnd")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: NetworkInsightsMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsAccessScopeAnalysesResult(_EC2ModelBase):
    network_insights_access_scope_analyses: NetworkInsightsAccessScopeAnalysisList = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalyses")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsAccessScopesRequest(_EC2ModelBase):
    network_insights_access_scope_ids: NetworkInsightsAccessScopeIdList = pydantic.Field(None, alias="NetworkInsightsAccessScopeIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: NetworkInsightsMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsAccessScopesResult(_EC2ModelBase):
    network_insights_access_scopes: NetworkInsightsAccessScopeList = pydantic.Field(None, alias="NetworkInsightsAccessScopes")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsAnalysesRequest(_EC2ModelBase):
    network_insights_analysis_ids: NetworkInsightsAnalysisIdList = pydantic.Field(None, alias="NetworkInsightsAnalysisIds")
    network_insights_path_id: NetworkInsightsPathId = pydantic.Field(None, alias="NetworkInsightsPathId")
    analysis_start_time: MillisecondDateTime = pydantic.Field(None, alias="AnalysisStartTime")
    analysis_end_time: MillisecondDateTime = pydantic.Field(None, alias="AnalysisEndTime")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: NetworkInsightsMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsAnalysesResult(_EC2ModelBase):
    network_insights_analyses: NetworkInsightsAnalysisList = pydantic.Field(None, alias="NetworkInsightsAnalyses")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsPathsRequest(_EC2ModelBase):
    network_insights_path_ids: NetworkInsightsPathIdList = pydantic.Field(None, alias="NetworkInsightsPathIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: NetworkInsightsMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInsightsPathsResult(_EC2ModelBase):
    network_insights_paths: NetworkInsightsPathList = pydantic.Field(None, alias="NetworkInsightsPaths")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInterfaceAttributeRequest(_EC2ModelBase):
    attribute: NetworkInterfaceAttribute = pydantic.Field(None, alias="Attribute")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")

class DescribeNetworkInterfaceAttributeResult(_EC2ModelBase):
    attachment: 'NetworkInterfaceAttachment' = pydantic.Field(None, alias="Attachment")
    description: 'AttributeValue' = pydantic.Field(None, alias="Description")
    groups: GroupIdentifierList = pydantic.Field(None, alias="Groups")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    source_dest_check: 'AttributeBooleanValue' = pydantic.Field(None, alias="SourceDestCheck")

class DescribeNetworkInterfacePermissionsRequest(_EC2ModelBase):
    network_interface_permission_ids: NetworkInterfacePermissionIdList = pydantic.Field(None, alias="NetworkInterfacePermissionIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeNetworkInterfacePermissionsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeNetworkInterfacePermissionsResult(_EC2ModelBase):
    network_interface_permissions: NetworkInterfacePermissionList = pydantic.Field(None, alias="NetworkInterfacePermissions")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeNetworkInterfacesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_interface_ids: NetworkInterfaceIdList = pydantic.Field(None, alias="NetworkInterfaceIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeNetworkInterfacesMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeNetworkInterfacesResult(_EC2ModelBase):
    network_interfaces: NetworkInterfaceList = pydantic.Field(None, alias="NetworkInterfaces")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribePlacementGroupsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_names: PlacementGroupStringList = pydantic.Field(None, alias="GroupNames")
    group_ids: PlacementGroupIdStringList = pydantic.Field(None, alias="GroupIds")

class DescribePlacementGroupsResult(_EC2ModelBase):
    placement_groups: PlacementGroupList = pydantic.Field(None, alias="PlacementGroups")

class DescribePrefixListsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    prefix_list_ids: PrefixListResourceIdStringList = pydantic.Field(None, alias="PrefixListIds")

class DescribePrefixListsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    prefix_lists: PrefixListSet = pydantic.Field(None, alias="PrefixLists")

class DescribePrincipalIdFormatRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    resources: ResourceList = pydantic.Field(None, alias="Resources")
    max_results: DescribePrincipalIdFormatMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribePrincipalIdFormatResult(_EC2ModelBase):
    principals: PrincipalIdFormatList = pydantic.Field(None, alias="Principals")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribePublicIpv4PoolsRequest(_EC2ModelBase):
    pool_ids: PublicIpv4PoolIdStringList = pydantic.Field(None, alias="PoolIds")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: PoolMaxResults = pydantic.Field(None, alias="MaxResults")
    filters: FilterList = pydantic.Field(None, alias="Filters")

class DescribePublicIpv4PoolsResult(_EC2ModelBase):
    public_ipv_4_pools: PublicIpv4PoolSet = pydantic.Field(None, alias="PublicIpv4Pools")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeRegionsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    region_names: RegionNameStringList = pydantic.Field(None, alias="RegionNames")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    all_regions: Boolean = pydantic.Field(None, alias="AllRegions")

class DescribeRegionsResult(_EC2ModelBase):
    regions: RegionList = pydantic.Field(None, alias="Regions")

class DescribeReplaceRootVolumeTasksRequest(_EC2ModelBase):
    replace_root_volume_task_ids: ReplaceRootVolumeTaskIds = pydantic.Field(None, alias="ReplaceRootVolumeTaskIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: DescribeReplaceRootVolumeTasksMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeReplaceRootVolumeTasksResult(_EC2ModelBase):
    replace_root_volume_tasks: ReplaceRootVolumeTasks = pydantic.Field(None, alias="ReplaceRootVolumeTasks")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeReservedInstancesListingsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    reserved_instances_id: ReservationId = pydantic.Field(None, alias="ReservedInstancesId")
    reserved_instances_listing_id: ReservedInstancesListingId = pydantic.Field(None, alias="ReservedInstancesListingId")

class DescribeReservedInstancesListingsResult(_EC2ModelBase):
    reserved_instances_listings: ReservedInstancesListingList = pydantic.Field(None, alias="ReservedInstancesListings")

class DescribeReservedInstancesModificationsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    reserved_instances_modification_ids: ReservedInstancesModificationIdStringList = pydantic.Field(None, alias="ReservedInstancesModificationIds")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeReservedInstancesModificationsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    reserved_instances_modifications: ReservedInstancesModificationList = pydantic.Field(None, alias="ReservedInstancesModifications")

class DescribeReservedInstancesOfferingsRequest(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    include_marketplace: Boolean = pydantic.Field(None, alias="IncludeMarketplace")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    max_duration: Long = pydantic.Field(None, alias="MaxDuration")
    max_instance_count: Integer = pydantic.Field(None, alias="MaxInstanceCount")
    min_duration: Long = pydantic.Field(None, alias="MinDuration")
    offering_class: OfferingClassType = pydantic.Field(None, alias="OfferingClass")
    product_description: RIProductDescription = pydantic.Field(None, alias="ProductDescription")
    reserved_instances_offering_ids: ReservedInstancesOfferingIdStringList = pydantic.Field(None, alias="ReservedInstancesOfferingIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_tenancy: Tenancy = pydantic.Field(None, alias="InstanceTenancy")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    offering_type: OfferingTypeValues = pydantic.Field(None, alias="OfferingType")

class DescribeReservedInstancesOfferingsResult(_EC2ModelBase):
    reserved_instances_offerings: ReservedInstancesOfferingList = pydantic.Field(None, alias="ReservedInstancesOfferings")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeReservedInstancesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    offering_class: OfferingClassType = pydantic.Field(None, alias="OfferingClass")
    reserved_instances_ids: ReservedInstancesIdStringList = pydantic.Field(None, alias="ReservedInstancesIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    offering_type: OfferingTypeValues = pydantic.Field(None, alias="OfferingType")

class DescribeReservedInstancesResult(_EC2ModelBase):
    reserved_instances: ReservedInstancesList = pydantic.Field(None, alias="ReservedInstances")

class DescribeRouteTablesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    route_table_ids: RouteTableIdStringList = pydantic.Field(None, alias="RouteTableIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeRouteTablesMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeRouteTablesResult(_EC2ModelBase):
    route_tables: RouteTableList = pydantic.Field(None, alias="RouteTables")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeScheduledInstanceAvailabilityRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    first_slot_start_time_range: 'SlotDateTimeRangeRequest' = pydantic.Field(None, alias="FirstSlotStartTimeRange")
    max_results: DescribeScheduledInstanceAvailabilityMaxResults = pydantic.Field(None, alias="MaxResults")
    max_slot_duration_in_hours: Integer = pydantic.Field(None, alias="MaxSlotDurationInHours")
    min_slot_duration_in_hours: Integer = pydantic.Field(None, alias="MinSlotDurationInHours")
    next_token: String = pydantic.Field(None, alias="NextToken")
    recurrence: 'ScheduledInstanceRecurrenceRequest' = pydantic.Field(None, alias="Recurrence")

class DescribeScheduledInstanceAvailabilityResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    scheduled_instance_availability_set: ScheduledInstanceAvailabilitySet = pydantic.Field(None, alias="ScheduledInstanceAvailabilitySet")

class DescribeScheduledInstancesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    scheduled_instance_ids: ScheduledInstanceIdRequestSet = pydantic.Field(None, alias="ScheduledInstanceIds")
    slot_start_time_range: 'SlotStartTimeRangeRequest' = pydantic.Field(None, alias="SlotStartTimeRange")

class DescribeScheduledInstancesResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    scheduled_instance_set: ScheduledInstanceSet = pydantic.Field(None, alias="ScheduledInstanceSet")

class DescribeSecurityGroupReferencesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_id: GroupIds = pydantic.Field(None, alias="GroupId")

class DescribeSecurityGroupReferencesResult(_EC2ModelBase):
    security_group_reference_set: SecurityGroupReferences = pydantic.Field(None, alias="SecurityGroupReferenceSet")

class DescribeSecurityGroupRulesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    security_group_rule_ids: SecurityGroupRuleIdList = pydantic.Field(None, alias="SecurityGroupRuleIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeSecurityGroupRulesMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeSecurityGroupRulesResult(_EC2ModelBase):
    security_group_rules: SecurityGroupRuleList = pydantic.Field(None, alias="SecurityGroupRules")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeSecurityGroupsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    group_ids: GroupIdStringList = pydantic.Field(None, alias="GroupIds")
    group_names: GroupNameStringList = pydantic.Field(None, alias="GroupNames")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeSecurityGroupsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeSecurityGroupsResult(_EC2ModelBase):
    security_groups: SecurityGroupList = pydantic.Field(None, alias="SecurityGroups")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeSnapshotAttributeRequest(_EC2ModelBase):
    attribute: SnapshotAttributeName = pydantic.Field(None, alias="Attribute")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeSnapshotAttributeResult(_EC2ModelBase):
    create_volume_permissions: CreateVolumePermissionList = pydantic.Field(None, alias="CreateVolumePermissions")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")

class DescribeSnapshotTierStatusRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeSnapshotTierStatusMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeSnapshotTierStatusResult(_EC2ModelBase):
    snapshot_tier_statuses: snapshotTierStatusSet = pydantic.Field(None, alias="SnapshotTierStatuses")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeSnapshotsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    owner_ids: OwnerStringList = pydantic.Field(None, alias="OwnerIds")
    restorable_by_user_ids: RestorableByStringList = pydantic.Field(None, alias="RestorableByUserIds")
    snapshot_ids: SnapshotIdStringList = pydantic.Field(None, alias="SnapshotIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeSnapshotsResult(_EC2ModelBase):
    snapshots: SnapshotList = pydantic.Field(None, alias="Snapshots")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeSpotDatafeedSubscriptionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeSpotDatafeedSubscriptionResult(_EC2ModelBase):
    spot_datafeed_subscription: 'SpotDatafeedSubscription' = pydantic.Field(None, alias="SpotDatafeedSubscription")

class DescribeSpotFleetInstancesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: DescribeSpotFleetInstancesMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_fleet_request_id: SpotFleetRequestId = pydantic.Field(None, alias="SpotFleetRequestId")

class DescribeSpotFleetInstancesResponse(_EC2ModelBase):
    active_instances: ActiveInstanceSet = pydantic.Field(None, alias="ActiveInstances")
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_fleet_request_id: String = pydantic.Field(None, alias="SpotFleetRequestId")

class DescribeSpotFleetRequestHistoryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    event_type: EventType = pydantic.Field(None, alias="EventType")
    max_results: DescribeSpotFleetRequestHistoryMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_fleet_request_id: SpotFleetRequestId = pydantic.Field(None, alias="SpotFleetRequestId")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")

class DescribeSpotFleetRequestHistoryResponse(_EC2ModelBase):
    history_records: HistoryRecords = pydantic.Field(None, alias="HistoryRecords")
    last_evaluated_time: DateTime = pydantic.Field(None, alias="LastEvaluatedTime")
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_fleet_request_id: String = pydantic.Field(None, alias="SpotFleetRequestId")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")

class DescribeSpotFleetRequestsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_fleet_request_ids: SpotFleetRequestIdList = pydantic.Field(None, alias="SpotFleetRequestIds")

class DescribeSpotFleetRequestsResponse(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_fleet_request_configs: SpotFleetRequestConfigSet = pydantic.Field(None, alias="SpotFleetRequestConfigs")

class DescribeSpotInstanceRequestsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    spot_instance_request_ids: SpotInstanceRequestIdList = pydantic.Field(None, alias="SpotInstanceRequestIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")

class DescribeSpotInstanceRequestsResult(_EC2ModelBase):
    spot_instance_requests: SpotInstanceRequestList = pydantic.Field(None, alias="SpotInstanceRequests")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeSpotPriceHistoryRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    end_time: DateTime = pydantic.Field(None, alias="EndTime")
    instance_types: InstanceTypeList = pydantic.Field(None, alias="InstanceTypes")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    product_descriptions: ProductDescriptionList = pydantic.Field(None, alias="ProductDescriptions")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")

class DescribeSpotPriceHistoryResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    spot_price_history: SpotPriceHistoryList = pydantic.Field(None, alias="SpotPriceHistory")

class DescribeStaleSecurityGroupsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: DescribeStaleSecurityGroupsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: DescribeStaleSecurityGroupsNextToken = pydantic.Field(None, alias="NextToken")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class DescribeStaleSecurityGroupsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    stale_security_group_set: StaleSecurityGroupSet = pydantic.Field(None, alias="StaleSecurityGroupSet")

class DescribeStoreImageTasksRequest(_EC2ModelBase):
    image_ids: ImageIdList = pydantic.Field(None, alias="ImageIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeStoreImageTasksRequestMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeStoreImageTasksResult(_EC2ModelBase):
    store_image_task_results: StoreImageTaskResultSet = pydantic.Field(None, alias="StoreImageTaskResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeSubnetsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    subnet_ids: SubnetIdStringList = pydantic.Field(None, alias="SubnetIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeSubnetsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeSubnetsResult(_EC2ModelBase):
    subnets: SubnetList = pydantic.Field(None, alias="Subnets")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTagsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTagsResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    tags: TagDescriptionList = pydantic.Field(None, alias="Tags")

class DescribeTrafficMirrorFiltersRequest(_EC2ModelBase):
    traffic_mirror_filter_ids: TrafficMirrorFilterIdList = pydantic.Field(None, alias="TrafficMirrorFilterIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TrafficMirroringMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeTrafficMirrorFiltersResult(_EC2ModelBase):
    traffic_mirror_filters: TrafficMirrorFilterSet = pydantic.Field(None, alias="TrafficMirrorFilters")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTrafficMirrorSessionsRequest(_EC2ModelBase):
    traffic_mirror_session_ids: TrafficMirrorSessionIdList = pydantic.Field(None, alias="TrafficMirrorSessionIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TrafficMirroringMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeTrafficMirrorSessionsResult(_EC2ModelBase):
    traffic_mirror_sessions: TrafficMirrorSessionSet = pydantic.Field(None, alias="TrafficMirrorSessions")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTrafficMirrorTargetsRequest(_EC2ModelBase):
    traffic_mirror_target_ids: TrafficMirrorTargetIdList = pydantic.Field(None, alias="TrafficMirrorTargetIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TrafficMirroringMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeTrafficMirrorTargetsResult(_EC2ModelBase):
    traffic_mirror_targets: TrafficMirrorTargetSet = pydantic.Field(None, alias="TrafficMirrorTargets")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayAttachmentsRequest(_EC2ModelBase):
    transit_gateway_attachment_ids: TransitGatewayAttachmentIdStringList = pydantic.Field(None, alias="TransitGatewayAttachmentIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayAttachmentsResult(_EC2ModelBase):
    transit_gateway_attachments: TransitGatewayAttachmentList = pydantic.Field(None, alias="TransitGatewayAttachments")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayConnectPeersRequest(_EC2ModelBase):
    transit_gateway_connect_peer_ids: TransitGatewayConnectPeerIdStringList = pydantic.Field(None, alias="TransitGatewayConnectPeerIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayConnectPeersResult(_EC2ModelBase):
    transit_gateway_connect_peers: TransitGatewayConnectPeerList = pydantic.Field(None, alias="TransitGatewayConnectPeers")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayConnectsRequest(_EC2ModelBase):
    transit_gateway_attachment_ids: TransitGatewayAttachmentIdStringList = pydantic.Field(None, alias="TransitGatewayAttachmentIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayConnectsResult(_EC2ModelBase):
    transit_gateway_connects: TransitGatewayConnectList = pydantic.Field(None, alias="TransitGatewayConnects")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayMulticastDomainsRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_ids: TransitGatewayMulticastDomainIdStringList = pydantic.Field(None, alias="TransitGatewayMulticastDomainIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayMulticastDomainsResult(_EC2ModelBase):
    transit_gateway_multicast_domains: TransitGatewayMulticastDomainList = pydantic.Field(None, alias="TransitGatewayMulticastDomains")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayPeeringAttachmentsRequest(_EC2ModelBase):
    transit_gateway_attachment_ids: TransitGatewayAttachmentIdStringList = pydantic.Field(None, alias="TransitGatewayAttachmentIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayPeeringAttachmentsResult(_EC2ModelBase):
    transit_gateway_peering_attachments: TransitGatewayPeeringAttachmentList = pydantic.Field(None, alias="TransitGatewayPeeringAttachments")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayPolicyTablesRequest(_EC2ModelBase):
    transit_gateway_policy_table_ids: TransitGatewayPolicyTableIdStringList = pydantic.Field(None, alias="TransitGatewayPolicyTableIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayPolicyTablesResult(_EC2ModelBase):
    transit_gateway_policy_tables: TransitGatewayPolicyTableList = pydantic.Field(None, alias="TransitGatewayPolicyTables")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayRouteTableAnnouncementsRequest(_EC2ModelBase):
    transit_gateway_route_table_announcement_ids: TransitGatewayRouteTableAnnouncementIdStringList = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayRouteTableAnnouncementsResult(_EC2ModelBase):
    transit_gateway_route_table_announcements: TransitGatewayRouteTableAnnouncementList = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncements")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayRouteTablesRequest(_EC2ModelBase):
    transit_gateway_route_table_ids: TransitGatewayRouteTableIdStringList = pydantic.Field(None, alias="TransitGatewayRouteTableIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayRouteTablesResult(_EC2ModelBase):
    transit_gateway_route_tables: TransitGatewayRouteTableList = pydantic.Field(None, alias="TransitGatewayRouteTables")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewayVpcAttachmentsRequest(_EC2ModelBase):
    transit_gateway_attachment_ids: TransitGatewayAttachmentIdStringList = pydantic.Field(None, alias="TransitGatewayAttachmentIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewayVpcAttachmentsResult(_EC2ModelBase):
    transit_gateway_vpc_attachments: TransitGatewayVpcAttachmentList = pydantic.Field(None, alias="TransitGatewayVpcAttachments")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTransitGatewaysRequest(_EC2ModelBase):
    transit_gateway_ids: TransitGatewayIdStringList = pydantic.Field(None, alias="TransitGatewayIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeTransitGatewaysResult(_EC2ModelBase):
    transit_gateways: TransitGatewayList = pydantic.Field(None, alias="TransitGateways")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeTrunkInterfaceAssociationsRequest(_EC2ModelBase):
    association_ids: TrunkInterfaceAssociationIdList = pydantic.Field(None, alias="AssociationIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeTrunkInterfaceAssociationsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeTrunkInterfaceAssociationsResult(_EC2ModelBase):
    interface_associations: TrunkInterfaceAssociationList = pydantic.Field(None, alias="InterfaceAssociations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVerifiedAccessEndpointsRequest(_EC2ModelBase):
    verified_access_endpoint_ids: VerifiedAccessEndpointIdList = pydantic.Field(None, alias="VerifiedAccessEndpointIds")
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    max_results: DescribeVerifiedAccessEndpointsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVerifiedAccessEndpointsResult(_EC2ModelBase):
    verified_access_endpoints: VerifiedAccessEndpointList = pydantic.Field(None, alias="VerifiedAccessEndpoints")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeVerifiedAccessGroupsRequest(_EC2ModelBase):
    verified_access_group_ids: VerifiedAccessGroupIdList = pydantic.Field(None, alias="VerifiedAccessGroupIds")
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    max_results: DescribeVerifiedAccessGroupMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVerifiedAccessGroupsResult(_EC2ModelBase):
    verified_access_groups: VerifiedAccessGroupList = pydantic.Field(None, alias="VerifiedAccessGroups")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeVerifiedAccessInstanceLoggingConfigurationsRequest(_EC2ModelBase):
    verified_access_instance_ids: VerifiedAccessInstanceIdList = pydantic.Field(None, alias="VerifiedAccessInstanceIds")
    max_results: DescribeVerifiedAccessInstanceLoggingConfigurationsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVerifiedAccessInstanceLoggingConfigurationsResult(_EC2ModelBase):
    logging_configurations: VerifiedAccessInstanceLoggingConfigurationList = pydantic.Field(None, alias="LoggingConfigurations")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeVerifiedAccessInstancesRequest(_EC2ModelBase):
    verified_access_instance_ids: VerifiedAccessInstanceIdList = pydantic.Field(None, alias="VerifiedAccessInstanceIds")
    max_results: DescribeVerifiedAccessInstancesMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVerifiedAccessInstancesResult(_EC2ModelBase):
    verified_access_instances: VerifiedAccessInstanceList = pydantic.Field(None, alias="VerifiedAccessInstances")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeVerifiedAccessTrustProvidersRequest(_EC2ModelBase):
    verified_access_trust_provider_ids: VerifiedAccessTrustProviderIdList = pydantic.Field(None, alias="VerifiedAccessTrustProviderIds")
    max_results: DescribeVerifiedAccessTrustProvidersMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVerifiedAccessTrustProvidersResult(_EC2ModelBase):
    verified_access_trust_providers: VerifiedAccessTrustProviderList = pydantic.Field(None, alias="VerifiedAccessTrustProviders")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class DescribeVolumeAttributeRequest(_EC2ModelBase):
    attribute: VolumeAttributeName = pydantic.Field(None, alias="Attribute")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVolumeAttributeResult(_EC2ModelBase):
    auto_enable_io: 'AttributeBooleanValue' = pydantic.Field(None, alias="AutoEnableIO")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    volume_id: String = pydantic.Field(None, alias="VolumeId")

class DescribeVolumeStatusRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    volume_ids: VolumeIdStringList = pydantic.Field(None, alias="VolumeIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVolumeStatusResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    volume_statuses: VolumeStatusList = pydantic.Field(None, alias="VolumeStatuses")

class DescribeVolumesModificationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    volume_ids: VolumeIdStringList = pydantic.Field(None, alias="VolumeIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")

class DescribeVolumesModificationsResult(_EC2ModelBase):
    volumes_modifications: VolumeModificationList = pydantic.Field(None, alias="VolumesModifications")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVolumesRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    volume_ids: VolumeIdStringList = pydantic.Field(None, alias="VolumeIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVolumesResult(_EC2ModelBase):
    volumes: VolumeList = pydantic.Field(None, alias="Volumes")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcAttributeRequest(_EC2ModelBase):
    attribute: VpcAttributeName = pydantic.Field(None, alias="Attribute")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVpcAttributeResult(_EC2ModelBase):
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    enable_dns_hostnames: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableDnsHostnames")
    enable_dns_support: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableDnsSupport")
    enable_network_address_usage_metrics: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableNetworkAddressUsageMetrics")

class DescribeVpcClassicLinkDnsSupportRequest(_EC2ModelBase):
    max_results: DescribeVpcClassicLinkDnsSupportMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: DescribeVpcClassicLinkDnsSupportNextToken = pydantic.Field(None, alias="NextToken")
    vpc_ids: VpcClassicLinkIdList = pydantic.Field(None, alias="VpcIds")

class DescribeVpcClassicLinkDnsSupportResult(_EC2ModelBase):
    next_token: DescribeVpcClassicLinkDnsSupportNextToken = pydantic.Field(None, alias="NextToken")
    vpcs: ClassicLinkDnsSupportList = pydantic.Field(None, alias="Vpcs")

class DescribeVpcClassicLinkRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_ids: VpcClassicLinkIdList = pydantic.Field(None, alias="VpcIds")

class DescribeVpcClassicLinkResult(_EC2ModelBase):
    vpcs: VpcClassicLinkList = pydantic.Field(None, alias="Vpcs")

class DescribeVpcEndpointConnectionNotificationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    connection_notification_id: ConnectionNotificationId = pydantic.Field(None, alias="ConnectionNotificationId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointConnectionNotificationsResult(_EC2ModelBase):
    connection_notification_set: ConnectionNotificationSet = pydantic.Field(None, alias="ConnectionNotificationSet")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointConnectionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointConnectionsResult(_EC2ModelBase):
    vpc_endpoint_connections: VpcEndpointConnectionSet = pydantic.Field(None, alias="VpcEndpointConnections")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointServiceConfigurationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_ids: VpcEndpointServiceIdList = pydantic.Field(None, alias="ServiceIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointServiceConfigurationsResult(_EC2ModelBase):
    service_configurations: ServiceConfigurationSet = pydantic.Field(None, alias="ServiceConfigurations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointServicePermissionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointServicePermissionsResult(_EC2ModelBase):
    allowed_principals: AllowedPrincipalSet = pydantic.Field(None, alias="AllowedPrincipals")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointServicesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_names: ValueStringList = pydantic.Field(None, alias="ServiceNames")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointServicesResult(_EC2ModelBase):
    service_names: ValueStringList = pydantic.Field(None, alias="ServiceNames")
    service_details: ServiceDetailSet = pydantic.Field(None, alias="ServiceDetails")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_endpoint_ids: VpcEndpointIdList = pydantic.Field(None, alias="VpcEndpointIds")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcEndpointsResult(_EC2ModelBase):
    vpc_endpoints: VpcEndpointSet = pydantic.Field(None, alias="VpcEndpoints")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcPeeringConnectionsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_peering_connection_ids: VpcPeeringConnectionIdList = pydantic.Field(None, alias="VpcPeeringConnectionIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeVpcPeeringConnectionsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeVpcPeeringConnectionsResult(_EC2ModelBase):
    vpc_peering_connections: VpcPeeringConnectionList = pydantic.Field(None, alias="VpcPeeringConnections")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpcsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    vpc_ids: VpcIdStringList = pydantic.Field(None, alias="VpcIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: DescribeVpcsMaxResults = pydantic.Field(None, alias="MaxResults")

class DescribeVpcsResult(_EC2ModelBase):
    vpcs: VpcList = pydantic.Field(None, alias="Vpcs")
    next_token: String = pydantic.Field(None, alias="NextToken")

class DescribeVpnConnectionsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    vpn_connection_ids: VpnConnectionIdStringList = pydantic.Field(None, alias="VpnConnectionIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVpnConnectionsResult(_EC2ModelBase):
    vpn_connections: VpnConnectionList = pydantic.Field(None, alias="VpnConnections")

class DescribeVpnGatewaysRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    vpn_gateway_ids: VpnGatewayIdStringList = pydantic.Field(None, alias="VpnGatewayIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DescribeVpnGatewaysResult(_EC2ModelBase):
    vpn_gateways: VpnGatewayList = pydantic.Field(None, alias="VpnGateways")

class DestinationOptionsRequest(_EC2ModelBase):
    file_format: DestinationFileFormat = pydantic.Field(None, alias="FileFormat")
    hive_compatible_partitions: Boolean = pydantic.Field(None, alias="HiveCompatiblePartitions")
    per_hour_partition: Boolean = pydantic.Field(None, alias="PerHourPartition")

class DestinationOptionsResponse(_EC2ModelBase):
    file_format: DestinationFileFormat = pydantic.Field(None, alias="FileFormat")
    hive_compatible_partitions: Boolean = pydantic.Field(None, alias="HiveCompatiblePartitions")
    per_hour_partition: Boolean = pydantic.Field(None, alias="PerHourPartition")

class DetachClassicLinkVpcRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class DetachClassicLinkVpcResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DetachInternetGatewayRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    internet_gateway_id: InternetGatewayId = pydantic.Field(None, alias="InternetGatewayId")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class DetachNetworkInterfaceRequest(_EC2ModelBase):
    attachment_id: NetworkInterfaceAttachmentId = pydantic.Field(None, alias="AttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    force: Boolean = pydantic.Field(None, alias="Force")

class DetachVerifiedAccessTrustProviderRequest(_EC2ModelBase):
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    verified_access_trust_provider_id: VerifiedAccessTrustProviderId = pydantic.Field(None, alias="VerifiedAccessTrustProviderId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DetachVerifiedAccessTrustProviderResult(_EC2ModelBase):
    verified_access_trust_provider: 'VerifiedAccessTrustProvider' = pydantic.Field(None, alias="VerifiedAccessTrustProvider")
    verified_access_instance: 'VerifiedAccessInstance' = pydantic.Field(None, alias="VerifiedAccessInstance")

class DetachVolumeRequest(_EC2ModelBase):
    device: String = pydantic.Field(None, alias="Device")
    force: Boolean = pydantic.Field(None, alias="Force")
    instance_id: InstanceIdForResolver = pydantic.Field(None, alias="InstanceId")
    volume_id: VolumeIdWithResolver = pydantic.Field(None, alias="VolumeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DetachVpnGatewayRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    vpn_gateway_id: VpnGatewayId = pydantic.Field(None, alias="VpnGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DeviceOptions(_EC2ModelBase):
    tenant_id: String = pydantic.Field(None, alias="TenantId")

class DhcpConfiguration(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    values: DhcpConfigurationValueList = pydantic.Field(None, alias="Values")

class DhcpOptions(_EC2ModelBase):
    dhcp_configurations: DhcpConfigurationList = pydantic.Field(None, alias="DhcpConfigurations")
    dhcp_options_id: String = pydantic.Field(None, alias="DhcpOptionsId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class DirectoryServiceAuthentication(_EC2ModelBase):
    directory_id: String = pydantic.Field(None, alias="DirectoryId")

class DirectoryServiceAuthenticationRequest(_EC2ModelBase):
    directory_id: String = pydantic.Field(None, alias="DirectoryId")

class DisableAddressTransferRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableAddressTransferResult(_EC2ModelBase):
    address_transfer: 'AddressTransfer' = pydantic.Field(None, alias="AddressTransfer")

class DisableAwsNetworkPerformanceMetricSubscriptionRequest(_EC2ModelBase):
    source: String = pydantic.Field(None, alias="Source")
    destination: String = pydantic.Field(None, alias="Destination")
    metric: MetricType = pydantic.Field(None, alias="Metric")
    statistic: StatisticType = pydantic.Field(None, alias="Statistic")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableAwsNetworkPerformanceMetricSubscriptionResult(_EC2ModelBase):
    output: Boolean = pydantic.Field(None, alias="Output")

class DisableEbsEncryptionByDefaultRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableEbsEncryptionByDefaultResult(_EC2ModelBase):
    ebs_encryption_by_default: Boolean = pydantic.Field(None, alias="EbsEncryptionByDefault")

class DisableFastLaunchRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    force: Boolean = pydantic.Field(None, alias="Force")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableFastLaunchResult(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    resource_type: FastLaunchResourceType = pydantic.Field(None, alias="ResourceType")
    snapshot_configuration: 'FastLaunchSnapshotConfigurationResponse' = pydantic.Field(None, alias="SnapshotConfiguration")
    launch_template: 'FastLaunchLaunchTemplateSpecificationResponse' = pydantic.Field(None, alias="LaunchTemplate")
    max_parallel_launches: Integer = pydantic.Field(None, alias="MaxParallelLaunches")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: FastLaunchStateCode = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    state_transition_time: MillisecondDateTime = pydantic.Field(None, alias="StateTransitionTime")

class DisableFastSnapshotRestoreErrorItem(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    fast_snapshot_restore_state_errors: DisableFastSnapshotRestoreStateErrorSet = pydantic.Field(None, alias="FastSnapshotRestoreStateErrors")

class DisableFastSnapshotRestoreStateError(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class DisableFastSnapshotRestoreStateErrorItem(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    error: 'DisableFastSnapshotRestoreStateError' = pydantic.Field(None, alias="Error")

class DisableFastSnapshotRestoreSuccessItem(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    state: FastSnapshotRestoreStateCode = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    owner_alias: String = pydantic.Field(None, alias="OwnerAlias")
    enabling_time: MillisecondDateTime = pydantic.Field(None, alias="EnablingTime")
    optimizing_time: MillisecondDateTime = pydantic.Field(None, alias="OptimizingTime")
    enabled_time: MillisecondDateTime = pydantic.Field(None, alias="EnabledTime")
    disabling_time: MillisecondDateTime = pydantic.Field(None, alias="DisablingTime")
    disabled_time: MillisecondDateTime = pydantic.Field(None, alias="DisabledTime")

class DisableFastSnapshotRestoresRequest(_EC2ModelBase):
    availability_zones: AvailabilityZoneStringList = pydantic.Field(None, alias="AvailabilityZones")
    source_snapshot_ids: SnapshotIdStringList = pydantic.Field(None, alias="SourceSnapshotIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableFastSnapshotRestoresResult(_EC2ModelBase):
    successful: DisableFastSnapshotRestoreSuccessSet = pydantic.Field(None, alias="Successful")
    unsuccessful: DisableFastSnapshotRestoreErrorSet = pydantic.Field(None, alias="Unsuccessful")

class DisableImageDeprecationRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableImageDeprecationResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DisableIpamOrganizationAdminAccountRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    delegated_admin_account_id: String = pydantic.Field(None, alias="DelegatedAdminAccountId")

class DisableIpamOrganizationAdminAccountResult(_EC2ModelBase):
    success: Boolean = pydantic.Field(None, alias="Success")

class DisableSerialConsoleAccessRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableSerialConsoleAccessResult(_EC2ModelBase):
    serial_console_access_enabled: Boolean = pydantic.Field(None, alias="SerialConsoleAccessEnabled")

class DisableTransitGatewayRouteTablePropagationRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")

class DisableTransitGatewayRouteTablePropagationResult(_EC2ModelBase):
    propagation: 'TransitGatewayPropagation' = pydantic.Field(None, alias="Propagation")

class DisableVgwRoutePropagationRequest(_EC2ModelBase):
    gateway_id: VpnGatewayId = pydantic.Field(None, alias="GatewayId")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisableVpcClassicLinkDnsSupportRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class DisableVpcClassicLinkDnsSupportResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DisableVpcClassicLinkRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class DisableVpcClassicLinkResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DisassociateAddressRequest(_EC2ModelBase):
    association_id: ElasticIpAssociationId = pydantic.Field(None, alias="AssociationId")
    public_ip: EipAllocationPublicIp = pydantic.Field(None, alias="PublicIp")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateClientVpnTargetNetworkRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    association_id: ClientVpnAssociationId = pydantic.Field(None, alias="AssociationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateClientVpnTargetNetworkResult(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    status: 'AssociationStatus' = pydantic.Field(None, alias="Status")

class DisassociateEnclaveCertificateIamRoleRequest(_EC2ModelBase):
    certificate_arn: CertificateId = pydantic.Field(None, alias="CertificateArn")
    role_arn: RoleId = pydantic.Field(None, alias="RoleArn")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateEnclaveCertificateIamRoleResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class DisassociateIamInstanceProfileRequest(_EC2ModelBase):
    association_id: IamInstanceProfileAssociationId = pydantic.Field(None, alias="AssociationId")

class DisassociateIamInstanceProfileResult(_EC2ModelBase):
    iam_instance_profile_association: 'IamInstanceProfileAssociation' = pydantic.Field(None, alias="IamInstanceProfileAssociation")

class DisassociateInstanceEventWindowRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_event_window_id: InstanceEventWindowId = pydantic.Field(None, alias="InstanceEventWindowId")
    association_target: 'InstanceEventWindowDisassociationRequest' = pydantic.Field(None, alias="AssociationTarget")

class DisassociateInstanceEventWindowResult(_EC2ModelBase):
    instance_event_window: 'InstanceEventWindow' = pydantic.Field(None, alias="InstanceEventWindow")

class DisassociateIpamResourceDiscoveryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_association_id: IpamResourceDiscoveryAssociationId = pydantic.Field(None, alias="IpamResourceDiscoveryAssociationId")

class DisassociateIpamResourceDiscoveryResult(_EC2ModelBase):
    ipam_resource_discovery_association: 'IpamResourceDiscoveryAssociation' = pydantic.Field(None, alias="IpamResourceDiscoveryAssociation")

class DisassociateNatGatewayAddressRequest(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    association_ids: EipAssociationIdList = pydantic.Field(None, alias="AssociationIds")
    max_drain_duration_seconds: DrainSeconds = pydantic.Field(None, alias="MaxDrainDurationSeconds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateNatGatewayAddressResult(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    nat_gateway_addresses: NatGatewayAddressList = pydantic.Field(None, alias="NatGatewayAddresses")

class DisassociateRouteTableRequest(_EC2ModelBase):
    association_id: RouteTableAssociationId = pydantic.Field(None, alias="AssociationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateSubnetCidrBlockRequest(_EC2ModelBase):
    association_id: SubnetCidrAssociationId = pydantic.Field(None, alias="AssociationId")

class DisassociateSubnetCidrBlockResult(_EC2ModelBase):
    ipv_6_cidr_block_association: 'SubnetIpv6CidrBlockAssociation' = pydantic.Field(None, alias="Ipv6CidrBlockAssociation")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")

class DisassociateTransitGatewayMulticastDomainRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    subnet_ids: TransitGatewaySubnetIdList = pydantic.Field(None, alias="SubnetIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateTransitGatewayMulticastDomainResult(_EC2ModelBase):
    associations: 'TransitGatewayMulticastDomainAssociations' = pydantic.Field(None, alias="Associations")

class DisassociateTransitGatewayPolicyTableRequest(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateTransitGatewayPolicyTableResult(_EC2ModelBase):
    association: 'TransitGatewayPolicyTableAssociation' = pydantic.Field(None, alias="Association")

class DisassociateTransitGatewayRouteTableRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateTransitGatewayRouteTableResult(_EC2ModelBase):
    association: 'TransitGatewayAssociation' = pydantic.Field(None, alias="Association")

class DisassociateTrunkInterfaceRequest(_EC2ModelBase):
    association_id: TrunkInterfaceAssociationId = pydantic.Field(None, alias="AssociationId")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class DisassociateTrunkInterfaceResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class DisassociateVpcCidrBlockRequest(_EC2ModelBase):
    association_id: VpcCidrAssociationId = pydantic.Field(None, alias="AssociationId")

class DisassociateVpcCidrBlockResult(_EC2ModelBase):
    ipv_6_cidr_block_association: 'VpcIpv6CidrBlockAssociation' = pydantic.Field(None, alias="Ipv6CidrBlockAssociation")
    cidr_block_association: 'VpcCidrBlockAssociation' = pydantic.Field(None, alias="CidrBlockAssociation")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class DiskImage(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    image: 'DiskImageDetail' = pydantic.Field(None, alias="Image")
    volume: 'VolumeDetail' = pydantic.Field(None, alias="Volume")

class DiskImageDescription(_EC2ModelBase):
    checksum: String = pydantic.Field(None, alias="Checksum")
    format: DiskImageFormat = pydantic.Field(None, alias="Format")
    import_manifest_url: ImportManifestUrl = pydantic.Field(None, alias="ImportManifestUrl")
    size: Long = pydantic.Field(None, alias="Size")

class DiskImageDetail(_EC2ModelBase):
    bytes: Long = pydantic.Field(None, alias="Bytes")
    format: DiskImageFormat = pydantic.Field(None, alias="Format")
    import_manifest_url: ImportManifestUrl = pydantic.Field(None, alias="ImportManifestUrl")

class DiskImageVolumeDescription(_EC2ModelBase):
    id: String = pydantic.Field(None, alias="Id")
    size: Long = pydantic.Field(None, alias="Size")

class DiskInfo(_EC2ModelBase):
    size_in_gb: DiskSize = pydantic.Field(None, alias="SizeInGB")
    count: DiskCount = pydantic.Field(None, alias="Count")
    type: DiskType = pydantic.Field(None, alias="Type")

class DnsEntry(_EC2ModelBase):
    dns_name: String = pydantic.Field(None, alias="DnsName")
    hosted_zone_id: String = pydantic.Field(None, alias="HostedZoneId")

class DnsOptions(_EC2ModelBase):
    dns_record_ip_type: DnsRecordIpType = pydantic.Field(None, alias="DnsRecordIpType")
    private_dns_only_for_inbound_resolver_endpoint: Boolean = pydantic.Field(None, alias="PrivateDnsOnlyForInboundResolverEndpoint")

class DnsOptionsSpecification(_EC2ModelBase):
    dns_record_ip_type: DnsRecordIpType = pydantic.Field(None, alias="DnsRecordIpType")
    private_dns_only_for_inbound_resolver_endpoint: Boolean = pydantic.Field(None, alias="PrivateDnsOnlyForInboundResolverEndpoint")

class DnsServersOptionsModifyStructure(_EC2ModelBase):
    custom_dns_servers: ValueStringList = pydantic.Field(None, alias="CustomDnsServers")
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class EbsBlockDevice(_EC2ModelBase):
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    iops: Integer = pydantic.Field(None, alias="Iops")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")
    volume_type: VolumeType = pydantic.Field(None, alias="VolumeType")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    throughput: Integer = pydantic.Field(None, alias="Throughput")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")

class EbsInfo(_EC2ModelBase):
    ebs_optimized_support: EbsOptimizedSupport = pydantic.Field(None, alias="EbsOptimizedSupport")
    encryption_support: EbsEncryptionSupport = pydantic.Field(None, alias="EncryptionSupport")
    ebs_optimized_info: 'EbsOptimizedInfo' = pydantic.Field(None, alias="EbsOptimizedInfo")
    nvme_support: EbsNvmeSupport = pydantic.Field(None, alias="NvmeSupport")

class EbsInstanceBlockDevice(_EC2ModelBase):
    attach_time: DateTime = pydantic.Field(None, alias="AttachTime")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    status: AttachmentStatus = pydantic.Field(None, alias="Status")
    volume_id: String = pydantic.Field(None, alias="VolumeId")

class EbsInstanceBlockDeviceSpecification(_EC2ModelBase):
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")

class EbsOptimizedInfo(_EC2ModelBase):
    baseline_bandwidth_in_mbps: BaselineBandwidthInMbps = pydantic.Field(None, alias="BaselineBandwidthInMbps")
    baseline_throughput_in_m_bps: BaselineThroughputInMBps = pydantic.Field(None, alias="BaselineThroughputInMBps")
    baseline_iops: BaselineIops = pydantic.Field(None, alias="BaselineIops")
    maximum_bandwidth_in_mbps: MaximumBandwidthInMbps = pydantic.Field(None, alias="MaximumBandwidthInMbps")
    maximum_throughput_in_m_bps: MaximumThroughputInMBps = pydantic.Field(None, alias="MaximumThroughputInMBps")
    maximum_iops: MaximumIops = pydantic.Field(None, alias="MaximumIops")

class EfaInfo(_EC2ModelBase):
    maximum_efa_interfaces: MaximumEfaInterfaces = pydantic.Field(None, alias="MaximumEfaInterfaces")

class EgressOnlyInternetGateway(_EC2ModelBase):
    attachments: InternetGatewayAttachmentList = pydantic.Field(None, alias="Attachments")
    egress_only_internet_gateway_id: EgressOnlyInternetGatewayId = pydantic.Field(None, alias="EgressOnlyInternetGatewayId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ElasticGpuAssociation(_EC2ModelBase):
    elastic_gpu_id: ElasticGpuId = pydantic.Field(None, alias="ElasticGpuId")
    elastic_gpu_association_id: String = pydantic.Field(None, alias="ElasticGpuAssociationId")
    elastic_gpu_association_state: String = pydantic.Field(None, alias="ElasticGpuAssociationState")
    elastic_gpu_association_time: String = pydantic.Field(None, alias="ElasticGpuAssociationTime")

class ElasticGpuHealth(_EC2ModelBase):
    status: ElasticGpuStatus = pydantic.Field(None, alias="Status")

class ElasticGpuSpecification(_EC2ModelBase):
    type: String = pydantic.Field(None, alias="Type")

class ElasticGpuSpecificationResponse(_EC2ModelBase):
    type: String = pydantic.Field(None, alias="Type")

class ElasticGpus(_EC2ModelBase):
    elastic_gpu_id: String = pydantic.Field(None, alias="ElasticGpuId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    elastic_gpu_type: String = pydantic.Field(None, alias="ElasticGpuType")
    elastic_gpu_health: 'ElasticGpuHealth' = pydantic.Field(None, alias="ElasticGpuHealth")
    elastic_gpu_state: ElasticGpuState = pydantic.Field(None, alias="ElasticGpuState")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ElasticInferenceAccelerator(_EC2ModelBase):
    type: String = pydantic.Field(None, alias="Type")
    count: ElasticInferenceAcceleratorCount = pydantic.Field(None, alias="Count")

class ElasticInferenceAcceleratorAssociation(_EC2ModelBase):
    elastic_inference_accelerator_arn: String = pydantic.Field(None, alias="ElasticInferenceAcceleratorArn")
    elastic_inference_accelerator_association_id: String = pydantic.Field(None, alias="ElasticInferenceAcceleratorAssociationId")
    elastic_inference_accelerator_association_state: String = pydantic.Field(None, alias="ElasticInferenceAcceleratorAssociationState")
    elastic_inference_accelerator_association_time: DateTime = pydantic.Field(None, alias="ElasticInferenceAcceleratorAssociationTime")

class EnaSrdSpecification(_EC2ModelBase):
    ena_srd_enabled: Boolean = pydantic.Field(None, alias="EnaSrdEnabled")
    ena_srd_udp_specification: 'EnaSrdUdpSpecification' = pydantic.Field(None, alias="EnaSrdUdpSpecification")

class EnaSrdUdpSpecification(_EC2ModelBase):
    ena_srd_udp_enabled: Boolean = pydantic.Field(None, alias="EnaSrdUdpEnabled")

class EnableAddressTransferRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    transfer_account_id: String = pydantic.Field(None, alias="TransferAccountId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableAddressTransferResult(_EC2ModelBase):
    address_transfer: 'AddressTransfer' = pydantic.Field(None, alias="AddressTransfer")

class EnableAwsNetworkPerformanceMetricSubscriptionRequest(_EC2ModelBase):
    source: String = pydantic.Field(None, alias="Source")
    destination: String = pydantic.Field(None, alias="Destination")
    metric: MetricType = pydantic.Field(None, alias="Metric")
    statistic: StatisticType = pydantic.Field(None, alias="Statistic")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableAwsNetworkPerformanceMetricSubscriptionResult(_EC2ModelBase):
    output: Boolean = pydantic.Field(None, alias="Output")

class EnableEbsEncryptionByDefaultRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableEbsEncryptionByDefaultResult(_EC2ModelBase):
    ebs_encryption_by_default: Boolean = pydantic.Field(None, alias="EbsEncryptionByDefault")

class EnableFastLaunchRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    resource_type: String = pydantic.Field(None, alias="ResourceType")
    snapshot_configuration: 'FastLaunchSnapshotConfigurationRequest' = pydantic.Field(None, alias="SnapshotConfiguration")
    launch_template: 'FastLaunchLaunchTemplateSpecificationRequest' = pydantic.Field(None, alias="LaunchTemplate")
    max_parallel_launches: Integer = pydantic.Field(None, alias="MaxParallelLaunches")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableFastLaunchResult(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    resource_type: FastLaunchResourceType = pydantic.Field(None, alias="ResourceType")
    snapshot_configuration: 'FastLaunchSnapshotConfigurationResponse' = pydantic.Field(None, alias="SnapshotConfiguration")
    launch_template: 'FastLaunchLaunchTemplateSpecificationResponse' = pydantic.Field(None, alias="LaunchTemplate")
    max_parallel_launches: Integer = pydantic.Field(None, alias="MaxParallelLaunches")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: FastLaunchStateCode = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    state_transition_time: MillisecondDateTime = pydantic.Field(None, alias="StateTransitionTime")

class EnableFastSnapshotRestoreErrorItem(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    fast_snapshot_restore_state_errors: EnableFastSnapshotRestoreStateErrorSet = pydantic.Field(None, alias="FastSnapshotRestoreStateErrors")

class EnableFastSnapshotRestoreStateError(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class EnableFastSnapshotRestoreStateErrorItem(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    error: 'EnableFastSnapshotRestoreStateError' = pydantic.Field(None, alias="Error")

class EnableFastSnapshotRestoreSuccessItem(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    state: FastSnapshotRestoreStateCode = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    owner_alias: String = pydantic.Field(None, alias="OwnerAlias")
    enabling_time: MillisecondDateTime = pydantic.Field(None, alias="EnablingTime")
    optimizing_time: MillisecondDateTime = pydantic.Field(None, alias="OptimizingTime")
    enabled_time: MillisecondDateTime = pydantic.Field(None, alias="EnabledTime")
    disabling_time: MillisecondDateTime = pydantic.Field(None, alias="DisablingTime")
    disabled_time: MillisecondDateTime = pydantic.Field(None, alias="DisabledTime")

class EnableFastSnapshotRestoresRequest(_EC2ModelBase):
    availability_zones: AvailabilityZoneStringList = pydantic.Field(None, alias="AvailabilityZones")
    source_snapshot_ids: SnapshotIdStringList = pydantic.Field(None, alias="SourceSnapshotIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableFastSnapshotRestoresResult(_EC2ModelBase):
    successful: EnableFastSnapshotRestoreSuccessSet = pydantic.Field(None, alias="Successful")
    unsuccessful: EnableFastSnapshotRestoreErrorSet = pydantic.Field(None, alias="Unsuccessful")

class EnableImageDeprecationRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    deprecate_at: MillisecondDateTime = pydantic.Field(None, alias="DeprecateAt")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableImageDeprecationResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class EnableIpamOrganizationAdminAccountRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    delegated_admin_account_id: String = pydantic.Field(None, alias="DelegatedAdminAccountId")

class EnableIpamOrganizationAdminAccountResult(_EC2ModelBase):
    success: Boolean = pydantic.Field(None, alias="Success")

class EnableReachabilityAnalyzerOrganizationSharingRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableReachabilityAnalyzerOrganizationSharingResult(_EC2ModelBase):
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class EnableSerialConsoleAccessRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableSerialConsoleAccessResult(_EC2ModelBase):
    serial_console_access_enabled: Boolean = pydantic.Field(None, alias="SerialConsoleAccessEnabled")

class EnableTransitGatewayRouteTablePropagationRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")

class EnableTransitGatewayRouteTablePropagationResult(_EC2ModelBase):
    propagation: 'TransitGatewayPropagation' = pydantic.Field(None, alias="Propagation")

class EnableVgwRoutePropagationRequest(_EC2ModelBase):
    gateway_id: VpnGatewayId = pydantic.Field(None, alias="GatewayId")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class EnableVolumeIORequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")

class EnableVpcClassicLinkDnsSupportRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class EnableVpcClassicLinkDnsSupportResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class EnableVpcClassicLinkRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")

class EnableVpcClassicLinkResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class EnclaveOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class EnclaveOptionsRequest(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class EventInformation(_EC2ModelBase):
    event_description: String = pydantic.Field(None, alias="EventDescription")
    event_sub_type: String = pydantic.Field(None, alias="EventSubType")
    instance_id: String = pydantic.Field(None, alias="InstanceId")

class Explanation(_EC2ModelBase):
    acl: 'AnalysisComponent' = pydantic.Field(None, alias="Acl")
    acl_rule: 'AnalysisAclRule' = pydantic.Field(None, alias="AclRule")
    address: IpAddress = pydantic.Field(None, alias="Address")
    addresses: IpAddressList = pydantic.Field(None, alias="Addresses")
    attached_to: 'AnalysisComponent' = pydantic.Field(None, alias="AttachedTo")
    availability_zones: ValueStringList = pydantic.Field(None, alias="AvailabilityZones")
    cidrs: ValueStringList = pydantic.Field(None, alias="Cidrs")
    component: 'AnalysisComponent' = pydantic.Field(None, alias="Component")
    customer_gateway: 'AnalysisComponent' = pydantic.Field(None, alias="CustomerGateway")
    destination: 'AnalysisComponent' = pydantic.Field(None, alias="Destination")
    destination_vpc: 'AnalysisComponent' = pydantic.Field(None, alias="DestinationVpc")
    direction: String = pydantic.Field(None, alias="Direction")
    explanation_code: String = pydantic.Field(None, alias="ExplanationCode")
    ingress_route_table: 'AnalysisComponent' = pydantic.Field(None, alias="IngressRouteTable")
    internet_gateway: 'AnalysisComponent' = pydantic.Field(None, alias="InternetGateway")
    load_balancer_arn: ResourceArn = pydantic.Field(None, alias="LoadBalancerArn")
    classic_load_balancer_listener: 'AnalysisLoadBalancerListener' = pydantic.Field(None, alias="ClassicLoadBalancerListener")
    load_balancer_listener_port: Port = pydantic.Field(None, alias="LoadBalancerListenerPort")
    load_balancer_target: 'AnalysisLoadBalancerTarget' = pydantic.Field(None, alias="LoadBalancerTarget")
    load_balancer_target_group: 'AnalysisComponent' = pydantic.Field(None, alias="LoadBalancerTargetGroup")
    load_balancer_target_groups: AnalysisComponentList = pydantic.Field(None, alias="LoadBalancerTargetGroups")
    load_balancer_target_port: Port = pydantic.Field(None, alias="LoadBalancerTargetPort")
    elastic_load_balancer_listener: 'AnalysisComponent' = pydantic.Field(None, alias="ElasticLoadBalancerListener")
    missing_component: String = pydantic.Field(None, alias="MissingComponent")
    nat_gateway: 'AnalysisComponent' = pydantic.Field(None, alias="NatGateway")
    network_interface: 'AnalysisComponent' = pydantic.Field(None, alias="NetworkInterface")
    packet_field: String = pydantic.Field(None, alias="PacketField")
    vpc_peering_connection: 'AnalysisComponent' = pydantic.Field(None, alias="VpcPeeringConnection")
    port: Port = pydantic.Field(None, alias="Port")
    port_ranges: PortRangeList = pydantic.Field(None, alias="PortRanges")
    prefix_list: 'AnalysisComponent' = pydantic.Field(None, alias="PrefixList")
    protocols: StringList = pydantic.Field(None, alias="Protocols")
    route_table_route: 'AnalysisRouteTableRoute' = pydantic.Field(None, alias="RouteTableRoute")
    route_table: 'AnalysisComponent' = pydantic.Field(None, alias="RouteTable")
    security_group: 'AnalysisComponent' = pydantic.Field(None, alias="SecurityGroup")
    security_group_rule: 'AnalysisSecurityGroupRule' = pydantic.Field(None, alias="SecurityGroupRule")
    security_groups: AnalysisComponentList = pydantic.Field(None, alias="SecurityGroups")
    source_vpc: 'AnalysisComponent' = pydantic.Field(None, alias="SourceVpc")
    state: String = pydantic.Field(None, alias="State")
    subnet: 'AnalysisComponent' = pydantic.Field(None, alias="Subnet")
    subnet_route_table: 'AnalysisComponent' = pydantic.Field(None, alias="SubnetRouteTable")
    vpc: 'AnalysisComponent' = pydantic.Field(None, alias="Vpc")
    vpc_endpoint: 'AnalysisComponent' = pydantic.Field(None, alias="VpcEndpoint")
    vpn_connection: 'AnalysisComponent' = pydantic.Field(None, alias="VpnConnection")
    vpn_gateway: 'AnalysisComponent' = pydantic.Field(None, alias="VpnGateway")
    transit_gateway: 'AnalysisComponent' = pydantic.Field(None, alias="TransitGateway")
    transit_gateway_route_table: 'AnalysisComponent' = pydantic.Field(None, alias="TransitGatewayRouteTable")
    transit_gateway_route_table_route: 'TransitGatewayRouteTableRoute' = pydantic.Field(None, alias="TransitGatewayRouteTableRoute")
    transit_gateway_attachment: 'AnalysisComponent' = pydantic.Field(None, alias="TransitGatewayAttachment")
    component_account: ComponentAccount = pydantic.Field(None, alias="ComponentAccount")
    component_region: ComponentRegion = pydantic.Field(None, alias="ComponentRegion")
    firewall_stateless_rule: 'FirewallStatelessRule' = pydantic.Field(None, alias="FirewallStatelessRule")
    firewall_stateful_rule: 'FirewallStatefulRule' = pydantic.Field(None, alias="FirewallStatefulRule")

class ExportClientVpnClientCertificateRevocationListRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ExportClientVpnClientCertificateRevocationListResult(_EC2ModelBase):
    certificate_revocation_list: String = pydantic.Field(None, alias="CertificateRevocationList")
    status: 'ClientCertificateRevocationListStatus' = pydantic.Field(None, alias="Status")

class ExportClientVpnClientConfigurationRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ExportClientVpnClientConfigurationResult(_EC2ModelBase):
    client_configuration: String = pydantic.Field(None, alias="ClientConfiguration")

class ExportImageRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    description: String = pydantic.Field(None, alias="Description")
    disk_image_format: DiskImageFormat = pydantic.Field(None, alias="DiskImageFormat")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    s_3_export_location: 'ExportTaskS3LocationRequest' = pydantic.Field(None, alias="S3ExportLocation")
    role_name: String = pydantic.Field(None, alias="RoleName")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class ExportImageResult(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    disk_image_format: DiskImageFormat = pydantic.Field(None, alias="DiskImageFormat")
    export_image_task_id: String = pydantic.Field(None, alias="ExportImageTaskId")
    image_id: String = pydantic.Field(None, alias="ImageId")
    role_name: String = pydantic.Field(None, alias="RoleName")
    progress: String = pydantic.Field(None, alias="Progress")
    s_3_export_location: 'ExportTaskS3Location' = pydantic.Field(None, alias="S3ExportLocation")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ExportImageTask(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    export_image_task_id: String = pydantic.Field(None, alias="ExportImageTaskId")
    image_id: String = pydantic.Field(None, alias="ImageId")
    progress: String = pydantic.Field(None, alias="Progress")
    s_3_export_location: 'ExportTaskS3Location' = pydantic.Field(None, alias="S3ExportLocation")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ExportTask(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    export_task_id: String = pydantic.Field(None, alias="ExportTaskId")
    export_to_s_3_task: 'ExportToS3Task' = pydantic.Field(None, alias="ExportToS3Task")
    instance_export_details: 'InstanceExportDetails' = pydantic.Field(None, alias="InstanceExportDetails")
    state: ExportTaskState = pydantic.Field(None, alias="State")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ExportTaskS3Location(_EC2ModelBase):
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")

class ExportTaskS3LocationRequest(_EC2ModelBase):
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")

class ExportToS3Task(_EC2ModelBase):
    container_format: ContainerFormat = pydantic.Field(None, alias="ContainerFormat")
    disk_image_format: DiskImageFormat = pydantic.Field(None, alias="DiskImageFormat")
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_key: String = pydantic.Field(None, alias="S3Key")

class ExportToS3TaskSpecification(_EC2ModelBase):
    container_format: ContainerFormat = pydantic.Field(None, alias="ContainerFormat")
    disk_image_format: DiskImageFormat = pydantic.Field(None, alias="DiskImageFormat")
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_prefix: String = pydantic.Field(None, alias="S3Prefix")

class ExportTransitGatewayRoutesRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ExportTransitGatewayRoutesResult(_EC2ModelBase):
    s_3_location: String = pydantic.Field(None, alias="S3Location")

class FailedCapacityReservationFleetCancellationResult(_EC2ModelBase):
    capacity_reservation_fleet_id: CapacityReservationFleetId = pydantic.Field(None, alias="CapacityReservationFleetId")
    cancel_capacity_reservation_fleet_error: 'CancelCapacityReservationFleetError' = pydantic.Field(None, alias="CancelCapacityReservationFleetError")

class FailedQueuedPurchaseDeletion(_EC2ModelBase):
    error: 'DeleteQueuedReservedInstancesError' = pydantic.Field(None, alias="Error")
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")

class FastLaunchLaunchTemplateSpecificationRequest(_EC2ModelBase):
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: String = pydantic.Field(None, alias="LaunchTemplateName")
    version: String = pydantic.Field(None, alias="Version")

class FastLaunchLaunchTemplateSpecificationResponse(_EC2ModelBase):
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: String = pydantic.Field(None, alias="LaunchTemplateName")
    version: String = pydantic.Field(None, alias="Version")

class FastLaunchSnapshotConfigurationRequest(_EC2ModelBase):
    target_resource_count: Integer = pydantic.Field(None, alias="TargetResourceCount")

class FastLaunchSnapshotConfigurationResponse(_EC2ModelBase):
    target_resource_count: Integer = pydantic.Field(None, alias="TargetResourceCount")

class FederatedAuthentication(_EC2ModelBase):
    saml_provider_arn: String = pydantic.Field(None, alias="SamlProviderArn")
    self_service_saml_provider_arn: String = pydantic.Field(None, alias="SelfServiceSamlProviderArn")

class FederatedAuthenticationRequest(_EC2ModelBase):
    saml_provider_arn: String = pydantic.Field(None, alias="SAMLProviderArn")
    self_service_saml_provider_arn: String = pydantic.Field(None, alias="SelfServiceSAMLProviderArn")

class Filter(_EC2ModelBase):
    name: String = pydantic.Field(None, alias="Name")
    values: ValueStringList = pydantic.Field(None, alias="Values")

class FilterPortRange(_EC2ModelBase):
    from_port: Port = pydantic.Field(None, alias="FromPort")
    to_port: Port = pydantic.Field(None, alias="ToPort")

class FirewallStatefulRule(_EC2ModelBase):
    rule_group_arn: ResourceArn = pydantic.Field(None, alias="RuleGroupArn")
    sources: ValueStringList = pydantic.Field(None, alias="Sources")
    destinations: ValueStringList = pydantic.Field(None, alias="Destinations")
    source_ports: PortRangeList = pydantic.Field(None, alias="SourcePorts")
    destination_ports: PortRangeList = pydantic.Field(None, alias="DestinationPorts")
    protocol: String = pydantic.Field(None, alias="Protocol")
    rule_action: String = pydantic.Field(None, alias="RuleAction")
    direction: String = pydantic.Field(None, alias="Direction")

class FirewallStatelessRule(_EC2ModelBase):
    rule_group_arn: ResourceArn = pydantic.Field(None, alias="RuleGroupArn")
    sources: ValueStringList = pydantic.Field(None, alias="Sources")
    destinations: ValueStringList = pydantic.Field(None, alias="Destinations")
    source_ports: PortRangeList = pydantic.Field(None, alias="SourcePorts")
    destination_ports: PortRangeList = pydantic.Field(None, alias="DestinationPorts")
    protocols: ProtocolIntList = pydantic.Field(None, alias="Protocols")
    rule_action: String = pydantic.Field(None, alias="RuleAction")
    priority: Priority = pydantic.Field(None, alias="Priority")

class FleetCapacityReservation(_EC2ModelBase):
    capacity_reservation_id: CapacityReservationId = pydantic.Field(None, alias="CapacityReservationId")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    instance_platform: CapacityReservationInstancePlatform = pydantic.Field(None, alias="InstancePlatform")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    total_instance_count: Integer = pydantic.Field(None, alias="TotalInstanceCount")
    fulfilled_capacity: Double = pydantic.Field(None, alias="FulfilledCapacity")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    create_date: MillisecondDateTime = pydantic.Field(None, alias="CreateDate")
    weight: DoubleWithConstraints = pydantic.Field(None, alias="Weight")
    priority: IntegerWithConstraints = pydantic.Field(None, alias="Priority")

class FleetData(_EC2ModelBase):
    activity_status: FleetActivityStatus = pydantic.Field(None, alias="ActivityStatus")
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")
    fleet_state: FleetStateCode = pydantic.Field(None, alias="FleetState")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    excess_capacity_termination_policy: FleetExcessCapacityTerminationPolicy = pydantic.Field(None, alias="ExcessCapacityTerminationPolicy")
    fulfilled_capacity: Double = pydantic.Field(None, alias="FulfilledCapacity")
    fulfilled_on_demand_capacity: Double = pydantic.Field(None, alias="FulfilledOnDemandCapacity")
    launch_template_configs: FleetLaunchTemplateConfigList = pydantic.Field(None, alias="LaunchTemplateConfigs")
    target_capacity_specification: 'TargetCapacitySpecification' = pydantic.Field(None, alias="TargetCapacitySpecification")
    terminate_instances_with_expiration: Boolean = pydantic.Field(None, alias="TerminateInstancesWithExpiration")
    type: FleetType = pydantic.Field(None, alias="Type")
    valid_from: DateTime = pydantic.Field(None, alias="ValidFrom")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    replace_unhealthy_instances: Boolean = pydantic.Field(None, alias="ReplaceUnhealthyInstances")
    spot_options: 'SpotOptions' = pydantic.Field(None, alias="SpotOptions")
    on_demand_options: 'OnDemandOptions' = pydantic.Field(None, alias="OnDemandOptions")
    tags: TagList = pydantic.Field(None, alias="Tags")
    errors: DescribeFleetsErrorSet = pydantic.Field(None, alias="Errors")
    instances: DescribeFleetsInstancesSet = pydantic.Field(None, alias="Instances")
    context: String = pydantic.Field(None, alias="Context")

class FleetLaunchTemplateConfig(_EC2ModelBase):
    launch_template_specification: 'FleetLaunchTemplateSpecification' = pydantic.Field(None, alias="LaunchTemplateSpecification")
    overrides: FleetLaunchTemplateOverridesList = pydantic.Field(None, alias="Overrides")

class FleetLaunchTemplateConfigRequest(_EC2ModelBase):
    launch_template_specification: 'FleetLaunchTemplateSpecificationRequest' = pydantic.Field(None, alias="LaunchTemplateSpecification")
    overrides: FleetLaunchTemplateOverridesListRequest = pydantic.Field(None, alias="Overrides")

class FleetLaunchTemplateOverrides(_EC2ModelBase):
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    max_price: String = pydantic.Field(None, alias="MaxPrice")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    weighted_capacity: Double = pydantic.Field(None, alias="WeightedCapacity")
    priority: Double = pydantic.Field(None, alias="Priority")
    placement: 'PlacementResponse' = pydantic.Field(None, alias="Placement")
    instance_requirements: 'InstanceRequirements' = pydantic.Field(None, alias="InstanceRequirements")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")

class FleetLaunchTemplateOverridesRequest(_EC2ModelBase):
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    max_price: String = pydantic.Field(None, alias="MaxPrice")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    weighted_capacity: Double = pydantic.Field(None, alias="WeightedCapacity")
    priority: Double = pydantic.Field(None, alias="Priority")
    placement: 'Placement' = pydantic.Field(None, alias="Placement")
    instance_requirements: 'InstanceRequirementsRequest' = pydantic.Field(None, alias="InstanceRequirements")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")

class FleetLaunchTemplateSpecification(_EC2ModelBase):
    launch_template_id: String = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    version: String = pydantic.Field(None, alias="Version")

class FleetLaunchTemplateSpecificationRequest(_EC2ModelBase):
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    version: String = pydantic.Field(None, alias="Version")

class FleetSpotCapacityRebalance(_EC2ModelBase):
    replacement_strategy: FleetReplacementStrategy = pydantic.Field(None, alias="ReplacementStrategy")
    termination_delay: Integer = pydantic.Field(None, alias="TerminationDelay")

class FleetSpotCapacityRebalanceRequest(_EC2ModelBase):
    replacement_strategy: FleetReplacementStrategy = pydantic.Field(None, alias="ReplacementStrategy")
    termination_delay: Integer = pydantic.Field(None, alias="TerminationDelay")

class FleetSpotMaintenanceStrategies(_EC2ModelBase):
    capacity_rebalance: 'FleetSpotCapacityRebalance' = pydantic.Field(None, alias="CapacityRebalance")

class FleetSpotMaintenanceStrategiesRequest(_EC2ModelBase):
    capacity_rebalance: 'FleetSpotCapacityRebalanceRequest' = pydantic.Field(None, alias="CapacityRebalance")

class FlowLog(_EC2ModelBase):
    creation_time: MillisecondDateTime = pydantic.Field(None, alias="CreationTime")
    deliver_logs_error_message: String = pydantic.Field(None, alias="DeliverLogsErrorMessage")
    deliver_logs_permission_arn: String = pydantic.Field(None, alias="DeliverLogsPermissionArn")
    deliver_cross_account_role: String = pydantic.Field(None, alias="DeliverCrossAccountRole")
    deliver_logs_status: String = pydantic.Field(None, alias="DeliverLogsStatus")
    flow_log_id: String = pydantic.Field(None, alias="FlowLogId")
    flow_log_status: String = pydantic.Field(None, alias="FlowLogStatus")
    log_group_name: String = pydantic.Field(None, alias="LogGroupName")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    traffic_type: TrafficType = pydantic.Field(None, alias="TrafficType")
    log_destination_type: LogDestinationType = pydantic.Field(None, alias="LogDestinationType")
    log_destination: String = pydantic.Field(None, alias="LogDestination")
    log_format: String = pydantic.Field(None, alias="LogFormat")
    tags: TagList = pydantic.Field(None, alias="Tags")
    max_aggregation_interval: Integer = pydantic.Field(None, alias="MaxAggregationInterval")
    destination_options: 'DestinationOptionsResponse' = pydantic.Field(None, alias="DestinationOptions")

class FpgaDeviceInfo(_EC2ModelBase):
    name: FpgaDeviceName = pydantic.Field(None, alias="Name")
    manufacturer: FpgaDeviceManufacturerName = pydantic.Field(None, alias="Manufacturer")
    count: FpgaDeviceCount = pydantic.Field(None, alias="Count")
    memory_info: 'FpgaDeviceMemoryInfo' = pydantic.Field(None, alias="MemoryInfo")

class FpgaDeviceMemoryInfo(_EC2ModelBase):
    size_in_mi_b: FpgaDeviceMemorySize = pydantic.Field(None, alias="SizeInMiB")

class FpgaImage(_EC2ModelBase):
    fpga_image_id: String = pydantic.Field(None, alias="FpgaImageId")
    fpga_image_global_id: String = pydantic.Field(None, alias="FpgaImageGlobalId")
    name: String = pydantic.Field(None, alias="Name")
    description: String = pydantic.Field(None, alias="Description")
    shell_version: String = pydantic.Field(None, alias="ShellVersion")
    pci_id: 'PciId' = pydantic.Field(None, alias="PciId")
    state: 'FpgaImageState' = pydantic.Field(None, alias="State")
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    update_time: DateTime = pydantic.Field(None, alias="UpdateTime")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    owner_alias: String = pydantic.Field(None, alias="OwnerAlias")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    tags: TagList = pydantic.Field(None, alias="Tags")
    public: Boolean = pydantic.Field(None, alias="Public")
    data_retention_support: Boolean = pydantic.Field(None, alias="DataRetentionSupport")
    instance_types: InstanceTypesList = pydantic.Field(None, alias="InstanceTypes")

class FpgaImageAttribute(_EC2ModelBase):
    fpga_image_id: String = pydantic.Field(None, alias="FpgaImageId")
    name: String = pydantic.Field(None, alias="Name")
    description: String = pydantic.Field(None, alias="Description")
    load_permissions: LoadPermissionList = pydantic.Field(None, alias="LoadPermissions")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")

class FpgaImageState(_EC2ModelBase):
    code: FpgaImageStateCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class FpgaInfo(_EC2ModelBase):
    fpgas: FpgaDeviceInfoList = pydantic.Field(None, alias="Fpgas")
    total_fpga_memory_in_mi_b: totalFpgaMemory = pydantic.Field(None, alias="TotalFpgaMemoryInMiB")

class GetAssociatedEnclaveCertificateIamRolesRequest(_EC2ModelBase):
    certificate_arn: CertificateId = pydantic.Field(None, alias="CertificateArn")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetAssociatedEnclaveCertificateIamRolesResult(_EC2ModelBase):
    associated_roles: AssociatedRolesList = pydantic.Field(None, alias="AssociatedRoles")

class GetAssociatedIpv6PoolCidrsRequest(_EC2ModelBase):
    pool_id: Ipv6PoolEc2Id = pydantic.Field(None, alias="PoolId")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: Ipv6PoolMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetAssociatedIpv6PoolCidrsResult(_EC2ModelBase):
    ipv_6_cidr_associations: Ipv6CidrAssociationSet = pydantic.Field(None, alias="Ipv6CidrAssociations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetAwsNetworkPerformanceDataRequest(_EC2ModelBase):
    data_queries: DataQueries = pydantic.Field(None, alias="DataQueries")
    start_time: MillisecondDateTime = pydantic.Field(None, alias="StartTime")
    end_time: MillisecondDateTime = pydantic.Field(None, alias="EndTime")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetAwsNetworkPerformanceDataResult(_EC2ModelBase):
    data_responses: DataResponses = pydantic.Field(None, alias="DataResponses")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetCapacityReservationUsageRequest(_EC2ModelBase):
    capacity_reservation_id: CapacityReservationId = pydantic.Field(None, alias="CapacityReservationId")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: GetCapacityReservationUsageRequestMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetCapacityReservationUsageResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    capacity_reservation_id: String = pydantic.Field(None, alias="CapacityReservationId")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    total_instance_count: Integer = pydantic.Field(None, alias="TotalInstanceCount")
    available_instance_count: Integer = pydantic.Field(None, alias="AvailableInstanceCount")
    state: CapacityReservationState = pydantic.Field(None, alias="State")
    instance_usages: InstanceUsageSet = pydantic.Field(None, alias="InstanceUsages")

class GetCoipPoolUsageRequest(_EC2ModelBase):
    pool_id: Ipv4PoolCoipId = pydantic.Field(None, alias="PoolId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: CoipPoolMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetCoipPoolUsageResult(_EC2ModelBase):
    coip_pool_id: String = pydantic.Field(None, alias="CoipPoolId")
    coip_address_usages: CoipAddressUsageSet = pydantic.Field(None, alias="CoipAddressUsages")
    local_gateway_route_table_id: String = pydantic.Field(None, alias="LocalGatewayRouteTableId")

class GetConsoleOutputRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    latest: Boolean = pydantic.Field(None, alias="Latest")

class GetConsoleOutputResult(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    output: String = pydantic.Field(None, alias="Output")
    timestamp: DateTime = pydantic.Field(None, alias="Timestamp")

class GetConsoleScreenshotRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    wake_up: Boolean = pydantic.Field(None, alias="WakeUp")

class GetConsoleScreenshotResult(_EC2ModelBase):
    image_data: String = pydantic.Field(None, alias="ImageData")
    instance_id: String = pydantic.Field(None, alias="InstanceId")

class GetDefaultCreditSpecificationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_family: UnlimitedSupportedInstanceFamily = pydantic.Field(None, alias="InstanceFamily")

class GetDefaultCreditSpecificationResult(_EC2ModelBase):
    instance_family_credit_specification: 'InstanceFamilyCreditSpecification' = pydantic.Field(None, alias="InstanceFamilyCreditSpecification")

class GetEbsDefaultKmsKeyIdRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetEbsDefaultKmsKeyIdResult(_EC2ModelBase):
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")

class GetEbsEncryptionByDefaultRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetEbsEncryptionByDefaultResult(_EC2ModelBase):
    ebs_encryption_by_default: Boolean = pydantic.Field(None, alias="EbsEncryptionByDefault")

class GetFlowLogsIntegrationTemplateRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    flow_log_id: VpcFlowLogId = pydantic.Field(None, alias="FlowLogId")
    config_delivery_s_3_destination_arn: String = pydantic.Field(None, alias="ConfigDeliveryS3DestinationArn")
    integrate_services: 'IntegrateServices' = pydantic.Field(None, alias="IntegrateServices")

class GetFlowLogsIntegrationTemplateResult(_EC2ModelBase):
    result: String = pydantic.Field(None, alias="Result")

class GetGroupsForCapacityReservationRequest(_EC2ModelBase):
    capacity_reservation_id: CapacityReservationId = pydantic.Field(None, alias="CapacityReservationId")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: GetGroupsForCapacityReservationRequestMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetGroupsForCapacityReservationResult(_EC2ModelBase):
    next_token: String = pydantic.Field(None, alias="NextToken")
    capacity_reservation_groups: CapacityReservationGroupSet = pydantic.Field(None, alias="CapacityReservationGroups")

class GetHostReservationPurchasePreviewRequest(_EC2ModelBase):
    host_id_set: RequestHostIdSet = pydantic.Field(None, alias="HostIdSet")
    offering_id: OfferingId = pydantic.Field(None, alias="OfferingId")

class GetHostReservationPurchasePreviewResult(_EC2ModelBase):
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    purchase: PurchaseSet = pydantic.Field(None, alias="Purchase")
    total_hourly_price: String = pydantic.Field(None, alias="TotalHourlyPrice")
    total_upfront_price: String = pydantic.Field(None, alias="TotalUpfrontPrice")

class GetInstanceTypesFromInstanceRequirementsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    architecture_types: ArchitectureTypeSet = pydantic.Field(None, alias="ArchitectureTypes")
    virtualization_types: VirtualizationTypeSet = pydantic.Field(None, alias="VirtualizationTypes")
    instance_requirements: 'InstanceRequirementsRequest' = pydantic.Field(None, alias="InstanceRequirements")
    max_results: Integer = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetInstanceTypesFromInstanceRequirementsResult(_EC2ModelBase):
    instance_types: InstanceTypeInfoFromInstanceRequirementsSet = pydantic.Field(None, alias="InstanceTypes")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetInstanceUefiDataRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetInstanceUefiDataResult(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    uefi_data: String = pydantic.Field(None, alias="UefiData")

class GetIpamAddressHistoryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    cidr: String = pydantic.Field(None, alias="Cidr")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    start_time: MillisecondDateTime = pydantic.Field(None, alias="StartTime")
    end_time: MillisecondDateTime = pydantic.Field(None, alias="EndTime")
    max_results: IpamAddressHistoryMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamAddressHistoryResult(_EC2ModelBase):
    history_records: IpamAddressHistoryRecordSet = pydantic.Field(None, alias="HistoryRecords")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamDiscoveredAccountsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    discovery_region: String = pydantic.Field(None, alias="DiscoveryRegion")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")

class GetIpamDiscoveredAccountsResult(_EC2ModelBase):
    ipam_discovered_accounts: IpamDiscoveredAccountSet = pydantic.Field(None, alias="IpamDiscoveredAccounts")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamDiscoveredResourceCidrsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    resource_region: String = pydantic.Field(None, alias="ResourceRegion")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")

class GetIpamDiscoveredResourceCidrsResult(_EC2ModelBase):
    ipam_discovered_resource_cidrs: IpamDiscoveredResourceCidrSet = pydantic.Field(None, alias="IpamDiscoveredResourceCidrs")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamPoolAllocationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    ipam_pool_allocation_id: IpamPoolAllocationId = pydantic.Field(None, alias="IpamPoolAllocationId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: GetIpamPoolAllocationsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamPoolAllocationsResult(_EC2ModelBase):
    ipam_pool_allocations: IpamPoolAllocationSet = pydantic.Field(None, alias="IpamPoolAllocations")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamPoolCidrsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamPoolCidrsResult(_EC2ModelBase):
    ipam_pool_cidrs: IpamPoolCidrSet = pydantic.Field(None, alias="IpamPoolCidrs")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetIpamResourceCidrsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: IpamMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: IpamResourceType = pydantic.Field(None, alias="ResourceType")
    resource_tag: 'RequestIpamResourceTag' = pydantic.Field(None, alias="ResourceTag")
    resource_owner: String = pydantic.Field(None, alias="ResourceOwner")

class GetIpamResourceCidrsResult(_EC2ModelBase):
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    ipam_resource_cidrs: IpamResourceCidrSet = pydantic.Field(None, alias="IpamResourceCidrs")

class GetLaunchTemplateDataRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")

class GetLaunchTemplateDataResult(_EC2ModelBase):
    launch_template_data: 'ResponseLaunchTemplateData' = pydantic.Field(None, alias="LaunchTemplateData")

class GetManagedPrefixListAssociationsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    max_results: GetManagedPrefixListAssociationsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetManagedPrefixListAssociationsResult(_EC2ModelBase):
    prefix_list_associations: PrefixListAssociationSet = pydantic.Field(None, alias="PrefixListAssociations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetManagedPrefixListEntriesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    target_version: Long = pydantic.Field(None, alias="TargetVersion")
    max_results: PrefixListMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetManagedPrefixListEntriesResult(_EC2ModelBase):
    entries: PrefixListEntrySet = pydantic.Field(None, alias="Entries")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetNetworkInsightsAccessScopeAnalysisFindingsRequest(_EC2ModelBase):
    network_insights_access_scope_analysis_id: NetworkInsightsAccessScopeAnalysisId = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisId")
    max_results: NetworkInsightsMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetNetworkInsightsAccessScopeAnalysisFindingsResult(_EC2ModelBase):
    network_insights_access_scope_analysis_id: NetworkInsightsAccessScopeAnalysisId = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisId")
    analysis_status: AnalysisStatus = pydantic.Field(None, alias="AnalysisStatus")
    analysis_findings: AccessScopeAnalysisFindingList = pydantic.Field(None, alias="AnalysisFindings")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetNetworkInsightsAccessScopeContentRequest(_EC2ModelBase):
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetNetworkInsightsAccessScopeContentResult(_EC2ModelBase):
    network_insights_access_scope_content: 'NetworkInsightsAccessScopeContent' = pydantic.Field(None, alias="NetworkInsightsAccessScopeContent")

class GetPasswordDataRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetPasswordDataResult(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    password_data: String = pydantic.Field(None, alias="PasswordData")
    timestamp: DateTime = pydantic.Field(None, alias="Timestamp")

class GetReservedInstancesExchangeQuoteRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    reserved_instance_ids: ReservedInstanceIdSet = pydantic.Field(None, alias="ReservedInstanceIds")
    target_configurations: TargetConfigurationRequestSet = pydantic.Field(None, alias="TargetConfigurations")

class GetReservedInstancesExchangeQuoteResult(_EC2ModelBase):
    currency_code: String = pydantic.Field(None, alias="CurrencyCode")
    is_valid_exchange: Boolean = pydantic.Field(None, alias="IsValidExchange")
    output_reserved_instances_will_expire_at: DateTime = pydantic.Field(None, alias="OutputReservedInstancesWillExpireAt")
    payment_due: String = pydantic.Field(None, alias="PaymentDue")
    reserved_instance_value_rollup: 'ReservationValue' = pydantic.Field(None, alias="ReservedInstanceValueRollup")
    reserved_instance_value_set: ReservedInstanceReservationValueSet = pydantic.Field(None, alias="ReservedInstanceValueSet")
    target_configuration_value_rollup: 'ReservationValue' = pydantic.Field(None, alias="TargetConfigurationValueRollup")
    target_configuration_value_set: TargetReservationValueSet = pydantic.Field(None, alias="TargetConfigurationValueSet")
    validation_failure_reason: String = pydantic.Field(None, alias="ValidationFailureReason")

class GetSerialConsoleAccessStatusRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetSerialConsoleAccessStatusResult(_EC2ModelBase):
    serial_console_access_enabled: Boolean = pydantic.Field(None, alias="SerialConsoleAccessEnabled")

class GetSpotPlacementScoresRequest(_EC2ModelBase):
    instance_types: InstanceTypes = pydantic.Field(None, alias="InstanceTypes")
    target_capacity: SpotPlacementScoresTargetCapacity = pydantic.Field(None, alias="TargetCapacity")
    target_capacity_unit_type: TargetCapacityUnitType = pydantic.Field(None, alias="TargetCapacityUnitType")
    single_availability_zone: Boolean = pydantic.Field(None, alias="SingleAvailabilityZone")
    region_names: RegionNames = pydantic.Field(None, alias="RegionNames")
    instance_requirements_with_metadata: 'InstanceRequirementsWithMetadataRequest' = pydantic.Field(None, alias="InstanceRequirementsWithMetadata")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    max_results: SpotPlacementScoresMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetSpotPlacementScoresResult(_EC2ModelBase):
    spot_placement_scores: SpotPlacementScores = pydantic.Field(None, alias="SpotPlacementScores")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetSubnetCidrReservationsRequest(_EC2ModelBase):
    filters: FilterList = pydantic.Field(None, alias="Filters")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: GetSubnetCidrReservationsMaxResults = pydantic.Field(None, alias="MaxResults")

class GetSubnetCidrReservationsResult(_EC2ModelBase):
    subnet_ipv_4_cidr_reservations: SubnetCidrReservationList = pydantic.Field(None, alias="SubnetIpv4CidrReservations")
    subnet_ipv_6_cidr_reservations: SubnetCidrReservationList = pydantic.Field(None, alias="SubnetIpv6CidrReservations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetTransitGatewayAttachmentPropagationsRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayAttachmentPropagationsResult(_EC2ModelBase):
    transit_gateway_attachment_propagations: TransitGatewayAttachmentPropagationList = pydantic.Field(None, alias="TransitGatewayAttachmentPropagations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetTransitGatewayMulticastDomainAssociationsRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayMulticastDomainAssociationsResult(_EC2ModelBase):
    multicast_domain_associations: TransitGatewayMulticastDomainAssociationList = pydantic.Field(None, alias="MulticastDomainAssociations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetTransitGatewayPolicyTableAssociationsRequest(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayPolicyTableAssociationsResult(_EC2ModelBase):
    associations: TransitGatewayPolicyTableAssociationList = pydantic.Field(None, alias="Associations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetTransitGatewayPolicyTableEntriesRequest(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayPolicyTableEntriesResult(_EC2ModelBase):
    transit_gateway_policy_table_entries: TransitGatewayPolicyTableEntryList = pydantic.Field(None, alias="TransitGatewayPolicyTableEntries")

class GetTransitGatewayPrefixListReferencesRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayPrefixListReferencesResult(_EC2ModelBase):
    transit_gateway_prefix_list_references: TransitGatewayPrefixListReferenceSet = pydantic.Field(None, alias="TransitGatewayPrefixListReferences")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetTransitGatewayRouteTableAssociationsRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayRouteTableAssociationsResult(_EC2ModelBase):
    associations: TransitGatewayRouteTableAssociationList = pydantic.Field(None, alias="Associations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetTransitGatewayRouteTablePropagationsRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetTransitGatewayRouteTablePropagationsResult(_EC2ModelBase):
    transit_gateway_route_table_propagations: TransitGatewayRouteTablePropagationList = pydantic.Field(None, alias="TransitGatewayRouteTablePropagations")
    next_token: String = pydantic.Field(None, alias="NextToken")

class GetVerifiedAccessEndpointPolicyRequest(_EC2ModelBase):
    verified_access_endpoint_id: VerifiedAccessEndpointId = pydantic.Field(None, alias="VerifiedAccessEndpointId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetVerifiedAccessEndpointPolicyResult(_EC2ModelBase):
    policy_enabled: Boolean = pydantic.Field(None, alias="PolicyEnabled")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")

class GetVerifiedAccessGroupPolicyRequest(_EC2ModelBase):
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetVerifiedAccessGroupPolicyResult(_EC2ModelBase):
    policy_enabled: Boolean = pydantic.Field(None, alias="PolicyEnabled")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")

class GetVpnConnectionDeviceSampleConfigurationRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    vpn_connection_device_type_id: VpnConnectionDeviceTypeId = pydantic.Field(None, alias="VpnConnectionDeviceTypeId")
    internet_key_exchange_version: String = pydantic.Field(None, alias="InternetKeyExchangeVersion")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetVpnConnectionDeviceSampleConfigurationResult(_EC2ModelBase):
    vpn_connection_device_sample_configuration: VpnConnectionDeviceSampleConfiguration = pydantic.Field(None, alias="VpnConnectionDeviceSampleConfiguration")

class GetVpnConnectionDeviceTypesRequest(_EC2ModelBase):
    max_results: GVCDMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetVpnConnectionDeviceTypesResult(_EC2ModelBase):
    vpn_connection_device_types: VpnConnectionDeviceTypeList = pydantic.Field(None, alias="VpnConnectionDeviceTypes")
    next_token: NextToken = pydantic.Field(None, alias="NextToken")

class GetVpnTunnelReplacementStatusRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    vpn_tunnel_outside_ip_address: String = pydantic.Field(None, alias="VpnTunnelOutsideIpAddress")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class GetVpnTunnelReplacementStatusResult(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    customer_gateway_id: CustomerGatewayId = pydantic.Field(None, alias="CustomerGatewayId")
    vpn_gateway_id: VpnGatewayId = pydantic.Field(None, alias="VpnGatewayId")
    vpn_tunnel_outside_ip_address: String = pydantic.Field(None, alias="VpnTunnelOutsideIpAddress")
    maintenance_details: 'MaintenanceDetails' = pydantic.Field(None, alias="MaintenanceDetails")

class GpuDeviceInfo(_EC2ModelBase):
    name: GpuDeviceName = pydantic.Field(None, alias="Name")
    manufacturer: GpuDeviceManufacturerName = pydantic.Field(None, alias="Manufacturer")
    count: GpuDeviceCount = pydantic.Field(None, alias="Count")
    memory_info: 'GpuDeviceMemoryInfo' = pydantic.Field(None, alias="MemoryInfo")

class GpuDeviceMemoryInfo(_EC2ModelBase):
    size_in_mi_b: GpuDeviceMemorySize = pydantic.Field(None, alias="SizeInMiB")

class GpuInfo(_EC2ModelBase):
    gpus: GpuDeviceInfoList = pydantic.Field(None, alias="Gpus")
    total_gpu_memory_in_mi_b: totalGpuMemory = pydantic.Field(None, alias="TotalGpuMemoryInMiB")

class GroupIdentifier(_EC2ModelBase):
    group_name: String = pydantic.Field(None, alias="GroupName")
    group_id: String = pydantic.Field(None, alias="GroupId")

class HibernationOptions(_EC2ModelBase):
    configured: Boolean = pydantic.Field(None, alias="Configured")

class HibernationOptionsRequest(_EC2ModelBase):
    configured: Boolean = pydantic.Field(None, alias="Configured")

class HistoryRecord(_EC2ModelBase):
    event_information: 'EventInformation' = pydantic.Field(None, alias="EventInformation")
    event_type: EventType = pydantic.Field(None, alias="EventType")
    timestamp: DateTime = pydantic.Field(None, alias="Timestamp")

class HistoryRecordEntry(_EC2ModelBase):
    event_information: 'EventInformation' = pydantic.Field(None, alias="EventInformation")
    event_type: FleetEventType = pydantic.Field(None, alias="EventType")
    timestamp: DateTime = pydantic.Field(None, alias="Timestamp")

class Host(_EC2ModelBase):
    auto_placement: AutoPlacement = pydantic.Field(None, alias="AutoPlacement")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    available_capacity: 'AvailableCapacity' = pydantic.Field(None, alias="AvailableCapacity")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    host_id: String = pydantic.Field(None, alias="HostId")
    host_properties: 'HostProperties' = pydantic.Field(None, alias="HostProperties")
    host_reservation_id: String = pydantic.Field(None, alias="HostReservationId")
    instances: HostInstanceList = pydantic.Field(None, alias="Instances")
    state: AllocationState = pydantic.Field(None, alias="State")
    allocation_time: DateTime = pydantic.Field(None, alias="AllocationTime")
    release_time: DateTime = pydantic.Field(None, alias="ReleaseTime")
    tags: TagList = pydantic.Field(None, alias="Tags")
    host_recovery: HostRecovery = pydantic.Field(None, alias="HostRecovery")
    allows_multiple_instance_types: AllowsMultipleInstanceTypes = pydantic.Field(None, alias="AllowsMultipleInstanceTypes")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    member_of_service_linked_resource_group: Boolean = pydantic.Field(None, alias="MemberOfServiceLinkedResourceGroup")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    host_maintenance: HostMaintenance = pydantic.Field(None, alias="HostMaintenance")

class HostInstance(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    owner_id: String = pydantic.Field(None, alias="OwnerId")

class HostOffering(_EC2ModelBase):
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    duration: Integer = pydantic.Field(None, alias="Duration")
    hourly_price: String = pydantic.Field(None, alias="HourlyPrice")
    instance_family: String = pydantic.Field(None, alias="InstanceFamily")
    offering_id: OfferingId = pydantic.Field(None, alias="OfferingId")
    payment_option: PaymentOption = pydantic.Field(None, alias="PaymentOption")
    upfront_price: String = pydantic.Field(None, alias="UpfrontPrice")

class HostProperties(_EC2ModelBase):
    cores: Integer = pydantic.Field(None, alias="Cores")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    instance_family: String = pydantic.Field(None, alias="InstanceFamily")
    sockets: Integer = pydantic.Field(None, alias="Sockets")
    total_v_cpus: Integer = pydantic.Field(None, alias="TotalVCpus")

class HostReservation(_EC2ModelBase):
    count: Integer = pydantic.Field(None, alias="Count")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    duration: Integer = pydantic.Field(None, alias="Duration")
    end: DateTime = pydantic.Field(None, alias="End")
    host_id_set: ResponseHostIdSet = pydantic.Field(None, alias="HostIdSet")
    host_reservation_id: HostReservationId = pydantic.Field(None, alias="HostReservationId")
    hourly_price: String = pydantic.Field(None, alias="HourlyPrice")
    instance_family: String = pydantic.Field(None, alias="InstanceFamily")
    offering_id: OfferingId = pydantic.Field(None, alias="OfferingId")
    payment_option: PaymentOption = pydantic.Field(None, alias="PaymentOption")
    start: DateTime = pydantic.Field(None, alias="Start")
    state: ReservationState = pydantic.Field(None, alias="State")
    upfront_price: String = pydantic.Field(None, alias="UpfrontPrice")
    tags: TagList = pydantic.Field(None, alias="Tags")

class IKEVersionsListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class IKEVersionsRequestListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class IamInstanceProfile(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")
    id: String = pydantic.Field(None, alias="Id")

class IamInstanceProfileAssociation(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    iam_instance_profile: 'IamInstanceProfile' = pydantic.Field(None, alias="IamInstanceProfile")
    state: IamInstanceProfileAssociationState = pydantic.Field(None, alias="State")
    timestamp: DateTime = pydantic.Field(None, alias="Timestamp")

class IamInstanceProfileSpecification(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")
    name: String = pydantic.Field(None, alias="Name")

class IcmpTypeCode(_EC2ModelBase):
    code: Integer = pydantic.Field(None, alias="Code")
    type: Integer = pydantic.Field(None, alias="Type")

class IdFormat(_EC2ModelBase):
    deadline: DateTime = pydantic.Field(None, alias="Deadline")
    resource: String = pydantic.Field(None, alias="Resource")
    use_long_ids: Boolean = pydantic.Field(None, alias="UseLongIds")

class Image(_EC2ModelBase):
    architecture: ArchitectureValues = pydantic.Field(None, alias="Architecture")
    creation_date: String = pydantic.Field(None, alias="CreationDate")
    image_id: String = pydantic.Field(None, alias="ImageId")
    image_location: String = pydantic.Field(None, alias="ImageLocation")
    image_type: ImageTypeValues = pydantic.Field(None, alias="ImageType")
    public: Boolean = pydantic.Field(None, alias="Public")
    kernel_id: String = pydantic.Field(None, alias="KernelId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    platform: PlatformValues = pydantic.Field(None, alias="Platform")
    platform_details: String = pydantic.Field(None, alias="PlatformDetails")
    usage_operation: String = pydantic.Field(None, alias="UsageOperation")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    ramdisk_id: String = pydantic.Field(None, alias="RamdiskId")
    state: ImageState = pydantic.Field(None, alias="State")
    block_device_mappings: BlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    description: String = pydantic.Field(None, alias="Description")
    ena_support: Boolean = pydantic.Field(None, alias="EnaSupport")
    hypervisor: HypervisorType = pydantic.Field(None, alias="Hypervisor")
    image_owner_alias: String = pydantic.Field(None, alias="ImageOwnerAlias")
    name: String = pydantic.Field(None, alias="Name")
    root_device_name: String = pydantic.Field(None, alias="RootDeviceName")
    root_device_type: DeviceType = pydantic.Field(None, alias="RootDeviceType")
    sriov_net_support: String = pydantic.Field(None, alias="SriovNetSupport")
    state_reason: 'StateReason' = pydantic.Field(None, alias="StateReason")
    tags: TagList = pydantic.Field(None, alias="Tags")
    virtualization_type: VirtualizationType = pydantic.Field(None, alias="VirtualizationType")
    boot_mode: BootModeValues = pydantic.Field(None, alias="BootMode")
    tpm_support: TpmSupportValues = pydantic.Field(None, alias="TpmSupport")
    deprecation_time: String = pydantic.Field(None, alias="DeprecationTime")
    imds_support: ImdsSupportValues = pydantic.Field(None, alias="ImdsSupport")

class ImageAttribute(_EC2ModelBase):
    block_device_mappings: BlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    image_id: String = pydantic.Field(None, alias="ImageId")
    launch_permissions: LaunchPermissionList = pydantic.Field(None, alias="LaunchPermissions")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    description: 'AttributeValue' = pydantic.Field(None, alias="Description")
    kernel_id: 'AttributeValue' = pydantic.Field(None, alias="KernelId")
    ramdisk_id: 'AttributeValue' = pydantic.Field(None, alias="RamdiskId")
    sriov_net_support: 'AttributeValue' = pydantic.Field(None, alias="SriovNetSupport")
    boot_mode: 'AttributeValue' = pydantic.Field(None, alias="BootMode")
    tpm_support: 'AttributeValue' = pydantic.Field(None, alias="TpmSupport")
    uefi_data: 'AttributeValue' = pydantic.Field(None, alias="UefiData")
    last_launched_time: 'AttributeValue' = pydantic.Field(None, alias="LastLaunchedTime")
    imds_support: 'AttributeValue' = pydantic.Field(None, alias="ImdsSupport")

class ImageDiskContainer(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    device_name: String = pydantic.Field(None, alias="DeviceName")
    format: String = pydantic.Field(None, alias="Format")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    url: SensitiveUrl = pydantic.Field(None, alias="Url")
    user_bucket: 'UserBucket' = pydantic.Field(None, alias="UserBucket")

class ImageRecycleBinInfo(_EC2ModelBase):
    image_id: String = pydantic.Field(None, alias="ImageId")
    name: String = pydantic.Field(None, alias="Name")
    description: String = pydantic.Field(None, alias="Description")
    recycle_bin_enter_time: MillisecondDateTime = pydantic.Field(None, alias="RecycleBinEnterTime")
    recycle_bin_exit_time: MillisecondDateTime = pydantic.Field(None, alias="RecycleBinExitTime")

class ImportClientVpnClientCertificateRevocationListRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    certificate_revocation_list: String = pydantic.Field(None, alias="CertificateRevocationList")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ImportClientVpnClientCertificateRevocationListResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ImportImageLicenseConfigurationRequest(_EC2ModelBase):
    license_configuration_arn: String = pydantic.Field(None, alias="LicenseConfigurationArn")

class ImportImageLicenseConfigurationResponse(_EC2ModelBase):
    license_configuration_arn: String = pydantic.Field(None, alias="LicenseConfigurationArn")

class ImportImageRequest(_EC2ModelBase):
    architecture: String = pydantic.Field(None, alias="Architecture")
    client_data: 'ClientData' = pydantic.Field(None, alias="ClientData")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    description: String = pydantic.Field(None, alias="Description")
    disk_containers: ImageDiskContainerList = pydantic.Field(None, alias="DiskContainers")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    hypervisor: String = pydantic.Field(None, alias="Hypervisor")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    license_type: String = pydantic.Field(None, alias="LicenseType")
    platform: String = pydantic.Field(None, alias="Platform")
    role_name: String = pydantic.Field(None, alias="RoleName")
    license_specifications: ImportImageLicenseSpecificationListRequest = pydantic.Field(None, alias="LicenseSpecifications")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    usage_operation: String = pydantic.Field(None, alias="UsageOperation")
    boot_mode: BootModeValues = pydantic.Field(None, alias="BootMode")

class ImportImageResult(_EC2ModelBase):
    architecture: String = pydantic.Field(None, alias="Architecture")
    description: String = pydantic.Field(None, alias="Description")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    hypervisor: String = pydantic.Field(None, alias="Hypervisor")
    image_id: String = pydantic.Field(None, alias="ImageId")
    import_task_id: ImportImageTaskId = pydantic.Field(None, alias="ImportTaskId")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    license_type: String = pydantic.Field(None, alias="LicenseType")
    platform: String = pydantic.Field(None, alias="Platform")
    progress: String = pydantic.Field(None, alias="Progress")
    snapshot_details: SnapshotDetailList = pydantic.Field(None, alias="SnapshotDetails")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    license_specifications: ImportImageLicenseSpecificationListResponse = pydantic.Field(None, alias="LicenseSpecifications")
    tags: TagList = pydantic.Field(None, alias="Tags")
    usage_operation: String = pydantic.Field(None, alias="UsageOperation")

class ImportImageTask(_EC2ModelBase):
    architecture: String = pydantic.Field(None, alias="Architecture")
    description: String = pydantic.Field(None, alias="Description")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    hypervisor: String = pydantic.Field(None, alias="Hypervisor")
    image_id: String = pydantic.Field(None, alias="ImageId")
    import_task_id: String = pydantic.Field(None, alias="ImportTaskId")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    license_type: String = pydantic.Field(None, alias="LicenseType")
    platform: String = pydantic.Field(None, alias="Platform")
    progress: String = pydantic.Field(None, alias="Progress")
    snapshot_details: SnapshotDetailList = pydantic.Field(None, alias="SnapshotDetails")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    tags: TagList = pydantic.Field(None, alias="Tags")
    license_specifications: ImportImageLicenseSpecificationListResponse = pydantic.Field(None, alias="LicenseSpecifications")
    usage_operation: String = pydantic.Field(None, alias="UsageOperation")
    boot_mode: BootModeValues = pydantic.Field(None, alias="BootMode")

class ImportInstanceLaunchSpecification(_EC2ModelBase):
    additional_info: String = pydantic.Field(None, alias="AdditionalInfo")
    architecture: ArchitectureValues = pydantic.Field(None, alias="Architecture")
    group_ids: SecurityGroupIdStringList = pydantic.Field(None, alias="GroupIds")
    group_names: SecurityGroupStringList = pydantic.Field(None, alias="GroupNames")
    instance_initiated_shutdown_behavior: ShutdownBehavior = pydantic.Field(None, alias="InstanceInitiatedShutdownBehavior")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    monitoring: Boolean = pydantic.Field(None, alias="Monitoring")
    placement: 'Placement' = pydantic.Field(None, alias="Placement")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    user_data: 'UserData' = pydantic.Field(None, alias="UserData")

class ImportInstanceRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    disk_images: DiskImageList = pydantic.Field(None, alias="DiskImages")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    launch_specification: 'ImportInstanceLaunchSpecification' = pydantic.Field(None, alias="LaunchSpecification")
    platform: PlatformValues = pydantic.Field(None, alias="Platform")

class ImportInstanceResult(_EC2ModelBase):
    conversion_task: 'ConversionTask' = pydantic.Field(None, alias="ConversionTask")

class ImportInstanceTaskDetails(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    platform: PlatformValues = pydantic.Field(None, alias="Platform")
    volumes: ImportInstanceVolumeDetailSet = pydantic.Field(None, alias="Volumes")

class ImportInstanceVolumeDetailItem(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    bytes_converted: Long = pydantic.Field(None, alias="BytesConverted")
    description: String = pydantic.Field(None, alias="Description")
    image: 'DiskImageDescription' = pydantic.Field(None, alias="Image")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    volume: 'DiskImageVolumeDescription' = pydantic.Field(None, alias="Volume")

class ImportKeyPairRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    key_name: String = pydantic.Field(None, alias="KeyName")
    public_key_material: Blob = pydantic.Field(None, alias="PublicKeyMaterial")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class ImportKeyPairResult(_EC2ModelBase):
    key_fingerprint: String = pydantic.Field(None, alias="KeyFingerprint")
    key_name: String = pydantic.Field(None, alias="KeyName")
    key_pair_id: String = pydantic.Field(None, alias="KeyPairId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ImportSnapshotRequest(_EC2ModelBase):
    client_data: 'ClientData' = pydantic.Field(None, alias="ClientData")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    description: String = pydantic.Field(None, alias="Description")
    disk_container: 'SnapshotDiskContainer' = pydantic.Field(None, alias="DiskContainer")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    role_name: String = pydantic.Field(None, alias="RoleName")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class ImportSnapshotResult(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    import_task_id: String = pydantic.Field(None, alias="ImportTaskId")
    snapshot_task_detail: 'SnapshotTaskDetail' = pydantic.Field(None, alias="SnapshotTaskDetail")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ImportSnapshotTask(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    import_task_id: String = pydantic.Field(None, alias="ImportTaskId")
    snapshot_task_detail: 'SnapshotTaskDetail' = pydantic.Field(None, alias="SnapshotTaskDetail")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ImportVolumeRequest(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    image: 'DiskImageDetail' = pydantic.Field(None, alias="Image")
    volume: 'VolumeDetail' = pydantic.Field(None, alias="Volume")

class ImportVolumeResult(_EC2ModelBase):
    conversion_task: 'ConversionTask' = pydantic.Field(None, alias="ConversionTask")

class ImportVolumeTaskDetails(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    bytes_converted: Long = pydantic.Field(None, alias="BytesConverted")
    description: String = pydantic.Field(None, alias="Description")
    image: 'DiskImageDescription' = pydantic.Field(None, alias="Image")
    volume: 'DiskImageVolumeDescription' = pydantic.Field(None, alias="Volume")

class InferenceAcceleratorInfo(_EC2ModelBase):
    accelerators: InferenceDeviceInfoList = pydantic.Field(None, alias="Accelerators")

class InferenceDeviceInfo(_EC2ModelBase):
    count: InferenceDeviceCount = pydantic.Field(None, alias="Count")
    name: InferenceDeviceName = pydantic.Field(None, alias="Name")
    manufacturer: InferenceDeviceManufacturerName = pydantic.Field(None, alias="Manufacturer")

class Instance(_EC2ModelBase):
    ami_launch_index: Integer = pydantic.Field(None, alias="AmiLaunchIndex")
    image_id: String = pydantic.Field(None, alias="ImageId")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    kernel_id: String = pydantic.Field(None, alias="KernelId")
    key_name: String = pydantic.Field(None, alias="KeyName")
    launch_time: DateTime = pydantic.Field(None, alias="LaunchTime")
    monitoring: 'Monitoring' = pydantic.Field(None, alias="Monitoring")
    placement: 'Placement' = pydantic.Field(None, alias="Placement")
    platform: PlatformValues = pydantic.Field(None, alias="Platform")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    public_dns_name: String = pydantic.Field(None, alias="PublicDnsName")
    public_ip_address: String = pydantic.Field(None, alias="PublicIpAddress")
    ramdisk_id: String = pydantic.Field(None, alias="RamdiskId")
    state: 'InstanceState' = pydantic.Field(None, alias="State")
    state_transition_reason: String = pydantic.Field(None, alias="StateTransitionReason")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    architecture: ArchitectureValues = pydantic.Field(None, alias="Architecture")
    block_device_mappings: InstanceBlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    ena_support: Boolean = pydantic.Field(None, alias="EnaSupport")
    hypervisor: HypervisorType = pydantic.Field(None, alias="Hypervisor")
    iam_instance_profile: 'IamInstanceProfile' = pydantic.Field(None, alias="IamInstanceProfile")
    instance_lifecycle: InstanceLifecycleType = pydantic.Field(None, alias="InstanceLifecycle")
    elastic_gpu_associations: ElasticGpuAssociationList = pydantic.Field(None, alias="ElasticGpuAssociations")
    elastic_inference_accelerator_associations: ElasticInferenceAcceleratorAssociationList = pydantic.Field(None, alias="ElasticInferenceAcceleratorAssociations")
    network_interfaces: InstanceNetworkInterfaceList = pydantic.Field(None, alias="NetworkInterfaces")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    root_device_name: String = pydantic.Field(None, alias="RootDeviceName")
    root_device_type: DeviceType = pydantic.Field(None, alias="RootDeviceType")
    security_groups: GroupIdentifierList = pydantic.Field(None, alias="SecurityGroups")
    source_dest_check: Boolean = pydantic.Field(None, alias="SourceDestCheck")
    spot_instance_request_id: String = pydantic.Field(None, alias="SpotInstanceRequestId")
    sriov_net_support: String = pydantic.Field(None, alias="SriovNetSupport")
    state_reason: 'StateReason' = pydantic.Field(None, alias="StateReason")
    tags: TagList = pydantic.Field(None, alias="Tags")
    virtualization_type: VirtualizationType = pydantic.Field(None, alias="VirtualizationType")
    cpu_options: 'CpuOptions' = pydantic.Field(None, alias="CpuOptions")
    capacity_reservation_id: String = pydantic.Field(None, alias="CapacityReservationId")
    capacity_reservation_specification: 'CapacityReservationSpecificationResponse' = pydantic.Field(None, alias="CapacityReservationSpecification")
    hibernation_options: 'HibernationOptions' = pydantic.Field(None, alias="HibernationOptions")
    licenses: LicenseList = pydantic.Field(None, alias="Licenses")
    metadata_options: 'InstanceMetadataOptionsResponse' = pydantic.Field(None, alias="MetadataOptions")
    enclave_options: 'EnclaveOptions' = pydantic.Field(None, alias="EnclaveOptions")
    boot_mode: BootModeValues = pydantic.Field(None, alias="BootMode")
    platform_details: String = pydantic.Field(None, alias="PlatformDetails")
    usage_operation: String = pydantic.Field(None, alias="UsageOperation")
    usage_operation_update_time: MillisecondDateTime = pydantic.Field(None, alias="UsageOperationUpdateTime")
    private_dns_name_options: 'PrivateDnsNameOptionsResponse' = pydantic.Field(None, alias="PrivateDnsNameOptions")
    ipv_6_address: String = pydantic.Field(None, alias="Ipv6Address")
    tpm_support: String = pydantic.Field(None, alias="TpmSupport")
    maintenance_options: 'InstanceMaintenanceOptions' = pydantic.Field(None, alias="MaintenanceOptions")
    current_instance_boot_mode: InstanceBootModeValues = pydantic.Field(None, alias="CurrentInstanceBootMode")

class InstanceAttribute(_EC2ModelBase):
    groups: GroupIdentifierList = pydantic.Field(None, alias="Groups")
    block_device_mappings: InstanceBlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    disable_api_termination: 'AttributeBooleanValue' = pydantic.Field(None, alias="DisableApiTermination")
    ena_support: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnaSupport")
    enclave_options: 'EnclaveOptions' = pydantic.Field(None, alias="EnclaveOptions")
    ebs_optimized: 'AttributeBooleanValue' = pydantic.Field(None, alias="EbsOptimized")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_initiated_shutdown_behavior: 'AttributeValue' = pydantic.Field(None, alias="InstanceInitiatedShutdownBehavior")
    instance_type: 'AttributeValue' = pydantic.Field(None, alias="InstanceType")
    kernel_id: 'AttributeValue' = pydantic.Field(None, alias="KernelId")
    product_codes: ProductCodeList = pydantic.Field(None, alias="ProductCodes")
    ramdisk_id: 'AttributeValue' = pydantic.Field(None, alias="RamdiskId")
    root_device_name: 'AttributeValue' = pydantic.Field(None, alias="RootDeviceName")
    source_dest_check: 'AttributeBooleanValue' = pydantic.Field(None, alias="SourceDestCheck")
    sriov_net_support: 'AttributeValue' = pydantic.Field(None, alias="SriovNetSupport")
    user_data: 'AttributeValue' = pydantic.Field(None, alias="UserData")
    disable_api_stop: 'AttributeBooleanValue' = pydantic.Field(None, alias="DisableApiStop")

class InstanceBlockDeviceMapping(_EC2ModelBase):
    device_name: String = pydantic.Field(None, alias="DeviceName")
    ebs: 'EbsInstanceBlockDevice' = pydantic.Field(None, alias="Ebs")

class InstanceBlockDeviceMappingSpecification(_EC2ModelBase):
    device_name: String = pydantic.Field(None, alias="DeviceName")
    ebs: 'EbsInstanceBlockDeviceSpecification' = pydantic.Field(None, alias="Ebs")
    no_device: String = pydantic.Field(None, alias="NoDevice")
    virtual_name: String = pydantic.Field(None, alias="VirtualName")

class InstanceCapacity(_EC2ModelBase):
    available_capacity: Integer = pydantic.Field(None, alias="AvailableCapacity")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    total_capacity: Integer = pydantic.Field(None, alias="TotalCapacity")

class InstanceCount(_EC2ModelBase):
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    state: ListingState = pydantic.Field(None, alias="State")

class InstanceCreditSpecification(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    cpu_credits: String = pydantic.Field(None, alias="CpuCredits")

class InstanceCreditSpecificationRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    cpu_credits: String = pydantic.Field(None, alias="CpuCredits")

class InstanceEventWindow(_EC2ModelBase):
    instance_event_window_id: InstanceEventWindowId = pydantic.Field(None, alias="InstanceEventWindowId")
    time_ranges: InstanceEventWindowTimeRangeList = pydantic.Field(None, alias="TimeRanges")
    name: String = pydantic.Field(None, alias="Name")
    cron_expression: InstanceEventWindowCronExpression = pydantic.Field(None, alias="CronExpression")
    association_target: 'InstanceEventWindowAssociationTarget' = pydantic.Field(None, alias="AssociationTarget")
    state: InstanceEventWindowState = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class InstanceEventWindowAssociationRequest(_EC2ModelBase):
    instance_ids: InstanceIdList = pydantic.Field(None, alias="InstanceIds")
    instance_tags: TagList = pydantic.Field(None, alias="InstanceTags")
    dedicated_host_ids: DedicatedHostIdList = pydantic.Field(None, alias="DedicatedHostIds")

class InstanceEventWindowAssociationTarget(_EC2ModelBase):
    instance_ids: InstanceIdList = pydantic.Field(None, alias="InstanceIds")
    tags: TagList = pydantic.Field(None, alias="Tags")
    dedicated_host_ids: DedicatedHostIdList = pydantic.Field(None, alias="DedicatedHostIds")

class InstanceEventWindowDisassociationRequest(_EC2ModelBase):
    instance_ids: InstanceIdList = pydantic.Field(None, alias="InstanceIds")
    instance_tags: TagList = pydantic.Field(None, alias="InstanceTags")
    dedicated_host_ids: DedicatedHostIdList = pydantic.Field(None, alias="DedicatedHostIds")

class InstanceEventWindowStateChange(_EC2ModelBase):
    instance_event_window_id: InstanceEventWindowId = pydantic.Field(None, alias="InstanceEventWindowId")
    state: InstanceEventWindowState = pydantic.Field(None, alias="State")

class InstanceEventWindowTimeRange(_EC2ModelBase):
    start_week_day: WeekDay = pydantic.Field(None, alias="StartWeekDay")
    start_hour: Hour = pydantic.Field(None, alias="StartHour")
    end_week_day: WeekDay = pydantic.Field(None, alias="EndWeekDay")
    end_hour: Hour = pydantic.Field(None, alias="EndHour")

class InstanceEventWindowTimeRangeRequest(_EC2ModelBase):
    start_week_day: WeekDay = pydantic.Field(None, alias="StartWeekDay")
    start_hour: Hour = pydantic.Field(None, alias="StartHour")
    end_week_day: WeekDay = pydantic.Field(None, alias="EndWeekDay")
    end_hour: Hour = pydantic.Field(None, alias="EndHour")

class InstanceExportDetails(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    target_environment: ExportEnvironment = pydantic.Field(None, alias="TargetEnvironment")

class InstanceFamilyCreditSpecification(_EC2ModelBase):
    instance_family: UnlimitedSupportedInstanceFamily = pydantic.Field(None, alias="InstanceFamily")
    cpu_credits: String = pydantic.Field(None, alias="CpuCredits")

class InstanceIpv4Prefix(_EC2ModelBase):
    ipv_4_prefix: String = pydantic.Field(None, alias="Ipv4Prefix")

class InstanceIpv6Address(_EC2ModelBase):
    ipv_6_address: String = pydantic.Field(None, alias="Ipv6Address")

class InstanceIpv6AddressRequest(_EC2ModelBase):
    ipv_6_address: String = pydantic.Field(None, alias="Ipv6Address")

class InstanceIpv6Prefix(_EC2ModelBase):
    ipv_6_prefix: String = pydantic.Field(None, alias="Ipv6Prefix")

class InstanceMaintenanceOptions(_EC2ModelBase):
    auto_recovery: InstanceAutoRecoveryState = pydantic.Field(None, alias="AutoRecovery")

class InstanceMaintenanceOptionsRequest(_EC2ModelBase):
    auto_recovery: InstanceAutoRecoveryState = pydantic.Field(None, alias="AutoRecovery")

class InstanceMarketOptionsRequest(_EC2ModelBase):
    market_type: MarketType = pydantic.Field(None, alias="MarketType")
    spot_options: 'SpotMarketOptions' = pydantic.Field(None, alias="SpotOptions")

class InstanceMetadataOptionsRequest(_EC2ModelBase):
    http_tokens: HttpTokensState = pydantic.Field(None, alias="HttpTokens")
    http_put_response_hop_limit: Integer = pydantic.Field(None, alias="HttpPutResponseHopLimit")
    http_endpoint: InstanceMetadataEndpointState = pydantic.Field(None, alias="HttpEndpoint")
    http_protocol_ipv_6: InstanceMetadataProtocolState = pydantic.Field(None, alias="HttpProtocolIpv6")
    instance_metadata_tags: InstanceMetadataTagsState = pydantic.Field(None, alias="InstanceMetadataTags")

class InstanceMetadataOptionsResponse(_EC2ModelBase):
    state: InstanceMetadataOptionsState = pydantic.Field(None, alias="State")
    http_tokens: HttpTokensState = pydantic.Field(None, alias="HttpTokens")
    http_put_response_hop_limit: Integer = pydantic.Field(None, alias="HttpPutResponseHopLimit")
    http_endpoint: InstanceMetadataEndpointState = pydantic.Field(None, alias="HttpEndpoint")
    http_protocol_ipv_6: InstanceMetadataProtocolState = pydantic.Field(None, alias="HttpProtocolIpv6")
    instance_metadata_tags: InstanceMetadataTagsState = pydantic.Field(None, alias="InstanceMetadataTags")

class InstanceMonitoring(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    monitoring: 'Monitoring' = pydantic.Field(None, alias="Monitoring")

class InstanceNetworkInterface(_EC2ModelBase):
    association: 'InstanceNetworkInterfaceAssociation' = pydantic.Field(None, alias="Association")
    attachment: 'InstanceNetworkInterfaceAttachment' = pydantic.Field(None, alias="Attachment")
    description: String = pydantic.Field(None, alias="Description")
    groups: GroupIdentifierList = pydantic.Field(None, alias="Groups")
    ipv_6_addresses: InstanceIpv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    mac_address: String = pydantic.Field(None, alias="MacAddress")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_addresses: InstancePrivateIpAddressList = pydantic.Field(None, alias="PrivateIpAddresses")
    source_dest_check: Boolean = pydantic.Field(None, alias="SourceDestCheck")
    status: NetworkInterfaceStatus = pydantic.Field(None, alias="Status")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    interface_type: String = pydantic.Field(None, alias="InterfaceType")
    ipv_4_prefixes: InstanceIpv4PrefixList = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_6_prefixes: InstanceIpv6PrefixList = pydantic.Field(None, alias="Ipv6Prefixes")

class InstanceNetworkInterfaceAssociation(_EC2ModelBase):
    carrier_ip: String = pydantic.Field(None, alias="CarrierIp")
    customer_owned_ip: String = pydantic.Field(None, alias="CustomerOwnedIp")
    ip_owner_id: String = pydantic.Field(None, alias="IpOwnerId")
    public_dns_name: String = pydantic.Field(None, alias="PublicDnsName")
    public_ip: String = pydantic.Field(None, alias="PublicIp")

class InstanceNetworkInterfaceAttachment(_EC2ModelBase):
    attach_time: DateTime = pydantic.Field(None, alias="AttachTime")
    attachment_id: String = pydantic.Field(None, alias="AttachmentId")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    status: AttachmentStatus = pydantic.Field(None, alias="Status")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")

class InstanceNetworkInterfaceSpecification(_EC2ModelBase):
    associate_public_ip_address: Boolean = pydantic.Field(None, alias="AssociatePublicIpAddress")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    description: String = pydantic.Field(None, alias="Description")
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    groups: SecurityGroupIdStringList = pydantic.Field(None, alias="Groups")
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: InstanceIpv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_addresses: PrivateIpAddressSpecificationList = pydantic.Field(None, alias="PrivateIpAddresses")
    secondary_private_ip_address_count: Integer = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    associate_carrier_ip_address: Boolean = pydantic.Field(None, alias="AssociateCarrierIpAddress")
    interface_type: String = pydantic.Field(None, alias="InterfaceType")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")
    ipv_4_prefixes: Ipv4PrefixList = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_4_prefix_count: Integer = pydantic.Field(None, alias="Ipv4PrefixCount")
    ipv_6_prefixes: Ipv6PrefixList = pydantic.Field(None, alias="Ipv6Prefixes")
    ipv_6_prefix_count: Integer = pydantic.Field(None, alias="Ipv6PrefixCount")

class InstancePrivateIpAddress(_EC2ModelBase):
    association: 'InstanceNetworkInterfaceAssociation' = pydantic.Field(None, alias="Association")
    primary: Boolean = pydantic.Field(None, alias="Primary")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")

class InstanceRequirements(_EC2ModelBase):
    v_cpu_count: 'VCpuCountRange' = pydantic.Field(None, alias="VCpuCount")
    memory_mi_b: 'MemoryMiB' = pydantic.Field(None, alias="MemoryMiB")
    cpu_manufacturers: CpuManufacturerSet = pydantic.Field(None, alias="CpuManufacturers")
    memory_gi_b_per_v_cpu: 'MemoryGiBPerVCpu' = pydantic.Field(None, alias="MemoryGiBPerVCpu")
    excluded_instance_types: ExcludedInstanceTypeSet = pydantic.Field(None, alias="ExcludedInstanceTypes")
    instance_generations: InstanceGenerationSet = pydantic.Field(None, alias="InstanceGenerations")
    spot_max_price_percentage_over_lowest_price: Integer = pydantic.Field(None, alias="SpotMaxPricePercentageOverLowestPrice")
    on_demand_max_price_percentage_over_lowest_price: Integer = pydantic.Field(None, alias="OnDemandMaxPricePercentageOverLowestPrice")
    bare_metal: BareMetal = pydantic.Field(None, alias="BareMetal")
    burstable_performance: BurstablePerformance = pydantic.Field(None, alias="BurstablePerformance")
    require_hibernate_support: Boolean = pydantic.Field(None, alias="RequireHibernateSupport")
    network_interface_count: 'NetworkInterfaceCount' = pydantic.Field(None, alias="NetworkInterfaceCount")
    local_storage: LocalStorage = pydantic.Field(None, alias="LocalStorage")
    local_storage_types: LocalStorageTypeSet = pydantic.Field(None, alias="LocalStorageTypes")
    total_local_storage_gb: 'TotalLocalStorageGB' = pydantic.Field(None, alias="TotalLocalStorageGB")
    baseline_ebs_bandwidth_mbps: 'BaselineEbsBandwidthMbps' = pydantic.Field(None, alias="BaselineEbsBandwidthMbps")
    accelerator_types: AcceleratorTypeSet = pydantic.Field(None, alias="AcceleratorTypes")
    accelerator_count: 'AcceleratorCount' = pydantic.Field(None, alias="AcceleratorCount")
    accelerator_manufacturers: AcceleratorManufacturerSet = pydantic.Field(None, alias="AcceleratorManufacturers")
    accelerator_names: AcceleratorNameSet = pydantic.Field(None, alias="AcceleratorNames")
    accelerator_total_memory_mi_b: 'AcceleratorTotalMemoryMiB' = pydantic.Field(None, alias="AcceleratorTotalMemoryMiB")
    network_bandwidth_gbps: 'NetworkBandwidthGbps' = pydantic.Field(None, alias="NetworkBandwidthGbps")
    allowed_instance_types: AllowedInstanceTypeSet = pydantic.Field(None, alias="AllowedInstanceTypes")

class InstanceRequirementsRequest(_EC2ModelBase):
    v_cpu_count: 'VCpuCountRangeRequest' = pydantic.Field(None, alias="VCpuCount")
    memory_mi_b: 'MemoryMiBRequest' = pydantic.Field(None, alias="MemoryMiB")
    cpu_manufacturers: CpuManufacturerSet = pydantic.Field(None, alias="CpuManufacturers")
    memory_gi_b_per_v_cpu: 'MemoryGiBPerVCpuRequest' = pydantic.Field(None, alias="MemoryGiBPerVCpu")
    excluded_instance_types: ExcludedInstanceTypeSet = pydantic.Field(None, alias="ExcludedInstanceTypes")
    instance_generations: InstanceGenerationSet = pydantic.Field(None, alias="InstanceGenerations")
    spot_max_price_percentage_over_lowest_price: Integer = pydantic.Field(None, alias="SpotMaxPricePercentageOverLowestPrice")
    on_demand_max_price_percentage_over_lowest_price: Integer = pydantic.Field(None, alias="OnDemandMaxPricePercentageOverLowestPrice")
    bare_metal: BareMetal = pydantic.Field(None, alias="BareMetal")
    burstable_performance: BurstablePerformance = pydantic.Field(None, alias="BurstablePerformance")
    require_hibernate_support: Boolean = pydantic.Field(None, alias="RequireHibernateSupport")
    network_interface_count: 'NetworkInterfaceCountRequest' = pydantic.Field(None, alias="NetworkInterfaceCount")
    local_storage: LocalStorage = pydantic.Field(None, alias="LocalStorage")
    local_storage_types: LocalStorageTypeSet = pydantic.Field(None, alias="LocalStorageTypes")
    total_local_storage_gb: 'TotalLocalStorageGBRequest' = pydantic.Field(None, alias="TotalLocalStorageGB")
    baseline_ebs_bandwidth_mbps: 'BaselineEbsBandwidthMbpsRequest' = pydantic.Field(None, alias="BaselineEbsBandwidthMbps")
    accelerator_types: AcceleratorTypeSet = pydantic.Field(None, alias="AcceleratorTypes")
    accelerator_count: 'AcceleratorCountRequest' = pydantic.Field(None, alias="AcceleratorCount")
    accelerator_manufacturers: AcceleratorManufacturerSet = pydantic.Field(None, alias="AcceleratorManufacturers")
    accelerator_names: AcceleratorNameSet = pydantic.Field(None, alias="AcceleratorNames")
    accelerator_total_memory_mi_b: 'AcceleratorTotalMemoryMiBRequest' = pydantic.Field(None, alias="AcceleratorTotalMemoryMiB")
    network_bandwidth_gbps: 'NetworkBandwidthGbpsRequest' = pydantic.Field(None, alias="NetworkBandwidthGbps")
    allowed_instance_types: AllowedInstanceTypeSet = pydantic.Field(None, alias="AllowedInstanceTypes")

class InstanceRequirementsWithMetadataRequest(_EC2ModelBase):
    architecture_types: ArchitectureTypeSet = pydantic.Field(None, alias="ArchitectureTypes")
    virtualization_types: VirtualizationTypeSet = pydantic.Field(None, alias="VirtualizationTypes")
    instance_requirements: 'InstanceRequirementsRequest' = pydantic.Field(None, alias="InstanceRequirements")

class InstanceSpecification(_EC2ModelBase):
    instance_id: InstanceIdWithVolumeResolver = pydantic.Field(None, alias="InstanceId")
    exclude_boot_volume: Boolean = pydantic.Field(None, alias="ExcludeBootVolume")
    exclude_data_volume_ids: VolumeIdStringList = pydantic.Field(None, alias="ExcludeDataVolumeIds")

class InstanceState(_EC2ModelBase):
    code: Integer = pydantic.Field(None, alias="Code")
    name: InstanceStateName = pydantic.Field(None, alias="Name")

class InstanceStateChange(_EC2ModelBase):
    current_state: 'InstanceState' = pydantic.Field(None, alias="CurrentState")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    previous_state: 'InstanceState' = pydantic.Field(None, alias="PreviousState")

class InstanceStatus(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    events: InstanceStatusEventList = pydantic.Field(None, alias="Events")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_state: 'InstanceState' = pydantic.Field(None, alias="InstanceState")
    instance_status: 'InstanceStatusSummary' = pydantic.Field(None, alias="InstanceStatus")
    system_status: 'InstanceStatusSummary' = pydantic.Field(None, alias="SystemStatus")

class InstanceStatusDetails(_EC2ModelBase):
    impaired_since: DateTime = pydantic.Field(None, alias="ImpairedSince")
    name: StatusName = pydantic.Field(None, alias="Name")
    status: StatusType = pydantic.Field(None, alias="Status")

class InstanceStatusEvent(_EC2ModelBase):
    instance_event_id: InstanceEventId = pydantic.Field(None, alias="InstanceEventId")
    code: EventCode = pydantic.Field(None, alias="Code")
    description: String = pydantic.Field(None, alias="Description")
    not_after: DateTime = pydantic.Field(None, alias="NotAfter")
    not_before: DateTime = pydantic.Field(None, alias="NotBefore")
    not_before_deadline: DateTime = pydantic.Field(None, alias="NotBeforeDeadline")

class InstanceStatusSummary(_EC2ModelBase):
    details: InstanceStatusDetailsList = pydantic.Field(None, alias="Details")
    status: SummaryStatus = pydantic.Field(None, alias="Status")

class InstanceStorageInfo(_EC2ModelBase):
    total_size_in_gb: DiskSize = pydantic.Field(None, alias="TotalSizeInGB")
    disks: DiskInfoList = pydantic.Field(None, alias="Disks")
    nvme_support: EphemeralNvmeSupport = pydantic.Field(None, alias="NvmeSupport")
    encryption_support: InstanceStorageEncryptionSupport = pydantic.Field(None, alias="EncryptionSupport")

class InstanceTagNotificationAttribute(_EC2ModelBase):
    instance_tag_keys: InstanceTagKeySet = pydantic.Field(None, alias="InstanceTagKeys")
    include_all_tags_of_instance: Boolean = pydantic.Field(None, alias="IncludeAllTagsOfInstance")

class InstanceTypeInfo(_EC2ModelBase):
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    current_generation: CurrentGenerationFlag = pydantic.Field(None, alias="CurrentGeneration")
    free_tier_eligible: FreeTierEligibleFlag = pydantic.Field(None, alias="FreeTierEligible")
    supported_usage_classes: UsageClassTypeList = pydantic.Field(None, alias="SupportedUsageClasses")
    supported_root_device_types: RootDeviceTypeList = pydantic.Field(None, alias="SupportedRootDeviceTypes")
    supported_virtualization_types: VirtualizationTypeList = pydantic.Field(None, alias="SupportedVirtualizationTypes")
    bare_metal: BareMetalFlag = pydantic.Field(None, alias="BareMetal")
    hypervisor: InstanceTypeHypervisor = pydantic.Field(None, alias="Hypervisor")
    processor_info: 'ProcessorInfo' = pydantic.Field(None, alias="ProcessorInfo")
    v_cpu_info: 'VCpuInfo' = pydantic.Field(None, alias="VCpuInfo")
    memory_info: 'MemoryInfo' = pydantic.Field(None, alias="MemoryInfo")
    instance_storage_supported: InstanceStorageFlag = pydantic.Field(None, alias="InstanceStorageSupported")
    instance_storage_info: 'InstanceStorageInfo' = pydantic.Field(None, alias="InstanceStorageInfo")
    ebs_info: 'EbsInfo' = pydantic.Field(None, alias="EbsInfo")
    network_info: 'NetworkInfo' = pydantic.Field(None, alias="NetworkInfo")
    gpu_info: 'GpuInfo' = pydantic.Field(None, alias="GpuInfo")
    fpga_info: 'FpgaInfo' = pydantic.Field(None, alias="FpgaInfo")
    placement_group_info: 'PlacementGroupInfo' = pydantic.Field(None, alias="PlacementGroupInfo")
    inference_accelerator_info: 'InferenceAcceleratorInfo' = pydantic.Field(None, alias="InferenceAcceleratorInfo")
    hibernation_supported: HibernationFlag = pydantic.Field(None, alias="HibernationSupported")
    burstable_performance_supported: BurstablePerformanceFlag = pydantic.Field(None, alias="BurstablePerformanceSupported")
    dedicated_hosts_supported: DedicatedHostFlag = pydantic.Field(None, alias="DedicatedHostsSupported")
    auto_recovery_supported: AutoRecoveryFlag = pydantic.Field(None, alias="AutoRecoverySupported")
    supported_boot_modes: BootModeTypeList = pydantic.Field(None, alias="SupportedBootModes")

class InstanceTypeInfoFromInstanceRequirements(_EC2ModelBase):
    instance_type: String = pydantic.Field(None, alias="InstanceType")

class InstanceTypeOffering(_EC2ModelBase):
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    location_type: LocationType = pydantic.Field(None, alias="LocationType")
    location: Location = pydantic.Field(None, alias="Location")

class InstanceUsage(_EC2ModelBase):
    account_id: String = pydantic.Field(None, alias="AccountId")
    used_instance_count: Integer = pydantic.Field(None, alias="UsedInstanceCount")

class IntegrateServices(_EC2ModelBase):
    athena_integrations: AthenaIntegrationsSet = pydantic.Field(None, alias="AthenaIntegrations")

class InternetGateway(_EC2ModelBase):
    attachments: InternetGatewayAttachmentList = pydantic.Field(None, alias="Attachments")
    internet_gateway_id: String = pydantic.Field(None, alias="InternetGatewayId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class InternetGatewayAttachment(_EC2ModelBase):
    state: AttachmentStatus = pydantic.Field(None, alias="State")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class IpPermission(_EC2ModelBase):
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    ip_ranges: IpRangeList = pydantic.Field(None, alias="IpRanges")
    ipv_6_ranges: Ipv6RangeList = pydantic.Field(None, alias="Ipv6Ranges")
    prefix_list_ids: PrefixListIdList = pydantic.Field(None, alias="PrefixListIds")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    user_id_group_pairs: UserIdGroupPairList = pydantic.Field(None, alias="UserIdGroupPairs")

class IpRange(_EC2ModelBase):
    cidr_ip: String = pydantic.Field(None, alias="CidrIp")
    description: String = pydantic.Field(None, alias="Description")

class Ipam(_EC2ModelBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    ipam_arn: ResourceArn = pydantic.Field(None, alias="IpamArn")
    ipam_region: String = pydantic.Field(None, alias="IpamRegion")
    public_default_scope_id: IpamScopeId = pydantic.Field(None, alias="PublicDefaultScopeId")
    private_default_scope_id: IpamScopeId = pydantic.Field(None, alias="PrivateDefaultScopeId")
    scope_count: Integer = pydantic.Field(None, alias="ScopeCount")
    description: String = pydantic.Field(None, alias="Description")
    operating_regions: IpamOperatingRegionSet = pydantic.Field(None, alias="OperatingRegions")
    state: IpamState = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")
    default_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="DefaultResourceDiscoveryId")
    default_resource_discovery_association_id: IpamResourceDiscoveryAssociationId = pydantic.Field(None, alias="DefaultResourceDiscoveryAssociationId")
    resource_discovery_association_count: Integer = pydantic.Field(None, alias="ResourceDiscoveryAssociationCount")

class IpamAddressHistoryRecord(_EC2ModelBase):
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    resource_region: String = pydantic.Field(None, alias="ResourceRegion")
    resource_type: IpamAddressHistoryResourceType = pydantic.Field(None, alias="ResourceType")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_cidr: String = pydantic.Field(None, alias="ResourceCidr")
    resource_name: String = pydantic.Field(None, alias="ResourceName")
    resource_compliance_status: IpamComplianceStatus = pydantic.Field(None, alias="ResourceComplianceStatus")
    resource_overlap_status: IpamOverlapStatus = pydantic.Field(None, alias="ResourceOverlapStatus")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    sampled_start_time: MillisecondDateTime = pydantic.Field(None, alias="SampledStartTime")
    sampled_end_time: MillisecondDateTime = pydantic.Field(None, alias="SampledEndTime")

class IpamCidrAuthorizationContext(_EC2ModelBase):
    message: String = pydantic.Field(None, alias="Message")
    signature: String = pydantic.Field(None, alias="Signature")

class IpamDiscoveredAccount(_EC2ModelBase):
    account_id: String = pydantic.Field(None, alias="AccountId")
    discovery_region: String = pydantic.Field(None, alias="DiscoveryRegion")
    failure_reason: 'IpamDiscoveryFailureReason' = pydantic.Field(None, alias="FailureReason")
    last_attempted_discovery_time: MillisecondDateTime = pydantic.Field(None, alias="LastAttemptedDiscoveryTime")
    last_successful_discovery_time: MillisecondDateTime = pydantic.Field(None, alias="LastSuccessfulDiscoveryTime")

class IpamDiscoveredResourceCidr(_EC2ModelBase):
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    resource_region: String = pydantic.Field(None, alias="ResourceRegion")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    resource_cidr: String = pydantic.Field(None, alias="ResourceCidr")
    resource_type: IpamResourceType = pydantic.Field(None, alias="ResourceType")
    resource_tags: IpamResourceTagList = pydantic.Field(None, alias="ResourceTags")
    ip_usage: BoxedDouble = pydantic.Field(None, alias="IpUsage")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    sample_time: MillisecondDateTime = pydantic.Field(None, alias="SampleTime")

class IpamDiscoveryFailureReason(_EC2ModelBase):
    code: IpamDiscoveryFailureCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class IpamOperatingRegion(_EC2ModelBase):
    region_name: String = pydantic.Field(None, alias="RegionName")

class IpamPool(_EC2ModelBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    source_ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="SourceIpamPoolId")
    ipam_pool_arn: ResourceArn = pydantic.Field(None, alias="IpamPoolArn")
    ipam_scope_arn: ResourceArn = pydantic.Field(None, alias="IpamScopeArn")
    ipam_scope_type: IpamScopeType = pydantic.Field(None, alias="IpamScopeType")
    ipam_arn: ResourceArn = pydantic.Field(None, alias="IpamArn")
    ipam_region: String = pydantic.Field(None, alias="IpamRegion")
    locale: String = pydantic.Field(None, alias="Locale")
    pool_depth: Integer = pydantic.Field(None, alias="PoolDepth")
    state: IpamPoolState = pydantic.Field(None, alias="State")
    state_message: String = pydantic.Field(None, alias="StateMessage")
    description: String = pydantic.Field(None, alias="Description")
    auto_import: Boolean = pydantic.Field(None, alias="AutoImport")
    publicly_advertisable: Boolean = pydantic.Field(None, alias="PubliclyAdvertisable")
    address_family: AddressFamily = pydantic.Field(None, alias="AddressFamily")
    allocation_min_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationMinNetmaskLength")
    allocation_max_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationMaxNetmaskLength")
    allocation_default_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationDefaultNetmaskLength")
    allocation_resource_tags: IpamResourceTagList = pydantic.Field(None, alias="AllocationResourceTags")
    tags: TagList = pydantic.Field(None, alias="Tags")
    aws_service: IpamPoolAwsService = pydantic.Field(None, alias="AwsService")
    public_ip_source: IpamPoolPublicIpSource = pydantic.Field(None, alias="PublicIpSource")

class IpamPoolAllocation(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    ipam_pool_allocation_id: IpamPoolAllocationId = pydantic.Field(None, alias="IpamPoolAllocationId")
    description: String = pydantic.Field(None, alias="Description")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: IpamPoolAllocationResourceType = pydantic.Field(None, alias="ResourceType")
    resource_region: String = pydantic.Field(None, alias="ResourceRegion")
    resource_owner: String = pydantic.Field(None, alias="ResourceOwner")

class IpamPoolCidr(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    state: IpamPoolCidrState = pydantic.Field(None, alias="State")
    failure_reason: 'IpamPoolCidrFailureReason' = pydantic.Field(None, alias="FailureReason")
    ipam_pool_cidr_id: IpamPoolCidrId = pydantic.Field(None, alias="IpamPoolCidrId")
    netmask_length: Integer = pydantic.Field(None, alias="NetmaskLength")

class IpamPoolCidrFailureReason(_EC2ModelBase):
    code: IpamPoolCidrFailureCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class IpamResourceCidr(_EC2ModelBase):
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    resource_region: String = pydantic.Field(None, alias="ResourceRegion")
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_name: String = pydantic.Field(None, alias="ResourceName")
    resource_cidr: String = pydantic.Field(None, alias="ResourceCidr")
    resource_type: IpamResourceType = pydantic.Field(None, alias="ResourceType")
    resource_tags: IpamResourceTagList = pydantic.Field(None, alias="ResourceTags")
    ip_usage: BoxedDouble = pydantic.Field(None, alias="IpUsage")
    compliance_status: IpamComplianceStatus = pydantic.Field(None, alias="ComplianceStatus")
    management_state: IpamManagementState = pydantic.Field(None, alias="ManagementState")
    overlap_status: IpamOverlapStatus = pydantic.Field(None, alias="OverlapStatus")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class IpamResourceDiscovery(_EC2ModelBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    ipam_resource_discovery_arn: String = pydantic.Field(None, alias="IpamResourceDiscoveryArn")
    ipam_resource_discovery_region: String = pydantic.Field(None, alias="IpamResourceDiscoveryRegion")
    description: String = pydantic.Field(None, alias="Description")
    operating_regions: IpamOperatingRegionSet = pydantic.Field(None, alias="OperatingRegions")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")
    state: IpamResourceDiscoveryState = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class IpamResourceDiscoveryAssociation(_EC2ModelBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    ipam_resource_discovery_association_id: IpamResourceDiscoveryAssociationId = pydantic.Field(None, alias="IpamResourceDiscoveryAssociationId")
    ipam_resource_discovery_association_arn: String = pydantic.Field(None, alias="IpamResourceDiscoveryAssociationArn")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    ipam_arn: ResourceArn = pydantic.Field(None, alias="IpamArn")
    ipam_region: String = pydantic.Field(None, alias="IpamRegion")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")
    resource_discovery_status: IpamAssociatedResourceDiscoveryStatus = pydantic.Field(None, alias="ResourceDiscoveryStatus")
    state: IpamResourceDiscoveryAssociationState = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class IpamResourceTag(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    value: String = pydantic.Field(None, alias="Value")

class IpamScope(_EC2ModelBase):
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")
    ipam_scope_arn: ResourceArn = pydantic.Field(None, alias="IpamScopeArn")
    ipam_arn: ResourceArn = pydantic.Field(None, alias="IpamArn")
    ipam_region: String = pydantic.Field(None, alias="IpamRegion")
    ipam_scope_type: IpamScopeType = pydantic.Field(None, alias="IpamScopeType")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")
    description: String = pydantic.Field(None, alias="Description")
    pool_count: Integer = pydantic.Field(None, alias="PoolCount")
    state: IpamScopeState = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class Ipv4PrefixSpecification(_EC2ModelBase):
    ipv_4_prefix: String = pydantic.Field(None, alias="Ipv4Prefix")

class Ipv4PrefixSpecificationRequest(_EC2ModelBase):
    ipv_4_prefix: String = pydantic.Field(None, alias="Ipv4Prefix")

class Ipv4PrefixSpecificationResponse(_EC2ModelBase):
    ipv_4_prefix: String = pydantic.Field(None, alias="Ipv4Prefix")

class Ipv6CidrAssociation(_EC2ModelBase):
    ipv_6_cidr: String = pydantic.Field(None, alias="Ipv6Cidr")
    associated_resource: String = pydantic.Field(None, alias="AssociatedResource")

class Ipv6CidrBlock(_EC2ModelBase):
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")

class Ipv6Pool(_EC2ModelBase):
    pool_id: String = pydantic.Field(None, alias="PoolId")
    description: String = pydantic.Field(None, alias="Description")
    pool_cidr_blocks: PoolCidrBlocksSet = pydantic.Field(None, alias="PoolCidrBlocks")
    tags: TagList = pydantic.Field(None, alias="Tags")

class Ipv6PrefixSpecification(_EC2ModelBase):
    ipv_6_prefix: String = pydantic.Field(None, alias="Ipv6Prefix")

class Ipv6PrefixSpecificationRequest(_EC2ModelBase):
    ipv_6_prefix: String = pydantic.Field(None, alias="Ipv6Prefix")

class Ipv6PrefixSpecificationResponse(_EC2ModelBase):
    ipv_6_prefix: String = pydantic.Field(None, alias="Ipv6Prefix")

class Ipv6Range(_EC2ModelBase):
    cidr_ipv_6: String = pydantic.Field(None, alias="CidrIpv6")
    description: String = pydantic.Field(None, alias="Description")

class KeyPair(_EC2ModelBase):
    key_fingerprint: String = pydantic.Field(None, alias="KeyFingerprint")
    key_material: SensitiveUserData = pydantic.Field(None, alias="KeyMaterial")
    key_name: String = pydantic.Field(None, alias="KeyName")
    key_pair_id: String = pydantic.Field(None, alias="KeyPairId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class KeyPairInfo(_EC2ModelBase):
    key_pair_id: String = pydantic.Field(None, alias="KeyPairId")
    key_fingerprint: String = pydantic.Field(None, alias="KeyFingerprint")
    key_name: String = pydantic.Field(None, alias="KeyName")
    key_type: KeyType = pydantic.Field(None, alias="KeyType")
    tags: TagList = pydantic.Field(None, alias="Tags")
    public_key: String = pydantic.Field(None, alias="PublicKey")
    create_time: MillisecondDateTime = pydantic.Field(None, alias="CreateTime")

class LastError(_EC2ModelBase):
    message: String = pydantic.Field(None, alias="Message")
    code: String = pydantic.Field(None, alias="Code")

class LaunchPermission(_EC2ModelBase):
    group: PermissionGroup = pydantic.Field(None, alias="Group")
    user_id: String = pydantic.Field(None, alias="UserId")
    organization_arn: String = pydantic.Field(None, alias="OrganizationArn")
    organizational_unit_arn: String = pydantic.Field(None, alias="OrganizationalUnitArn")

class LaunchPermissionModifications(_EC2ModelBase):
    add: LaunchPermissionList = pydantic.Field(None, alias="Add")
    remove: LaunchPermissionList = pydantic.Field(None, alias="Remove")

class LaunchSpecification(_EC2ModelBase):
    user_data: SensitiveUserData = pydantic.Field(None, alias="UserData")
    security_groups: GroupIdentifierList = pydantic.Field(None, alias="SecurityGroups")
    addressing_type: String = pydantic.Field(None, alias="AddressingType")
    block_device_mappings: BlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'IamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    image_id: String = pydantic.Field(None, alias="ImageId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    kernel_id: String = pydantic.Field(None, alias="KernelId")
    key_name: String = pydantic.Field(None, alias="KeyName")
    network_interfaces: InstanceNetworkInterfaceSpecificationList = pydantic.Field(None, alias="NetworkInterfaces")
    placement: 'SpotPlacement' = pydantic.Field(None, alias="Placement")
    ramdisk_id: String = pydantic.Field(None, alias="RamdiskId")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    monitoring: 'RunInstancesMonitoringEnabled' = pydantic.Field(None, alias="Monitoring")

class LaunchTemplate(_EC2ModelBase):
    launch_template_id: String = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    created_by: String = pydantic.Field(None, alias="CreatedBy")
    default_version_number: Long = pydantic.Field(None, alias="DefaultVersionNumber")
    latest_version_number: Long = pydantic.Field(None, alias="LatestVersionNumber")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LaunchTemplateAndOverridesResponse(_EC2ModelBase):
    launch_template_specification: 'FleetLaunchTemplateSpecification' = pydantic.Field(None, alias="LaunchTemplateSpecification")
    overrides: 'FleetLaunchTemplateOverrides' = pydantic.Field(None, alias="Overrides")

class LaunchTemplateBlockDeviceMapping(_EC2ModelBase):
    device_name: String = pydantic.Field(None, alias="DeviceName")
    virtual_name: String = pydantic.Field(None, alias="VirtualName")
    ebs: 'LaunchTemplateEbsBlockDevice' = pydantic.Field(None, alias="Ebs")
    no_device: String = pydantic.Field(None, alias="NoDevice")

class LaunchTemplateBlockDeviceMappingRequest(_EC2ModelBase):
    device_name: String = pydantic.Field(None, alias="DeviceName")
    virtual_name: String = pydantic.Field(None, alias="VirtualName")
    ebs: 'LaunchTemplateEbsBlockDeviceRequest' = pydantic.Field(None, alias="Ebs")
    no_device: String = pydantic.Field(None, alias="NoDevice")

class LaunchTemplateCapacityReservationSpecificationRequest(_EC2ModelBase):
    capacity_reservation_preference: CapacityReservationPreference = pydantic.Field(None, alias="CapacityReservationPreference")
    capacity_reservation_target: 'CapacityReservationTarget' = pydantic.Field(None, alias="CapacityReservationTarget")

class LaunchTemplateCapacityReservationSpecificationResponse(_EC2ModelBase):
    capacity_reservation_preference: CapacityReservationPreference = pydantic.Field(None, alias="CapacityReservationPreference")
    capacity_reservation_target: 'CapacityReservationTargetResponse' = pydantic.Field(None, alias="CapacityReservationTarget")

class LaunchTemplateConfig(_EC2ModelBase):
    launch_template_specification: 'FleetLaunchTemplateSpecification' = pydantic.Field(None, alias="LaunchTemplateSpecification")
    overrides: LaunchTemplateOverridesList = pydantic.Field(None, alias="Overrides")

class LaunchTemplateCpuOptions(_EC2ModelBase):
    core_count: Integer = pydantic.Field(None, alias="CoreCount")
    threads_per_core: Integer = pydantic.Field(None, alias="ThreadsPerCore")
    amd_sev_snp: AmdSevSnpSpecification = pydantic.Field(None, alias="AmdSevSnp")

class LaunchTemplateCpuOptionsRequest(_EC2ModelBase):
    core_count: Integer = pydantic.Field(None, alias="CoreCount")
    threads_per_core: Integer = pydantic.Field(None, alias="ThreadsPerCore")
    amd_sev_snp: AmdSevSnpSpecification = pydantic.Field(None, alias="AmdSevSnp")

class LaunchTemplateEbsBlockDevice(_EC2ModelBase):
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    iops: Integer = pydantic.Field(None, alias="Iops")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")
    volume_type: VolumeType = pydantic.Field(None, alias="VolumeType")
    throughput: Integer = pydantic.Field(None, alias="Throughput")

class LaunchTemplateEbsBlockDeviceRequest(_EC2ModelBase):
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    iops: Integer = pydantic.Field(None, alias="Iops")
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")
    volume_type: VolumeType = pydantic.Field(None, alias="VolumeType")
    throughput: Integer = pydantic.Field(None, alias="Throughput")

class LaunchTemplateElasticInferenceAccelerator(_EC2ModelBase):
    type: String = pydantic.Field(None, alias="Type")
    count: LaunchTemplateElasticInferenceAcceleratorCount = pydantic.Field(None, alias="Count")

class LaunchTemplateElasticInferenceAcceleratorResponse(_EC2ModelBase):
    type: String = pydantic.Field(None, alias="Type")
    count: Integer = pydantic.Field(None, alias="Count")

class LaunchTemplateEnclaveOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class LaunchTemplateEnclaveOptionsRequest(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class LaunchTemplateHibernationOptions(_EC2ModelBase):
    configured: Boolean = pydantic.Field(None, alias="Configured")

class LaunchTemplateHibernationOptionsRequest(_EC2ModelBase):
    configured: Boolean = pydantic.Field(None, alias="Configured")

class LaunchTemplateIamInstanceProfileSpecification(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")
    name: String = pydantic.Field(None, alias="Name")

class LaunchTemplateIamInstanceProfileSpecificationRequest(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")
    name: String = pydantic.Field(None, alias="Name")

class LaunchTemplateInstanceMaintenanceOptions(_EC2ModelBase):
    auto_recovery: LaunchTemplateAutoRecoveryState = pydantic.Field(None, alias="AutoRecovery")

class LaunchTemplateInstanceMaintenanceOptionsRequest(_EC2ModelBase):
    auto_recovery: LaunchTemplateAutoRecoveryState = pydantic.Field(None, alias="AutoRecovery")

class LaunchTemplateInstanceMarketOptions(_EC2ModelBase):
    market_type: MarketType = pydantic.Field(None, alias="MarketType")
    spot_options: 'LaunchTemplateSpotMarketOptions' = pydantic.Field(None, alias="SpotOptions")

class LaunchTemplateInstanceMarketOptionsRequest(_EC2ModelBase):
    market_type: MarketType = pydantic.Field(None, alias="MarketType")
    spot_options: 'LaunchTemplateSpotMarketOptionsRequest' = pydantic.Field(None, alias="SpotOptions")

class LaunchTemplateInstanceMetadataOptions(_EC2ModelBase):
    state: LaunchTemplateInstanceMetadataOptionsState = pydantic.Field(None, alias="State")
    http_tokens: LaunchTemplateHttpTokensState = pydantic.Field(None, alias="HttpTokens")
    http_put_response_hop_limit: Integer = pydantic.Field(None, alias="HttpPutResponseHopLimit")
    http_endpoint: LaunchTemplateInstanceMetadataEndpointState = pydantic.Field(None, alias="HttpEndpoint")
    http_protocol_ipv_6: LaunchTemplateInstanceMetadataProtocolIpv6 = pydantic.Field(None, alias="HttpProtocolIpv6")
    instance_metadata_tags: LaunchTemplateInstanceMetadataTagsState = pydantic.Field(None, alias="InstanceMetadataTags")

class LaunchTemplateInstanceMetadataOptionsRequest(_EC2ModelBase):
    http_tokens: LaunchTemplateHttpTokensState = pydantic.Field(None, alias="HttpTokens")
    http_put_response_hop_limit: Integer = pydantic.Field(None, alias="HttpPutResponseHopLimit")
    http_endpoint: LaunchTemplateInstanceMetadataEndpointState = pydantic.Field(None, alias="HttpEndpoint")
    http_protocol_ipv_6: LaunchTemplateInstanceMetadataProtocolIpv6 = pydantic.Field(None, alias="HttpProtocolIpv6")
    instance_metadata_tags: LaunchTemplateInstanceMetadataTagsState = pydantic.Field(None, alias="InstanceMetadataTags")

class LaunchTemplateInstanceNetworkInterfaceSpecification(_EC2ModelBase):
    associate_carrier_ip_address: Boolean = pydantic.Field(None, alias="AssociateCarrierIpAddress")
    associate_public_ip_address: Boolean = pydantic.Field(None, alias="AssociatePublicIpAddress")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    description: String = pydantic.Field(None, alias="Description")
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    groups: GroupIdStringList = pydantic.Field(None, alias="Groups")
    interface_type: String = pydantic.Field(None, alias="InterfaceType")
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: InstanceIpv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_addresses: PrivateIpAddressSpecificationList = pydantic.Field(None, alias="PrivateIpAddresses")
    secondary_private_ip_address_count: Integer = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")
    ipv_4_prefixes: Ipv4PrefixListResponse = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_4_prefix_count: Integer = pydantic.Field(None, alias="Ipv4PrefixCount")
    ipv_6_prefixes: Ipv6PrefixListResponse = pydantic.Field(None, alias="Ipv6Prefixes")
    ipv_6_prefix_count: Integer = pydantic.Field(None, alias="Ipv6PrefixCount")

class LaunchTemplateInstanceNetworkInterfaceSpecificationRequest(_EC2ModelBase):
    associate_carrier_ip_address: Boolean = pydantic.Field(None, alias="AssociateCarrierIpAddress")
    associate_public_ip_address: Boolean = pydantic.Field(None, alias="AssociatePublicIpAddress")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    description: String = pydantic.Field(None, alias="Description")
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    groups: SecurityGroupIdStringList = pydantic.Field(None, alias="Groups")
    interface_type: String = pydantic.Field(None, alias="InterfaceType")
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: InstanceIpv6AddressListRequest = pydantic.Field(None, alias="Ipv6Addresses")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_addresses: PrivateIpAddressSpecificationList = pydantic.Field(None, alias="PrivateIpAddresses")
    secondary_private_ip_address_count: Integer = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")
    ipv_4_prefixes: Ipv4PrefixList = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_4_prefix_count: Integer = pydantic.Field(None, alias="Ipv4PrefixCount")
    ipv_6_prefixes: Ipv6PrefixList = pydantic.Field(None, alias="Ipv6Prefixes")
    ipv_6_prefix_count: Integer = pydantic.Field(None, alias="Ipv6PrefixCount")

class LaunchTemplateLicenseConfiguration(_EC2ModelBase):
    license_configuration_arn: String = pydantic.Field(None, alias="LicenseConfigurationArn")

class LaunchTemplateLicenseConfigurationRequest(_EC2ModelBase):
    license_configuration_arn: String = pydantic.Field(None, alias="LicenseConfigurationArn")

class LaunchTemplateOverrides(_EC2ModelBase):
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    spot_price: String = pydantic.Field(None, alias="SpotPrice")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    weighted_capacity: Double = pydantic.Field(None, alias="WeightedCapacity")
    priority: Double = pydantic.Field(None, alias="Priority")
    instance_requirements: 'InstanceRequirements' = pydantic.Field(None, alias="InstanceRequirements")

class LaunchTemplatePlacement(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    affinity: String = pydantic.Field(None, alias="Affinity")
    group_name: String = pydantic.Field(None, alias="GroupName")
    host_id: String = pydantic.Field(None, alias="HostId")
    tenancy: Tenancy = pydantic.Field(None, alias="Tenancy")
    spread_domain: String = pydantic.Field(None, alias="SpreadDomain")
    host_resource_group_arn: String = pydantic.Field(None, alias="HostResourceGroupArn")
    partition_number: Integer = pydantic.Field(None, alias="PartitionNumber")
    group_id: PlacementGroupId = pydantic.Field(None, alias="GroupId")

class LaunchTemplatePlacementRequest(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    affinity: String = pydantic.Field(None, alias="Affinity")
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")
    host_id: DedicatedHostId = pydantic.Field(None, alias="HostId")
    tenancy: Tenancy = pydantic.Field(None, alias="Tenancy")
    spread_domain: String = pydantic.Field(None, alias="SpreadDomain")
    host_resource_group_arn: String = pydantic.Field(None, alias="HostResourceGroupArn")
    partition_number: Integer = pydantic.Field(None, alias="PartitionNumber")
    group_id: PlacementGroupId = pydantic.Field(None, alias="GroupId")

class LaunchTemplatePrivateDnsNameOptions(_EC2ModelBase):
    hostname_type: HostnameType = pydantic.Field(None, alias="HostnameType")
    enable_resource_name_dns_a_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsARecord")
    enable_resource_name_dns_aaaa_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecord")

class LaunchTemplatePrivateDnsNameOptionsRequest(_EC2ModelBase):
    hostname_type: HostnameType = pydantic.Field(None, alias="HostnameType")
    enable_resource_name_dns_a_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsARecord")
    enable_resource_name_dns_aaaa_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecord")

class LaunchTemplateSpecification(_EC2ModelBase):
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: String = pydantic.Field(None, alias="LaunchTemplateName")
    version: String = pydantic.Field(None, alias="Version")

class LaunchTemplateSpotMarketOptions(_EC2ModelBase):
    max_price: String = pydantic.Field(None, alias="MaxPrice")
    spot_instance_type: SpotInstanceType = pydantic.Field(None, alias="SpotInstanceType")
    block_duration_minutes: Integer = pydantic.Field(None, alias="BlockDurationMinutes")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    instance_interruption_behavior: InstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")

class LaunchTemplateSpotMarketOptionsRequest(_EC2ModelBase):
    max_price: String = pydantic.Field(None, alias="MaxPrice")
    spot_instance_type: SpotInstanceType = pydantic.Field(None, alias="SpotInstanceType")
    block_duration_minutes: Integer = pydantic.Field(None, alias="BlockDurationMinutes")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    instance_interruption_behavior: InstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")

class LaunchTemplateTagSpecification(_EC2ModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LaunchTemplateTagSpecificationRequest(_EC2ModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LaunchTemplateVersion(_EC2ModelBase):
    launch_template_id: String = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    version_number: Long = pydantic.Field(None, alias="VersionNumber")
    version_description: VersionDescription = pydantic.Field(None, alias="VersionDescription")
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    created_by: String = pydantic.Field(None, alias="CreatedBy")
    default_version: Boolean = pydantic.Field(None, alias="DefaultVersion")
    launch_template_data: 'ResponseLaunchTemplateData' = pydantic.Field(None, alias="LaunchTemplateData")

class LaunchTemplatesMonitoring(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class LaunchTemplatesMonitoringRequest(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class LicenseConfiguration(_EC2ModelBase):
    license_configuration_arn: String = pydantic.Field(None, alias="LicenseConfigurationArn")

class LicenseConfigurationRequest(_EC2ModelBase):
    license_configuration_arn: String = pydantic.Field(None, alias="LicenseConfigurationArn")

class ListImagesInRecycleBinRequest(_EC2ModelBase):
    image_ids: ImageIdStringList = pydantic.Field(None, alias="ImageIds")
    next_token: String = pydantic.Field(None, alias="NextToken")
    max_results: ListImagesInRecycleBinMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ListImagesInRecycleBinResult(_EC2ModelBase):
    images: ImageRecycleBinInfoList = pydantic.Field(None, alias="Images")
    next_token: String = pydantic.Field(None, alias="NextToken")

class ListSnapshotsInRecycleBinRequest(_EC2ModelBase):
    max_results: ListSnapshotsInRecycleBinMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    snapshot_ids: SnapshotIdStringList = pydantic.Field(None, alias="SnapshotIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ListSnapshotsInRecycleBinResult(_EC2ModelBase):
    snapshots: SnapshotRecycleBinInfoList = pydantic.Field(None, alias="Snapshots")
    next_token: String = pydantic.Field(None, alias="NextToken")

class LoadBalancersConfig(_EC2ModelBase):
    classic_load_balancers_config: 'ClassicLoadBalancersConfig' = pydantic.Field(None, alias="ClassicLoadBalancersConfig")
    target_groups_config: 'TargetGroupsConfig' = pydantic.Field(None, alias="TargetGroupsConfig")

class LoadPermission(_EC2ModelBase):
    user_id: String = pydantic.Field(None, alias="UserId")
    group: PermissionGroup = pydantic.Field(None, alias="Group")

class LoadPermissionModifications(_EC2ModelBase):
    add: LoadPermissionListRequest = pydantic.Field(None, alias="Add")
    remove: LoadPermissionListRequest = pydantic.Field(None, alias="Remove")

class LoadPermissionRequest(_EC2ModelBase):
    group: PermissionGroup = pydantic.Field(None, alias="Group")
    user_id: String = pydantic.Field(None, alias="UserId")

class LocalGateway(_EC2ModelBase):
    local_gateway_id: LocalGatewayId = pydantic.Field(None, alias="LocalGatewayId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: String = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LocalGatewayRoute(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    local_gateway_virtual_interface_group_id: LocalGatewayVirtualInterfaceGroupId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupId")
    type: LocalGatewayRouteType = pydantic.Field(None, alias="Type")
    state: LocalGatewayRouteState = pydantic.Field(None, alias="State")
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_route_table_arn: ResourceArn = pydantic.Field(None, alias="LocalGatewayRouteTableArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    coip_pool_id: CoipPoolId = pydantic.Field(None, alias="CoipPoolId")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")

class LocalGatewayRouteTable(_EC2ModelBase):
    local_gateway_route_table_id: String = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_route_table_arn: ResourceArn = pydantic.Field(None, alias="LocalGatewayRouteTableArn")
    local_gateway_id: LocalGatewayId = pydantic.Field(None, alias="LocalGatewayId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: String = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")
    mode: LocalGatewayRouteTableMode = pydantic.Field(None, alias="Mode")
    state_reason: 'StateReason' = pydantic.Field(None, alias="StateReason")

class LocalGatewayRouteTableVirtualInterfaceGroupAssociation(_EC2ModelBase):
    local_gateway_route_table_virtual_interface_group_association_id: LocalGatewayRouteTableVirtualInterfaceGroupAssociationId = pydantic.Field(None, alias="LocalGatewayRouteTableVirtualInterfaceGroupAssociationId")
    local_gateway_virtual_interface_group_id: LocalGatewayVirtualInterfaceGroupId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupId")
    local_gateway_id: String = pydantic.Field(None, alias="LocalGatewayId")
    local_gateway_route_table_id: LocalGatewayId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_route_table_arn: ResourceArn = pydantic.Field(None, alias="LocalGatewayRouteTableArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: String = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LocalGatewayRouteTableVpcAssociation(_EC2ModelBase):
    local_gateway_route_table_vpc_association_id: LocalGatewayRouteTableVpcAssociationId = pydantic.Field(None, alias="LocalGatewayRouteTableVpcAssociationId")
    local_gateway_route_table_id: String = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_route_table_arn: ResourceArn = pydantic.Field(None, alias="LocalGatewayRouteTableArn")
    local_gateway_id: String = pydantic.Field(None, alias="LocalGatewayId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    state: String = pydantic.Field(None, alias="State")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LocalGatewayVirtualInterface(_EC2ModelBase):
    local_gateway_virtual_interface_id: LocalGatewayVirtualInterfaceId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceId")
    local_gateway_id: String = pydantic.Field(None, alias="LocalGatewayId")
    vlan: Integer = pydantic.Field(None, alias="Vlan")
    local_address: String = pydantic.Field(None, alias="LocalAddress")
    peer_address: String = pydantic.Field(None, alias="PeerAddress")
    local_bgp_asn: Integer = pydantic.Field(None, alias="LocalBgpAsn")
    peer_bgp_asn: Integer = pydantic.Field(None, alias="PeerBgpAsn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class LocalGatewayVirtualInterfaceGroup(_EC2ModelBase):
    local_gateway_virtual_interface_group_id: LocalGatewayVirtualInterfaceGroupId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupId")
    local_gateway_virtual_interface_ids: LocalGatewayVirtualInterfaceIdSet = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceIds")
    local_gateway_id: String = pydantic.Field(None, alias="LocalGatewayId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class MaintenanceDetails(_EC2ModelBase):
    pending_maintenance: String = pydantic.Field(None, alias="PendingMaintenance")
    maintenance_auto_applied_after: MillisecondDateTime = pydantic.Field(None, alias="MaintenanceAutoAppliedAfter")
    last_maintenance_applied: MillisecondDateTime = pydantic.Field(None, alias="LastMaintenanceApplied")

class ManagedPrefixList(_EC2ModelBase):
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    address_family: String = pydantic.Field(None, alias="AddressFamily")
    state: PrefixListState = pydantic.Field(None, alias="State")
    state_message: String = pydantic.Field(None, alias="StateMessage")
    prefix_list_arn: ResourceArn = pydantic.Field(None, alias="PrefixListArn")
    prefix_list_name: String = pydantic.Field(None, alias="PrefixListName")
    max_entries: Integer = pydantic.Field(None, alias="MaxEntries")
    version: Long = pydantic.Field(None, alias="Version")
    tags: TagList = pydantic.Field(None, alias="Tags")
    owner_id: String = pydantic.Field(None, alias="OwnerId")

class MemoryGiBPerVCpu(_EC2ModelBase):
    min: Double = pydantic.Field(None, alias="Min")
    max: Double = pydantic.Field(None, alias="Max")

class MemoryGiBPerVCpuRequest(_EC2ModelBase):
    min: Double = pydantic.Field(None, alias="Min")
    max: Double = pydantic.Field(None, alias="Max")

class MemoryInfo(_EC2ModelBase):
    size_in_mi_b: MemorySize = pydantic.Field(None, alias="SizeInMiB")

class MemoryMiB(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class MemoryMiBRequest(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class MetricPoint(_EC2ModelBase):
    start_date: MillisecondDateTime = pydantic.Field(None, alias="StartDate")
    end_date: MillisecondDateTime = pydantic.Field(None, alias="EndDate")
    value: Float = pydantic.Field(None, alias="Value")
    status: String = pydantic.Field(None, alias="Status")

class ModifyAddressAttributeRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    domain_name: String = pydantic.Field(None, alias="DomainName")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyAddressAttributeResult(_EC2ModelBase):
    address: 'AddressAttribute' = pydantic.Field(None, alias="Address")

class ModifyAvailabilityZoneGroupRequest(_EC2ModelBase):
    group_name: String = pydantic.Field(None, alias="GroupName")
    opt_in_status: ModifyAvailabilityZoneOptInStatus = pydantic.Field(None, alias="OptInStatus")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyAvailabilityZoneGroupResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyCapacityReservationFleetRequest(_EC2ModelBase):
    capacity_reservation_fleet_id: CapacityReservationFleetId = pydantic.Field(None, alias="CapacityReservationFleetId")
    total_target_capacity: Integer = pydantic.Field(None, alias="TotalTargetCapacity")
    end_date: MillisecondDateTime = pydantic.Field(None, alias="EndDate")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    remove_end_date: Boolean = pydantic.Field(None, alias="RemoveEndDate")

class ModifyCapacityReservationFleetResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyCapacityReservationRequest(_EC2ModelBase):
    capacity_reservation_id: CapacityReservationId = pydantic.Field(None, alias="CapacityReservationId")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    end_date: DateTime = pydantic.Field(None, alias="EndDate")
    end_date_type: EndDateType = pydantic.Field(None, alias="EndDateType")
    accept: Boolean = pydantic.Field(None, alias="Accept")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    additional_info: String = pydantic.Field(None, alias="AdditionalInfo")

class ModifyCapacityReservationResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyClientVpnEndpointRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    server_certificate_arn: String = pydantic.Field(None, alias="ServerCertificateArn")
    connection_log_options: 'ConnectionLogOptions' = pydantic.Field(None, alias="ConnectionLogOptions")
    dns_servers: 'DnsServersOptionsModifyStructure' = pydantic.Field(None, alias="DnsServers")
    vpn_port: Integer = pydantic.Field(None, alias="VpnPort")
    description: String = pydantic.Field(None, alias="Description")
    split_tunnel: Boolean = pydantic.Field(None, alias="SplitTunnel")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    security_group_ids: ClientVpnSecurityGroupIdSet = pydantic.Field(None, alias="SecurityGroupIds")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    self_service_portal: SelfServicePortal = pydantic.Field(None, alias="SelfServicePortal")
    client_connect_options: 'ClientConnectOptions' = pydantic.Field(None, alias="ClientConnectOptions")
    session_timeout_hours: Integer = pydantic.Field(None, alias="SessionTimeoutHours")
    client_login_banner_options: 'ClientLoginBannerOptions' = pydantic.Field(None, alias="ClientLoginBannerOptions")

class ModifyClientVpnEndpointResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyDefaultCreditSpecificationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_family: UnlimitedSupportedInstanceFamily = pydantic.Field(None, alias="InstanceFamily")
    cpu_credits: String = pydantic.Field(None, alias="CpuCredits")

class ModifyDefaultCreditSpecificationResult(_EC2ModelBase):
    instance_family_credit_specification: 'InstanceFamilyCreditSpecification' = pydantic.Field(None, alias="InstanceFamilyCreditSpecification")

class ModifyEbsDefaultKmsKeyIdRequest(_EC2ModelBase):
    kms_key_id: KmsKeyId = pydantic.Field(None, alias="KmsKeyId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyEbsDefaultKmsKeyIdResult(_EC2ModelBase):
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")

class ModifyFleetRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    excess_capacity_termination_policy: FleetExcessCapacityTerminationPolicy = pydantic.Field(None, alias="ExcessCapacityTerminationPolicy")
    launch_template_configs: FleetLaunchTemplateConfigListRequest = pydantic.Field(None, alias="LaunchTemplateConfigs")
    fleet_id: FleetId = pydantic.Field(None, alias="FleetId")
    target_capacity_specification: 'TargetCapacitySpecificationRequest' = pydantic.Field(None, alias="TargetCapacitySpecification")
    context: String = pydantic.Field(None, alias="Context")

class ModifyFleetResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyFpgaImageAttributeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    fpga_image_id: FpgaImageId = pydantic.Field(None, alias="FpgaImageId")
    attribute: FpgaImageAttributeName = pydantic.Field(None, alias="Attribute")
    operation_type: OperationType = pydantic.Field(None, alias="OperationType")
    user_ids: UserIdStringList = pydantic.Field(None, alias="UserIds")
    user_groups: UserGroupStringList = pydantic.Field(None, alias="UserGroups")
    product_codes: ProductCodeStringList = pydantic.Field(None, alias="ProductCodes")
    load_permission: 'LoadPermissionModifications' = pydantic.Field(None, alias="LoadPermission")
    description: String = pydantic.Field(None, alias="Description")
    name: String = pydantic.Field(None, alias="Name")

class ModifyFpgaImageAttributeResult(_EC2ModelBase):
    fpga_image_attribute: 'FpgaImageAttribute' = pydantic.Field(None, alias="FpgaImageAttribute")

class ModifyHostsRequest(_EC2ModelBase):
    auto_placement: AutoPlacement = pydantic.Field(None, alias="AutoPlacement")
    host_ids: RequestHostIdList = pydantic.Field(None, alias="HostIds")
    host_recovery: HostRecovery = pydantic.Field(None, alias="HostRecovery")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    instance_family: String = pydantic.Field(None, alias="InstanceFamily")
    host_maintenance: HostMaintenance = pydantic.Field(None, alias="HostMaintenance")

class ModifyHostsResult(_EC2ModelBase):
    successful: ResponseHostIdList = pydantic.Field(None, alias="Successful")
    unsuccessful: UnsuccessfulItemList = pydantic.Field(None, alias="Unsuccessful")

class ModifyIdFormatRequest(_EC2ModelBase):
    resource: String = pydantic.Field(None, alias="Resource")
    use_long_ids: Boolean = pydantic.Field(None, alias="UseLongIds")

class ModifyIdentityIdFormatRequest(_EC2ModelBase):
    principal_arn: String = pydantic.Field(None, alias="PrincipalArn")
    resource: String = pydantic.Field(None, alias="Resource")
    use_long_ids: Boolean = pydantic.Field(None, alias="UseLongIds")

class ModifyImageAttributeRequest(_EC2ModelBase):
    attribute: String = pydantic.Field(None, alias="Attribute")
    description: 'AttributeValue' = pydantic.Field(None, alias="Description")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    launch_permission: 'LaunchPermissionModifications' = pydantic.Field(None, alias="LaunchPermission")
    operation_type: OperationType = pydantic.Field(None, alias="OperationType")
    product_codes: ProductCodeStringList = pydantic.Field(None, alias="ProductCodes")
    user_groups: UserGroupStringList = pydantic.Field(None, alias="UserGroups")
    user_ids: UserIdStringList = pydantic.Field(None, alias="UserIds")
    value: String = pydantic.Field(None, alias="Value")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    organization_arns: OrganizationArnStringList = pydantic.Field(None, alias="OrganizationArns")
    organizational_unit_arns: OrganizationalUnitArnStringList = pydantic.Field(None, alias="OrganizationalUnitArns")
    imds_support: 'AttributeValue' = pydantic.Field(None, alias="ImdsSupport")

class ModifyInstanceAttributeRequest(_EC2ModelBase):
    source_dest_check: 'AttributeBooleanValue' = pydantic.Field(None, alias="SourceDestCheck")
    attribute: InstanceAttributeName = pydantic.Field(None, alias="Attribute")
    block_device_mappings: InstanceBlockDeviceMappingSpecificationList = pydantic.Field(None, alias="BlockDeviceMappings")
    disable_api_termination: 'AttributeBooleanValue' = pydantic.Field(None, alias="DisableApiTermination")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ebs_optimized: 'AttributeBooleanValue' = pydantic.Field(None, alias="EbsOptimized")
    ena_support: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnaSupport")
    groups: GroupIdStringList = pydantic.Field(None, alias="Groups")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    instance_initiated_shutdown_behavior: 'AttributeValue' = pydantic.Field(None, alias="InstanceInitiatedShutdownBehavior")
    instance_type: 'AttributeValue' = pydantic.Field(None, alias="InstanceType")
    kernel: 'AttributeValue' = pydantic.Field(None, alias="Kernel")
    ramdisk: 'AttributeValue' = pydantic.Field(None, alias="Ramdisk")
    sriov_net_support: 'AttributeValue' = pydantic.Field(None, alias="SriovNetSupport")
    user_data: 'BlobAttributeValue' = pydantic.Field(None, alias="UserData")
    value: String = pydantic.Field(None, alias="Value")
    disable_api_stop: 'AttributeBooleanValue' = pydantic.Field(None, alias="DisableApiStop")

class ModifyInstanceCapacityReservationAttributesRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    capacity_reservation_specification: 'CapacityReservationSpecification' = pydantic.Field(None, alias="CapacityReservationSpecification")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyInstanceCapacityReservationAttributesResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyInstanceCreditSpecificationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    instance_credit_specifications: InstanceCreditSpecificationListRequest = pydantic.Field(None, alias="InstanceCreditSpecifications")

class ModifyInstanceCreditSpecificationResult(_EC2ModelBase):
    successful_instance_credit_specifications: SuccessfulInstanceCreditSpecificationSet = pydantic.Field(None, alias="SuccessfulInstanceCreditSpecifications")
    unsuccessful_instance_credit_specifications: UnsuccessfulInstanceCreditSpecificationSet = pydantic.Field(None, alias="UnsuccessfulInstanceCreditSpecifications")

class ModifyInstanceEventStartTimeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    instance_event_id: String = pydantic.Field(None, alias="InstanceEventId")
    not_before: DateTime = pydantic.Field(None, alias="NotBefore")

class ModifyInstanceEventStartTimeResult(_EC2ModelBase):
    event: 'InstanceStatusEvent' = pydantic.Field(None, alias="Event")

class ModifyInstanceEventWindowRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    name: String = pydantic.Field(None, alias="Name")
    instance_event_window_id: InstanceEventWindowId = pydantic.Field(None, alias="InstanceEventWindowId")
    time_ranges: InstanceEventWindowTimeRangeRequestSet = pydantic.Field(None, alias="TimeRanges")
    cron_expression: InstanceEventWindowCronExpression = pydantic.Field(None, alias="CronExpression")

class ModifyInstanceEventWindowResult(_EC2ModelBase):
    instance_event_window: 'InstanceEventWindow' = pydantic.Field(None, alias="InstanceEventWindow")

class ModifyInstanceMaintenanceOptionsRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    auto_recovery: InstanceAutoRecoveryState = pydantic.Field(None, alias="AutoRecovery")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyInstanceMaintenanceOptionsResult(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    auto_recovery: InstanceAutoRecoveryState = pydantic.Field(None, alias="AutoRecovery")

class ModifyInstanceMetadataOptionsRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    http_tokens: HttpTokensState = pydantic.Field(None, alias="HttpTokens")
    http_put_response_hop_limit: Integer = pydantic.Field(None, alias="HttpPutResponseHopLimit")
    http_endpoint: InstanceMetadataEndpointState = pydantic.Field(None, alias="HttpEndpoint")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    http_protocol_ipv_6: InstanceMetadataProtocolState = pydantic.Field(None, alias="HttpProtocolIpv6")
    instance_metadata_tags: InstanceMetadataTagsState = pydantic.Field(None, alias="InstanceMetadataTags")

class ModifyInstanceMetadataOptionsResult(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_metadata_options: 'InstanceMetadataOptionsResponse' = pydantic.Field(None, alias="InstanceMetadataOptions")

class ModifyInstancePlacementRequest(_EC2ModelBase):
    affinity: Affinity = pydantic.Field(None, alias="Affinity")
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")
    host_id: DedicatedHostId = pydantic.Field(None, alias="HostId")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    tenancy: HostTenancy = pydantic.Field(None, alias="Tenancy")
    partition_number: Integer = pydantic.Field(None, alias="PartitionNumber")
    host_resource_group_arn: String = pydantic.Field(None, alias="HostResourceGroupArn")
    group_id: PlacementGroupId = pydantic.Field(None, alias="GroupId")

class ModifyInstancePlacementResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyIpamPoolRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    description: String = pydantic.Field(None, alias="Description")
    auto_import: Boolean = pydantic.Field(None, alias="AutoImport")
    allocation_min_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationMinNetmaskLength")
    allocation_max_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationMaxNetmaskLength")
    allocation_default_netmask_length: IpamNetmaskLength = pydantic.Field(None, alias="AllocationDefaultNetmaskLength")
    clear_allocation_default_netmask_length: Boolean = pydantic.Field(None, alias="ClearAllocationDefaultNetmaskLength")
    add_allocation_resource_tags: RequestIpamResourceTagList = pydantic.Field(None, alias="AddAllocationResourceTags")
    remove_allocation_resource_tags: RequestIpamResourceTagList = pydantic.Field(None, alias="RemoveAllocationResourceTags")

class ModifyIpamPoolResult(_EC2ModelBase):
    ipam_pool: 'IpamPool' = pydantic.Field(None, alias="IpamPool")

class ModifyIpamRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_id: IpamId = pydantic.Field(None, alias="IpamId")
    description: String = pydantic.Field(None, alias="Description")
    add_operating_regions: AddIpamOperatingRegionSet = pydantic.Field(None, alias="AddOperatingRegions")
    remove_operating_regions: RemoveIpamOperatingRegionSet = pydantic.Field(None, alias="RemoveOperatingRegions")

class ModifyIpamResourceCidrRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_cidr: String = pydantic.Field(None, alias="ResourceCidr")
    resource_region: String = pydantic.Field(None, alias="ResourceRegion")
    current_ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="CurrentIpamScopeId")
    destination_ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="DestinationIpamScopeId")
    monitored: Boolean = pydantic.Field(None, alias="Monitored")

class ModifyIpamResourceCidrResult(_EC2ModelBase):
    ipam_resource_cidr: 'IpamResourceCidr' = pydantic.Field(None, alias="IpamResourceCidr")

class ModifyIpamResourceDiscoveryRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_resource_discovery_id: IpamResourceDiscoveryId = pydantic.Field(None, alias="IpamResourceDiscoveryId")
    description: String = pydantic.Field(None, alias="Description")
    add_operating_regions: AddIpamOperatingRegionSet = pydantic.Field(None, alias="AddOperatingRegions")
    remove_operating_regions: RemoveIpamOperatingRegionSet = pydantic.Field(None, alias="RemoveOperatingRegions")

class ModifyIpamResourceDiscoveryResult(_EC2ModelBase):
    ipam_resource_discovery: 'IpamResourceDiscovery' = pydantic.Field(None, alias="IpamResourceDiscovery")

class ModifyIpamResult(_EC2ModelBase):
    ipam: 'Ipam' = pydantic.Field(None, alias="Ipam")

class ModifyIpamScopeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_scope_id: IpamScopeId = pydantic.Field(None, alias="IpamScopeId")
    description: String = pydantic.Field(None, alias="Description")

class ModifyIpamScopeResult(_EC2ModelBase):
    ipam_scope: 'IpamScope' = pydantic.Field(None, alias="IpamScope")

class ModifyLaunchTemplateRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    launch_template_id: LaunchTemplateId = pydantic.Field(None, alias="LaunchTemplateId")
    launch_template_name: LaunchTemplateName = pydantic.Field(None, alias="LaunchTemplateName")
    default_version: String = pydantic.Field(None, alias="DefaultVersion")

class ModifyLaunchTemplateResult(_EC2ModelBase):
    launch_template: 'LaunchTemplate' = pydantic.Field(None, alias="LaunchTemplate")

class ModifyLocalGatewayRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    local_gateway_virtual_interface_group_id: LocalGatewayVirtualInterfaceGroupId = pydantic.Field(None, alias="LocalGatewayVirtualInterfaceGroupId")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")

class ModifyLocalGatewayRouteResult(_EC2ModelBase):
    route: 'LocalGatewayRoute' = pydantic.Field(None, alias="Route")

class ModifyManagedPrefixListRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    current_version: Long = pydantic.Field(None, alias="CurrentVersion")
    prefix_list_name: String = pydantic.Field(None, alias="PrefixListName")
    add_entries: AddPrefixListEntries = pydantic.Field(None, alias="AddEntries")
    remove_entries: RemovePrefixListEntries = pydantic.Field(None, alias="RemoveEntries")
    max_entries: Integer = pydantic.Field(None, alias="MaxEntries")

class ModifyManagedPrefixListResult(_EC2ModelBase):
    prefix_list: 'ManagedPrefixList' = pydantic.Field(None, alias="PrefixList")

class ModifyNetworkInterfaceAttributeRequest(_EC2ModelBase):
    attachment: 'NetworkInterfaceAttachmentChanges' = pydantic.Field(None, alias="Attachment")
    description: 'AttributeValue' = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    groups: SecurityGroupIdStringList = pydantic.Field(None, alias="Groups")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    source_dest_check: 'AttributeBooleanValue' = pydantic.Field(None, alias="SourceDestCheck")
    ena_srd_specification: 'EnaSrdSpecification' = pydantic.Field(None, alias="EnaSrdSpecification")

class ModifyPrivateDnsNameOptionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    private_dns_hostname_type: HostnameType = pydantic.Field(None, alias="PrivateDnsHostnameType")
    enable_resource_name_dns_a_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsARecord")
    enable_resource_name_dns_aaaa_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecord")

class ModifyPrivateDnsNameOptionsResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyReservedInstancesRequest(_EC2ModelBase):
    reserved_instances_ids: ReservedInstancesIdStringList = pydantic.Field(None, alias="ReservedInstancesIds")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    target_configurations: ReservedInstancesConfigurationList = pydantic.Field(None, alias="TargetConfigurations")

class ModifyReservedInstancesResult(_EC2ModelBase):
    reserved_instances_modification_id: String = pydantic.Field(None, alias="ReservedInstancesModificationId")

class ModifySecurityGroupRulesRequest(_EC2ModelBase):
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    security_group_rules: SecurityGroupRuleUpdateList = pydantic.Field(None, alias="SecurityGroupRules")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifySecurityGroupRulesResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifySnapshotAttributeRequest(_EC2ModelBase):
    attribute: SnapshotAttributeName = pydantic.Field(None, alias="Attribute")
    create_volume_permission: 'CreateVolumePermissionModifications' = pydantic.Field(None, alias="CreateVolumePermission")
    group_names: GroupNameStringList = pydantic.Field(None, alias="GroupNames")
    operation_type: OperationType = pydantic.Field(None, alias="OperationType")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    user_ids: UserIdStringList = pydantic.Field(None, alias="UserIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifySnapshotTierRequest(_EC2ModelBase):
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    storage_tier: TargetStorageTier = pydantic.Field(None, alias="StorageTier")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifySnapshotTierResult(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    tiering_start_time: MillisecondDateTime = pydantic.Field(None, alias="TieringStartTime")

class ModifySpotFleetRequestRequest(_EC2ModelBase):
    excess_capacity_termination_policy: ExcessCapacityTerminationPolicy = pydantic.Field(None, alias="ExcessCapacityTerminationPolicy")
    launch_template_configs: LaunchTemplateConfigList = pydantic.Field(None, alias="LaunchTemplateConfigs")
    spot_fleet_request_id: SpotFleetRequestId = pydantic.Field(None, alias="SpotFleetRequestId")
    target_capacity: Integer = pydantic.Field(None, alias="TargetCapacity")
    on_demand_target_capacity: Integer = pydantic.Field(None, alias="OnDemandTargetCapacity")
    context: String = pydantic.Field(None, alias="Context")

class ModifySpotFleetRequestResponse(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifySubnetAttributeRequest(_EC2ModelBase):
    assign_ipv_6_address_on_creation: 'AttributeBooleanValue' = pydantic.Field(None, alias="AssignIpv6AddressOnCreation")
    map_public_ip_on_launch: 'AttributeBooleanValue' = pydantic.Field(None, alias="MapPublicIpOnLaunch")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    map_customer_owned_ip_on_launch: 'AttributeBooleanValue' = pydantic.Field(None, alias="MapCustomerOwnedIpOnLaunch")
    customer_owned_ipv_4_pool: CoipPoolId = pydantic.Field(None, alias="CustomerOwnedIpv4Pool")
    enable_dns_64: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableDns64")
    private_dns_hostname_type_on_launch: HostnameType = pydantic.Field(None, alias="PrivateDnsHostnameTypeOnLaunch")
    enable_resource_name_dns_a_record_on_launch: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableResourceNameDnsARecordOnLaunch")
    enable_resource_name_dns_aaaa_record_on_launch: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecordOnLaunch")
    enable_lni_at_device_index: Integer = pydantic.Field(None, alias="EnableLniAtDeviceIndex")
    disable_lni_at_device_index: 'AttributeBooleanValue' = pydantic.Field(None, alias="DisableLniAtDeviceIndex")

class ModifyTrafficMirrorFilterNetworkServicesRequest(_EC2ModelBase):
    traffic_mirror_filter_id: TrafficMirrorFilterId = pydantic.Field(None, alias="TrafficMirrorFilterId")
    add_network_services: TrafficMirrorNetworkServiceList = pydantic.Field(None, alias="AddNetworkServices")
    remove_network_services: TrafficMirrorNetworkServiceList = pydantic.Field(None, alias="RemoveNetworkServices")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyTrafficMirrorFilterNetworkServicesResult(_EC2ModelBase):
    traffic_mirror_filter: 'TrafficMirrorFilter' = pydantic.Field(None, alias="TrafficMirrorFilter")

class ModifyTrafficMirrorFilterRuleRequest(_EC2ModelBase):
    traffic_mirror_filter_rule_id: TrafficMirrorFilterRuleIdWithResolver = pydantic.Field(None, alias="TrafficMirrorFilterRuleId")
    traffic_direction: TrafficDirection = pydantic.Field(None, alias="TrafficDirection")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")
    rule_action: TrafficMirrorRuleAction = pydantic.Field(None, alias="RuleAction")
    destination_port_range: 'TrafficMirrorPortRangeRequest' = pydantic.Field(None, alias="DestinationPortRange")
    source_port_range: 'TrafficMirrorPortRangeRequest' = pydantic.Field(None, alias="SourcePortRange")
    protocol: Integer = pydantic.Field(None, alias="Protocol")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    source_cidr_block: String = pydantic.Field(None, alias="SourceCidrBlock")
    description: String = pydantic.Field(None, alias="Description")
    remove_fields: TrafficMirrorFilterRuleFieldList = pydantic.Field(None, alias="RemoveFields")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyTrafficMirrorFilterRuleResult(_EC2ModelBase):
    traffic_mirror_filter_rule: 'TrafficMirrorFilterRule' = pydantic.Field(None, alias="TrafficMirrorFilterRule")

class ModifyTrafficMirrorSessionRequest(_EC2ModelBase):
    traffic_mirror_session_id: TrafficMirrorSessionId = pydantic.Field(None, alias="TrafficMirrorSessionId")
    traffic_mirror_target_id: TrafficMirrorTargetId = pydantic.Field(None, alias="TrafficMirrorTargetId")
    traffic_mirror_filter_id: TrafficMirrorFilterId = pydantic.Field(None, alias="TrafficMirrorFilterId")
    packet_length: Integer = pydantic.Field(None, alias="PacketLength")
    session_number: Integer = pydantic.Field(None, alias="SessionNumber")
    virtual_network_id: Integer = pydantic.Field(None, alias="VirtualNetworkId")
    description: String = pydantic.Field(None, alias="Description")
    remove_fields: TrafficMirrorSessionFieldList = pydantic.Field(None, alias="RemoveFields")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyTrafficMirrorSessionResult(_EC2ModelBase):
    traffic_mirror_session: 'TrafficMirrorSession' = pydantic.Field(None, alias="TrafficMirrorSession")

class ModifyTransitGatewayOptions(_EC2ModelBase):
    add_transit_gateway_cidr_blocks: TransitGatewayCidrBlockStringList = pydantic.Field(None, alias="AddTransitGatewayCidrBlocks")
    remove_transit_gateway_cidr_blocks: TransitGatewayCidrBlockStringList = pydantic.Field(None, alias="RemoveTransitGatewayCidrBlocks")
    vpn_ecmp_support: VpnEcmpSupportValue = pydantic.Field(None, alias="VpnEcmpSupport")
    dns_support: DnsSupportValue = pydantic.Field(None, alias="DnsSupport")
    auto_accept_shared_attachments: AutoAcceptSharedAttachmentsValue = pydantic.Field(None, alias="AutoAcceptSharedAttachments")
    default_route_table_association: DefaultRouteTableAssociationValue = pydantic.Field(None, alias="DefaultRouteTableAssociation")
    association_default_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="AssociationDefaultRouteTableId")
    default_route_table_propagation: DefaultRouteTablePropagationValue = pydantic.Field(None, alias="DefaultRouteTablePropagation")
    propagation_default_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="PropagationDefaultRouteTableId")
    amazon_side_asn: Long = pydantic.Field(None, alias="AmazonSideAsn")

class ModifyTransitGatewayPrefixListReferenceRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    blackhole: Boolean = pydantic.Field(None, alias="Blackhole")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyTransitGatewayPrefixListReferenceResult(_EC2ModelBase):
    transit_gateway_prefix_list_reference: 'TransitGatewayPrefixListReference' = pydantic.Field(None, alias="TransitGatewayPrefixListReference")

class ModifyTransitGatewayRequest(_EC2ModelBase):
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    description: String = pydantic.Field(None, alias="Description")
    options: 'ModifyTransitGatewayOptions' = pydantic.Field(None, alias="Options")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyTransitGatewayResult(_EC2ModelBase):
    transit_gateway: 'TransitGateway' = pydantic.Field(None, alias="TransitGateway")

class ModifyTransitGatewayVpcAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    add_subnet_ids: TransitGatewaySubnetIdList = pydantic.Field(None, alias="AddSubnetIds")
    remove_subnet_ids: TransitGatewaySubnetIdList = pydantic.Field(None, alias="RemoveSubnetIds")
    options: 'ModifyTransitGatewayVpcAttachmentRequestOptions' = pydantic.Field(None, alias="Options")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyTransitGatewayVpcAttachmentRequestOptions(_EC2ModelBase):
    dns_support: DnsSupportValue = pydantic.Field(None, alias="DnsSupport")
    ipv_6_support: Ipv6SupportValue = pydantic.Field(None, alias="Ipv6Support")
    appliance_mode_support: ApplianceModeSupportValue = pydantic.Field(None, alias="ApplianceModeSupport")

class ModifyTransitGatewayVpcAttachmentResult(_EC2ModelBase):
    transit_gateway_vpc_attachment: 'TransitGatewayVpcAttachment' = pydantic.Field(None, alias="TransitGatewayVpcAttachment")

class ModifyVerifiedAccessEndpointEniOptions(_EC2ModelBase):
    protocol: VerifiedAccessEndpointProtocol = pydantic.Field(None, alias="Protocol")
    port: VerifiedAccessEndpointPortNumber = pydantic.Field(None, alias="Port")

class ModifyVerifiedAccessEndpointLoadBalancerOptions(_EC2ModelBase):
    subnet_ids: ModifyVerifiedAccessEndpointSubnetIdList = pydantic.Field(None, alias="SubnetIds")
    protocol: VerifiedAccessEndpointProtocol = pydantic.Field(None, alias="Protocol")
    port: VerifiedAccessEndpointPortNumber = pydantic.Field(None, alias="Port")

class ModifyVerifiedAccessEndpointPolicyRequest(_EC2ModelBase):
    verified_access_endpoint_id: VerifiedAccessEndpointId = pydantic.Field(None, alias="VerifiedAccessEndpointId")
    policy_enabled: Boolean = pydantic.Field(None, alias="PolicyEnabled")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVerifiedAccessEndpointPolicyResult(_EC2ModelBase):
    policy_enabled: Boolean = pydantic.Field(None, alias="PolicyEnabled")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")

class ModifyVerifiedAccessEndpointRequest(_EC2ModelBase):
    verified_access_endpoint_id: VerifiedAccessEndpointId = pydantic.Field(None, alias="VerifiedAccessEndpointId")
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    load_balancer_options: 'ModifyVerifiedAccessEndpointLoadBalancerOptions' = pydantic.Field(None, alias="LoadBalancerOptions")
    network_interface_options: 'ModifyVerifiedAccessEndpointEniOptions' = pydantic.Field(None, alias="NetworkInterfaceOptions")
    description: String = pydantic.Field(None, alias="Description")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVerifiedAccessEndpointResult(_EC2ModelBase):
    verified_access_endpoint: 'VerifiedAccessEndpoint' = pydantic.Field(None, alias="VerifiedAccessEndpoint")

class ModifyVerifiedAccessGroupPolicyRequest(_EC2ModelBase):
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    policy_enabled: Boolean = pydantic.Field(None, alias="PolicyEnabled")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVerifiedAccessGroupPolicyResult(_EC2ModelBase):
    policy_enabled: Boolean = pydantic.Field(None, alias="PolicyEnabled")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")

class ModifyVerifiedAccessGroupRequest(_EC2ModelBase):
    verified_access_group_id: VerifiedAccessGroupId = pydantic.Field(None, alias="VerifiedAccessGroupId")
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    description: String = pydantic.Field(None, alias="Description")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVerifiedAccessGroupResult(_EC2ModelBase):
    verified_access_group: 'VerifiedAccessGroup' = pydantic.Field(None, alias="VerifiedAccessGroup")

class ModifyVerifiedAccessInstanceLoggingConfigurationRequest(_EC2ModelBase):
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    access_logs: 'VerifiedAccessLogOptions' = pydantic.Field(None, alias="AccessLogs")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class ModifyVerifiedAccessInstanceLoggingConfigurationResult(_EC2ModelBase):
    logging_configuration: 'VerifiedAccessInstanceLoggingConfiguration' = pydantic.Field(None, alias="LoggingConfiguration")

class ModifyVerifiedAccessInstanceRequest(_EC2ModelBase):
    verified_access_instance_id: VerifiedAccessInstanceId = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class ModifyVerifiedAccessInstanceResult(_EC2ModelBase):
    verified_access_instance: 'VerifiedAccessInstance' = pydantic.Field(None, alias="VerifiedAccessInstance")

class ModifyVerifiedAccessTrustProviderOidcOptions(_EC2ModelBase):
    issuer: String = pydantic.Field(None, alias="Issuer")
    authorization_endpoint: String = pydantic.Field(None, alias="AuthorizationEndpoint")
    token_endpoint: String = pydantic.Field(None, alias="TokenEndpoint")
    user_info_endpoint: String = pydantic.Field(None, alias="UserInfoEndpoint")
    client_id: String = pydantic.Field(None, alias="ClientId")
    client_secret: ClientSecretType = pydantic.Field(None, alias="ClientSecret")
    scope: String = pydantic.Field(None, alias="Scope")

class ModifyVerifiedAccessTrustProviderRequest(_EC2ModelBase):
    verified_access_trust_provider_id: VerifiedAccessTrustProviderId = pydantic.Field(None, alias="VerifiedAccessTrustProviderId")
    oidc_options: 'ModifyVerifiedAccessTrustProviderOidcOptions' = pydantic.Field(None, alias="OidcOptions")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class ModifyVerifiedAccessTrustProviderResult(_EC2ModelBase):
    verified_access_trust_provider: 'VerifiedAccessTrustProvider' = pydantic.Field(None, alias="VerifiedAccessTrustProvider")

class ModifyVolumeAttributeRequest(_EC2ModelBase):
    auto_enable_io: 'AttributeBooleanValue' = pydantic.Field(None, alias="AutoEnableIO")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVolumeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    size: Integer = pydantic.Field(None, alias="Size")
    volume_type: VolumeType = pydantic.Field(None, alias="VolumeType")
    iops: Integer = pydantic.Field(None, alias="Iops")
    throughput: Integer = pydantic.Field(None, alias="Throughput")
    multi_attach_enabled: Boolean = pydantic.Field(None, alias="MultiAttachEnabled")

class ModifyVolumeResult(_EC2ModelBase):
    volume_modification: 'VolumeModification' = pydantic.Field(None, alias="VolumeModification")

class ModifyVpcAttributeRequest(_EC2ModelBase):
    enable_dns_hostnames: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableDnsHostnames")
    enable_dns_support: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableDnsSupport")
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    enable_network_address_usage_metrics: 'AttributeBooleanValue' = pydantic.Field(None, alias="EnableNetworkAddressUsageMetrics")

class ModifyVpcEndpointConnectionNotificationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    connection_notification_id: ConnectionNotificationId = pydantic.Field(None, alias="ConnectionNotificationId")
    connection_notification_arn: String = pydantic.Field(None, alias="ConnectionNotificationArn")
    connection_events: ValueStringList = pydantic.Field(None, alias="ConnectionEvents")

class ModifyVpcEndpointConnectionNotificationResult(_EC2ModelBase):
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class ModifyVpcEndpointRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_endpoint_id: VpcEndpointId = pydantic.Field(None, alias="VpcEndpointId")
    reset_policy: Boolean = pydantic.Field(None, alias="ResetPolicy")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    add_route_table_ids: VpcEndpointRouteTableIdList = pydantic.Field(None, alias="AddRouteTableIds")
    remove_route_table_ids: VpcEndpointRouteTableIdList = pydantic.Field(None, alias="RemoveRouteTableIds")
    add_subnet_ids: VpcEndpointSubnetIdList = pydantic.Field(None, alias="AddSubnetIds")
    remove_subnet_ids: VpcEndpointSubnetIdList = pydantic.Field(None, alias="RemoveSubnetIds")
    add_security_group_ids: VpcEndpointSecurityGroupIdList = pydantic.Field(None, alias="AddSecurityGroupIds")
    remove_security_group_ids: VpcEndpointSecurityGroupIdList = pydantic.Field(None, alias="RemoveSecurityGroupIds")
    ip_address_type: IpAddressType = pydantic.Field(None, alias="IpAddressType")
    dns_options: 'DnsOptionsSpecification' = pydantic.Field(None, alias="DnsOptions")
    private_dns_enabled: Boolean = pydantic.Field(None, alias="PrivateDnsEnabled")

class ModifyVpcEndpointResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyVpcEndpointServiceConfigurationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    remove_private_dns_name: Boolean = pydantic.Field(None, alias="RemovePrivateDnsName")
    acceptance_required: Boolean = pydantic.Field(None, alias="AcceptanceRequired")
    add_network_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="AddNetworkLoadBalancerArns")
    remove_network_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="RemoveNetworkLoadBalancerArns")
    add_gateway_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="AddGatewayLoadBalancerArns")
    remove_gateway_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="RemoveGatewayLoadBalancerArns")
    add_supported_ip_address_types: ValueStringList = pydantic.Field(None, alias="AddSupportedIpAddressTypes")
    remove_supported_ip_address_types: ValueStringList = pydantic.Field(None, alias="RemoveSupportedIpAddressTypes")

class ModifyVpcEndpointServiceConfigurationResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ModifyVpcEndpointServicePayerResponsibilityRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    payer_responsibility: PayerResponsibility = pydantic.Field(None, alias="PayerResponsibility")

class ModifyVpcEndpointServicePayerResponsibilityResult(_EC2ModelBase):
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class ModifyVpcEndpointServicePermissionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    add_allowed_principals: ValueStringList = pydantic.Field(None, alias="AddAllowedPrincipals")
    remove_allowed_principals: ValueStringList = pydantic.Field(None, alias="RemoveAllowedPrincipals")

class ModifyVpcEndpointServicePermissionsResult(_EC2ModelBase):
    added_principals: AddedPrincipalSet = pydantic.Field(None, alias="AddedPrincipals")
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class ModifyVpcPeeringConnectionOptionsRequest(_EC2ModelBase):
    accepter_peering_connection_options: 'PeeringConnectionOptionsRequest' = pydantic.Field(None, alias="AccepterPeeringConnectionOptions")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    requester_peering_connection_options: 'PeeringConnectionOptionsRequest' = pydantic.Field(None, alias="RequesterPeeringConnectionOptions")
    vpc_peering_connection_id: VpcPeeringConnectionId = pydantic.Field(None, alias="VpcPeeringConnectionId")

class ModifyVpcPeeringConnectionOptionsResult(_EC2ModelBase):
    accepter_peering_connection_options: 'PeeringConnectionOptions' = pydantic.Field(None, alias="AccepterPeeringConnectionOptions")
    requester_peering_connection_options: 'PeeringConnectionOptions' = pydantic.Field(None, alias="RequesterPeeringConnectionOptions")

class ModifyVpcTenancyRequest(_EC2ModelBase):
    vpc_id: VpcId = pydantic.Field(None, alias="VpcId")
    instance_tenancy: VpcTenancy = pydantic.Field(None, alias="InstanceTenancy")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVpcTenancyResult(_EC2ModelBase):
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class ModifyVpnConnectionOptionsRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    local_ipv_4_network_cidr: String = pydantic.Field(None, alias="LocalIpv4NetworkCidr")
    remote_ipv_4_network_cidr: String = pydantic.Field(None, alias="RemoteIpv4NetworkCidr")
    local_ipv_6_network_cidr: String = pydantic.Field(None, alias="LocalIpv6NetworkCidr")
    remote_ipv_6_network_cidr: String = pydantic.Field(None, alias="RemoteIpv6NetworkCidr")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVpnConnectionOptionsResult(_EC2ModelBase):
    vpn_connection: 'VpnConnection' = pydantic.Field(None, alias="VpnConnection")

class ModifyVpnConnectionRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    customer_gateway_id: CustomerGatewayId = pydantic.Field(None, alias="CustomerGatewayId")
    vpn_gateway_id: VpnGatewayId = pydantic.Field(None, alias="VpnGatewayId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVpnConnectionResult(_EC2ModelBase):
    vpn_connection: 'VpnConnection' = pydantic.Field(None, alias="VpnConnection")

class ModifyVpnTunnelCertificateRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    vpn_tunnel_outside_ip_address: String = pydantic.Field(None, alias="VpnTunnelOutsideIpAddress")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ModifyVpnTunnelCertificateResult(_EC2ModelBase):
    vpn_connection: 'VpnConnection' = pydantic.Field(None, alias="VpnConnection")

class ModifyVpnTunnelOptionsRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    vpn_tunnel_outside_ip_address: String = pydantic.Field(None, alias="VpnTunnelOutsideIpAddress")
    tunnel_options: 'ModifyVpnTunnelOptionsSpecification' = pydantic.Field(None, alias="TunnelOptions")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    skip_tunnel_replacement: Boolean = pydantic.Field(None, alias="SkipTunnelReplacement")

class ModifyVpnTunnelOptionsResult(_EC2ModelBase):
    vpn_connection: 'VpnConnection' = pydantic.Field(None, alias="VpnConnection")

class ModifyVpnTunnelOptionsSpecification(_EC2ModelBase):
    tunnel_inside_cidr: String = pydantic.Field(None, alias="TunnelInsideCidr")
    tunnel_inside_ipv_6_cidr: String = pydantic.Field(None, alias="TunnelInsideIpv6Cidr")
    pre_shared_key: String = pydantic.Field(None, alias="PreSharedKey")
    phase_1_lifetime_seconds: Integer = pydantic.Field(None, alias="Phase1LifetimeSeconds")
    phase_2_lifetime_seconds: Integer = pydantic.Field(None, alias="Phase2LifetimeSeconds")
    rekey_margin_time_seconds: Integer = pydantic.Field(None, alias="RekeyMarginTimeSeconds")
    rekey_fuzz_percentage: Integer = pydantic.Field(None, alias="RekeyFuzzPercentage")
    replay_window_size: Integer = pydantic.Field(None, alias="ReplayWindowSize")
    dpd_timeout_seconds: Integer = pydantic.Field(None, alias="DPDTimeoutSeconds")
    dpd_timeout_action: String = pydantic.Field(None, alias="DPDTimeoutAction")
    phase_1_encryption_algorithms: Phase1EncryptionAlgorithmsRequestList = pydantic.Field(None, alias="Phase1EncryptionAlgorithms")
    phase_2_encryption_algorithms: Phase2EncryptionAlgorithmsRequestList = pydantic.Field(None, alias="Phase2EncryptionAlgorithms")
    phase_1_integrity_algorithms: Phase1IntegrityAlgorithmsRequestList = pydantic.Field(None, alias="Phase1IntegrityAlgorithms")
    phase_2_integrity_algorithms: Phase2IntegrityAlgorithmsRequestList = pydantic.Field(None, alias="Phase2IntegrityAlgorithms")
    phase_1_dh_group_numbers: Phase1DHGroupNumbersRequestList = pydantic.Field(None, alias="Phase1DHGroupNumbers")
    phase_2_dh_group_numbers: Phase2DHGroupNumbersRequestList = pydantic.Field(None, alias="Phase2DHGroupNumbers")
    ike_versions: IKEVersionsRequestList = pydantic.Field(None, alias="IKEVersions")
    startup_action: String = pydantic.Field(None, alias="StartupAction")
    log_options: 'VpnTunnelLogOptionsSpecification' = pydantic.Field(None, alias="LogOptions")
    enable_tunnel_lifecycle_control: Boolean = pydantic.Field(None, alias="EnableTunnelLifecycleControl")

class MonitorInstancesRequest(_EC2ModelBase):
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class MonitorInstancesResult(_EC2ModelBase):
    instance_monitorings: InstanceMonitoringList = pydantic.Field(None, alias="InstanceMonitorings")

class Monitoring(_EC2ModelBase):
    state: MonitoringState = pydantic.Field(None, alias="State")

class MoveAddressToVpcRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    public_ip: String = pydantic.Field(None, alias="PublicIp")

class MoveAddressToVpcResult(_EC2ModelBase):
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    status: Status = pydantic.Field(None, alias="Status")

class MoveByoipCidrToIpamRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    cidr: String = pydantic.Field(None, alias="Cidr")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    ipam_pool_owner: String = pydantic.Field(None, alias="IpamPoolOwner")

class MoveByoipCidrToIpamResult(_EC2ModelBase):
    byoip_cidr: 'ByoipCidr' = pydantic.Field(None, alias="ByoipCidr")

class MovingAddressStatus(_EC2ModelBase):
    move_status: MoveStatus = pydantic.Field(None, alias="MoveStatus")
    public_ip: String = pydantic.Field(None, alias="PublicIp")

class NatGateway(_EC2ModelBase):
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    delete_time: DateTime = pydantic.Field(None, alias="DeleteTime")
    failure_code: String = pydantic.Field(None, alias="FailureCode")
    failure_message: String = pydantic.Field(None, alias="FailureMessage")
    nat_gateway_addresses: NatGatewayAddressList = pydantic.Field(None, alias="NatGatewayAddresses")
    nat_gateway_id: String = pydantic.Field(None, alias="NatGatewayId")
    provisioned_bandwidth: 'ProvisionedBandwidth' = pydantic.Field(None, alias="ProvisionedBandwidth")
    state: NatGatewayState = pydantic.Field(None, alias="State")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    connectivity_type: ConnectivityType = pydantic.Field(None, alias="ConnectivityType")

class NatGatewayAddress(_EC2ModelBase):
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip: String = pydantic.Field(None, alias="PrivateIp")
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    association_id: String = pydantic.Field(None, alias="AssociationId")
    is_primary: Boolean = pydantic.Field(None, alias="IsPrimary")
    failure_message: String = pydantic.Field(None, alias="FailureMessage")
    status: NatGatewayAddressStatus = pydantic.Field(None, alias="Status")

class NetworkAcl(_EC2ModelBase):
    associations: NetworkAclAssociationList = pydantic.Field(None, alias="Associations")
    entries: NetworkAclEntryList = pydantic.Field(None, alias="Entries")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")
    network_acl_id: String = pydantic.Field(None, alias="NetworkAclId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")

class NetworkAclAssociation(_EC2ModelBase):
    network_acl_association_id: String = pydantic.Field(None, alias="NetworkAclAssociationId")
    network_acl_id: String = pydantic.Field(None, alias="NetworkAclId")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")

class NetworkAclEntry(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    egress: Boolean = pydantic.Field(None, alias="Egress")
    icmp_type_code: 'IcmpTypeCode' = pydantic.Field(None, alias="IcmpTypeCode")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    port_range: 'PortRange' = pydantic.Field(None, alias="PortRange")
    protocol: String = pydantic.Field(None, alias="Protocol")
    rule_action: RuleAction = pydantic.Field(None, alias="RuleAction")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")

class NetworkBandwidthGbps(_EC2ModelBase):
    min: Double = pydantic.Field(None, alias="Min")
    max: Double = pydantic.Field(None, alias="Max")

class NetworkBandwidthGbpsRequest(_EC2ModelBase):
    min: Double = pydantic.Field(None, alias="Min")
    max: Double = pydantic.Field(None, alias="Max")

class NetworkCardInfo(_EC2ModelBase):
    network_card_index: NetworkCardIndex = pydantic.Field(None, alias="NetworkCardIndex")
    network_performance: NetworkPerformance = pydantic.Field(None, alias="NetworkPerformance")
    maximum_network_interfaces: MaxNetworkInterfaces = pydantic.Field(None, alias="MaximumNetworkInterfaces")

class NetworkInfo(_EC2ModelBase):
    network_performance: NetworkPerformance = pydantic.Field(None, alias="NetworkPerformance")
    maximum_network_interfaces: MaxNetworkInterfaces = pydantic.Field(None, alias="MaximumNetworkInterfaces")
    maximum_network_cards: MaximumNetworkCards = pydantic.Field(None, alias="MaximumNetworkCards")
    default_network_card_index: DefaultNetworkCardIndex = pydantic.Field(None, alias="DefaultNetworkCardIndex")
    network_cards: NetworkCardInfoList = pydantic.Field(None, alias="NetworkCards")
    ipv_4_addresses_per_interface: MaxIpv4AddrPerInterface = pydantic.Field(None, alias="Ipv4AddressesPerInterface")
    ipv_6_addresses_per_interface: MaxIpv6AddrPerInterface = pydantic.Field(None, alias="Ipv6AddressesPerInterface")
    ipv_6_supported: Ipv6Flag = pydantic.Field(None, alias="Ipv6Supported")
    ena_support: EnaSupport = pydantic.Field(None, alias="EnaSupport")
    efa_supported: EfaSupportedFlag = pydantic.Field(None, alias="EfaSupported")
    efa_info: 'EfaInfo' = pydantic.Field(None, alias="EfaInfo")
    encryption_in_transit_supported: EncryptionInTransitSupported = pydantic.Field(None, alias="EncryptionInTransitSupported")
    ena_srd_supported: EnaSrdSupported = pydantic.Field(None, alias="EnaSrdSupported")

class NetworkInsightsAccessScope(_EC2ModelBase):
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    network_insights_access_scope_arn: ResourceArn = pydantic.Field(None, alias="NetworkInsightsAccessScopeArn")
    created_date: MillisecondDateTime = pydantic.Field(None, alias="CreatedDate")
    updated_date: MillisecondDateTime = pydantic.Field(None, alias="UpdatedDate")
    tags: TagList = pydantic.Field(None, alias="Tags")

class NetworkInsightsAccessScopeAnalysis(_EC2ModelBase):
    network_insights_access_scope_analysis_id: NetworkInsightsAccessScopeAnalysisId = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisId")
    network_insights_access_scope_analysis_arn: ResourceArn = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysisArn")
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    status: AnalysisStatus = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    warning_message: String = pydantic.Field(None, alias="WarningMessage")
    start_date: MillisecondDateTime = pydantic.Field(None, alias="StartDate")
    end_date: MillisecondDateTime = pydantic.Field(None, alias="EndDate")
    findings_found: FindingsFound = pydantic.Field(None, alias="FindingsFound")
    analyzed_eni_count: Integer = pydantic.Field(None, alias="AnalyzedEniCount")
    tags: TagList = pydantic.Field(None, alias="Tags")

class NetworkInsightsAccessScopeContent(_EC2ModelBase):
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    match_paths: AccessScopePathList = pydantic.Field(None, alias="MatchPaths")
    exclude_paths: AccessScopePathList = pydantic.Field(None, alias="ExcludePaths")

class NetworkInsightsAnalysis(_EC2ModelBase):
    network_insights_analysis_id: NetworkInsightsAnalysisId = pydantic.Field(None, alias="NetworkInsightsAnalysisId")
    network_insights_analysis_arn: ResourceArn = pydantic.Field(None, alias="NetworkInsightsAnalysisArn")
    network_insights_path_id: NetworkInsightsPathId = pydantic.Field(None, alias="NetworkInsightsPathId")
    additional_accounts: ValueStringList = pydantic.Field(None, alias="AdditionalAccounts")
    filter_in_arns: ArnList = pydantic.Field(None, alias="FilterInArns")
    start_date: MillisecondDateTime = pydantic.Field(None, alias="StartDate")
    status: AnalysisStatus = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    warning_message: String = pydantic.Field(None, alias="WarningMessage")
    network_path_found: Boolean = pydantic.Field(None, alias="NetworkPathFound")
    forward_path_components: PathComponentList = pydantic.Field(None, alias="ForwardPathComponents")
    return_path_components: PathComponentList = pydantic.Field(None, alias="ReturnPathComponents")
    explanations: ExplanationList = pydantic.Field(None, alias="Explanations")
    alternate_path_hints: AlternatePathHintList = pydantic.Field(None, alias="AlternatePathHints")
    suggested_accounts: ValueStringList = pydantic.Field(None, alias="SuggestedAccounts")
    tags: TagList = pydantic.Field(None, alias="Tags")

class NetworkInsightsPath(_EC2ModelBase):
    network_insights_path_id: NetworkInsightsPathId = pydantic.Field(None, alias="NetworkInsightsPathId")
    network_insights_path_arn: ResourceArn = pydantic.Field(None, alias="NetworkInsightsPathArn")
    created_date: MillisecondDateTime = pydantic.Field(None, alias="CreatedDate")
    source: String = pydantic.Field(None, alias="Source")
    destination: String = pydantic.Field(None, alias="Destination")
    source_arn: ResourceArn = pydantic.Field(None, alias="SourceArn")
    destination_arn: ResourceArn = pydantic.Field(None, alias="DestinationArn")
    source_ip: IpAddress = pydantic.Field(None, alias="SourceIp")
    destination_ip: IpAddress = pydantic.Field(None, alias="DestinationIp")
    protocol: Protocol = pydantic.Field(None, alias="Protocol")
    destination_port: Integer = pydantic.Field(None, alias="DestinationPort")
    tags: TagList = pydantic.Field(None, alias="Tags")
    filter_at_source: 'PathFilter' = pydantic.Field(None, alias="FilterAtSource")
    filter_at_destination: 'PathFilter' = pydantic.Field(None, alias="FilterAtDestination")

class NetworkInterface(_EC2ModelBase):
    association: 'NetworkInterfaceAssociation' = pydantic.Field(None, alias="Association")
    attachment: 'NetworkInterfaceAttachment' = pydantic.Field(None, alias="Attachment")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    description: String = pydantic.Field(None, alias="Description")
    groups: GroupIdentifierList = pydantic.Field(None, alias="Groups")
    interface_type: NetworkInterfaceType = pydantic.Field(None, alias="InterfaceType")
    ipv_6_addresses: NetworkInterfaceIpv6AddressesList = pydantic.Field(None, alias="Ipv6Addresses")
    mac_address: String = pydantic.Field(None, alias="MacAddress")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_addresses: NetworkInterfacePrivateIpAddressList = pydantic.Field(None, alias="PrivateIpAddresses")
    ipv_4_prefixes: Ipv4PrefixesList = pydantic.Field(None, alias="Ipv4Prefixes")
    ipv_6_prefixes: Ipv6PrefixesList = pydantic.Field(None, alias="Ipv6Prefixes")
    requester_id: String = pydantic.Field(None, alias="RequesterId")
    requester_managed: Boolean = pydantic.Field(None, alias="RequesterManaged")
    source_dest_check: Boolean = pydantic.Field(None, alias="SourceDestCheck")
    status: NetworkInterfaceStatus = pydantic.Field(None, alias="Status")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    tag_set: TagList = pydantic.Field(None, alias="TagSet")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    deny_all_igw_traffic: Boolean = pydantic.Field(None, alias="DenyAllIgwTraffic")
    ipv_6_native: Boolean = pydantic.Field(None, alias="Ipv6Native")
    ipv_6_address: String = pydantic.Field(None, alias="Ipv6Address")

class NetworkInterfaceAssociation(_EC2ModelBase):
    allocation_id: String = pydantic.Field(None, alias="AllocationId")
    association_id: String = pydantic.Field(None, alias="AssociationId")
    ip_owner_id: String = pydantic.Field(None, alias="IpOwnerId")
    public_dns_name: String = pydantic.Field(None, alias="PublicDnsName")
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    customer_owned_ip: String = pydantic.Field(None, alias="CustomerOwnedIp")
    carrier_ip: String = pydantic.Field(None, alias="CarrierIp")

class NetworkInterfaceAttachment(_EC2ModelBase):
    attach_time: DateTime = pydantic.Field(None, alias="AttachTime")
    attachment_id: String = pydantic.Field(None, alias="AttachmentId")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    network_card_index: Integer = pydantic.Field(None, alias="NetworkCardIndex")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_owner_id: String = pydantic.Field(None, alias="InstanceOwnerId")
    status: AttachmentStatus = pydantic.Field(None, alias="Status")
    ena_srd_specification: 'AttachmentEnaSrdSpecification' = pydantic.Field(None, alias="EnaSrdSpecification")

class NetworkInterfaceAttachmentChanges(_EC2ModelBase):
    attachment_id: NetworkInterfaceAttachmentId = pydantic.Field(None, alias="AttachmentId")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")

class NetworkInterfaceCount(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class NetworkInterfaceCountRequest(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class NetworkInterfaceIpv6Address(_EC2ModelBase):
    ipv_6_address: String = pydantic.Field(None, alias="Ipv6Address")

class NetworkInterfacePermission(_EC2ModelBase):
    network_interface_permission_id: String = pydantic.Field(None, alias="NetworkInterfacePermissionId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    aws_account_id: String = pydantic.Field(None, alias="AwsAccountId")
    aws_service: String = pydantic.Field(None, alias="AwsService")
    permission: InterfacePermissionType = pydantic.Field(None, alias="Permission")
    permission_state: 'NetworkInterfacePermissionState' = pydantic.Field(None, alias="PermissionState")

class NetworkInterfacePermissionState(_EC2ModelBase):
    state: NetworkInterfacePermissionStateCode = pydantic.Field(None, alias="State")
    status_message: String = pydantic.Field(None, alias="StatusMessage")

class NetworkInterfacePrivateIpAddress(_EC2ModelBase):
    association: 'NetworkInterfaceAssociation' = pydantic.Field(None, alias="Association")
    primary: Boolean = pydantic.Field(None, alias="Primary")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")

class NewDhcpConfiguration(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    values: ValueStringList = pydantic.Field(None, alias="Values")

class OidcOptions(_EC2ModelBase):
    issuer: String = pydantic.Field(None, alias="Issuer")
    authorization_endpoint: String = pydantic.Field(None, alias="AuthorizationEndpoint")
    token_endpoint: String = pydantic.Field(None, alias="TokenEndpoint")
    user_info_endpoint: String = pydantic.Field(None, alias="UserInfoEndpoint")
    client_id: String = pydantic.Field(None, alias="ClientId")
    client_secret: ClientSecretType = pydantic.Field(None, alias="ClientSecret")
    scope: String = pydantic.Field(None, alias="Scope")

class OnDemandOptions(_EC2ModelBase):
    allocation_strategy: FleetOnDemandAllocationStrategy = pydantic.Field(None, alias="AllocationStrategy")
    capacity_reservation_options: 'CapacityReservationOptions' = pydantic.Field(None, alias="CapacityReservationOptions")
    single_instance_type: Boolean = pydantic.Field(None, alias="SingleInstanceType")
    single_availability_zone: Boolean = pydantic.Field(None, alias="SingleAvailabilityZone")
    min_target_capacity: Integer = pydantic.Field(None, alias="MinTargetCapacity")
    max_total_price: String = pydantic.Field(None, alias="MaxTotalPrice")

class OnDemandOptionsRequest(_EC2ModelBase):
    allocation_strategy: FleetOnDemandAllocationStrategy = pydantic.Field(None, alias="AllocationStrategy")
    capacity_reservation_options: 'CapacityReservationOptionsRequest' = pydantic.Field(None, alias="CapacityReservationOptions")
    single_instance_type: Boolean = pydantic.Field(None, alias="SingleInstanceType")
    single_availability_zone: Boolean = pydantic.Field(None, alias="SingleAvailabilityZone")
    min_target_capacity: Integer = pydantic.Field(None, alias="MinTargetCapacity")
    max_total_price: String = pydantic.Field(None, alias="MaxTotalPrice")

class PacketHeaderStatement(_EC2ModelBase):
    source_addresses: ValueStringList = pydantic.Field(None, alias="SourceAddresses")
    destination_addresses: ValueStringList = pydantic.Field(None, alias="DestinationAddresses")
    source_ports: ValueStringList = pydantic.Field(None, alias="SourcePorts")
    destination_ports: ValueStringList = pydantic.Field(None, alias="DestinationPorts")
    source_prefix_lists: ValueStringList = pydantic.Field(None, alias="SourcePrefixLists")
    destination_prefix_lists: ValueStringList = pydantic.Field(None, alias="DestinationPrefixLists")
    protocols: ProtocolList = pydantic.Field(None, alias="Protocols")

class PacketHeaderStatementRequest(_EC2ModelBase):
    source_addresses: ValueStringList = pydantic.Field(None, alias="SourceAddresses")
    destination_addresses: ValueStringList = pydantic.Field(None, alias="DestinationAddresses")
    source_ports: ValueStringList = pydantic.Field(None, alias="SourcePorts")
    destination_ports: ValueStringList = pydantic.Field(None, alias="DestinationPorts")
    source_prefix_lists: ValueStringList = pydantic.Field(None, alias="SourcePrefixLists")
    destination_prefix_lists: ValueStringList = pydantic.Field(None, alias="DestinationPrefixLists")
    protocols: ProtocolList = pydantic.Field(None, alias="Protocols")

class PathComponent(_EC2ModelBase):
    sequence_number: Integer = pydantic.Field(None, alias="SequenceNumber")
    acl_rule: 'AnalysisAclRule' = pydantic.Field(None, alias="AclRule")
    attached_to: 'AnalysisComponent' = pydantic.Field(None, alias="AttachedTo")
    component: 'AnalysisComponent' = pydantic.Field(None, alias="Component")
    destination_vpc: 'AnalysisComponent' = pydantic.Field(None, alias="DestinationVpc")
    outbound_header: 'AnalysisPacketHeader' = pydantic.Field(None, alias="OutboundHeader")
    inbound_header: 'AnalysisPacketHeader' = pydantic.Field(None, alias="InboundHeader")
    route_table_route: 'AnalysisRouteTableRoute' = pydantic.Field(None, alias="RouteTableRoute")
    security_group_rule: 'AnalysisSecurityGroupRule' = pydantic.Field(None, alias="SecurityGroupRule")
    source_vpc: 'AnalysisComponent' = pydantic.Field(None, alias="SourceVpc")
    subnet: 'AnalysisComponent' = pydantic.Field(None, alias="Subnet")
    vpc: 'AnalysisComponent' = pydantic.Field(None, alias="Vpc")
    additional_details: AdditionalDetailList = pydantic.Field(None, alias="AdditionalDetails")
    transit_gateway: 'AnalysisComponent' = pydantic.Field(None, alias="TransitGateway")
    transit_gateway_route_table_route: 'TransitGatewayRouteTableRoute' = pydantic.Field(None, alias="TransitGatewayRouteTableRoute")
    explanations: ExplanationList = pydantic.Field(None, alias="Explanations")
    elastic_load_balancer_listener: 'AnalysisComponent' = pydantic.Field(None, alias="ElasticLoadBalancerListener")
    firewall_stateless_rule: 'FirewallStatelessRule' = pydantic.Field(None, alias="FirewallStatelessRule")
    firewall_stateful_rule: 'FirewallStatefulRule' = pydantic.Field(None, alias="FirewallStatefulRule")
    service_name: String = pydantic.Field(None, alias="ServiceName")

class PathFilter(_EC2ModelBase):
    source_address: IpAddress = pydantic.Field(None, alias="SourceAddress")
    source_port_range: 'FilterPortRange' = pydantic.Field(None, alias="SourcePortRange")
    destination_address: IpAddress = pydantic.Field(None, alias="DestinationAddress")
    destination_port_range: 'FilterPortRange' = pydantic.Field(None, alias="DestinationPortRange")

class PathRequestFilter(_EC2ModelBase):
    source_address: IpAddress = pydantic.Field(None, alias="SourceAddress")
    source_port_range: 'RequestFilterPortRange' = pydantic.Field(None, alias="SourcePortRange")
    destination_address: IpAddress = pydantic.Field(None, alias="DestinationAddress")
    destination_port_range: 'RequestFilterPortRange' = pydantic.Field(None, alias="DestinationPortRange")

class PathStatement(_EC2ModelBase):
    packet_header_statement: 'PacketHeaderStatement' = pydantic.Field(None, alias="PacketHeaderStatement")
    resource_statement: 'ResourceStatement' = pydantic.Field(None, alias="ResourceStatement")

class PathStatementRequest(_EC2ModelBase):
    packet_header_statement: 'PacketHeaderStatementRequest' = pydantic.Field(None, alias="PacketHeaderStatement")
    resource_statement: 'ResourceStatementRequest' = pydantic.Field(None, alias="ResourceStatement")

class PciId(_EC2ModelBase):
    device_id: String = pydantic.Field(None, alias="DeviceId")
    vendor_id: String = pydantic.Field(None, alias="VendorId")
    subsystem_id: String = pydantic.Field(None, alias="SubsystemId")
    subsystem_vendor_id: String = pydantic.Field(None, alias="SubsystemVendorId")

class PeeringAttachmentStatus(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class PeeringConnectionOptions(_EC2ModelBase):
    allow_dns_resolution_from_remote_vpc: Boolean = pydantic.Field(None, alias="AllowDnsResolutionFromRemoteVpc")
    allow_egress_from_local_classic_link_to_remote_vpc: Boolean = pydantic.Field(None, alias="AllowEgressFromLocalClassicLinkToRemoteVpc")
    allow_egress_from_local_vpc_to_remote_classic_link: Boolean = pydantic.Field(None, alias="AllowEgressFromLocalVpcToRemoteClassicLink")

class PeeringConnectionOptionsRequest(_EC2ModelBase):
    allow_dns_resolution_from_remote_vpc: Boolean = pydantic.Field(None, alias="AllowDnsResolutionFromRemoteVpc")
    allow_egress_from_local_classic_link_to_remote_vpc: Boolean = pydantic.Field(None, alias="AllowEgressFromLocalClassicLinkToRemoteVpc")
    allow_egress_from_local_vpc_to_remote_classic_link: Boolean = pydantic.Field(None, alias="AllowEgressFromLocalVpcToRemoteClassicLink")

class PeeringTgwInfo(_EC2ModelBase):
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    core_network_id: String = pydantic.Field(None, alias="CoreNetworkId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    region: String = pydantic.Field(None, alias="Region")

class Phase1DHGroupNumbersListValue(_EC2ModelBase):
    value: Integer = pydantic.Field(None, alias="Value")

class Phase1DHGroupNumbersRequestListValue(_EC2ModelBase):
    value: Integer = pydantic.Field(None, alias="Value")

class Phase1EncryptionAlgorithmsListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase1EncryptionAlgorithmsRequestListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase1IntegrityAlgorithmsListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase1IntegrityAlgorithmsRequestListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase2DHGroupNumbersListValue(_EC2ModelBase):
    value: Integer = pydantic.Field(None, alias="Value")

class Phase2DHGroupNumbersRequestListValue(_EC2ModelBase):
    value: Integer = pydantic.Field(None, alias="Value")

class Phase2EncryptionAlgorithmsListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase2EncryptionAlgorithmsRequestListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase2IntegrityAlgorithmsListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Phase2IntegrityAlgorithmsRequestListValue(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")

class Placement(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    affinity: String = pydantic.Field(None, alias="Affinity")
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")
    partition_number: Integer = pydantic.Field(None, alias="PartitionNumber")
    host_id: String = pydantic.Field(None, alias="HostId")
    tenancy: Tenancy = pydantic.Field(None, alias="Tenancy")
    spread_domain: String = pydantic.Field(None, alias="SpreadDomain")
    host_resource_group_arn: String = pydantic.Field(None, alias="HostResourceGroupArn")
    group_id: PlacementGroupId = pydantic.Field(None, alias="GroupId")

class PlacementGroup(_EC2ModelBase):
    group_name: String = pydantic.Field(None, alias="GroupName")
    state: PlacementGroupState = pydantic.Field(None, alias="State")
    strategy: PlacementStrategy = pydantic.Field(None, alias="Strategy")
    partition_count: Integer = pydantic.Field(None, alias="PartitionCount")
    group_id: String = pydantic.Field(None, alias="GroupId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    group_arn: String = pydantic.Field(None, alias="GroupArn")
    spread_level: SpreadLevel = pydantic.Field(None, alias="SpreadLevel")

class PlacementGroupInfo(_EC2ModelBase):
    supported_strategies: PlacementGroupStrategyList = pydantic.Field(None, alias="SupportedStrategies")

class PlacementResponse(_EC2ModelBase):
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")

class PoolCidrBlock(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")

class PortRange(_EC2ModelBase):
    From_: Integer = pydantic.Field(None, alias="From")
    to: Integer = pydantic.Field(None, alias="To")

class PrefixList(_EC2ModelBase):
    cidrs: ValueStringList = pydantic.Field(None, alias="Cidrs")
    prefix_list_id: String = pydantic.Field(None, alias="PrefixListId")
    prefix_list_name: String = pydantic.Field(None, alias="PrefixListName")

class PrefixListAssociation(_EC2ModelBase):
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_owner: String = pydantic.Field(None, alias="ResourceOwner")

class PrefixListEntry(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    description: String = pydantic.Field(None, alias="Description")

class PrefixListId(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    prefix_list_id: String = pydantic.Field(None, alias="PrefixListId")

class PriceSchedule(_EC2ModelBase):
    active: Boolean = pydantic.Field(None, alias="Active")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    price: Double = pydantic.Field(None, alias="Price")
    term: Long = pydantic.Field(None, alias="Term")

class PriceScheduleSpecification(_EC2ModelBase):
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    price: Double = pydantic.Field(None, alias="Price")
    term: Long = pydantic.Field(None, alias="Term")

class PricingDetail(_EC2ModelBase):
    count: Integer = pydantic.Field(None, alias="Count")
    price: Double = pydantic.Field(None, alias="Price")

class PrincipalIdFormat(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")
    statuses: IdFormatList = pydantic.Field(None, alias="Statuses")

class PrivateDnsDetails(_EC2ModelBase):
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")

class PrivateDnsNameConfiguration(_EC2ModelBase):
    state: DnsNameState = pydantic.Field(None, alias="State")
    type: String = pydantic.Field(None, alias="Type")
    value: String = pydantic.Field(None, alias="Value")
    name: String = pydantic.Field(None, alias="Name")

class PrivateDnsNameOptionsOnLaunch(_EC2ModelBase):
    hostname_type: HostnameType = pydantic.Field(None, alias="HostnameType")
    enable_resource_name_dns_a_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsARecord")
    enable_resource_name_dns_aaaa_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecord")

class PrivateDnsNameOptionsRequest(_EC2ModelBase):
    hostname_type: HostnameType = pydantic.Field(None, alias="HostnameType")
    enable_resource_name_dns_a_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsARecord")
    enable_resource_name_dns_aaaa_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecord")

class PrivateDnsNameOptionsResponse(_EC2ModelBase):
    hostname_type: HostnameType = pydantic.Field(None, alias="HostnameType")
    enable_resource_name_dns_a_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsARecord")
    enable_resource_name_dns_aaaa_record: Boolean = pydantic.Field(None, alias="EnableResourceNameDnsAAAARecord")

class PrivateIpAddressSpecification(_EC2ModelBase):
    primary: Boolean = pydantic.Field(None, alias="Primary")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")

class ProcessorInfo(_EC2ModelBase):
    supported_architectures: ArchitectureTypeList = pydantic.Field(None, alias="SupportedArchitectures")
    sustained_clock_speed_in_ghz: ProcessorSustainedClockSpeed = pydantic.Field(None, alias="SustainedClockSpeedInGhz")
    supported_features: SupportedAdditionalProcessorFeatureList = pydantic.Field(None, alias="SupportedFeatures")

class ProductCode(_EC2ModelBase):
    product_code_id: String = pydantic.Field(None, alias="ProductCodeId")
    product_code_type: ProductCodeValues = pydantic.Field(None, alias="ProductCodeType")

class PropagatingVgw(_EC2ModelBase):
    gateway_id: String = pydantic.Field(None, alias="GatewayId")

class ProvisionByoipCidrRequest(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    cidr_authorization_context: 'CidrAuthorizationContext' = pydantic.Field(None, alias="CidrAuthorizationContext")
    publicly_advertisable: Boolean = pydantic.Field(None, alias="PubliclyAdvertisable")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    pool_tag_specifications: TagSpecificationList = pydantic.Field(None, alias="PoolTagSpecifications")
    multi_region: Boolean = pydantic.Field(None, alias="MultiRegion")

class ProvisionByoipCidrResult(_EC2ModelBase):
    byoip_cidr: 'ByoipCidr' = pydantic.Field(None, alias="ByoipCidr")

class ProvisionIpamPoolCidrRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    cidr: String = pydantic.Field(None, alias="Cidr")
    cidr_authorization_context: 'IpamCidrAuthorizationContext' = pydantic.Field(None, alias="CidrAuthorizationContext")
    netmask_length: Integer = pydantic.Field(None, alias="NetmaskLength")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class ProvisionIpamPoolCidrResult(_EC2ModelBase):
    ipam_pool_cidr: 'IpamPoolCidr' = pydantic.Field(None, alias="IpamPoolCidr")

class ProvisionPublicIpv4PoolCidrRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    pool_id: Ipv4PoolEc2Id = pydantic.Field(None, alias="PoolId")
    netmask_length: Integer = pydantic.Field(None, alias="NetmaskLength")

class ProvisionPublicIpv4PoolCidrResult(_EC2ModelBase):
    pool_id: Ipv4PoolEc2Id = pydantic.Field(None, alias="PoolId")
    pool_address_range: 'PublicIpv4PoolRange' = pydantic.Field(None, alias="PoolAddressRange")

class ProvisionedBandwidth(_EC2ModelBase):
    provision_time: DateTime = pydantic.Field(None, alias="ProvisionTime")
    provisioned: String = pydantic.Field(None, alias="Provisioned")
    request_time: DateTime = pydantic.Field(None, alias="RequestTime")
    requested: String = pydantic.Field(None, alias="Requested")
    status: String = pydantic.Field(None, alias="Status")

class PtrUpdateStatus(_EC2ModelBase):
    value: String = pydantic.Field(None, alias="Value")
    status: String = pydantic.Field(None, alias="Status")
    reason: String = pydantic.Field(None, alias="Reason")

class PublicIpv4Pool(_EC2ModelBase):
    pool_id: String = pydantic.Field(None, alias="PoolId")
    description: String = pydantic.Field(None, alias="Description")
    pool_address_ranges: PublicIpv4PoolRangeSet = pydantic.Field(None, alias="PoolAddressRanges")
    total_address_count: Integer = pydantic.Field(None, alias="TotalAddressCount")
    total_available_address_count: Integer = pydantic.Field(None, alias="TotalAvailableAddressCount")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    tags: TagList = pydantic.Field(None, alias="Tags")

class PublicIpv4PoolRange(_EC2ModelBase):
    first_address: String = pydantic.Field(None, alias="FirstAddress")
    last_address: String = pydantic.Field(None, alias="LastAddress")
    address_count: Integer = pydantic.Field(None, alias="AddressCount")
    available_address_count: Integer = pydantic.Field(None, alias="AvailableAddressCount")

class Purchase(_EC2ModelBase):
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    duration: Integer = pydantic.Field(None, alias="Duration")
    host_id_set: ResponseHostIdSet = pydantic.Field(None, alias="HostIdSet")
    host_reservation_id: HostReservationId = pydantic.Field(None, alias="HostReservationId")
    hourly_price: String = pydantic.Field(None, alias="HourlyPrice")
    instance_family: String = pydantic.Field(None, alias="InstanceFamily")
    payment_option: PaymentOption = pydantic.Field(None, alias="PaymentOption")
    upfront_price: String = pydantic.Field(None, alias="UpfrontPrice")

class PurchaseHostReservationRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    host_id_set: RequestHostIdSet = pydantic.Field(None, alias="HostIdSet")
    limit_price: String = pydantic.Field(None, alias="LimitPrice")
    offering_id: OfferingId = pydantic.Field(None, alias="OfferingId")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class PurchaseHostReservationResult(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    purchase: PurchaseSet = pydantic.Field(None, alias="Purchase")
    total_hourly_price: String = pydantic.Field(None, alias="TotalHourlyPrice")
    total_upfront_price: String = pydantic.Field(None, alias="TotalUpfrontPrice")

class PurchaseRequest(_EC2ModelBase):
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    purchase_token: String = pydantic.Field(None, alias="PurchaseToken")

class PurchaseReservedInstancesOfferingRequest(_EC2ModelBase):
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    reserved_instances_offering_id: ReservedInstancesOfferingId = pydantic.Field(None, alias="ReservedInstancesOfferingId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    limit_price: 'ReservedInstanceLimitPrice' = pydantic.Field(None, alias="LimitPrice")
    purchase_time: DateTime = pydantic.Field(None, alias="PurchaseTime")

class PurchaseReservedInstancesOfferingResult(_EC2ModelBase):
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")

class PurchaseScheduledInstancesRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    purchase_requests: PurchaseRequestSet = pydantic.Field(None, alias="PurchaseRequests")

class PurchaseScheduledInstancesResult(_EC2ModelBase):
    scheduled_instance_set: PurchasedScheduledInstanceSet = pydantic.Field(None, alias="ScheduledInstanceSet")

class RebootInstancesRequest(_EC2ModelBase):
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RecurringCharge(_EC2ModelBase):
    amount: Double = pydantic.Field(None, alias="Amount")
    frequency: RecurringChargeFrequency = pydantic.Field(None, alias="Frequency")

class ReferencedSecurityGroup(_EC2ModelBase):
    group_id: String = pydantic.Field(None, alias="GroupId")
    peering_status: String = pydantic.Field(None, alias="PeeringStatus")
    user_id: String = pydantic.Field(None, alias="UserId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    vpc_peering_connection_id: String = pydantic.Field(None, alias="VpcPeeringConnectionId")

class Region(_EC2ModelBase):
    endpoint: String = pydantic.Field(None, alias="Endpoint")
    region_name: String = pydantic.Field(None, alias="RegionName")
    opt_in_status: String = pydantic.Field(None, alias="OptInStatus")

class RegisterImageRequest(_EC2ModelBase):
    image_location: String = pydantic.Field(None, alias="ImageLocation")
    architecture: ArchitectureValues = pydantic.Field(None, alias="Architecture")
    block_device_mappings: BlockDeviceMappingRequestList = pydantic.Field(None, alias="BlockDeviceMappings")
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ena_support: Boolean = pydantic.Field(None, alias="EnaSupport")
    kernel_id: KernelId = pydantic.Field(None, alias="KernelId")
    name: String = pydantic.Field(None, alias="Name")
    billing_products: BillingProductList = pydantic.Field(None, alias="BillingProducts")
    ramdisk_id: RamdiskId = pydantic.Field(None, alias="RamdiskId")
    root_device_name: String = pydantic.Field(None, alias="RootDeviceName")
    sriov_net_support: String = pydantic.Field(None, alias="SriovNetSupport")
    virtualization_type: String = pydantic.Field(None, alias="VirtualizationType")
    boot_mode: BootModeValues = pydantic.Field(None, alias="BootMode")
    tpm_support: TpmSupportValues = pydantic.Field(None, alias="TpmSupport")
    uefi_data: StringType = pydantic.Field(None, alias="UefiData")
    imds_support: ImdsSupportValues = pydantic.Field(None, alias="ImdsSupport")

class RegisterImageResult(_EC2ModelBase):
    image_id: String = pydantic.Field(None, alias="ImageId")

class RegisterInstanceEventNotificationAttributesRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_tag_attribute: 'RegisterInstanceTagAttributeRequest' = pydantic.Field(None, alias="InstanceTagAttribute")

class RegisterInstanceEventNotificationAttributesResult(_EC2ModelBase):
    instance_tag_attribute: 'InstanceTagNotificationAttribute' = pydantic.Field(None, alias="InstanceTagAttribute")

class RegisterInstanceTagAttributeRequest(_EC2ModelBase):
    include_all_tags_of_instance: Boolean = pydantic.Field(None, alias="IncludeAllTagsOfInstance")
    instance_tag_keys: InstanceTagKeySet = pydantic.Field(None, alias="InstanceTagKeys")

class RegisterTransitGatewayMulticastGroupMembersRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")
    network_interface_ids: TransitGatewayNetworkInterfaceIdList = pydantic.Field(None, alias="NetworkInterfaceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RegisterTransitGatewayMulticastGroupMembersResult(_EC2ModelBase):
    registered_multicast_group_members: 'TransitGatewayMulticastRegisteredGroupMembers' = pydantic.Field(None, alias="RegisteredMulticastGroupMembers")

class RegisterTransitGatewayMulticastGroupSourcesRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")
    network_interface_ids: TransitGatewayNetworkInterfaceIdList = pydantic.Field(None, alias="NetworkInterfaceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RegisterTransitGatewayMulticastGroupSourcesResult(_EC2ModelBase):
    registered_multicast_group_sources: 'TransitGatewayMulticastRegisteredGroupSources' = pydantic.Field(None, alias="RegisteredMulticastGroupSources")

class RejectTransitGatewayMulticastDomainAssociationsRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    subnet_ids: ValueStringList = pydantic.Field(None, alias="SubnetIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RejectTransitGatewayMulticastDomainAssociationsResult(_EC2ModelBase):
    associations: 'TransitGatewayMulticastDomainAssociations' = pydantic.Field(None, alias="Associations")

class RejectTransitGatewayPeeringAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RejectTransitGatewayPeeringAttachmentResult(_EC2ModelBase):
    transit_gateway_peering_attachment: 'TransitGatewayPeeringAttachment' = pydantic.Field(None, alias="TransitGatewayPeeringAttachment")

class RejectTransitGatewayVpcAttachmentRequest(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RejectTransitGatewayVpcAttachmentResult(_EC2ModelBase):
    transit_gateway_vpc_attachment: 'TransitGatewayVpcAttachment' = pydantic.Field(None, alias="TransitGatewayVpcAttachment")

class RejectVpcEndpointConnectionsRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")
    vpc_endpoint_ids: VpcEndpointIdList = pydantic.Field(None, alias="VpcEndpointIds")

class RejectVpcEndpointConnectionsResult(_EC2ModelBase):
    unsuccessful: UnsuccessfulItemSet = pydantic.Field(None, alias="Unsuccessful")

class RejectVpcPeeringConnectionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_peering_connection_id: VpcPeeringConnectionId = pydantic.Field(None, alias="VpcPeeringConnectionId")

class RejectVpcPeeringConnectionResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ReleaseAddressRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ReleaseHostsRequest(_EC2ModelBase):
    host_ids: RequestHostIdList = pydantic.Field(None, alias="HostIds")

class ReleaseHostsResult(_EC2ModelBase):
    successful: ResponseHostIdList = pydantic.Field(None, alias="Successful")
    unsuccessful: UnsuccessfulItemList = pydantic.Field(None, alias="Unsuccessful")

class ReleaseIpamPoolAllocationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ipam_pool_id: IpamPoolId = pydantic.Field(None, alias="IpamPoolId")
    cidr: String = pydantic.Field(None, alias="Cidr")
    ipam_pool_allocation_id: IpamPoolAllocationId = pydantic.Field(None, alias="IpamPoolAllocationId")

class ReleaseIpamPoolAllocationResult(_EC2ModelBase):
    success: Boolean = pydantic.Field(None, alias="Success")

class RemoveIpamOperatingRegion(_EC2ModelBase):
    region_name: String = pydantic.Field(None, alias="RegionName")

class RemovePrefixListEntry(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")

class ReplaceIamInstanceProfileAssociationRequest(_EC2ModelBase):
    iam_instance_profile: 'IamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    association_id: IamInstanceProfileAssociationId = pydantic.Field(None, alias="AssociationId")

class ReplaceIamInstanceProfileAssociationResult(_EC2ModelBase):
    iam_instance_profile_association: 'IamInstanceProfileAssociation' = pydantic.Field(None, alias="IamInstanceProfileAssociation")

class ReplaceNetworkAclAssociationRequest(_EC2ModelBase):
    association_id: NetworkAclAssociationId = pydantic.Field(None, alias="AssociationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_acl_id: NetworkAclId = pydantic.Field(None, alias="NetworkAclId")

class ReplaceNetworkAclAssociationResult(_EC2ModelBase):
    new_association_id: String = pydantic.Field(None, alias="NewAssociationId")

class ReplaceNetworkAclEntryRequest(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    egress: Boolean = pydantic.Field(None, alias="Egress")
    icmp_type_code: 'IcmpTypeCode' = pydantic.Field(None, alias="IcmpTypeCode")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    network_acl_id: NetworkAclId = pydantic.Field(None, alias="NetworkAclId")
    port_range: 'PortRange' = pydantic.Field(None, alias="PortRange")
    protocol: String = pydantic.Field(None, alias="Protocol")
    rule_action: RuleAction = pydantic.Field(None, alias="RuleAction")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")

class ReplaceRootVolumeTask(_EC2ModelBase):
    replace_root_volume_task_id: ReplaceRootVolumeTaskId = pydantic.Field(None, alias="ReplaceRootVolumeTaskId")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    task_state: ReplaceRootVolumeTaskState = pydantic.Field(None, alias="TaskState")
    start_time: String = pydantic.Field(None, alias="StartTime")
    complete_time: String = pydantic.Field(None, alias="CompleteTime")
    tags: TagList = pydantic.Field(None, alias="Tags")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    delete_replaced_root_volume: Boolean = pydantic.Field(None, alias="DeleteReplacedRootVolume")

class ReplaceRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    destination_ipv_6_cidr_block: String = pydantic.Field(None, alias="DestinationIpv6CidrBlock")
    destination_prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="DestinationPrefixListId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    vpc_endpoint_id: VpcEndpointId = pydantic.Field(None, alias="VpcEndpointId")
    egress_only_internet_gateway_id: EgressOnlyInternetGatewayId = pydantic.Field(None, alias="EgressOnlyInternetGatewayId")
    gateway_id: RouteGatewayId = pydantic.Field(None, alias="GatewayId")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    local_target: Boolean = pydantic.Field(None, alias="LocalTarget")
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    local_gateway_id: LocalGatewayId = pydantic.Field(None, alias="LocalGatewayId")
    carrier_gateway_id: CarrierGatewayId = pydantic.Field(None, alias="CarrierGatewayId")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")
    vpc_peering_connection_id: VpcPeeringConnectionId = pydantic.Field(None, alias="VpcPeeringConnectionId")
    core_network_arn: CoreNetworkArn = pydantic.Field(None, alias="CoreNetworkArn")

class ReplaceRouteTableAssociationRequest(_EC2ModelBase):
    association_id: RouteTableAssociationId = pydantic.Field(None, alias="AssociationId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    route_table_id: RouteTableId = pydantic.Field(None, alias="RouteTableId")

class ReplaceRouteTableAssociationResult(_EC2ModelBase):
    new_association_id: String = pydantic.Field(None, alias="NewAssociationId")
    association_state: 'RouteTableAssociationState' = pydantic.Field(None, alias="AssociationState")

class ReplaceTransitGatewayRouteRequest(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    blackhole: Boolean = pydantic.Field(None, alias="Blackhole")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ReplaceTransitGatewayRouteResult(_EC2ModelBase):
    route: 'TransitGatewayRoute' = pydantic.Field(None, alias="Route")

class ReplaceVpnTunnelRequest(_EC2ModelBase):
    vpn_connection_id: VpnConnectionId = pydantic.Field(None, alias="VpnConnectionId")
    vpn_tunnel_outside_ip_address: String = pydantic.Field(None, alias="VpnTunnelOutsideIpAddress")
    apply_pending_maintenance: Boolean = pydantic.Field(None, alias="ApplyPendingMaintenance")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ReplaceVpnTunnelResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ReportInstanceStatusRequest(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    end_time: DateTime = pydantic.Field(None, alias="EndTime")
    instances: InstanceIdStringList = pydantic.Field(None, alias="Instances")
    reason_codes: ReasonCodesList = pydantic.Field(None, alias="ReasonCodes")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")
    status: ReportStatusType = pydantic.Field(None, alias="Status")

class RequestFilterPortRange(_EC2ModelBase):
    from_port: Port = pydantic.Field(None, alias="FromPort")
    to_port: Port = pydantic.Field(None, alias="ToPort")

class RequestIpamResourceTag(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    value: String = pydantic.Field(None, alias="Value")

class RequestLaunchTemplateData(_EC2ModelBase):
    kernel_id: KernelId = pydantic.Field(None, alias="KernelId")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'LaunchTemplateIamInstanceProfileSpecificationRequest' = pydantic.Field(None, alias="IamInstanceProfile")
    block_device_mappings: LaunchTemplateBlockDeviceMappingRequestList = pydantic.Field(None, alias="BlockDeviceMappings")
    network_interfaces: LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList = pydantic.Field(None, alias="NetworkInterfaces")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    key_name: KeyPairName = pydantic.Field(None, alias="KeyName")
    monitoring: 'LaunchTemplatesMonitoringRequest' = pydantic.Field(None, alias="Monitoring")
    placement: 'LaunchTemplatePlacementRequest' = pydantic.Field(None, alias="Placement")
    ram_disk_id: RamdiskId = pydantic.Field(None, alias="RamDiskId")
    disable_api_termination: Boolean = pydantic.Field(None, alias="DisableApiTermination")
    instance_initiated_shutdown_behavior: ShutdownBehavior = pydantic.Field(None, alias="InstanceInitiatedShutdownBehavior")
    user_data: SensitiveUserData = pydantic.Field(None, alias="UserData")
    tag_specifications: LaunchTemplateTagSpecificationRequestList = pydantic.Field(None, alias="TagSpecifications")
    elastic_gpu_specifications: ElasticGpuSpecificationList = pydantic.Field(None, alias="ElasticGpuSpecifications")
    elastic_inference_accelerators: LaunchTemplateElasticInferenceAcceleratorList = pydantic.Field(None, alias="ElasticInferenceAccelerators")
    security_group_ids: SecurityGroupIdStringList = pydantic.Field(None, alias="SecurityGroupIds")
    security_groups: SecurityGroupStringList = pydantic.Field(None, alias="SecurityGroups")
    instance_market_options: 'LaunchTemplateInstanceMarketOptionsRequest' = pydantic.Field(None, alias="InstanceMarketOptions")
    credit_specification: 'CreditSpecificationRequest' = pydantic.Field(None, alias="CreditSpecification")
    cpu_options: 'LaunchTemplateCpuOptionsRequest' = pydantic.Field(None, alias="CpuOptions")
    capacity_reservation_specification: 'LaunchTemplateCapacityReservationSpecificationRequest' = pydantic.Field(None, alias="CapacityReservationSpecification")
    license_specifications: LaunchTemplateLicenseSpecificationListRequest = pydantic.Field(None, alias="LicenseSpecifications")
    hibernation_options: 'LaunchTemplateHibernationOptionsRequest' = pydantic.Field(None, alias="HibernationOptions")
    metadata_options: 'LaunchTemplateInstanceMetadataOptionsRequest' = pydantic.Field(None, alias="MetadataOptions")
    enclave_options: 'LaunchTemplateEnclaveOptionsRequest' = pydantic.Field(None, alias="EnclaveOptions")
    instance_requirements: 'InstanceRequirementsRequest' = pydantic.Field(None, alias="InstanceRequirements")
    private_dns_name_options: 'LaunchTemplatePrivateDnsNameOptionsRequest' = pydantic.Field(None, alias="PrivateDnsNameOptions")
    maintenance_options: 'LaunchTemplateInstanceMaintenanceOptionsRequest' = pydantic.Field(None, alias="MaintenanceOptions")
    disable_api_stop: Boolean = pydantic.Field(None, alias="DisableApiStop")

class RequestSpotFleetRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    spot_fleet_request_config: 'SpotFleetRequestConfigData' = pydantic.Field(None, alias="SpotFleetRequestConfig")

class RequestSpotFleetResponse(_EC2ModelBase):
    spot_fleet_request_id: String = pydantic.Field(None, alias="SpotFleetRequestId")

class RequestSpotInstancesRequest(_EC2ModelBase):
    availability_zone_group: String = pydantic.Field(None, alias="AvailabilityZoneGroup")
    block_duration_minutes: Integer = pydantic.Field(None, alias="BlockDurationMinutes")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    launch_group: String = pydantic.Field(None, alias="LaunchGroup")
    launch_specification: 'RequestSpotLaunchSpecification' = pydantic.Field(None, alias="LaunchSpecification")
    spot_price: String = pydantic.Field(None, alias="SpotPrice")
    type: SpotInstanceType = pydantic.Field(None, alias="Type")
    valid_from: DateTime = pydantic.Field(None, alias="ValidFrom")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    instance_interruption_behavior: InstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")

class RequestSpotInstancesResult(_EC2ModelBase):
    spot_instance_requests: SpotInstanceRequestList = pydantic.Field(None, alias="SpotInstanceRequests")

class RequestSpotLaunchSpecification(_EC2ModelBase):
    security_group_ids: RequestSpotLaunchSpecificationSecurityGroupIdList = pydantic.Field(None, alias="SecurityGroupIds")
    security_groups: RequestSpotLaunchSpecificationSecurityGroupList = pydantic.Field(None, alias="SecurityGroups")
    addressing_type: String = pydantic.Field(None, alias="AddressingType")
    block_device_mappings: BlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'IamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    kernel_id: KernelId = pydantic.Field(None, alias="KernelId")
    key_name: KeyPairName = pydantic.Field(None, alias="KeyName")
    monitoring: 'RunInstancesMonitoringEnabled' = pydantic.Field(None, alias="Monitoring")
    network_interfaces: InstanceNetworkInterfaceSpecificationList = pydantic.Field(None, alias="NetworkInterfaces")
    placement: 'SpotPlacement' = pydantic.Field(None, alias="Placement")
    ramdisk_id: RamdiskId = pydantic.Field(None, alias="RamdiskId")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    user_data: SensitiveUserData = pydantic.Field(None, alias="UserData")

class Reservation(_EC2ModelBase):
    groups: GroupIdentifierList = pydantic.Field(None, alias="Groups")
    instances: InstanceList = pydantic.Field(None, alias="Instances")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    requester_id: String = pydantic.Field(None, alias="RequesterId")
    reservation_id: String = pydantic.Field(None, alias="ReservationId")

class ReservationFleetInstanceSpecification(_EC2ModelBase):
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    instance_platform: CapacityReservationInstancePlatform = pydantic.Field(None, alias="InstancePlatform")
    weight: DoubleWithConstraints = pydantic.Field(None, alias="Weight")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    priority: IntegerWithConstraints = pydantic.Field(None, alias="Priority")

class ReservationValue(_EC2ModelBase):
    hourly_price: String = pydantic.Field(None, alias="HourlyPrice")
    remaining_total_value: String = pydantic.Field(None, alias="RemainingTotalValue")
    remaining_upfront_value: String = pydantic.Field(None, alias="RemainingUpfrontValue")

class ReservedInstanceLimitPrice(_EC2ModelBase):
    amount: Double = pydantic.Field(None, alias="Amount")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")

class ReservedInstanceReservationValue(_EC2ModelBase):
    reservation_value: 'ReservationValue' = pydantic.Field(None, alias="ReservationValue")
    reserved_instance_id: String = pydantic.Field(None, alias="ReservedInstanceId")

class ReservedInstances(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    duration: Long = pydantic.Field(None, alias="Duration")
    end: DateTime = pydantic.Field(None, alias="End")
    fixed_price: Float = pydantic.Field(None, alias="FixedPrice")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    product_description: RIProductDescription = pydantic.Field(None, alias="ProductDescription")
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")
    start: DateTime = pydantic.Field(None, alias="Start")
    state: ReservedInstanceState = pydantic.Field(None, alias="State")
    usage_price: Float = pydantic.Field(None, alias="UsagePrice")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    instance_tenancy: Tenancy = pydantic.Field(None, alias="InstanceTenancy")
    offering_class: OfferingClassType = pydantic.Field(None, alias="OfferingClass")
    offering_type: OfferingTypeValues = pydantic.Field(None, alias="OfferingType")
    recurring_charges: RecurringChargesList = pydantic.Field(None, alias="RecurringCharges")
    scope: scope = pydantic.Field(None, alias="Scope")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ReservedInstancesConfiguration(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    platform: String = pydantic.Field(None, alias="Platform")
    scope: scope = pydantic.Field(None, alias="Scope")

class ReservedInstancesId(_EC2ModelBase):
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")

class ReservedInstancesListing(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    create_date: DateTime = pydantic.Field(None, alias="CreateDate")
    instance_counts: InstanceCountList = pydantic.Field(None, alias="InstanceCounts")
    price_schedules: PriceScheduleList = pydantic.Field(None, alias="PriceSchedules")
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")
    reserved_instances_listing_id: String = pydantic.Field(None, alias="ReservedInstancesListingId")
    status: ListingStatus = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    tags: TagList = pydantic.Field(None, alias="Tags")
    update_date: DateTime = pydantic.Field(None, alias="UpdateDate")

class ReservedInstancesModification(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    create_date: DateTime = pydantic.Field(None, alias="CreateDate")
    effective_date: DateTime = pydantic.Field(None, alias="EffectiveDate")
    modification_results: ReservedInstancesModificationResultList = pydantic.Field(None, alias="ModificationResults")
    reserved_instances_ids: ReservedIntancesIds = pydantic.Field(None, alias="ReservedInstancesIds")
    reserved_instances_modification_id: String = pydantic.Field(None, alias="ReservedInstancesModificationId")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    update_date: DateTime = pydantic.Field(None, alias="UpdateDate")

class ReservedInstancesModificationResult(_EC2ModelBase):
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")
    target_configuration: 'ReservedInstancesConfiguration' = pydantic.Field(None, alias="TargetConfiguration")

class ReservedInstancesOffering(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    duration: Long = pydantic.Field(None, alias="Duration")
    fixed_price: Float = pydantic.Field(None, alias="FixedPrice")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    product_description: RIProductDescription = pydantic.Field(None, alias="ProductDescription")
    reserved_instances_offering_id: String = pydantic.Field(None, alias="ReservedInstancesOfferingId")
    usage_price: Float = pydantic.Field(None, alias="UsagePrice")
    currency_code: CurrencyCodeValues = pydantic.Field(None, alias="CurrencyCode")
    instance_tenancy: Tenancy = pydantic.Field(None, alias="InstanceTenancy")
    marketplace: Boolean = pydantic.Field(None, alias="Marketplace")
    offering_class: OfferingClassType = pydantic.Field(None, alias="OfferingClass")
    offering_type: OfferingTypeValues = pydantic.Field(None, alias="OfferingType")
    pricing_details: PricingDetailsList = pydantic.Field(None, alias="PricingDetails")
    recurring_charges: RecurringChargesList = pydantic.Field(None, alias="RecurringCharges")
    scope: scope = pydantic.Field(None, alias="Scope")

class ResetAddressAttributeRequest(_EC2ModelBase):
    allocation_id: AllocationId = pydantic.Field(None, alias="AllocationId")
    attribute: AddressAttributeName = pydantic.Field(None, alias="Attribute")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ResetAddressAttributeResult(_EC2ModelBase):
    address: 'AddressAttribute' = pydantic.Field(None, alias="Address")

class ResetEbsDefaultKmsKeyIdRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ResetEbsDefaultKmsKeyIdResult(_EC2ModelBase):
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")

class ResetFpgaImageAttributeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    fpga_image_id: FpgaImageId = pydantic.Field(None, alias="FpgaImageId")
    attribute: ResetFpgaImageAttributeName = pydantic.Field(None, alias="Attribute")

class ResetFpgaImageAttributeResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class ResetImageAttributeRequest(_EC2ModelBase):
    attribute: ResetImageAttributeName = pydantic.Field(None, alias="Attribute")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ResetInstanceAttributeRequest(_EC2ModelBase):
    attribute: InstanceAttributeName = pydantic.Field(None, alias="Attribute")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")

class ResetNetworkInterfaceAttributeRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    source_dest_check: String = pydantic.Field(None, alias="SourceDestCheck")

class ResetSnapshotAttributeRequest(_EC2ModelBase):
    attribute: SnapshotAttributeName = pydantic.Field(None, alias="Attribute")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ResourceStatement(_EC2ModelBase):
    resources: ValueStringList = pydantic.Field(None, alias="Resources")
    resource_types: ValueStringList = pydantic.Field(None, alias="ResourceTypes")

class ResourceStatementRequest(_EC2ModelBase):
    resources: ValueStringList = pydantic.Field(None, alias="Resources")
    resource_types: ValueStringList = pydantic.Field(None, alias="ResourceTypes")

class ResponseError(_EC2ModelBase):
    code: LaunchTemplateErrorCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ResponseLaunchTemplateData(_EC2ModelBase):
    kernel_id: String = pydantic.Field(None, alias="KernelId")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'LaunchTemplateIamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    block_device_mappings: LaunchTemplateBlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    network_interfaces: LaunchTemplateInstanceNetworkInterfaceSpecificationList = pydantic.Field(None, alias="NetworkInterfaces")
    image_id: String = pydantic.Field(None, alias="ImageId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    key_name: String = pydantic.Field(None, alias="KeyName")
    monitoring: 'LaunchTemplatesMonitoring' = pydantic.Field(None, alias="Monitoring")
    placement: 'LaunchTemplatePlacement' = pydantic.Field(None, alias="Placement")
    ram_disk_id: String = pydantic.Field(None, alias="RamDiskId")
    disable_api_termination: Boolean = pydantic.Field(None, alias="DisableApiTermination")
    instance_initiated_shutdown_behavior: ShutdownBehavior = pydantic.Field(None, alias="InstanceInitiatedShutdownBehavior")
    user_data: SensitiveUserData = pydantic.Field(None, alias="UserData")
    tag_specifications: LaunchTemplateTagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    elastic_gpu_specifications: ElasticGpuSpecificationResponseList = pydantic.Field(None, alias="ElasticGpuSpecifications")
    elastic_inference_accelerators: LaunchTemplateElasticInferenceAcceleratorResponseList = pydantic.Field(None, alias="ElasticInferenceAccelerators")
    security_group_ids: ValueStringList = pydantic.Field(None, alias="SecurityGroupIds")
    security_groups: ValueStringList = pydantic.Field(None, alias="SecurityGroups")
    instance_market_options: 'LaunchTemplateInstanceMarketOptions' = pydantic.Field(None, alias="InstanceMarketOptions")
    credit_specification: 'CreditSpecification' = pydantic.Field(None, alias="CreditSpecification")
    cpu_options: 'LaunchTemplateCpuOptions' = pydantic.Field(None, alias="CpuOptions")
    capacity_reservation_specification: 'LaunchTemplateCapacityReservationSpecificationResponse' = pydantic.Field(None, alias="CapacityReservationSpecification")
    license_specifications: LaunchTemplateLicenseList = pydantic.Field(None, alias="LicenseSpecifications")
    hibernation_options: 'LaunchTemplateHibernationOptions' = pydantic.Field(None, alias="HibernationOptions")
    metadata_options: 'LaunchTemplateInstanceMetadataOptions' = pydantic.Field(None, alias="MetadataOptions")
    enclave_options: 'LaunchTemplateEnclaveOptions' = pydantic.Field(None, alias="EnclaveOptions")
    instance_requirements: 'InstanceRequirements' = pydantic.Field(None, alias="InstanceRequirements")
    private_dns_name_options: 'LaunchTemplatePrivateDnsNameOptions' = pydantic.Field(None, alias="PrivateDnsNameOptions")
    maintenance_options: 'LaunchTemplateInstanceMaintenanceOptions' = pydantic.Field(None, alias="MaintenanceOptions")
    disable_api_stop: Boolean = pydantic.Field(None, alias="DisableApiStop")

class RestoreAddressToClassicRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    public_ip: String = pydantic.Field(None, alias="PublicIp")

class RestoreAddressToClassicResult(_EC2ModelBase):
    public_ip: String = pydantic.Field(None, alias="PublicIp")
    status: Status = pydantic.Field(None, alias="Status")

class RestoreImageFromRecycleBinRequest(_EC2ModelBase):
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RestoreImageFromRecycleBinResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class RestoreManagedPrefixListVersionRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    previous_version: Long = pydantic.Field(None, alias="PreviousVersion")
    current_version: Long = pydantic.Field(None, alias="CurrentVersion")

class RestoreManagedPrefixListVersionResult(_EC2ModelBase):
    prefix_list: 'ManagedPrefixList' = pydantic.Field(None, alias="PrefixList")

class RestoreSnapshotFromRecycleBinRequest(_EC2ModelBase):
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RestoreSnapshotFromRecycleBinResult(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    description: String = pydantic.Field(None, alias="Description")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    progress: String = pydantic.Field(None, alias="Progress")
    start_time: MillisecondDateTime = pydantic.Field(None, alias="StartTime")
    state: SnapshotState = pydantic.Field(None, alias="State")
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")

class RestoreSnapshotTierRequest(_EC2ModelBase):
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    temporary_restore_days: RestoreSnapshotTierRequestTemporaryRestoreDays = pydantic.Field(None, alias="TemporaryRestoreDays")
    permanent_restore: Boolean = pydantic.Field(None, alias="PermanentRestore")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RestoreSnapshotTierResult(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    restore_start_time: MillisecondDateTime = pydantic.Field(None, alias="RestoreStartTime")
    restore_duration: Integer = pydantic.Field(None, alias="RestoreDuration")
    is_permanent_restore: Boolean = pydantic.Field(None, alias="IsPermanentRestore")

class RevokeClientVpnIngressRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    target_network_cidr: String = pydantic.Field(None, alias="TargetNetworkCidr")
    access_group_id: String = pydantic.Field(None, alias="AccessGroupId")
    revoke_all_groups: Boolean = pydantic.Field(None, alias="RevokeAllGroups")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class RevokeClientVpnIngressResult(_EC2ModelBase):
    status: 'ClientVpnAuthorizationRuleStatus' = pydantic.Field(None, alias="Status")

class RevokeSecurityGroupEgressRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    security_group_rule_ids: SecurityGroupRuleIdList = pydantic.Field(None, alias="SecurityGroupRuleIds")
    cidr_ip: String = pydantic.Field(None, alias="CidrIp")
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    source_security_group_name: String = pydantic.Field(None, alias="SourceSecurityGroupName")
    source_security_group_owner_id: String = pydantic.Field(None, alias="SourceSecurityGroupOwnerId")

class RevokeSecurityGroupEgressResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")
    unknown_ip_permissions: IpPermissionList = pydantic.Field(None, alias="UnknownIpPermissions")

class RevokeSecurityGroupIngressRequest(_EC2ModelBase):
    cidr_ip: String = pydantic.Field(None, alias="CidrIp")
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    group_name: SecurityGroupName = pydantic.Field(None, alias="GroupName")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    source_security_group_name: String = pydantic.Field(None, alias="SourceSecurityGroupName")
    source_security_group_owner_id: String = pydantic.Field(None, alias="SourceSecurityGroupOwnerId")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    security_group_rule_ids: SecurityGroupRuleIdList = pydantic.Field(None, alias="SecurityGroupRuleIds")

class RevokeSecurityGroupIngressResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")
    unknown_ip_permissions: IpPermissionList = pydantic.Field(None, alias="UnknownIpPermissions")

class Route(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    destination_ipv_6_cidr_block: String = pydantic.Field(None, alias="DestinationIpv6CidrBlock")
    destination_prefix_list_id: String = pydantic.Field(None, alias="DestinationPrefixListId")
    egress_only_internet_gateway_id: String = pydantic.Field(None, alias="EgressOnlyInternetGatewayId")
    gateway_id: String = pydantic.Field(None, alias="GatewayId")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    instance_owner_id: String = pydantic.Field(None, alias="InstanceOwnerId")
    nat_gateway_id: String = pydantic.Field(None, alias="NatGatewayId")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    local_gateway_id: String = pydantic.Field(None, alias="LocalGatewayId")
    carrier_gateway_id: CarrierGatewayId = pydantic.Field(None, alias="CarrierGatewayId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    origin: RouteOrigin = pydantic.Field(None, alias="Origin")
    state: RouteState = pydantic.Field(None, alias="State")
    vpc_peering_connection_id: String = pydantic.Field(None, alias="VpcPeeringConnectionId")
    core_network_arn: CoreNetworkArn = pydantic.Field(None, alias="CoreNetworkArn")

class RouteTable(_EC2ModelBase):
    associations: RouteTableAssociationList = pydantic.Field(None, alias="Associations")
    propagating_vgws: PropagatingVgwList = pydantic.Field(None, alias="PropagatingVgws")
    route_table_id: String = pydantic.Field(None, alias="RouteTableId")
    routes: RouteList = pydantic.Field(None, alias="Routes")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")

class RouteTableAssociation(_EC2ModelBase):
    main: Boolean = pydantic.Field(None, alias="Main")
    route_table_association_id: String = pydantic.Field(None, alias="RouteTableAssociationId")
    route_table_id: String = pydantic.Field(None, alias="RouteTableId")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    gateway_id: String = pydantic.Field(None, alias="GatewayId")
    association_state: 'RouteTableAssociationState' = pydantic.Field(None, alias="AssociationState")

class RouteTableAssociationState(_EC2ModelBase):
    state: RouteTableAssociationStateCode = pydantic.Field(None, alias="State")
    status_message: String = pydantic.Field(None, alias="StatusMessage")

class RuleGroupRuleOptionsPair(_EC2ModelBase):
    rule_group_arn: ResourceArn = pydantic.Field(None, alias="RuleGroupArn")
    rule_options: RuleOptionList = pydantic.Field(None, alias="RuleOptions")

class RuleGroupTypePair(_EC2ModelBase):
    rule_group_arn: ResourceArn = pydantic.Field(None, alias="RuleGroupArn")
    rule_group_type: String = pydantic.Field(None, alias="RuleGroupType")

class RuleOption(_EC2ModelBase):
    keyword: String = pydantic.Field(None, alias="Keyword")
    settings: StringList = pydantic.Field(None, alias="Settings")

class RunInstancesMonitoringEnabled(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class RunInstancesRequest(_EC2ModelBase):
    block_device_mappings: BlockDeviceMappingRequestList = pydantic.Field(None, alias="BlockDeviceMappings")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: InstanceIpv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    kernel_id: KernelId = pydantic.Field(None, alias="KernelId")
    key_name: KeyPairName = pydantic.Field(None, alias="KeyName")
    max_count: Integer = pydantic.Field(None, alias="MaxCount")
    min_count: Integer = pydantic.Field(None, alias="MinCount")
    monitoring: 'RunInstancesMonitoringEnabled' = pydantic.Field(None, alias="Monitoring")
    placement: 'Placement' = pydantic.Field(None, alias="Placement")
    ramdisk_id: RamdiskId = pydantic.Field(None, alias="RamdiskId")
    security_group_ids: SecurityGroupIdStringList = pydantic.Field(None, alias="SecurityGroupIds")
    security_groups: SecurityGroupStringList = pydantic.Field(None, alias="SecurityGroups")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    user_data: RunInstancesUserData = pydantic.Field(None, alias="UserData")
    additional_info: String = pydantic.Field(None, alias="AdditionalInfo")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    disable_api_termination: Boolean = pydantic.Field(None, alias="DisableApiTermination")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'IamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    instance_initiated_shutdown_behavior: ShutdownBehavior = pydantic.Field(None, alias="InstanceInitiatedShutdownBehavior")
    network_interfaces: InstanceNetworkInterfaceSpecificationList = pydantic.Field(None, alias="NetworkInterfaces")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    elastic_gpu_specification: ElasticGpuSpecifications = pydantic.Field(None, alias="ElasticGpuSpecification")
    elastic_inference_accelerators: ElasticInferenceAccelerators = pydantic.Field(None, alias="ElasticInferenceAccelerators")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    launch_template: 'LaunchTemplateSpecification' = pydantic.Field(None, alias="LaunchTemplate")
    instance_market_options: 'InstanceMarketOptionsRequest' = pydantic.Field(None, alias="InstanceMarketOptions")
    credit_specification: 'CreditSpecificationRequest' = pydantic.Field(None, alias="CreditSpecification")
    cpu_options: 'CpuOptionsRequest' = pydantic.Field(None, alias="CpuOptions")
    capacity_reservation_specification: 'CapacityReservationSpecification' = pydantic.Field(None, alias="CapacityReservationSpecification")
    hibernation_options: 'HibernationOptionsRequest' = pydantic.Field(None, alias="HibernationOptions")
    license_specifications: LicenseSpecificationListRequest = pydantic.Field(None, alias="LicenseSpecifications")
    metadata_options: 'InstanceMetadataOptionsRequest' = pydantic.Field(None, alias="MetadataOptions")
    enclave_options: 'EnclaveOptionsRequest' = pydantic.Field(None, alias="EnclaveOptions")
    private_dns_name_options: 'PrivateDnsNameOptionsRequest' = pydantic.Field(None, alias="PrivateDnsNameOptions")
    maintenance_options: 'InstanceMaintenanceOptionsRequest' = pydantic.Field(None, alias="MaintenanceOptions")
    disable_api_stop: Boolean = pydantic.Field(None, alias="DisableApiStop")

class RunScheduledInstancesRequest(_EC2ModelBase):
    client_token: String = pydantic.Field(None, alias="ClientToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    launch_specification: 'ScheduledInstancesLaunchSpecification' = pydantic.Field(None, alias="LaunchSpecification")
    scheduled_instance_id: ScheduledInstanceId = pydantic.Field(None, alias="ScheduledInstanceId")

class RunScheduledInstancesResult(_EC2ModelBase):
    instance_id_set: InstanceIdSet = pydantic.Field(None, alias="InstanceIdSet")

class S3ObjectTag(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    value: String = pydantic.Field(None, alias="Value")

class S3Storage(_EC2ModelBase):
    aws_access_key_id: String = pydantic.Field(None, alias="AWSAccessKeyId")
    bucket: String = pydantic.Field(None, alias="Bucket")
    prefix: String = pydantic.Field(None, alias="Prefix")
    upload_policy: Blob = pydantic.Field(None, alias="UploadPolicy")
    upload_policy_signature: String = pydantic.Field(None, alias="UploadPolicySignature")

class ScheduledInstance(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    create_date: DateTime = pydantic.Field(None, alias="CreateDate")
    hourly_price: String = pydantic.Field(None, alias="HourlyPrice")
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    network_platform: String = pydantic.Field(None, alias="NetworkPlatform")
    next_slot_start_time: DateTime = pydantic.Field(None, alias="NextSlotStartTime")
    platform: String = pydantic.Field(None, alias="Platform")
    previous_slot_end_time: DateTime = pydantic.Field(None, alias="PreviousSlotEndTime")
    recurrence: 'ScheduledInstanceRecurrence' = pydantic.Field(None, alias="Recurrence")
    scheduled_instance_id: String = pydantic.Field(None, alias="ScheduledInstanceId")
    slot_duration_in_hours: Integer = pydantic.Field(None, alias="SlotDurationInHours")
    term_end_date: DateTime = pydantic.Field(None, alias="TermEndDate")
    term_start_date: DateTime = pydantic.Field(None, alias="TermStartDate")
    total_scheduled_instance_hours: Integer = pydantic.Field(None, alias="TotalScheduledInstanceHours")

class ScheduledInstanceAvailability(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    available_instance_count: Integer = pydantic.Field(None, alias="AvailableInstanceCount")
    first_slot_start_time: DateTime = pydantic.Field(None, alias="FirstSlotStartTime")
    hourly_price: String = pydantic.Field(None, alias="HourlyPrice")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    max_term_duration_in_days: Integer = pydantic.Field(None, alias="MaxTermDurationInDays")
    min_term_duration_in_days: Integer = pydantic.Field(None, alias="MinTermDurationInDays")
    network_platform: String = pydantic.Field(None, alias="NetworkPlatform")
    platform: String = pydantic.Field(None, alias="Platform")
    purchase_token: String = pydantic.Field(None, alias="PurchaseToken")
    recurrence: 'ScheduledInstanceRecurrence' = pydantic.Field(None, alias="Recurrence")
    slot_duration_in_hours: Integer = pydantic.Field(None, alias="SlotDurationInHours")
    total_scheduled_instance_hours: Integer = pydantic.Field(None, alias="TotalScheduledInstanceHours")

class ScheduledInstanceRecurrence(_EC2ModelBase):
    frequency: String = pydantic.Field(None, alias="Frequency")
    interval: Integer = pydantic.Field(None, alias="Interval")
    occurrence_day_set: OccurrenceDaySet = pydantic.Field(None, alias="OccurrenceDaySet")
    occurrence_relative_to_end: Boolean = pydantic.Field(None, alias="OccurrenceRelativeToEnd")
    occurrence_unit: String = pydantic.Field(None, alias="OccurrenceUnit")

class ScheduledInstanceRecurrenceRequest(_EC2ModelBase):
    frequency: String = pydantic.Field(None, alias="Frequency")
    interval: Integer = pydantic.Field(None, alias="Interval")
    occurrence_days: OccurrenceDayRequestSet = pydantic.Field(None, alias="OccurrenceDays")
    occurrence_relative_to_end: Boolean = pydantic.Field(None, alias="OccurrenceRelativeToEnd")
    occurrence_unit: String = pydantic.Field(None, alias="OccurrenceUnit")

class ScheduledInstancesBlockDeviceMapping(_EC2ModelBase):
    device_name: String = pydantic.Field(None, alias="DeviceName")
    ebs: 'ScheduledInstancesEbs' = pydantic.Field(None, alias="Ebs")
    no_device: String = pydantic.Field(None, alias="NoDevice")
    virtual_name: String = pydantic.Field(None, alias="VirtualName")

class ScheduledInstancesEbs(_EC2ModelBase):
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    iops: Integer = pydantic.Field(None, alias="Iops")
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")
    volume_type: String = pydantic.Field(None, alias="VolumeType")

class ScheduledInstancesIamInstanceProfile(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")
    name: String = pydantic.Field(None, alias="Name")

class ScheduledInstancesIpv6Address(_EC2ModelBase):
    ipv_6_address: Ipv6Address = pydantic.Field(None, alias="Ipv6Address")

class ScheduledInstancesLaunchSpecification(_EC2ModelBase):
    block_device_mappings: ScheduledInstancesBlockDeviceMappingSet = pydantic.Field(None, alias="BlockDeviceMappings")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'ScheduledInstancesIamInstanceProfile' = pydantic.Field(None, alias="IamInstanceProfile")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    instance_type: String = pydantic.Field(None, alias="InstanceType")
    kernel_id: KernelId = pydantic.Field(None, alias="KernelId")
    key_name: KeyPairName = pydantic.Field(None, alias="KeyName")
    monitoring: 'ScheduledInstancesMonitoring' = pydantic.Field(None, alias="Monitoring")
    network_interfaces: ScheduledInstancesNetworkInterfaceSet = pydantic.Field(None, alias="NetworkInterfaces")
    placement: 'ScheduledInstancesPlacement' = pydantic.Field(None, alias="Placement")
    ramdisk_id: RamdiskId = pydantic.Field(None, alias="RamdiskId")
    security_group_ids: ScheduledInstancesSecurityGroupIdSet = pydantic.Field(None, alias="SecurityGroupIds")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    user_data: String = pydantic.Field(None, alias="UserData")

class ScheduledInstancesMonitoring(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class ScheduledInstancesNetworkInterface(_EC2ModelBase):
    associate_public_ip_address: Boolean = pydantic.Field(None, alias="AssociatePublicIpAddress")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")
    description: String = pydantic.Field(None, alias="Description")
    device_index: Integer = pydantic.Field(None, alias="DeviceIndex")
    groups: ScheduledInstancesSecurityGroupIdSet = pydantic.Field(None, alias="Groups")
    ipv_6_address_count: Integer = pydantic.Field(None, alias="Ipv6AddressCount")
    ipv_6_addresses: ScheduledInstancesIpv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")
    private_ip_address_configs: PrivateIpAddressConfigSet = pydantic.Field(None, alias="PrivateIpAddressConfigs")
    secondary_private_ip_address_count: Integer = pydantic.Field(None, alias="SecondaryPrivateIpAddressCount")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")

class ScheduledInstancesPlacement(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")

class ScheduledInstancesPrivateIpAddressConfig(_EC2ModelBase):
    primary: Boolean = pydantic.Field(None, alias="Primary")
    private_ip_address: String = pydantic.Field(None, alias="PrivateIpAddress")

class SearchLocalGatewayRoutesRequest(_EC2ModelBase):
    local_gateway_route_table_id: LocalGatewayRoutetableId = pydantic.Field(None, alias="LocalGatewayRouteTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: MaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class SearchLocalGatewayRoutesResult(_EC2ModelBase):
    routes: LocalGatewayRouteList = pydantic.Field(None, alias="Routes")
    next_token: String = pydantic.Field(None, alias="NextToken")

class SearchTransitGatewayMulticastGroupsRequest(_EC2ModelBase):
    transit_gateway_multicast_domain_id: TransitGatewayMulticastDomainId = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    next_token: String = pydantic.Field(None, alias="NextToken")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class SearchTransitGatewayMulticastGroupsResult(_EC2ModelBase):
    multicast_groups: TransitGatewayMulticastGroupList = pydantic.Field(None, alias="MulticastGroups")
    next_token: String = pydantic.Field(None, alias="NextToken")

class SearchTransitGatewayRoutesRequest(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    filters: FilterList = pydantic.Field(None, alias="Filters")
    max_results: TransitGatewayMaxResults = pydantic.Field(None, alias="MaxResults")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class SearchTransitGatewayRoutesResult(_EC2ModelBase):
    routes: TransitGatewayRouteList = pydantic.Field(None, alias="Routes")
    additional_routes_available: Boolean = pydantic.Field(None, alias="AdditionalRoutesAvailable")

class SecurityGroup(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    group_name: String = pydantic.Field(None, alias="GroupName")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    group_id: String = pydantic.Field(None, alias="GroupId")
    ip_permissions_egress: IpPermissionList = pydantic.Field(None, alias="IpPermissionsEgress")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class SecurityGroupIdentifier(_EC2ModelBase):
    group_id: String = pydantic.Field(None, alias="GroupId")
    group_name: String = pydantic.Field(None, alias="GroupName")

class SecurityGroupReference(_EC2ModelBase):
    group_id: String = pydantic.Field(None, alias="GroupId")
    referencing_vpc_id: String = pydantic.Field(None, alias="ReferencingVpcId")
    vpc_peering_connection_id: String = pydantic.Field(None, alias="VpcPeeringConnectionId")

class SecurityGroupRule(_EC2ModelBase):
    security_group_rule_id: SecurityGroupRuleId = pydantic.Field(None, alias="SecurityGroupRuleId")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    group_owner_id: String = pydantic.Field(None, alias="GroupOwnerId")
    is_egress: Boolean = pydantic.Field(None, alias="IsEgress")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    cidr_ipv_4: String = pydantic.Field(None, alias="CidrIpv4")
    cidr_ipv_6: String = pydantic.Field(None, alias="CidrIpv6")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    referenced_group_info: 'ReferencedSecurityGroup' = pydantic.Field(None, alias="ReferencedGroupInfo")
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")

class SecurityGroupRuleDescription(_EC2ModelBase):
    security_group_rule_id: String = pydantic.Field(None, alias="SecurityGroupRuleId")
    description: String = pydantic.Field(None, alias="Description")

class SecurityGroupRuleRequest(_EC2ModelBase):
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    cidr_ipv_4: String = pydantic.Field(None, alias="CidrIpv4")
    cidr_ipv_6: String = pydantic.Field(None, alias="CidrIpv6")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    referenced_group_id: SecurityGroupId = pydantic.Field(None, alias="ReferencedGroupId")
    description: String = pydantic.Field(None, alias="Description")

class SecurityGroupRuleUpdate(_EC2ModelBase):
    security_group_rule_id: SecurityGroupRuleId = pydantic.Field(None, alias="SecurityGroupRuleId")
    security_group_rule: 'SecurityGroupRuleRequest' = pydantic.Field(None, alias="SecurityGroupRule")

class SendDiagnosticInterruptRequest(_EC2ModelBase):
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class ServiceConfiguration(_EC2ModelBase):
    service_type: ServiceTypeDetailSet = pydantic.Field(None, alias="ServiceType")
    service_id: String = pydantic.Field(None, alias="ServiceId")
    service_name: String = pydantic.Field(None, alias="ServiceName")
    service_state: ServiceState = pydantic.Field(None, alias="ServiceState")
    availability_zones: ValueStringList = pydantic.Field(None, alias="AvailabilityZones")
    acceptance_required: Boolean = pydantic.Field(None, alias="AcceptanceRequired")
    manages_vpc_endpoints: Boolean = pydantic.Field(None, alias="ManagesVpcEndpoints")
    network_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="NetworkLoadBalancerArns")
    gateway_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="GatewayLoadBalancerArns")
    supported_ip_address_types: SupportedIpAddressTypes = pydantic.Field(None, alias="SupportedIpAddressTypes")
    base_endpoint_dns_names: ValueStringList = pydantic.Field(None, alias="BaseEndpointDnsNames")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_dns_name_configuration: 'PrivateDnsNameConfiguration' = pydantic.Field(None, alias="PrivateDnsNameConfiguration")
    payer_responsibility: PayerResponsibility = pydantic.Field(None, alias="PayerResponsibility")
    tags: TagList = pydantic.Field(None, alias="Tags")

class ServiceDetail(_EC2ModelBase):
    service_name: String = pydantic.Field(None, alias="ServiceName")
    service_id: String = pydantic.Field(None, alias="ServiceId")
    service_type: ServiceTypeDetailSet = pydantic.Field(None, alias="ServiceType")
    availability_zones: ValueStringList = pydantic.Field(None, alias="AvailabilityZones")
    owner: String = pydantic.Field(None, alias="Owner")
    base_endpoint_dns_names: ValueStringList = pydantic.Field(None, alias="BaseEndpointDnsNames")
    private_dns_name: String = pydantic.Field(None, alias="PrivateDnsName")
    private_dns_names: PrivateDnsDetailsSet = pydantic.Field(None, alias="PrivateDnsNames")
    vpc_endpoint_policy_supported: Boolean = pydantic.Field(None, alias="VpcEndpointPolicySupported")
    acceptance_required: Boolean = pydantic.Field(None, alias="AcceptanceRequired")
    manages_vpc_endpoints: Boolean = pydantic.Field(None, alias="ManagesVpcEndpoints")
    payer_responsibility: PayerResponsibility = pydantic.Field(None, alias="PayerResponsibility")
    tags: TagList = pydantic.Field(None, alias="Tags")
    private_dns_name_verification_state: DnsNameState = pydantic.Field(None, alias="PrivateDnsNameVerificationState")
    supported_ip_address_types: SupportedIpAddressTypes = pydantic.Field(None, alias="SupportedIpAddressTypes")

class ServiceTypeDetail(_EC2ModelBase):
    service_type: ServiceType = pydantic.Field(None, alias="ServiceType")

class SlotDateTimeRangeRequest(_EC2ModelBase):
    earliest_time: DateTime = pydantic.Field(None, alias="EarliestTime")
    latest_time: DateTime = pydantic.Field(None, alias="LatestTime")

class SlotStartTimeRangeRequest(_EC2ModelBase):
    earliest_time: DateTime = pydantic.Field(None, alias="EarliestTime")
    latest_time: DateTime = pydantic.Field(None, alias="LatestTime")

class Snapshot(_EC2ModelBase):
    data_encryption_key_id: String = pydantic.Field(None, alias="DataEncryptionKeyId")
    description: String = pydantic.Field(None, alias="Description")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    progress: String = pydantic.Field(None, alias="Progress")
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")
    state: SnapshotState = pydantic.Field(None, alias="State")
    state_message: String = pydantic.Field(None, alias="StateMessage")
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")
    owner_alias: String = pydantic.Field(None, alias="OwnerAlias")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_tier: StorageTier = pydantic.Field(None, alias="StorageTier")
    restore_expiry_time: MillisecondDateTime = pydantic.Field(None, alias="RestoreExpiryTime")

class SnapshotDetail(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    device_name: String = pydantic.Field(None, alias="DeviceName")
    disk_image_size: Double = pydantic.Field(None, alias="DiskImageSize")
    format: String = pydantic.Field(None, alias="Format")
    progress: String = pydantic.Field(None, alias="Progress")
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    url: SensitiveUrl = pydantic.Field(None, alias="Url")
    user_bucket: 'UserBucketDetails' = pydantic.Field(None, alias="UserBucket")

class SnapshotDiskContainer(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    format: String = pydantic.Field(None, alias="Format")
    url: SensitiveUrl = pydantic.Field(None, alias="Url")
    user_bucket: 'UserBucket' = pydantic.Field(None, alias="UserBucket")

class SnapshotInfo(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    state: SnapshotState = pydantic.Field(None, alias="State")
    volume_size: Integer = pydantic.Field(None, alias="VolumeSize")
    start_time: MillisecondDateTime = pydantic.Field(None, alias="StartTime")
    progress: String = pydantic.Field(None, alias="Progress")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")

class SnapshotRecycleBinInfo(_EC2ModelBase):
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    recycle_bin_enter_time: MillisecondDateTime = pydantic.Field(None, alias="RecycleBinEnterTime")
    recycle_bin_exit_time: MillisecondDateTime = pydantic.Field(None, alias="RecycleBinExitTime")
    description: String = pydantic.Field(None, alias="Description")
    volume_id: String = pydantic.Field(None, alias="VolumeId")

class SnapshotTaskDetail(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    disk_image_size: Double = pydantic.Field(None, alias="DiskImageSize")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    format: String = pydantic.Field(None, alias="Format")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    progress: String = pydantic.Field(None, alias="Progress")
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    status: String = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    url: SensitiveUrl = pydantic.Field(None, alias="Url")
    user_bucket: 'UserBucketDetails' = pydantic.Field(None, alias="UserBucket")

class SnapshotTierStatus(_EC2ModelBase):
    snapshot_id: SnapshotId = pydantic.Field(None, alias="SnapshotId")
    volume_id: VolumeId = pydantic.Field(None, alias="VolumeId")
    status: SnapshotState = pydantic.Field(None, alias="Status")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    storage_tier: StorageTier = pydantic.Field(None, alias="StorageTier")
    last_tiering_start_time: MillisecondDateTime = pydantic.Field(None, alias="LastTieringStartTime")
    last_tiering_progress: Integer = pydantic.Field(None, alias="LastTieringProgress")
    last_tiering_operation_status: TieringOperationStatus = pydantic.Field(None, alias="LastTieringOperationStatus")
    last_tiering_operation_status_detail: String = pydantic.Field(None, alias="LastTieringOperationStatusDetail")
    archival_complete_time: MillisecondDateTime = pydantic.Field(None, alias="ArchivalCompleteTime")
    restore_expiry_time: MillisecondDateTime = pydantic.Field(None, alias="RestoreExpiryTime")

class SpotCapacityRebalance(_EC2ModelBase):
    replacement_strategy: ReplacementStrategy = pydantic.Field(None, alias="ReplacementStrategy")
    termination_delay: Integer = pydantic.Field(None, alias="TerminationDelay")

class SpotDatafeedSubscription(_EC2ModelBase):
    bucket: String = pydantic.Field(None, alias="Bucket")
    fault: 'SpotInstanceStateFault' = pydantic.Field(None, alias="Fault")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    prefix: String = pydantic.Field(None, alias="Prefix")
    state: DatafeedSubscriptionState = pydantic.Field(None, alias="State")

class SpotFleetLaunchSpecification(_EC2ModelBase):
    security_groups: GroupIdentifierList = pydantic.Field(None, alias="SecurityGroups")
    addressing_type: String = pydantic.Field(None, alias="AddressingType")
    block_device_mappings: BlockDeviceMappingList = pydantic.Field(None, alias="BlockDeviceMappings")
    ebs_optimized: Boolean = pydantic.Field(None, alias="EbsOptimized")
    iam_instance_profile: 'IamInstanceProfileSpecification' = pydantic.Field(None, alias="IamInstanceProfile")
    image_id: ImageId = pydantic.Field(None, alias="ImageId")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    kernel_id: String = pydantic.Field(None, alias="KernelId")
    key_name: KeyPairName = pydantic.Field(None, alias="KeyName")
    monitoring: 'SpotFleetMonitoring' = pydantic.Field(None, alias="Monitoring")
    network_interfaces: InstanceNetworkInterfaceSpecificationList = pydantic.Field(None, alias="NetworkInterfaces")
    placement: 'SpotPlacement' = pydantic.Field(None, alias="Placement")
    ramdisk_id: String = pydantic.Field(None, alias="RamdiskId")
    spot_price: String = pydantic.Field(None, alias="SpotPrice")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    user_data: SensitiveUserData = pydantic.Field(None, alias="UserData")
    weighted_capacity: Double = pydantic.Field(None, alias="WeightedCapacity")
    tag_specifications: SpotFleetTagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    instance_requirements: 'InstanceRequirements' = pydantic.Field(None, alias="InstanceRequirements")

class SpotFleetMonitoring(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")

class SpotFleetRequestConfig(_EC2ModelBase):
    activity_status: ActivityStatus = pydantic.Field(None, alias="ActivityStatus")
    create_time: MillisecondDateTime = pydantic.Field(None, alias="CreateTime")
    spot_fleet_request_config: 'SpotFleetRequestConfigData' = pydantic.Field(None, alias="SpotFleetRequestConfig")
    spot_fleet_request_id: String = pydantic.Field(None, alias="SpotFleetRequestId")
    spot_fleet_request_state: BatchState = pydantic.Field(None, alias="SpotFleetRequestState")
    tags: TagList = pydantic.Field(None, alias="Tags")

class SpotFleetRequestConfigData(_EC2ModelBase):
    allocation_strategy: AllocationStrategy = pydantic.Field(None, alias="AllocationStrategy")
    on_demand_allocation_strategy: OnDemandAllocationStrategy = pydantic.Field(None, alias="OnDemandAllocationStrategy")
    spot_maintenance_strategies: 'SpotMaintenanceStrategies' = pydantic.Field(None, alias="SpotMaintenanceStrategies")
    client_token: String = pydantic.Field(None, alias="ClientToken")
    excess_capacity_termination_policy: ExcessCapacityTerminationPolicy = pydantic.Field(None, alias="ExcessCapacityTerminationPolicy")
    fulfilled_capacity: Double = pydantic.Field(None, alias="FulfilledCapacity")
    on_demand_fulfilled_capacity: Double = pydantic.Field(None, alias="OnDemandFulfilledCapacity")
    iam_fleet_role: String = pydantic.Field(None, alias="IamFleetRole")
    launch_specifications: LaunchSpecsList = pydantic.Field(None, alias="LaunchSpecifications")
    launch_template_configs: LaunchTemplateConfigList = pydantic.Field(None, alias="LaunchTemplateConfigs")
    spot_price: String = pydantic.Field(None, alias="SpotPrice")
    target_capacity: Integer = pydantic.Field(None, alias="TargetCapacity")
    on_demand_target_capacity: Integer = pydantic.Field(None, alias="OnDemandTargetCapacity")
    on_demand_max_total_price: String = pydantic.Field(None, alias="OnDemandMaxTotalPrice")
    spot_max_total_price: String = pydantic.Field(None, alias="SpotMaxTotalPrice")
    terminate_instances_with_expiration: Boolean = pydantic.Field(None, alias="TerminateInstancesWithExpiration")
    type: FleetType = pydantic.Field(None, alias="Type")
    valid_from: DateTime = pydantic.Field(None, alias="ValidFrom")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    replace_unhealthy_instances: Boolean = pydantic.Field(None, alias="ReplaceUnhealthyInstances")
    instance_interruption_behavior: InstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")
    load_balancers_config: 'LoadBalancersConfig' = pydantic.Field(None, alias="LoadBalancersConfig")
    instance_pools_to_use_count: Integer = pydantic.Field(None, alias="InstancePoolsToUseCount")
    context: String = pydantic.Field(None, alias="Context")
    target_capacity_unit_type: TargetCapacityUnitType = pydantic.Field(None, alias="TargetCapacityUnitType")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")

class SpotFleetTagSpecification(_EC2ModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    tags: TagList = pydantic.Field(None, alias="Tags")

class SpotInstanceRequest(_EC2ModelBase):
    actual_block_hourly_price: String = pydantic.Field(None, alias="ActualBlockHourlyPrice")
    availability_zone_group: String = pydantic.Field(None, alias="AvailabilityZoneGroup")
    block_duration_minutes: Integer = pydantic.Field(None, alias="BlockDurationMinutes")
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    fault: 'SpotInstanceStateFault' = pydantic.Field(None, alias="Fault")
    instance_id: InstanceId = pydantic.Field(None, alias="InstanceId")
    launch_group: String = pydantic.Field(None, alias="LaunchGroup")
    launch_specification: 'LaunchSpecification' = pydantic.Field(None, alias="LaunchSpecification")
    launched_availability_zone: String = pydantic.Field(None, alias="LaunchedAvailabilityZone")
    product_description: RIProductDescription = pydantic.Field(None, alias="ProductDescription")
    spot_instance_request_id: String = pydantic.Field(None, alias="SpotInstanceRequestId")
    spot_price: String = pydantic.Field(None, alias="SpotPrice")
    state: SpotInstanceState = pydantic.Field(None, alias="State")
    status: 'SpotInstanceStatus' = pydantic.Field(None, alias="Status")
    tags: TagList = pydantic.Field(None, alias="Tags")
    type: SpotInstanceType = pydantic.Field(None, alias="Type")
    valid_from: DateTime = pydantic.Field(None, alias="ValidFrom")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    instance_interruption_behavior: InstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")

class SpotInstanceStateFault(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class SpotInstanceStatus(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")
    update_time: DateTime = pydantic.Field(None, alias="UpdateTime")

class SpotMaintenanceStrategies(_EC2ModelBase):
    capacity_rebalance: 'SpotCapacityRebalance' = pydantic.Field(None, alias="CapacityRebalance")

class SpotMarketOptions(_EC2ModelBase):
    max_price: String = pydantic.Field(None, alias="MaxPrice")
    spot_instance_type: SpotInstanceType = pydantic.Field(None, alias="SpotInstanceType")
    block_duration_minutes: Integer = pydantic.Field(None, alias="BlockDurationMinutes")
    valid_until: DateTime = pydantic.Field(None, alias="ValidUntil")
    instance_interruption_behavior: InstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")

class SpotOptions(_EC2ModelBase):
    allocation_strategy: SpotAllocationStrategy = pydantic.Field(None, alias="AllocationStrategy")
    maintenance_strategies: 'FleetSpotMaintenanceStrategies' = pydantic.Field(None, alias="MaintenanceStrategies")
    instance_interruption_behavior: SpotInstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")
    instance_pools_to_use_count: Integer = pydantic.Field(None, alias="InstancePoolsToUseCount")
    single_instance_type: Boolean = pydantic.Field(None, alias="SingleInstanceType")
    single_availability_zone: Boolean = pydantic.Field(None, alias="SingleAvailabilityZone")
    min_target_capacity: Integer = pydantic.Field(None, alias="MinTargetCapacity")
    max_total_price: String = pydantic.Field(None, alias="MaxTotalPrice")

class SpotOptionsRequest(_EC2ModelBase):
    allocation_strategy: SpotAllocationStrategy = pydantic.Field(None, alias="AllocationStrategy")
    maintenance_strategies: 'FleetSpotMaintenanceStrategiesRequest' = pydantic.Field(None, alias="MaintenanceStrategies")
    instance_interruption_behavior: SpotInstanceInterruptionBehavior = pydantic.Field(None, alias="InstanceInterruptionBehavior")
    instance_pools_to_use_count: Integer = pydantic.Field(None, alias="InstancePoolsToUseCount")
    single_instance_type: Boolean = pydantic.Field(None, alias="SingleInstanceType")
    single_availability_zone: Boolean = pydantic.Field(None, alias="SingleAvailabilityZone")
    min_target_capacity: Integer = pydantic.Field(None, alias="MinTargetCapacity")
    max_total_price: String = pydantic.Field(None, alias="MaxTotalPrice")

class SpotPlacement(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    group_name: PlacementGroupName = pydantic.Field(None, alias="GroupName")
    tenancy: Tenancy = pydantic.Field(None, alias="Tenancy")

class SpotPlacementScore(_EC2ModelBase):
    region: String = pydantic.Field(None, alias="Region")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    score: Integer = pydantic.Field(None, alias="Score")

class SpotPrice(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    instance_type: InstanceType = pydantic.Field(None, alias="InstanceType")
    product_description: RIProductDescription = pydantic.Field(None, alias="ProductDescription")
    spot_price: String = pydantic.Field(None, alias="SpotPrice")
    timestamp: DateTime = pydantic.Field(None, alias="Timestamp")

class StaleIpPermission(_EC2ModelBase):
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    ip_protocol: String = pydantic.Field(None, alias="IpProtocol")
    ip_ranges: IpRanges = pydantic.Field(None, alias="IpRanges")
    prefix_list_ids: PrefixListIdSet = pydantic.Field(None, alias="PrefixListIds")
    to_port: Integer = pydantic.Field(None, alias="ToPort")
    user_id_group_pairs: UserIdGroupPairSet = pydantic.Field(None, alias="UserIdGroupPairs")

class StaleSecurityGroup(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    group_id: String = pydantic.Field(None, alias="GroupId")
    group_name: String = pydantic.Field(None, alias="GroupName")
    stale_ip_permissions: StaleIpPermissionSet = pydantic.Field(None, alias="StaleIpPermissions")
    stale_ip_permissions_egress: StaleIpPermissionSet = pydantic.Field(None, alias="StaleIpPermissionsEgress")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class StartInstancesRequest(_EC2ModelBase):
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    additional_info: String = pydantic.Field(None, alias="AdditionalInfo")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class StartInstancesResult(_EC2ModelBase):
    starting_instances: InstanceStateChangeList = pydantic.Field(None, alias="StartingInstances")

class StartNetworkInsightsAccessScopeAnalysisRequest(_EC2ModelBase):
    network_insights_access_scope_id: NetworkInsightsAccessScopeId = pydantic.Field(None, alias="NetworkInsightsAccessScopeId")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class StartNetworkInsightsAccessScopeAnalysisResult(_EC2ModelBase):
    network_insights_access_scope_analysis: 'NetworkInsightsAccessScopeAnalysis' = pydantic.Field(None, alias="NetworkInsightsAccessScopeAnalysis")

class StartNetworkInsightsAnalysisRequest(_EC2ModelBase):
    network_insights_path_id: NetworkInsightsPathId = pydantic.Field(None, alias="NetworkInsightsPathId")
    additional_accounts: ValueStringList = pydantic.Field(None, alias="AdditionalAccounts")
    filter_in_arns: ArnList = pydantic.Field(None, alias="FilterInArns")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    tag_specifications: TagSpecificationList = pydantic.Field(None, alias="TagSpecifications")
    client_token: String = pydantic.Field(None, alias="ClientToken")

class StartNetworkInsightsAnalysisResult(_EC2ModelBase):
    network_insights_analysis: 'NetworkInsightsAnalysis' = pydantic.Field(None, alias="NetworkInsightsAnalysis")

class StartVpcEndpointServicePrivateDnsVerificationRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    service_id: VpcEndpointServiceId = pydantic.Field(None, alias="ServiceId")

class StartVpcEndpointServicePrivateDnsVerificationResult(_EC2ModelBase):
    return_value: Boolean = pydantic.Field(None, alias="ReturnValue")

class StateReason(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class StopInstancesRequest(_EC2ModelBase):
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    hibernate: Boolean = pydantic.Field(None, alias="Hibernate")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    force: Boolean = pydantic.Field(None, alias="Force")

class StopInstancesResult(_EC2ModelBase):
    stopping_instances: InstanceStateChangeList = pydantic.Field(None, alias="StoppingInstances")

class Storage(_EC2ModelBase):
    s_3: 'S3Storage' = pydantic.Field(None, alias="S3")

class StorageLocation(_EC2ModelBase):
    bucket: String = pydantic.Field(None, alias="Bucket")
    key: String = pydantic.Field(None, alias="Key")

class StoreImageTaskResult(_EC2ModelBase):
    ami_id: String = pydantic.Field(None, alias="AmiId")
    task_start_time: MillisecondDateTime = pydantic.Field(None, alias="TaskStartTime")
    bucket: String = pydantic.Field(None, alias="Bucket")
    s_3_object_key: String = pydantic.Field(None, alias="S3objectKey")
    progress_percentage: Integer = pydantic.Field(None, alias="ProgressPercentage")
    store_task_state: String = pydantic.Field(None, alias="StoreTaskState")
    store_task_failure_reason: String = pydantic.Field(None, alias="StoreTaskFailureReason")

class Subnet(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    availability_zone_id: String = pydantic.Field(None, alias="AvailabilityZoneId")
    available_ip_address_count: Integer = pydantic.Field(None, alias="AvailableIpAddressCount")
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    default_for_az: Boolean = pydantic.Field(None, alias="DefaultForAz")
    enable_lni_at_device_index: Integer = pydantic.Field(None, alias="EnableLniAtDeviceIndex")
    map_public_ip_on_launch: Boolean = pydantic.Field(None, alias="MapPublicIpOnLaunch")
    map_customer_owned_ip_on_launch: Boolean = pydantic.Field(None, alias="MapCustomerOwnedIpOnLaunch")
    customer_owned_ipv_4_pool: CoipPoolId = pydantic.Field(None, alias="CustomerOwnedIpv4Pool")
    state: SubnetState = pydantic.Field(None, alias="State")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    assign_ipv_6_address_on_creation: Boolean = pydantic.Field(None, alias="AssignIpv6AddressOnCreation")
    ipv_6_cidr_block_association_set: SubnetIpv6CidrBlockAssociationSet = pydantic.Field(None, alias="Ipv6CidrBlockAssociationSet")
    tags: TagList = pydantic.Field(None, alias="Tags")
    subnet_arn: String = pydantic.Field(None, alias="SubnetArn")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    enable_dns_64: Boolean = pydantic.Field(None, alias="EnableDns64")
    ipv_6_native: Boolean = pydantic.Field(None, alias="Ipv6Native")
    private_dns_name_options_on_launch: 'PrivateDnsNameOptionsOnLaunch' = pydantic.Field(None, alias="PrivateDnsNameOptionsOnLaunch")

class SubnetAssociation(_EC2ModelBase):
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    state: TransitGatewayMulitcastDomainAssociationState = pydantic.Field(None, alias="State")

class SubnetCidrBlockState(_EC2ModelBase):
    state: SubnetCidrBlockStateCode = pydantic.Field(None, alias="State")
    status_message: String = pydantic.Field(None, alias="StatusMessage")

class SubnetCidrReservation(_EC2ModelBase):
    subnet_cidr_reservation_id: SubnetCidrReservationId = pydantic.Field(None, alias="SubnetCidrReservationId")
    subnet_id: SubnetId = pydantic.Field(None, alias="SubnetId")
    cidr: String = pydantic.Field(None, alias="Cidr")
    reservation_type: SubnetCidrReservationType = pydantic.Field(None, alias="ReservationType")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")

class SubnetIpv6CidrBlockAssociation(_EC2ModelBase):
    association_id: SubnetCidrAssociationId = pydantic.Field(None, alias="AssociationId")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    ipv_6_cidr_block_state: 'SubnetCidrBlockState' = pydantic.Field(None, alias="Ipv6CidrBlockState")

class Subscription(_EC2ModelBase):
    source: String = pydantic.Field(None, alias="Source")
    destination: String = pydantic.Field(None, alias="Destination")
    metric: MetricType = pydantic.Field(None, alias="Metric")
    statistic: StatisticType = pydantic.Field(None, alias="Statistic")
    period: PeriodType = pydantic.Field(None, alias="Period")

class SuccessfulInstanceCreditSpecificationItem(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")

class SuccessfulQueuedPurchaseDeletion(_EC2ModelBase):
    reserved_instances_id: String = pydantic.Field(None, alias="ReservedInstancesId")

class Tag(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    value: String = pydantic.Field(None, alias="Value")

class TagDescription(_EC2ModelBase):
    key: String = pydantic.Field(None, alias="Key")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    value: String = pydantic.Field(None, alias="Value")

class TagSpecification(_EC2ModelBase):
    resource_type: ResourceType = pydantic.Field(None, alias="ResourceType")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TargetCapacitySpecification(_EC2ModelBase):
    total_target_capacity: Integer = pydantic.Field(None, alias="TotalTargetCapacity")
    on_demand_target_capacity: Integer = pydantic.Field(None, alias="OnDemandTargetCapacity")
    spot_target_capacity: Integer = pydantic.Field(None, alias="SpotTargetCapacity")
    default_target_capacity_type: DefaultTargetCapacityType = pydantic.Field(None, alias="DefaultTargetCapacityType")
    target_capacity_unit_type: TargetCapacityUnitType = pydantic.Field(None, alias="TargetCapacityUnitType")

class TargetCapacitySpecificationRequest(_EC2ModelBase):
    total_target_capacity: Integer = pydantic.Field(None, alias="TotalTargetCapacity")
    on_demand_target_capacity: Integer = pydantic.Field(None, alias="OnDemandTargetCapacity")
    spot_target_capacity: Integer = pydantic.Field(None, alias="SpotTargetCapacity")
    default_target_capacity_type: DefaultTargetCapacityType = pydantic.Field(None, alias="DefaultTargetCapacityType")
    target_capacity_unit_type: TargetCapacityUnitType = pydantic.Field(None, alias="TargetCapacityUnitType")

class TargetConfiguration(_EC2ModelBase):
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    offering_id: String = pydantic.Field(None, alias="OfferingId")

class TargetConfigurationRequest(_EC2ModelBase):
    instance_count: Integer = pydantic.Field(None, alias="InstanceCount")
    offering_id: ReservedInstancesOfferingId = pydantic.Field(None, alias="OfferingId")

class TargetGroup(_EC2ModelBase):
    arn: String = pydantic.Field(None, alias="Arn")

class TargetGroupsConfig(_EC2ModelBase):
    target_groups: TargetGroups = pydantic.Field(None, alias="TargetGroups")

class TargetNetwork(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    target_network_id: String = pydantic.Field(None, alias="TargetNetworkId")
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    status: 'AssociationStatus' = pydantic.Field(None, alias="Status")
    security_groups: ValueStringList = pydantic.Field(None, alias="SecurityGroups")

class TargetReservationValue(_EC2ModelBase):
    reservation_value: 'ReservationValue' = pydantic.Field(None, alias="ReservationValue")
    target_configuration: 'TargetConfiguration' = pydantic.Field(None, alias="TargetConfiguration")

class TerminateClientVpnConnectionsRequest(_EC2ModelBase):
    client_vpn_endpoint_id: ClientVpnEndpointId = pydantic.Field(None, alias="ClientVpnEndpointId")
    connection_id: VpnConnectionId = pydantic.Field(None, alias="ConnectionId")
    username: String = pydantic.Field(None, alias="Username")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class TerminateClientVpnConnectionsResult(_EC2ModelBase):
    client_vpn_endpoint_id: String = pydantic.Field(None, alias="ClientVpnEndpointId")
    username: String = pydantic.Field(None, alias="Username")
    connection_statuses: TerminateConnectionStatusSet = pydantic.Field(None, alias="ConnectionStatuses")

class TerminateConnectionStatus(_EC2ModelBase):
    connection_id: String = pydantic.Field(None, alias="ConnectionId")
    previous_status: 'ClientVpnConnectionStatus' = pydantic.Field(None, alias="PreviousStatus")
    current_status: 'ClientVpnConnectionStatus' = pydantic.Field(None, alias="CurrentStatus")

class TerminateInstancesRequest(_EC2ModelBase):
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class TerminateInstancesResult(_EC2ModelBase):
    terminating_instances: InstanceStateChangeList = pydantic.Field(None, alias="TerminatingInstances")

class ThroughResourcesStatement(_EC2ModelBase):
    resource_statement: 'ResourceStatement' = pydantic.Field(None, alias="ResourceStatement")

class ThroughResourcesStatementRequest(_EC2ModelBase):
    resource_statement: 'ResourceStatementRequest' = pydantic.Field(None, alias="ResourceStatement")

class TotalLocalStorageGB(_EC2ModelBase):
    min: Double = pydantic.Field(None, alias="Min")
    max: Double = pydantic.Field(None, alias="Max")

class TotalLocalStorageGBRequest(_EC2ModelBase):
    min: Double = pydantic.Field(None, alias="Min")
    max: Double = pydantic.Field(None, alias="Max")

class TrafficMirrorFilter(_EC2ModelBase):
    traffic_mirror_filter_id: String = pydantic.Field(None, alias="TrafficMirrorFilterId")
    ingress_filter_rules: TrafficMirrorFilterRuleList = pydantic.Field(None, alias="IngressFilterRules")
    egress_filter_rules: TrafficMirrorFilterRuleList = pydantic.Field(None, alias="EgressFilterRules")
    network_services: TrafficMirrorNetworkServiceList = pydantic.Field(None, alias="NetworkServices")
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TrafficMirrorFilterRule(_EC2ModelBase):
    traffic_mirror_filter_rule_id: String = pydantic.Field(None, alias="TrafficMirrorFilterRuleId")
    traffic_mirror_filter_id: String = pydantic.Field(None, alias="TrafficMirrorFilterId")
    traffic_direction: TrafficDirection = pydantic.Field(None, alias="TrafficDirection")
    rule_number: Integer = pydantic.Field(None, alias="RuleNumber")
    rule_action: TrafficMirrorRuleAction = pydantic.Field(None, alias="RuleAction")
    protocol: Integer = pydantic.Field(None, alias="Protocol")
    destination_port_range: 'TrafficMirrorPortRange' = pydantic.Field(None, alias="DestinationPortRange")
    source_port_range: 'TrafficMirrorPortRange' = pydantic.Field(None, alias="SourcePortRange")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    source_cidr_block: String = pydantic.Field(None, alias="SourceCidrBlock")
    description: String = pydantic.Field(None, alias="Description")

class TrafficMirrorPortRange(_EC2ModelBase):
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    to_port: Integer = pydantic.Field(None, alias="ToPort")

class TrafficMirrorPortRangeRequest(_EC2ModelBase):
    from_port: Integer = pydantic.Field(None, alias="FromPort")
    to_port: Integer = pydantic.Field(None, alias="ToPort")

class TrafficMirrorSession(_EC2ModelBase):
    traffic_mirror_session_id: String = pydantic.Field(None, alias="TrafficMirrorSessionId")
    traffic_mirror_target_id: String = pydantic.Field(None, alias="TrafficMirrorTargetId")
    traffic_mirror_filter_id: String = pydantic.Field(None, alias="TrafficMirrorFilterId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    packet_length: Integer = pydantic.Field(None, alias="PacketLength")
    session_number: Integer = pydantic.Field(None, alias="SessionNumber")
    virtual_network_id: Integer = pydantic.Field(None, alias="VirtualNetworkId")
    description: String = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TrafficMirrorTarget(_EC2ModelBase):
    traffic_mirror_target_id: String = pydantic.Field(None, alias="TrafficMirrorTargetId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    network_load_balancer_arn: String = pydantic.Field(None, alias="NetworkLoadBalancerArn")
    type: TrafficMirrorTargetType = pydantic.Field(None, alias="Type")
    description: String = pydantic.Field(None, alias="Description")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    tags: TagList = pydantic.Field(None, alias="Tags")
    gateway_load_balancer_endpoint_id: String = pydantic.Field(None, alias="GatewayLoadBalancerEndpointId")

class TransitGateway(_EC2ModelBase):
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    transit_gateway_arn: String = pydantic.Field(None, alias="TransitGatewayArn")
    state: TransitGatewayState = pydantic.Field(None, alias="State")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    description: String = pydantic.Field(None, alias="Description")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    options: 'TransitGatewayOptions' = pydantic.Field(None, alias="Options")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayAssociation(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    state: TransitGatewayAssociationState = pydantic.Field(None, alias="State")

class TransitGatewayAttachment(_EC2ModelBase):
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    transit_gateway_owner_id: String = pydantic.Field(None, alias="TransitGatewayOwnerId")
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    state: TransitGatewayAttachmentState = pydantic.Field(None, alias="State")
    association: 'TransitGatewayAttachmentAssociation' = pydantic.Field(None, alias="Association")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayAttachmentAssociation(_EC2ModelBase):
    transit_gateway_route_table_id: String = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    state: TransitGatewayAssociationState = pydantic.Field(None, alias="State")

class TransitGatewayAttachmentBgpConfiguration(_EC2ModelBase):
    transit_gateway_asn: Long = pydantic.Field(None, alias="TransitGatewayAsn")
    peer_asn: Long = pydantic.Field(None, alias="PeerAsn")
    transit_gateway_address: String = pydantic.Field(None, alias="TransitGatewayAddress")
    peer_address: String = pydantic.Field(None, alias="PeerAddress")
    bgp_status: BgpStatus = pydantic.Field(None, alias="BgpStatus")

class TransitGatewayAttachmentPropagation(_EC2ModelBase):
    transit_gateway_route_table_id: String = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    state: TransitGatewayPropagationState = pydantic.Field(None, alias="State")

class TransitGatewayConnect(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    transport_transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransportTransitGatewayAttachmentId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    state: TransitGatewayAttachmentState = pydantic.Field(None, alias="State")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    options: 'TransitGatewayConnectOptions' = pydantic.Field(None, alias="Options")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayConnectOptions(_EC2ModelBase):
    protocol: ProtocolValue = pydantic.Field(None, alias="Protocol")

class TransitGatewayConnectPeer(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    transit_gateway_connect_peer_id: TransitGatewayConnectPeerId = pydantic.Field(None, alias="TransitGatewayConnectPeerId")
    state: TransitGatewayConnectPeerState = pydantic.Field(None, alias="State")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    connect_peer_configuration: 'TransitGatewayConnectPeerConfiguration' = pydantic.Field(None, alias="ConnectPeerConfiguration")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayConnectPeerConfiguration(_EC2ModelBase):
    transit_gateway_address: String = pydantic.Field(None, alias="TransitGatewayAddress")
    peer_address: String = pydantic.Field(None, alias="PeerAddress")
    inside_cidr_blocks: InsideCidrBlocksStringList = pydantic.Field(None, alias="InsideCidrBlocks")
    protocol: ProtocolValue = pydantic.Field(None, alias="Protocol")
    bgp_configurations: TransitGatewayAttachmentBgpConfigurationList = pydantic.Field(None, alias="BgpConfigurations")

class TransitGatewayConnectRequestBgpOptions(_EC2ModelBase):
    peer_asn: Long = pydantic.Field(None, alias="PeerAsn")

class TransitGatewayMulticastDeregisteredGroupMembers(_EC2ModelBase):
    transit_gateway_multicast_domain_id: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    deregistered_network_interface_ids: ValueStringList = pydantic.Field(None, alias="DeregisteredNetworkInterfaceIds")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")

class TransitGatewayMulticastDeregisteredGroupSources(_EC2ModelBase):
    transit_gateway_multicast_domain_id: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    deregistered_network_interface_ids: ValueStringList = pydantic.Field(None, alias="DeregisteredNetworkInterfaceIds")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")

class TransitGatewayMulticastDomain(_EC2ModelBase):
    transit_gateway_multicast_domain_id: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    transit_gateway_multicast_domain_arn: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainArn")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    options: 'TransitGatewayMulticastDomainOptions' = pydantic.Field(None, alias="Options")
    state: TransitGatewayMulticastDomainState = pydantic.Field(None, alias="State")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayMulticastDomainAssociation(_EC2ModelBase):
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    subnet: 'SubnetAssociation' = pydantic.Field(None, alias="Subnet")

class TransitGatewayMulticastDomainAssociations(_EC2ModelBase):
    transit_gateway_multicast_domain_id: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    subnets: SubnetAssociationList = pydantic.Field(None, alias="Subnets")

class TransitGatewayMulticastDomainOptions(_EC2ModelBase):
    igmpv_2_support: Igmpv2SupportValue = pydantic.Field(None, alias="Igmpv2Support")
    static_sources_support: StaticSourcesSupportValue = pydantic.Field(None, alias="StaticSourcesSupport")
    auto_accept_shared_associations: AutoAcceptSharedAssociationsValue = pydantic.Field(None, alias="AutoAcceptSharedAssociations")

class TransitGatewayMulticastGroup(_EC2ModelBase):
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    subnet_id: String = pydantic.Field(None, alias="SubnetId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    resource_owner_id: String = pydantic.Field(None, alias="ResourceOwnerId")
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    group_member: Boolean = pydantic.Field(None, alias="GroupMember")
    group_source: Boolean = pydantic.Field(None, alias="GroupSource")
    member_type: MembershipType = pydantic.Field(None, alias="MemberType")
    source_type: MembershipType = pydantic.Field(None, alias="SourceType")

class TransitGatewayMulticastRegisteredGroupMembers(_EC2ModelBase):
    transit_gateway_multicast_domain_id: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    registered_network_interface_ids: ValueStringList = pydantic.Field(None, alias="RegisteredNetworkInterfaceIds")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")

class TransitGatewayMulticastRegisteredGroupSources(_EC2ModelBase):
    transit_gateway_multicast_domain_id: String = pydantic.Field(None, alias="TransitGatewayMulticastDomainId")
    registered_network_interface_ids: ValueStringList = pydantic.Field(None, alias="RegisteredNetworkInterfaceIds")
    group_ip_address: String = pydantic.Field(None, alias="GroupIpAddress")

class TransitGatewayOptions(_EC2ModelBase):
    amazon_side_asn: Long = pydantic.Field(None, alias="AmazonSideAsn")
    transit_gateway_cidr_blocks: ValueStringList = pydantic.Field(None, alias="TransitGatewayCidrBlocks")
    auto_accept_shared_attachments: AutoAcceptSharedAttachmentsValue = pydantic.Field(None, alias="AutoAcceptSharedAttachments")
    default_route_table_association: DefaultRouteTableAssociationValue = pydantic.Field(None, alias="DefaultRouteTableAssociation")
    association_default_route_table_id: String = pydantic.Field(None, alias="AssociationDefaultRouteTableId")
    default_route_table_propagation: DefaultRouteTablePropagationValue = pydantic.Field(None, alias="DefaultRouteTablePropagation")
    propagation_default_route_table_id: String = pydantic.Field(None, alias="PropagationDefaultRouteTableId")
    vpn_ecmp_support: VpnEcmpSupportValue = pydantic.Field(None, alias="VpnEcmpSupport")
    dns_support: DnsSupportValue = pydantic.Field(None, alias="DnsSupport")
    multicast_support: MulticastSupportValue = pydantic.Field(None, alias="MulticastSupport")

class TransitGatewayPeeringAttachment(_EC2ModelBase):
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    accepter_transit_gateway_attachment_id: String = pydantic.Field(None, alias="AccepterTransitGatewayAttachmentId")
    requester_tgw_info: 'PeeringTgwInfo' = pydantic.Field(None, alias="RequesterTgwInfo")
    accepter_tgw_info: 'PeeringTgwInfo' = pydantic.Field(None, alias="AccepterTgwInfo")
    options: 'TransitGatewayPeeringAttachmentOptions' = pydantic.Field(None, alias="Options")
    status: 'PeeringAttachmentStatus' = pydantic.Field(None, alias="Status")
    state: TransitGatewayAttachmentState = pydantic.Field(None, alias="State")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayPeeringAttachmentOptions(_EC2ModelBase):
    dynamic_routing: DynamicRoutingValue = pydantic.Field(None, alias="DynamicRouting")

class TransitGatewayPolicyRule(_EC2ModelBase):
    source_cidr_block: String = pydantic.Field(None, alias="SourceCidrBlock")
    source_port_range: String = pydantic.Field(None, alias="SourcePortRange")
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    destination_port_range: String = pydantic.Field(None, alias="DestinationPortRange")
    protocol: String = pydantic.Field(None, alias="Protocol")
    meta_data: 'TransitGatewayPolicyRuleMetaData' = pydantic.Field(None, alias="MetaData")

class TransitGatewayPolicyRuleMetaData(_EC2ModelBase):
    meta_data_key: String = pydantic.Field(None, alias="MetaDataKey")
    meta_data_value: String = pydantic.Field(None, alias="MetaDataValue")

class TransitGatewayPolicyTable(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    state: TransitGatewayPolicyTableState = pydantic.Field(None, alias="State")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayPolicyTableAssociation(_EC2ModelBase):
    transit_gateway_policy_table_id: TransitGatewayPolicyTableId = pydantic.Field(None, alias="TransitGatewayPolicyTableId")
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    state: TransitGatewayAssociationState = pydantic.Field(None, alias="State")

class TransitGatewayPolicyTableEntry(_EC2ModelBase):
    policy_rule_number: String = pydantic.Field(None, alias="PolicyRuleNumber")
    policy_rule: 'TransitGatewayPolicyRule' = pydantic.Field(None, alias="PolicyRule")
    target_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TargetRouteTableId")

class TransitGatewayPrefixListAttachment(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    resource_id: String = pydantic.Field(None, alias="ResourceId")

class TransitGatewayPrefixListReference(_EC2ModelBase):
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    prefix_list_owner_id: String = pydantic.Field(None, alias="PrefixListOwnerId")
    state: TransitGatewayPrefixListReferenceState = pydantic.Field(None, alias="State")
    blackhole: Boolean = pydantic.Field(None, alias="Blackhole")
    transit_gateway_attachment: 'TransitGatewayPrefixListAttachment' = pydantic.Field(None, alias="TransitGatewayAttachment")

class TransitGatewayPropagation(_EC2ModelBase):
    transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    transit_gateway_route_table_id: String = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    state: TransitGatewayPropagationState = pydantic.Field(None, alias="State")
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")

class TransitGatewayRequestOptions(_EC2ModelBase):
    amazon_side_asn: Long = pydantic.Field(None, alias="AmazonSideAsn")
    auto_accept_shared_attachments: AutoAcceptSharedAttachmentsValue = pydantic.Field(None, alias="AutoAcceptSharedAttachments")
    default_route_table_association: DefaultRouteTableAssociationValue = pydantic.Field(None, alias="DefaultRouteTableAssociation")
    default_route_table_propagation: DefaultRouteTablePropagationValue = pydantic.Field(None, alias="DefaultRouteTablePropagation")
    vpn_ecmp_support: VpnEcmpSupportValue = pydantic.Field(None, alias="VpnEcmpSupport")
    dns_support: DnsSupportValue = pydantic.Field(None, alias="DnsSupport")
    multicast_support: MulticastSupportValue = pydantic.Field(None, alias="MulticastSupport")
    transit_gateway_cidr_blocks: TransitGatewayCidrBlockStringList = pydantic.Field(None, alias="TransitGatewayCidrBlocks")

class TransitGatewayRoute(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    prefix_list_id: PrefixListResourceId = pydantic.Field(None, alias="PrefixListId")
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")
    transit_gateway_attachments: TransitGatewayRouteAttachmentList = pydantic.Field(None, alias="TransitGatewayAttachments")
    type: TransitGatewayRouteType = pydantic.Field(None, alias="Type")
    state: TransitGatewayRouteState = pydantic.Field(None, alias="State")

class TransitGatewayRouteAttachment(_EC2ModelBase):
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")

class TransitGatewayRouteTable(_EC2ModelBase):
    transit_gateway_route_table_id: String = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    state: TransitGatewayRouteTableState = pydantic.Field(None, alias="State")
    default_association_route_table: Boolean = pydantic.Field(None, alias="DefaultAssociationRouteTable")
    default_propagation_route_table: Boolean = pydantic.Field(None, alias="DefaultPropagationRouteTable")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayRouteTableAnnouncement(_EC2ModelBase):
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")
    transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="TransitGatewayId")
    core_network_id: String = pydantic.Field(None, alias="CoreNetworkId")
    peer_transit_gateway_id: TransitGatewayId = pydantic.Field(None, alias="PeerTransitGatewayId")
    peer_core_network_id: String = pydantic.Field(None, alias="PeerCoreNetworkId")
    peering_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="PeeringAttachmentId")
    announcement_direction: TransitGatewayRouteTableAnnouncementDirection = pydantic.Field(None, alias="AnnouncementDirection")
    transit_gateway_route_table_id: TransitGatewayRouteTableId = pydantic.Field(None, alias="TransitGatewayRouteTableId")
    state: TransitGatewayRouteTableAnnouncementState = pydantic.Field(None, alias="State")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayRouteTableAssociation(_EC2ModelBase):
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    state: TransitGatewayAssociationState = pydantic.Field(None, alias="State")

class TransitGatewayRouteTablePropagation(_EC2ModelBase):
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: TransitGatewayAttachmentResourceType = pydantic.Field(None, alias="ResourceType")
    state: TransitGatewayPropagationState = pydantic.Field(None, alias="State")
    transit_gateway_route_table_announcement_id: TransitGatewayRouteTableAnnouncementId = pydantic.Field(None, alias="TransitGatewayRouteTableAnnouncementId")

class TransitGatewayRouteTableRoute(_EC2ModelBase):
    destination_cidr: String = pydantic.Field(None, alias="DestinationCidr")
    state: String = pydantic.Field(None, alias="State")
    route_origin: String = pydantic.Field(None, alias="RouteOrigin")
    prefix_list_id: String = pydantic.Field(None, alias="PrefixListId")
    attachment_id: String = pydantic.Field(None, alias="AttachmentId")
    resource_id: String = pydantic.Field(None, alias="ResourceId")
    resource_type: String = pydantic.Field(None, alias="ResourceType")

class TransitGatewayVpcAttachment(_EC2ModelBase):
    transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransitGatewayAttachmentId")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    vpc_owner_id: String = pydantic.Field(None, alias="VpcOwnerId")
    state: TransitGatewayAttachmentState = pydantic.Field(None, alias="State")
    subnet_ids: ValueStringList = pydantic.Field(None, alias="SubnetIds")
    creation_time: DateTime = pydantic.Field(None, alias="CreationTime")
    options: 'TransitGatewayVpcAttachmentOptions' = pydantic.Field(None, alias="Options")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TransitGatewayVpcAttachmentOptions(_EC2ModelBase):
    dns_support: DnsSupportValue = pydantic.Field(None, alias="DnsSupport")
    ipv_6_support: Ipv6SupportValue = pydantic.Field(None, alias="Ipv6Support")
    appliance_mode_support: ApplianceModeSupportValue = pydantic.Field(None, alias="ApplianceModeSupport")

class TrunkInterfaceAssociation(_EC2ModelBase):
    association_id: TrunkInterfaceAssociationId = pydantic.Field(None, alias="AssociationId")
    branch_interface_id: String = pydantic.Field(None, alias="BranchInterfaceId")
    trunk_interface_id: String = pydantic.Field(None, alias="TrunkInterfaceId")
    interface_protocol: InterfaceProtocolType = pydantic.Field(None, alias="InterfaceProtocol")
    vlan_id: Integer = pydantic.Field(None, alias="VlanId")
    gre_key: Integer = pydantic.Field(None, alias="GreKey")
    tags: TagList = pydantic.Field(None, alias="Tags")

class TunnelOption(_EC2ModelBase):
    outside_ip_address: String = pydantic.Field(None, alias="OutsideIpAddress")
    tunnel_inside_cidr: String = pydantic.Field(None, alias="TunnelInsideCidr")
    tunnel_inside_ipv_6_cidr: String = pydantic.Field(None, alias="TunnelInsideIpv6Cidr")
    pre_shared_key: String = pydantic.Field(None, alias="PreSharedKey")
    phase_1_lifetime_seconds: Integer = pydantic.Field(None, alias="Phase1LifetimeSeconds")
    phase_2_lifetime_seconds: Integer = pydantic.Field(None, alias="Phase2LifetimeSeconds")
    rekey_margin_time_seconds: Integer = pydantic.Field(None, alias="RekeyMarginTimeSeconds")
    rekey_fuzz_percentage: Integer = pydantic.Field(None, alias="RekeyFuzzPercentage")
    replay_window_size: Integer = pydantic.Field(None, alias="ReplayWindowSize")
    dpd_timeout_seconds: Integer = pydantic.Field(None, alias="DpdTimeoutSeconds")
    dpd_timeout_action: String = pydantic.Field(None, alias="DpdTimeoutAction")
    phase_1_encryption_algorithms: Phase1EncryptionAlgorithmsList = pydantic.Field(None, alias="Phase1EncryptionAlgorithms")
    phase_2_encryption_algorithms: Phase2EncryptionAlgorithmsList = pydantic.Field(None, alias="Phase2EncryptionAlgorithms")
    phase_1_integrity_algorithms: Phase1IntegrityAlgorithmsList = pydantic.Field(None, alias="Phase1IntegrityAlgorithms")
    phase_2_integrity_algorithms: Phase2IntegrityAlgorithmsList = pydantic.Field(None, alias="Phase2IntegrityAlgorithms")
    phase_1_dh_group_numbers: Phase1DHGroupNumbersList = pydantic.Field(None, alias="Phase1DHGroupNumbers")
    phase_2_dh_group_numbers: Phase2DHGroupNumbersList = pydantic.Field(None, alias="Phase2DHGroupNumbers")
    ike_versions: IKEVersionsList = pydantic.Field(None, alias="IkeVersions")
    startup_action: String = pydantic.Field(None, alias="StartupAction")
    log_options: 'VpnTunnelLogOptions' = pydantic.Field(None, alias="LogOptions")
    enable_tunnel_lifecycle_control: Boolean = pydantic.Field(None, alias="EnableTunnelLifecycleControl")

class UnassignIpv6AddressesRequest(_EC2ModelBase):
    ipv_6_addresses: Ipv6AddressList = pydantic.Field(None, alias="Ipv6Addresses")
    ipv_6_prefixes: IpPrefixList = pydantic.Field(None, alias="Ipv6Prefixes")
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")

class UnassignIpv6AddressesResult(_EC2ModelBase):
    network_interface_id: String = pydantic.Field(None, alias="NetworkInterfaceId")
    unassigned_ipv_6_addresses: Ipv6AddressList = pydantic.Field(None, alias="UnassignedIpv6Addresses")
    unassigned_ipv_6_prefixes: IpPrefixList = pydantic.Field(None, alias="UnassignedIpv6Prefixes")

class UnassignPrivateIpAddressesRequest(_EC2ModelBase):
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    private_ip_addresses: PrivateIpAddressStringList = pydantic.Field(None, alias="PrivateIpAddresses")
    ipv_4_prefixes: IpPrefixList = pydantic.Field(None, alias="Ipv4Prefixes")

class UnassignPrivateNatGatewayAddressRequest(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    private_ip_addresses: IpList = pydantic.Field(None, alias="PrivateIpAddresses")
    max_drain_duration_seconds: DrainSeconds = pydantic.Field(None, alias="MaxDrainDurationSeconds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class UnassignPrivateNatGatewayAddressResult(_EC2ModelBase):
    nat_gateway_id: NatGatewayId = pydantic.Field(None, alias="NatGatewayId")
    nat_gateway_addresses: NatGatewayAddressList = pydantic.Field(None, alias="NatGatewayAddresses")

class UnmonitorInstancesRequest(_EC2ModelBase):
    instance_ids: InstanceIdStringList = pydantic.Field(None, alias="InstanceIds")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class UnmonitorInstancesResult(_EC2ModelBase):
    instance_monitorings: InstanceMonitoringList = pydantic.Field(None, alias="InstanceMonitorings")

class UnsuccessfulInstanceCreditSpecificationItem(_EC2ModelBase):
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    error: 'UnsuccessfulInstanceCreditSpecificationItemError' = pydantic.Field(None, alias="Error")

class UnsuccessfulInstanceCreditSpecificationItemError(_EC2ModelBase):
    code: UnsuccessfulInstanceCreditSpecificationErrorCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class UnsuccessfulItem(_EC2ModelBase):
    error: 'UnsuccessfulItemError' = pydantic.Field(None, alias="Error")
    resource_id: String = pydantic.Field(None, alias="ResourceId")

class UnsuccessfulItemError(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class UpdateSecurityGroupRuleDescriptionsEgressRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    group_name: SecurityGroupName = pydantic.Field(None, alias="GroupName")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    security_group_rule_descriptions: SecurityGroupRuleDescriptionList = pydantic.Field(None, alias="SecurityGroupRuleDescriptions")

class UpdateSecurityGroupRuleDescriptionsEgressResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class UpdateSecurityGroupRuleDescriptionsIngressRequest(_EC2ModelBase):
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")
    group_id: SecurityGroupId = pydantic.Field(None, alias="GroupId")
    group_name: SecurityGroupName = pydantic.Field(None, alias="GroupName")
    ip_permissions: IpPermissionList = pydantic.Field(None, alias="IpPermissions")
    security_group_rule_descriptions: SecurityGroupRuleDescriptionList = pydantic.Field(None, alias="SecurityGroupRuleDescriptions")

class UpdateSecurityGroupRuleDescriptionsIngressResult(_EC2ModelBase):
    Return_: Boolean = pydantic.Field(None, alias="Return")

class UserBucket(_EC2ModelBase):
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_key: String = pydantic.Field(None, alias="S3Key")

class UserBucketDetails(_EC2ModelBase):
    s_3_bucket: String = pydantic.Field(None, alias="S3Bucket")
    s_3_key: String = pydantic.Field(None, alias="S3Key")

class UserData(_EC2ModelBase):
    data: String = pydantic.Field(None, alias="Data")

class UserIdGroupPair(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    group_id: String = pydantic.Field(None, alias="GroupId")
    group_name: String = pydantic.Field(None, alias="GroupName")
    peering_status: String = pydantic.Field(None, alias="PeeringStatus")
    user_id: String = pydantic.Field(None, alias="UserId")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    vpc_peering_connection_id: String = pydantic.Field(None, alias="VpcPeeringConnectionId")

class VCpuCountRange(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class VCpuCountRangeRequest(_EC2ModelBase):
    min: Integer = pydantic.Field(None, alias="Min")
    max: Integer = pydantic.Field(None, alias="Max")

class VCpuInfo(_EC2ModelBase):
    default_v_cpus: VCpuCount = pydantic.Field(None, alias="DefaultVCpus")
    default_cores: CoreCount = pydantic.Field(None, alias="DefaultCores")
    default_threads_per_core: ThreadsPerCore = pydantic.Field(None, alias="DefaultThreadsPerCore")
    valid_cores: CoreCountList = pydantic.Field(None, alias="ValidCores")
    valid_threads_per_core: ThreadsPerCoreList = pydantic.Field(None, alias="ValidThreadsPerCore")

class ValidationError(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class ValidationWarning(_EC2ModelBase):
    errors: ErrorSet = pydantic.Field(None, alias="Errors")

class VerifiedAccessEndpoint(_EC2ModelBase):
    verified_access_instance_id: String = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    verified_access_group_id: String = pydantic.Field(None, alias="VerifiedAccessGroupId")
    verified_access_endpoint_id: String = pydantic.Field(None, alias="VerifiedAccessEndpointId")
    application_domain: String = pydantic.Field(None, alias="ApplicationDomain")
    endpoint_type: VerifiedAccessEndpointType = pydantic.Field(None, alias="EndpointType")
    attachment_type: VerifiedAccessEndpointAttachmentType = pydantic.Field(None, alias="AttachmentType")
    domain_certificate_arn: String = pydantic.Field(None, alias="DomainCertificateArn")
    endpoint_domain: String = pydantic.Field(None, alias="EndpointDomain")
    device_validation_domain: String = pydantic.Field(None, alias="DeviceValidationDomain")
    security_group_ids: SecurityGroupIdList = pydantic.Field(None, alias="SecurityGroupIds")
    load_balancer_options: 'VerifiedAccessEndpointLoadBalancerOptions' = pydantic.Field(None, alias="LoadBalancerOptions")
    network_interface_options: 'VerifiedAccessEndpointEniOptions' = pydantic.Field(None, alias="NetworkInterfaceOptions")
    status: 'VerifiedAccessEndpointStatus' = pydantic.Field(None, alias="Status")
    description: String = pydantic.Field(None, alias="Description")
    creation_time: String = pydantic.Field(None, alias="CreationTime")
    last_updated_time: String = pydantic.Field(None, alias="LastUpdatedTime")
    deletion_time: String = pydantic.Field(None, alias="DeletionTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VerifiedAccessEndpointEniOptions(_EC2ModelBase):
    network_interface_id: NetworkInterfaceId = pydantic.Field(None, alias="NetworkInterfaceId")
    protocol: VerifiedAccessEndpointProtocol = pydantic.Field(None, alias="Protocol")
    port: VerifiedAccessEndpointPortNumber = pydantic.Field(None, alias="Port")

class VerifiedAccessEndpointLoadBalancerOptions(_EC2ModelBase):
    protocol: VerifiedAccessEndpointProtocol = pydantic.Field(None, alias="Protocol")
    port: VerifiedAccessEndpointPortNumber = pydantic.Field(None, alias="Port")
    load_balancer_arn: String = pydantic.Field(None, alias="LoadBalancerArn")
    subnet_ids: VerifiedAccessEndpointSubnetIdList = pydantic.Field(None, alias="SubnetIds")

class VerifiedAccessEndpointStatus(_EC2ModelBase):
    code: VerifiedAccessEndpointStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class VerifiedAccessGroup(_EC2ModelBase):
    verified_access_group_id: String = pydantic.Field(None, alias="VerifiedAccessGroupId")
    verified_access_instance_id: String = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    description: String = pydantic.Field(None, alias="Description")
    owner: String = pydantic.Field(None, alias="Owner")
    verified_access_group_arn: String = pydantic.Field(None, alias="VerifiedAccessGroupArn")
    creation_time: String = pydantic.Field(None, alias="CreationTime")
    last_updated_time: String = pydantic.Field(None, alias="LastUpdatedTime")
    deletion_time: String = pydantic.Field(None, alias="DeletionTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VerifiedAccessInstance(_EC2ModelBase):
    verified_access_instance_id: String = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    description: String = pydantic.Field(None, alias="Description")
    verified_access_trust_providers: VerifiedAccessTrustProviderCondensedList = pydantic.Field(None, alias="VerifiedAccessTrustProviders")
    creation_time: String = pydantic.Field(None, alias="CreationTime")
    last_updated_time: String = pydantic.Field(None, alias="LastUpdatedTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VerifiedAccessInstanceLoggingConfiguration(_EC2ModelBase):
    verified_access_instance_id: String = pydantic.Field(None, alias="VerifiedAccessInstanceId")
    access_logs: 'VerifiedAccessLogs' = pydantic.Field(None, alias="AccessLogs")

class VerifiedAccessLogCloudWatchLogsDestination(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    delivery_status: 'VerifiedAccessLogDeliveryStatus' = pydantic.Field(None, alias="DeliveryStatus")
    log_group: String = pydantic.Field(None, alias="LogGroup")

class VerifiedAccessLogCloudWatchLogsDestinationOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    log_group: String = pydantic.Field(None, alias="LogGroup")

class VerifiedAccessLogDeliveryStatus(_EC2ModelBase):
    code: VerifiedAccessLogDeliveryStatusCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class VerifiedAccessLogKinesisDataFirehoseDestination(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    delivery_status: 'VerifiedAccessLogDeliveryStatus' = pydantic.Field(None, alias="DeliveryStatus")
    delivery_stream: String = pydantic.Field(None, alias="DeliveryStream")

class VerifiedAccessLogKinesisDataFirehoseDestinationOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    delivery_stream: String = pydantic.Field(None, alias="DeliveryStream")

class VerifiedAccessLogOptions(_EC2ModelBase):
    s_3: 'VerifiedAccessLogS3DestinationOptions' = pydantic.Field(None, alias="S3")
    cloud_watch_logs: 'VerifiedAccessLogCloudWatchLogsDestinationOptions' = pydantic.Field(None, alias="CloudWatchLogs")
    kinesis_data_firehose: 'VerifiedAccessLogKinesisDataFirehoseDestinationOptions' = pydantic.Field(None, alias="KinesisDataFirehose")

class VerifiedAccessLogS3Destination(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    delivery_status: 'VerifiedAccessLogDeliveryStatus' = pydantic.Field(None, alias="DeliveryStatus")
    bucket_name: String = pydantic.Field(None, alias="BucketName")
    prefix: String = pydantic.Field(None, alias="Prefix")
    bucket_owner: String = pydantic.Field(None, alias="BucketOwner")

class VerifiedAccessLogS3DestinationOptions(_EC2ModelBase):
    enabled: Boolean = pydantic.Field(None, alias="Enabled")
    bucket_name: String = pydantic.Field(None, alias="BucketName")
    prefix: String = pydantic.Field(None, alias="Prefix")
    bucket_owner: String = pydantic.Field(None, alias="BucketOwner")

class VerifiedAccessLogs(_EC2ModelBase):
    s_3: 'VerifiedAccessLogS3Destination' = pydantic.Field(None, alias="S3")
    cloud_watch_logs: 'VerifiedAccessLogCloudWatchLogsDestination' = pydantic.Field(None, alias="CloudWatchLogs")
    kinesis_data_firehose: 'VerifiedAccessLogKinesisDataFirehoseDestination' = pydantic.Field(None, alias="KinesisDataFirehose")

class VerifiedAccessTrustProvider(_EC2ModelBase):
    verified_access_trust_provider_id: String = pydantic.Field(None, alias="VerifiedAccessTrustProviderId")
    description: String = pydantic.Field(None, alias="Description")
    trust_provider_type: TrustProviderType = pydantic.Field(None, alias="TrustProviderType")
    user_trust_provider_type: UserTrustProviderType = pydantic.Field(None, alias="UserTrustProviderType")
    device_trust_provider_type: DeviceTrustProviderType = pydantic.Field(None, alias="DeviceTrustProviderType")
    oidc_options: 'OidcOptions' = pydantic.Field(None, alias="OidcOptions")
    device_options: 'DeviceOptions' = pydantic.Field(None, alias="DeviceOptions")
    policy_reference_name: String = pydantic.Field(None, alias="PolicyReferenceName")
    creation_time: String = pydantic.Field(None, alias="CreationTime")
    last_updated_time: String = pydantic.Field(None, alias="LastUpdatedTime")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VerifiedAccessTrustProviderCondensed(_EC2ModelBase):
    verified_access_trust_provider_id: String = pydantic.Field(None, alias="VerifiedAccessTrustProviderId")
    description: String = pydantic.Field(None, alias="Description")
    trust_provider_type: TrustProviderType = pydantic.Field(None, alias="TrustProviderType")
    user_trust_provider_type: UserTrustProviderType = pydantic.Field(None, alias="UserTrustProviderType")
    device_trust_provider_type: DeviceTrustProviderType = pydantic.Field(None, alias="DeviceTrustProviderType")

class VgwTelemetry(_EC2ModelBase):
    accepted_route_count: Integer = pydantic.Field(None, alias="AcceptedRouteCount")
    last_status_change: DateTime = pydantic.Field(None, alias="LastStatusChange")
    outside_ip_address: String = pydantic.Field(None, alias="OutsideIpAddress")
    status: TelemetryStatus = pydantic.Field(None, alias="Status")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    certificate_arn: String = pydantic.Field(None, alias="CertificateArn")

class Volume(_EC2ModelBase):
    attachments: VolumeAttachmentList = pydantic.Field(None, alias="Attachments")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    create_time: DateTime = pydantic.Field(None, alias="CreateTime")
    encrypted: Boolean = pydantic.Field(None, alias="Encrypted")
    kms_key_id: String = pydantic.Field(None, alias="KmsKeyId")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    size: Integer = pydantic.Field(None, alias="Size")
    snapshot_id: String = pydantic.Field(None, alias="SnapshotId")
    state: VolumeState = pydantic.Field(None, alias="State")
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    iops: Integer = pydantic.Field(None, alias="Iops")
    tags: TagList = pydantic.Field(None, alias="Tags")
    volume_type: VolumeType = pydantic.Field(None, alias="VolumeType")
    fast_restored: Boolean = pydantic.Field(None, alias="FastRestored")
    multi_attach_enabled: Boolean = pydantic.Field(None, alias="MultiAttachEnabled")
    throughput: Integer = pydantic.Field(None, alias="Throughput")

class VolumeAttachment(_EC2ModelBase):
    attach_time: DateTime = pydantic.Field(None, alias="AttachTime")
    device: String = pydantic.Field(None, alias="Device")
    instance_id: String = pydantic.Field(None, alias="InstanceId")
    state: VolumeAttachmentState = pydantic.Field(None, alias="State")
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    delete_on_termination: Boolean = pydantic.Field(None, alias="DeleteOnTermination")

class VolumeDetail(_EC2ModelBase):
    size: Long = pydantic.Field(None, alias="Size")

class VolumeModification(_EC2ModelBase):
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    modification_state: VolumeModificationState = pydantic.Field(None, alias="ModificationState")
    status_message: String = pydantic.Field(None, alias="StatusMessage")
    target_size: Integer = pydantic.Field(None, alias="TargetSize")
    target_iops: Integer = pydantic.Field(None, alias="TargetIops")
    target_volume_type: VolumeType = pydantic.Field(None, alias="TargetVolumeType")
    target_throughput: Integer = pydantic.Field(None, alias="TargetThroughput")
    target_multi_attach_enabled: Boolean = pydantic.Field(None, alias="TargetMultiAttachEnabled")
    original_size: Integer = pydantic.Field(None, alias="OriginalSize")
    original_iops: Integer = pydantic.Field(None, alias="OriginalIops")
    original_volume_type: VolumeType = pydantic.Field(None, alias="OriginalVolumeType")
    original_throughput: Integer = pydantic.Field(None, alias="OriginalThroughput")
    original_multi_attach_enabled: Boolean = pydantic.Field(None, alias="OriginalMultiAttachEnabled")
    progress: Long = pydantic.Field(None, alias="Progress")
    start_time: DateTime = pydantic.Field(None, alias="StartTime")
    end_time: DateTime = pydantic.Field(None, alias="EndTime")

class VolumeStatusAction(_EC2ModelBase):
    code: String = pydantic.Field(None, alias="Code")
    description: String = pydantic.Field(None, alias="Description")
    event_id: String = pydantic.Field(None, alias="EventId")
    event_type: String = pydantic.Field(None, alias="EventType")

class VolumeStatusAttachmentStatus(_EC2ModelBase):
    io_performance: String = pydantic.Field(None, alias="IoPerformance")
    instance_id: String = pydantic.Field(None, alias="InstanceId")

class VolumeStatusDetails(_EC2ModelBase):
    name: VolumeStatusName = pydantic.Field(None, alias="Name")
    status: String = pydantic.Field(None, alias="Status")

class VolumeStatusEvent(_EC2ModelBase):
    description: String = pydantic.Field(None, alias="Description")
    event_id: String = pydantic.Field(None, alias="EventId")
    event_type: String = pydantic.Field(None, alias="EventType")
    not_after: MillisecondDateTime = pydantic.Field(None, alias="NotAfter")
    not_before: MillisecondDateTime = pydantic.Field(None, alias="NotBefore")
    instance_id: String = pydantic.Field(None, alias="InstanceId")

class VolumeStatusInfo(_EC2ModelBase):
    details: VolumeStatusDetailsList = pydantic.Field(None, alias="Details")
    status: VolumeStatusInfoStatus = pydantic.Field(None, alias="Status")

class VolumeStatusItem(_EC2ModelBase):
    actions: VolumeStatusActionsList = pydantic.Field(None, alias="Actions")
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    outpost_arn: String = pydantic.Field(None, alias="OutpostArn")
    events: VolumeStatusEventsList = pydantic.Field(None, alias="Events")
    volume_id: String = pydantic.Field(None, alias="VolumeId")
    volume_status: 'VolumeStatusInfo' = pydantic.Field(None, alias="VolumeStatus")
    attachment_statuses: VolumeStatusAttachmentStatusList = pydantic.Field(None, alias="AttachmentStatuses")

class Vpc(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    dhcp_options_id: String = pydantic.Field(None, alias="DhcpOptionsId")
    state: VpcState = pydantic.Field(None, alias="State")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    instance_tenancy: Tenancy = pydantic.Field(None, alias="InstanceTenancy")
    ipv_6_cidr_block_association_set: VpcIpv6CidrBlockAssociationSet = pydantic.Field(None, alias="Ipv6CidrBlockAssociationSet")
    cidr_block_association_set: VpcCidrBlockAssociationSet = pydantic.Field(None, alias="CidrBlockAssociationSet")
    is_default: Boolean = pydantic.Field(None, alias="IsDefault")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VpcAttachment(_EC2ModelBase):
    state: AttachmentStatus = pydantic.Field(None, alias="State")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class VpcCidrBlockAssociation(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    cidr_block_state: 'VpcCidrBlockState' = pydantic.Field(None, alias="CidrBlockState")

class VpcCidrBlockState(_EC2ModelBase):
    state: VpcCidrBlockStateCode = pydantic.Field(None, alias="State")
    status_message: String = pydantic.Field(None, alias="StatusMessage")

class VpcClassicLink(_EC2ModelBase):
    classic_link_enabled: Boolean = pydantic.Field(None, alias="ClassicLinkEnabled")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vpc_id: String = pydantic.Field(None, alias="VpcId")

class VpcEndpoint(_EC2ModelBase):
    vpc_endpoint_id: String = pydantic.Field(None, alias="VpcEndpointId")
    vpc_endpoint_type: VpcEndpointType = pydantic.Field(None, alias="VpcEndpointType")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    service_name: String = pydantic.Field(None, alias="ServiceName")
    state: State = pydantic.Field(None, alias="State")
    policy_document: String = pydantic.Field(None, alias="PolicyDocument")
    route_table_ids: ValueStringList = pydantic.Field(None, alias="RouteTableIds")
    subnet_ids: ValueStringList = pydantic.Field(None, alias="SubnetIds")
    groups: GroupIdentifierSet = pydantic.Field(None, alias="Groups")
    ip_address_type: IpAddressType = pydantic.Field(None, alias="IpAddressType")
    dns_options: 'DnsOptions' = pydantic.Field(None, alias="DnsOptions")
    private_dns_enabled: Boolean = pydantic.Field(None, alias="PrivateDnsEnabled")
    requester_managed: Boolean = pydantic.Field(None, alias="RequesterManaged")
    network_interface_ids: ValueStringList = pydantic.Field(None, alias="NetworkInterfaceIds")
    dns_entries: DnsEntrySet = pydantic.Field(None, alias="DnsEntries")
    creation_timestamp: MillisecondDateTime = pydantic.Field(None, alias="CreationTimestamp")
    tags: TagList = pydantic.Field(None, alias="Tags")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    last_error: 'LastError' = pydantic.Field(None, alias="LastError")

class VpcEndpointConnection(_EC2ModelBase):
    service_id: String = pydantic.Field(None, alias="ServiceId")
    vpc_endpoint_id: String = pydantic.Field(None, alias="VpcEndpointId")
    vpc_endpoint_owner: String = pydantic.Field(None, alias="VpcEndpointOwner")
    vpc_endpoint_state: State = pydantic.Field(None, alias="VpcEndpointState")
    creation_timestamp: MillisecondDateTime = pydantic.Field(None, alias="CreationTimestamp")
    dns_entries: DnsEntrySet = pydantic.Field(None, alias="DnsEntries")
    network_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="NetworkLoadBalancerArns")
    gateway_load_balancer_arns: ValueStringList = pydantic.Field(None, alias="GatewayLoadBalancerArns")
    ip_address_type: IpAddressType = pydantic.Field(None, alias="IpAddressType")
    vpc_endpoint_connection_id: String = pydantic.Field(None, alias="VpcEndpointConnectionId")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VpcIpv6CidrBlockAssociation(_EC2ModelBase):
    association_id: String = pydantic.Field(None, alias="AssociationId")
    ipv_6_cidr_block: String = pydantic.Field(None, alias="Ipv6CidrBlock")
    ipv_6_cidr_block_state: 'VpcCidrBlockState' = pydantic.Field(None, alias="Ipv6CidrBlockState")
    network_border_group: String = pydantic.Field(None, alias="NetworkBorderGroup")
    ipv_6_pool: String = pydantic.Field(None, alias="Ipv6Pool")

class VpcPeeringConnection(_EC2ModelBase):
    accepter_vpc_info: 'VpcPeeringConnectionVpcInfo' = pydantic.Field(None, alias="AccepterVpcInfo")
    expiration_time: DateTime = pydantic.Field(None, alias="ExpirationTime")
    requester_vpc_info: 'VpcPeeringConnectionVpcInfo' = pydantic.Field(None, alias="RequesterVpcInfo")
    status: 'VpcPeeringConnectionStateReason' = pydantic.Field(None, alias="Status")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vpc_peering_connection_id: String = pydantic.Field(None, alias="VpcPeeringConnectionId")

class VpcPeeringConnectionOptionsDescription(_EC2ModelBase):
    allow_dns_resolution_from_remote_vpc: Boolean = pydantic.Field(None, alias="AllowDnsResolutionFromRemoteVpc")
    allow_egress_from_local_classic_link_to_remote_vpc: Boolean = pydantic.Field(None, alias="AllowEgressFromLocalClassicLinkToRemoteVpc")
    allow_egress_from_local_vpc_to_remote_classic_link: Boolean = pydantic.Field(None, alias="AllowEgressFromLocalVpcToRemoteClassicLink")

class VpcPeeringConnectionStateReason(_EC2ModelBase):
    code: VpcPeeringConnectionStateReasonCode = pydantic.Field(None, alias="Code")
    message: String = pydantic.Field(None, alias="Message")

class VpcPeeringConnectionVpcInfo(_EC2ModelBase):
    cidr_block: String = pydantic.Field(None, alias="CidrBlock")
    ipv_6_cidr_block_set: Ipv6CidrBlockSet = pydantic.Field(None, alias="Ipv6CidrBlockSet")
    cidr_block_set: CidrBlockSet = pydantic.Field(None, alias="CidrBlockSet")
    owner_id: String = pydantic.Field(None, alias="OwnerId")
    peering_options: 'VpcPeeringConnectionOptionsDescription' = pydantic.Field(None, alias="PeeringOptions")
    vpc_id: String = pydantic.Field(None, alias="VpcId")
    region: String = pydantic.Field(None, alias="Region")

class VpnConnection(_EC2ModelBase):
    customer_gateway_configuration: String = pydantic.Field(None, alias="CustomerGatewayConfiguration")
    customer_gateway_id: String = pydantic.Field(None, alias="CustomerGatewayId")
    category: String = pydantic.Field(None, alias="Category")
    state: VpnState = pydantic.Field(None, alias="State")
    type: GatewayType = pydantic.Field(None, alias="Type")
    vpn_connection_id: String = pydantic.Field(None, alias="VpnConnectionId")
    vpn_gateway_id: String = pydantic.Field(None, alias="VpnGatewayId")
    transit_gateway_id: String = pydantic.Field(None, alias="TransitGatewayId")
    core_network_arn: String = pydantic.Field(None, alias="CoreNetworkArn")
    core_network_attachment_arn: String = pydantic.Field(None, alias="CoreNetworkAttachmentArn")
    gateway_association_state: GatewayAssociationState = pydantic.Field(None, alias="GatewayAssociationState")
    options: 'VpnConnectionOptions' = pydantic.Field(None, alias="Options")
    routes: VpnStaticRouteList = pydantic.Field(None, alias="Routes")
    tags: TagList = pydantic.Field(None, alias="Tags")
    vgw_telemetry: VgwTelemetryList = pydantic.Field(None, alias="VgwTelemetry")

class VpnConnectionDeviceType(_EC2ModelBase):
    vpn_connection_device_type_id: String = pydantic.Field(None, alias="VpnConnectionDeviceTypeId")
    vendor: String = pydantic.Field(None, alias="Vendor")
    platform: String = pydantic.Field(None, alias="Platform")
    software: String = pydantic.Field(None, alias="Software")

class VpnConnectionOptions(_EC2ModelBase):
    enable_acceleration: Boolean = pydantic.Field(None, alias="EnableAcceleration")
    static_routes_only: Boolean = pydantic.Field(None, alias="StaticRoutesOnly")
    local_ipv_4_network_cidr: String = pydantic.Field(None, alias="LocalIpv4NetworkCidr")
    remote_ipv_4_network_cidr: String = pydantic.Field(None, alias="RemoteIpv4NetworkCidr")
    local_ipv_6_network_cidr: String = pydantic.Field(None, alias="LocalIpv6NetworkCidr")
    remote_ipv_6_network_cidr: String = pydantic.Field(None, alias="RemoteIpv6NetworkCidr")
    outside_ip_address_type: String = pydantic.Field(None, alias="OutsideIpAddressType")
    transport_transit_gateway_attachment_id: String = pydantic.Field(None, alias="TransportTransitGatewayAttachmentId")
    tunnel_inside_ip_version: TunnelInsideIpVersion = pydantic.Field(None, alias="TunnelInsideIpVersion")
    tunnel_options: TunnelOptionsList = pydantic.Field(None, alias="TunnelOptions")

class VpnConnectionOptionsSpecification(_EC2ModelBase):
    enable_acceleration: Boolean = pydantic.Field(None, alias="EnableAcceleration")
    static_routes_only: Boolean = pydantic.Field(None, alias="StaticRoutesOnly")
    tunnel_inside_ip_version: TunnelInsideIpVersion = pydantic.Field(None, alias="TunnelInsideIpVersion")
    tunnel_options: VpnTunnelOptionsSpecificationsList = pydantic.Field(None, alias="TunnelOptions")
    local_ipv_4_network_cidr: String = pydantic.Field(None, alias="LocalIpv4NetworkCidr")
    remote_ipv_4_network_cidr: String = pydantic.Field(None, alias="RemoteIpv4NetworkCidr")
    local_ipv_6_network_cidr: String = pydantic.Field(None, alias="LocalIpv6NetworkCidr")
    remote_ipv_6_network_cidr: String = pydantic.Field(None, alias="RemoteIpv6NetworkCidr")
    outside_ip_address_type: String = pydantic.Field(None, alias="OutsideIpAddressType")
    transport_transit_gateway_attachment_id: TransitGatewayAttachmentId = pydantic.Field(None, alias="TransportTransitGatewayAttachmentId")

class VpnGateway(_EC2ModelBase):
    availability_zone: String = pydantic.Field(None, alias="AvailabilityZone")
    state: VpnState = pydantic.Field(None, alias="State")
    type: GatewayType = pydantic.Field(None, alias="Type")
    vpc_attachments: VpcAttachmentList = pydantic.Field(None, alias="VpcAttachments")
    vpn_gateway_id: String = pydantic.Field(None, alias="VpnGatewayId")
    amazon_side_asn: Long = pydantic.Field(None, alias="AmazonSideAsn")
    tags: TagList = pydantic.Field(None, alias="Tags")

class VpnStaticRoute(_EC2ModelBase):
    destination_cidr_block: String = pydantic.Field(None, alias="DestinationCidrBlock")
    source: VpnStaticRouteSource = pydantic.Field(None, alias="Source")
    state: VpnState = pydantic.Field(None, alias="State")

class VpnTunnelLogOptions(_EC2ModelBase):
    cloud_watch_log_options: 'CloudWatchLogOptions' = pydantic.Field(None, alias="CloudWatchLogOptions")

class VpnTunnelLogOptionsSpecification(_EC2ModelBase):
    cloud_watch_log_options: 'CloudWatchLogOptionsSpecification' = pydantic.Field(None, alias="CloudWatchLogOptions")

class VpnTunnelOptionsSpecification(_EC2ModelBase):
    tunnel_inside_cidr: String = pydantic.Field(None, alias="TunnelInsideCidr")
    tunnel_inside_ipv_6_cidr: String = pydantic.Field(None, alias="TunnelInsideIpv6Cidr")
    pre_shared_key: String = pydantic.Field(None, alias="PreSharedKey")
    phase_1_lifetime_seconds: Integer = pydantic.Field(None, alias="Phase1LifetimeSeconds")
    phase_2_lifetime_seconds: Integer = pydantic.Field(None, alias="Phase2LifetimeSeconds")
    rekey_margin_time_seconds: Integer = pydantic.Field(None, alias="RekeyMarginTimeSeconds")
    rekey_fuzz_percentage: Integer = pydantic.Field(None, alias="RekeyFuzzPercentage")
    replay_window_size: Integer = pydantic.Field(None, alias="ReplayWindowSize")
    dpd_timeout_seconds: Integer = pydantic.Field(None, alias="DPDTimeoutSeconds")
    dpd_timeout_action: String = pydantic.Field(None, alias="DPDTimeoutAction")
    phase_1_encryption_algorithms: Phase1EncryptionAlgorithmsRequestList = pydantic.Field(None, alias="Phase1EncryptionAlgorithms")
    phase_2_encryption_algorithms: Phase2EncryptionAlgorithmsRequestList = pydantic.Field(None, alias="Phase2EncryptionAlgorithms")
    phase_1_integrity_algorithms: Phase1IntegrityAlgorithmsRequestList = pydantic.Field(None, alias="Phase1IntegrityAlgorithms")
    phase_2_integrity_algorithms: Phase2IntegrityAlgorithmsRequestList = pydantic.Field(None, alias="Phase2IntegrityAlgorithms")
    phase_1_dh_group_numbers: Phase1DHGroupNumbersRequestList = pydantic.Field(None, alias="Phase1DHGroupNumbers")
    phase_2_dh_group_numbers: Phase2DHGroupNumbersRequestList = pydantic.Field(None, alias="Phase2DHGroupNumbers")
    ike_versions: IKEVersionsRequestList = pydantic.Field(None, alias="IKEVersions")
    startup_action: String = pydantic.Field(None, alias="StartupAction")
    log_options: 'VpnTunnelLogOptionsSpecification' = pydantic.Field(None, alias="LogOptions")
    enable_tunnel_lifecycle_control: Boolean = pydantic.Field(None, alias="EnableTunnelLifecycleControl")

class WithdrawByoipCidrRequest(_EC2ModelBase):
    cidr: String = pydantic.Field(None, alias="Cidr")
    dry_run: Boolean = pydantic.Field(None, alias="DryRun")

class WithdrawByoipCidrResult(_EC2ModelBase):
    byoip_cidr: 'ByoipCidr' = pydantic.Field(None, alias="ByoipCidr")

AcceleratorCount.update_forward_refs()
AcceleratorCountRequest.update_forward_refs()
AcceleratorTotalMemoryMiB.update_forward_refs()
AcceleratorTotalMemoryMiBRequest.update_forward_refs()
AcceptAddressTransferRequest.update_forward_refs()
AcceptAddressTransferResult.update_forward_refs()
AcceptReservedInstancesExchangeQuoteRequest.update_forward_refs()
AcceptReservedInstancesExchangeQuoteResult.update_forward_refs()
AcceptTransitGatewayMulticastDomainAssociationsRequest.update_forward_refs()
AcceptTransitGatewayMulticastDomainAssociationsResult.update_forward_refs()
AcceptTransitGatewayPeeringAttachmentRequest.update_forward_refs()
AcceptTransitGatewayPeeringAttachmentResult.update_forward_refs()
AcceptTransitGatewayVpcAttachmentRequest.update_forward_refs()
AcceptTransitGatewayVpcAttachmentResult.update_forward_refs()
AcceptVpcEndpointConnectionsRequest.update_forward_refs()
AcceptVpcEndpointConnectionsResult.update_forward_refs()
AcceptVpcPeeringConnectionRequest.update_forward_refs()
AcceptVpcPeeringConnectionResult.update_forward_refs()
AccessScopeAnalysisFinding.update_forward_refs()
AccessScopePath.update_forward_refs()
AccessScopePathRequest.update_forward_refs()
AccountAttribute.update_forward_refs()
AccountAttributeValue.update_forward_refs()
ActiveInstance.update_forward_refs()
AddIpamOperatingRegion.update_forward_refs()
AddPrefixListEntry.update_forward_refs()
AddedPrincipal.update_forward_refs()
AdditionalDetail.update_forward_refs()
Address.update_forward_refs()
AddressAttribute.update_forward_refs()
AddressTransfer.update_forward_refs()
AdvertiseByoipCidrRequest.update_forward_refs()
AdvertiseByoipCidrResult.update_forward_refs()
AllocateAddressRequest.update_forward_refs()
AllocateAddressResult.update_forward_refs()
AllocateHostsRequest.update_forward_refs()
AllocateHostsResult.update_forward_refs()
AllocateIpamPoolCidrRequest.update_forward_refs()
AllocateIpamPoolCidrResult.update_forward_refs()
AllowedPrincipal.update_forward_refs()
AlternatePathHint.update_forward_refs()
AnalysisAclRule.update_forward_refs()
AnalysisComponent.update_forward_refs()
AnalysisLoadBalancerListener.update_forward_refs()
AnalysisLoadBalancerTarget.update_forward_refs()
AnalysisPacketHeader.update_forward_refs()
AnalysisRouteTableRoute.update_forward_refs()
AnalysisSecurityGroupRule.update_forward_refs()
ApplySecurityGroupsToClientVpnTargetNetworkRequest.update_forward_refs()
ApplySecurityGroupsToClientVpnTargetNetworkResult.update_forward_refs()
AssignIpv6AddressesRequest.update_forward_refs()
AssignIpv6AddressesResult.update_forward_refs()
AssignPrivateIpAddressesRequest.update_forward_refs()
AssignPrivateIpAddressesResult.update_forward_refs()
AssignPrivateNatGatewayAddressRequest.update_forward_refs()
AssignPrivateNatGatewayAddressResult.update_forward_refs()
AssignedPrivateIpAddress.update_forward_refs()
AssociateAddressRequest.update_forward_refs()
AssociateAddressResult.update_forward_refs()
AssociateClientVpnTargetNetworkRequest.update_forward_refs()
AssociateClientVpnTargetNetworkResult.update_forward_refs()
AssociateDhcpOptionsRequest.update_forward_refs()
AssociateEnclaveCertificateIamRoleRequest.update_forward_refs()
AssociateEnclaveCertificateIamRoleResult.update_forward_refs()
AssociateIamInstanceProfileRequest.update_forward_refs()
AssociateIamInstanceProfileResult.update_forward_refs()
AssociateInstanceEventWindowRequest.update_forward_refs()
AssociateInstanceEventWindowResult.update_forward_refs()
AssociateIpamResourceDiscoveryRequest.update_forward_refs()
AssociateIpamResourceDiscoveryResult.update_forward_refs()
AssociateNatGatewayAddressRequest.update_forward_refs()
AssociateNatGatewayAddressResult.update_forward_refs()
AssociateRouteTableRequest.update_forward_refs()
AssociateRouteTableResult.update_forward_refs()
AssociateSubnetCidrBlockRequest.update_forward_refs()
AssociateSubnetCidrBlockResult.update_forward_refs()
AssociateTransitGatewayMulticastDomainRequest.update_forward_refs()
AssociateTransitGatewayMulticastDomainResult.update_forward_refs()
AssociateTransitGatewayPolicyTableRequest.update_forward_refs()
AssociateTransitGatewayPolicyTableResult.update_forward_refs()
AssociateTransitGatewayRouteTableRequest.update_forward_refs()
AssociateTransitGatewayRouteTableResult.update_forward_refs()
AssociateTrunkInterfaceRequest.update_forward_refs()
AssociateTrunkInterfaceResult.update_forward_refs()
AssociateVpcCidrBlockRequest.update_forward_refs()
AssociateVpcCidrBlockResult.update_forward_refs()
AssociatedRole.update_forward_refs()
AssociatedTargetNetwork.update_forward_refs()
AssociationStatus.update_forward_refs()
AthenaIntegration.update_forward_refs()
AttachClassicLinkVpcRequest.update_forward_refs()
AttachClassicLinkVpcResult.update_forward_refs()
AttachInternetGatewayRequest.update_forward_refs()
AttachNetworkInterfaceRequest.update_forward_refs()
AttachNetworkInterfaceResult.update_forward_refs()
AttachVerifiedAccessTrustProviderRequest.update_forward_refs()
AttachVerifiedAccessTrustProviderResult.update_forward_refs()
AttachVolumeRequest.update_forward_refs()
AttachVpnGatewayRequest.update_forward_refs()
AttachVpnGatewayResult.update_forward_refs()
AttachmentEnaSrdSpecification.update_forward_refs()
AttachmentEnaSrdUdpSpecification.update_forward_refs()
AttributeBooleanValue.update_forward_refs()
AttributeValue.update_forward_refs()
AuthorizationRule.update_forward_refs()
AuthorizeClientVpnIngressRequest.update_forward_refs()
AuthorizeClientVpnIngressResult.update_forward_refs()
AuthorizeSecurityGroupEgressRequest.update_forward_refs()
AuthorizeSecurityGroupEgressResult.update_forward_refs()
AuthorizeSecurityGroupIngressRequest.update_forward_refs()
AuthorizeSecurityGroupIngressResult.update_forward_refs()
AvailabilityZone.update_forward_refs()
AvailabilityZoneMessage.update_forward_refs()
AvailableCapacity.update_forward_refs()
BaselineEbsBandwidthMbps.update_forward_refs()
BaselineEbsBandwidthMbpsRequest.update_forward_refs()
BlobAttributeValue.update_forward_refs()
BlockDeviceMapping.update_forward_refs()
BundleInstanceRequest.update_forward_refs()
BundleInstanceResult.update_forward_refs()
BundleTask.update_forward_refs()
BundleTaskError.update_forward_refs()
ByoipCidr.update_forward_refs()
CancelBundleTaskRequest.update_forward_refs()
CancelBundleTaskResult.update_forward_refs()
CancelCapacityReservationFleetError.update_forward_refs()
CancelCapacityReservationFleetsRequest.update_forward_refs()
CancelCapacityReservationFleetsResult.update_forward_refs()
CancelCapacityReservationRequest.update_forward_refs()
CancelCapacityReservationResult.update_forward_refs()
CancelConversionRequest.update_forward_refs()
CancelExportTaskRequest.update_forward_refs()
CancelImageLaunchPermissionRequest.update_forward_refs()
CancelImageLaunchPermissionResult.update_forward_refs()
CancelImportTaskRequest.update_forward_refs()
CancelImportTaskResult.update_forward_refs()
CancelReservedInstancesListingRequest.update_forward_refs()
CancelReservedInstancesListingResult.update_forward_refs()
CancelSpotFleetRequestsError.update_forward_refs()
CancelSpotFleetRequestsErrorItem.update_forward_refs()
CancelSpotFleetRequestsRequest.update_forward_refs()
CancelSpotFleetRequestsResponse.update_forward_refs()
CancelSpotFleetRequestsSuccessItem.update_forward_refs()
CancelSpotInstanceRequestsRequest.update_forward_refs()
CancelSpotInstanceRequestsResult.update_forward_refs()
CancelledSpotInstanceRequest.update_forward_refs()
CapacityAllocation.update_forward_refs()
CapacityReservation.update_forward_refs()
CapacityReservationFleet.update_forward_refs()
CapacityReservationFleetCancellationState.update_forward_refs()
CapacityReservationGroup.update_forward_refs()
CapacityReservationOptions.update_forward_refs()
CapacityReservationOptionsRequest.update_forward_refs()
CapacityReservationSpecification.update_forward_refs()
CapacityReservationSpecificationResponse.update_forward_refs()
CapacityReservationTarget.update_forward_refs()
CapacityReservationTargetResponse.update_forward_refs()
CarrierGateway.update_forward_refs()
CertificateAuthentication.update_forward_refs()
CertificateAuthenticationRequest.update_forward_refs()
CidrAuthorizationContext.update_forward_refs()
CidrBlock.update_forward_refs()
ClassicLinkDnsSupport.update_forward_refs()
ClassicLinkInstance.update_forward_refs()
ClassicLoadBalancer.update_forward_refs()
ClassicLoadBalancersConfig.update_forward_refs()
ClientCertificateRevocationListStatus.update_forward_refs()
ClientConnectOptions.update_forward_refs()
ClientConnectResponseOptions.update_forward_refs()
ClientData.update_forward_refs()
ClientLoginBannerOptions.update_forward_refs()
ClientLoginBannerResponseOptions.update_forward_refs()
ClientVpnAuthentication.update_forward_refs()
ClientVpnAuthenticationRequest.update_forward_refs()
ClientVpnAuthorizationRuleStatus.update_forward_refs()
ClientVpnConnection.update_forward_refs()
ClientVpnConnectionStatus.update_forward_refs()
ClientVpnEndpoint.update_forward_refs()
ClientVpnEndpointAttributeStatus.update_forward_refs()
ClientVpnEndpointStatus.update_forward_refs()
ClientVpnRoute.update_forward_refs()
ClientVpnRouteStatus.update_forward_refs()
CloudWatchLogOptions.update_forward_refs()
CloudWatchLogOptionsSpecification.update_forward_refs()
CoipAddressUsage.update_forward_refs()
CoipCidr.update_forward_refs()
CoipPool.update_forward_refs()
ConfirmProductInstanceRequest.update_forward_refs()
ConfirmProductInstanceResult.update_forward_refs()
ConnectionLogOptions.update_forward_refs()
ConnectionLogResponseOptions.update_forward_refs()
ConnectionNotification.update_forward_refs()
ConversionTask.update_forward_refs()
CopyFpgaImageRequest.update_forward_refs()
CopyFpgaImageResult.update_forward_refs()
CopyImageRequest.update_forward_refs()
CopyImageResult.update_forward_refs()
CopySnapshotRequest.update_forward_refs()
CopySnapshotResult.update_forward_refs()
CpuOptions.update_forward_refs()
CpuOptionsRequest.update_forward_refs()
CreateCapacityReservationFleetRequest.update_forward_refs()
CreateCapacityReservationFleetResult.update_forward_refs()
CreateCapacityReservationRequest.update_forward_refs()
CreateCapacityReservationResult.update_forward_refs()
CreateCarrierGatewayRequest.update_forward_refs()
CreateCarrierGatewayResult.update_forward_refs()
CreateClientVpnEndpointRequest.update_forward_refs()
CreateClientVpnEndpointResult.update_forward_refs()
CreateClientVpnRouteRequest.update_forward_refs()
CreateClientVpnRouteResult.update_forward_refs()
CreateCoipCidrRequest.update_forward_refs()
CreateCoipCidrResult.update_forward_refs()
CreateCoipPoolRequest.update_forward_refs()
CreateCoipPoolResult.update_forward_refs()
CreateCustomerGatewayRequest.update_forward_refs()
CreateCustomerGatewayResult.update_forward_refs()
CreateDefaultSubnetRequest.update_forward_refs()
CreateDefaultSubnetResult.update_forward_refs()
CreateDefaultVpcRequest.update_forward_refs()
CreateDefaultVpcResult.update_forward_refs()
CreateDhcpOptionsRequest.update_forward_refs()
CreateDhcpOptionsResult.update_forward_refs()
CreateEgressOnlyInternetGatewayRequest.update_forward_refs()
CreateEgressOnlyInternetGatewayResult.update_forward_refs()
CreateFleetError.update_forward_refs()
CreateFleetInstance.update_forward_refs()
CreateFleetRequest.update_forward_refs()
CreateFleetResult.update_forward_refs()
CreateFlowLogsRequest.update_forward_refs()
CreateFlowLogsResult.update_forward_refs()
CreateFpgaImageRequest.update_forward_refs()
CreateFpgaImageResult.update_forward_refs()
CreateImageRequest.update_forward_refs()
CreateImageResult.update_forward_refs()
CreateInstanceEventWindowRequest.update_forward_refs()
CreateInstanceEventWindowResult.update_forward_refs()
CreateInstanceExportTaskRequest.update_forward_refs()
CreateInstanceExportTaskResult.update_forward_refs()
CreateInternetGatewayRequest.update_forward_refs()
CreateInternetGatewayResult.update_forward_refs()
CreateIpamPoolRequest.update_forward_refs()
CreateIpamPoolResult.update_forward_refs()
CreateIpamRequest.update_forward_refs()
CreateIpamResourceDiscoveryRequest.update_forward_refs()
CreateIpamResourceDiscoveryResult.update_forward_refs()
CreateIpamResult.update_forward_refs()
CreateIpamScopeRequest.update_forward_refs()
CreateIpamScopeResult.update_forward_refs()
CreateKeyPairRequest.update_forward_refs()
CreateLaunchTemplateRequest.update_forward_refs()
CreateLaunchTemplateResult.update_forward_refs()
CreateLaunchTemplateVersionRequest.update_forward_refs()
CreateLaunchTemplateVersionResult.update_forward_refs()
CreateLocalGatewayRouteRequest.update_forward_refs()
CreateLocalGatewayRouteResult.update_forward_refs()
CreateLocalGatewayRouteTableRequest.update_forward_refs()
CreateLocalGatewayRouteTableResult.update_forward_refs()
CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest.update_forward_refs()
CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult.update_forward_refs()
CreateLocalGatewayRouteTableVpcAssociationRequest.update_forward_refs()
CreateLocalGatewayRouteTableVpcAssociationResult.update_forward_refs()
CreateManagedPrefixListRequest.update_forward_refs()
CreateManagedPrefixListResult.update_forward_refs()
CreateNatGatewayRequest.update_forward_refs()
CreateNatGatewayResult.update_forward_refs()
CreateNetworkAclEntryRequest.update_forward_refs()
CreateNetworkAclRequest.update_forward_refs()
CreateNetworkAclResult.update_forward_refs()
CreateNetworkInsightsAccessScopeRequest.update_forward_refs()
CreateNetworkInsightsAccessScopeResult.update_forward_refs()
CreateNetworkInsightsPathRequest.update_forward_refs()
CreateNetworkInsightsPathResult.update_forward_refs()
CreateNetworkInterfacePermissionRequest.update_forward_refs()
CreateNetworkInterfacePermissionResult.update_forward_refs()
CreateNetworkInterfaceRequest.update_forward_refs()
CreateNetworkInterfaceResult.update_forward_refs()
CreatePlacementGroupRequest.update_forward_refs()
CreatePlacementGroupResult.update_forward_refs()
CreatePublicIpv4PoolRequest.update_forward_refs()
CreatePublicIpv4PoolResult.update_forward_refs()
CreateReplaceRootVolumeTaskRequest.update_forward_refs()
CreateReplaceRootVolumeTaskResult.update_forward_refs()
CreateReservedInstancesListingRequest.update_forward_refs()
CreateReservedInstancesListingResult.update_forward_refs()
CreateRestoreImageTaskRequest.update_forward_refs()
CreateRestoreImageTaskResult.update_forward_refs()
CreateRouteRequest.update_forward_refs()
CreateRouteResult.update_forward_refs()
CreateRouteTableRequest.update_forward_refs()
CreateRouteTableResult.update_forward_refs()
CreateSecurityGroupRequest.update_forward_refs()
CreateSecurityGroupResult.update_forward_refs()
CreateSnapshotRequest.update_forward_refs()
CreateSnapshotsRequest.update_forward_refs()
CreateSnapshotsResult.update_forward_refs()
CreateSpotDatafeedSubscriptionRequest.update_forward_refs()
CreateSpotDatafeedSubscriptionResult.update_forward_refs()
CreateStoreImageTaskRequest.update_forward_refs()
CreateStoreImageTaskResult.update_forward_refs()
CreateSubnetCidrReservationRequest.update_forward_refs()
CreateSubnetCidrReservationResult.update_forward_refs()
CreateSubnetRequest.update_forward_refs()
CreateSubnetResult.update_forward_refs()
CreateTagsRequest.update_forward_refs()
CreateTrafficMirrorFilterRequest.update_forward_refs()
CreateTrafficMirrorFilterResult.update_forward_refs()
CreateTrafficMirrorFilterRuleRequest.update_forward_refs()
CreateTrafficMirrorFilterRuleResult.update_forward_refs()
CreateTrafficMirrorSessionRequest.update_forward_refs()
CreateTrafficMirrorSessionResult.update_forward_refs()
CreateTrafficMirrorTargetRequest.update_forward_refs()
CreateTrafficMirrorTargetResult.update_forward_refs()
CreateTransitGatewayConnectPeerRequest.update_forward_refs()
CreateTransitGatewayConnectPeerResult.update_forward_refs()
CreateTransitGatewayConnectRequest.update_forward_refs()
CreateTransitGatewayConnectRequestOptions.update_forward_refs()
CreateTransitGatewayConnectResult.update_forward_refs()
CreateTransitGatewayMulticastDomainRequest.update_forward_refs()
CreateTransitGatewayMulticastDomainRequestOptions.update_forward_refs()
CreateTransitGatewayMulticastDomainResult.update_forward_refs()
CreateTransitGatewayPeeringAttachmentRequest.update_forward_refs()
CreateTransitGatewayPeeringAttachmentRequestOptions.update_forward_refs()
CreateTransitGatewayPeeringAttachmentResult.update_forward_refs()
CreateTransitGatewayPolicyTableRequest.update_forward_refs()
CreateTransitGatewayPolicyTableResult.update_forward_refs()
CreateTransitGatewayPrefixListReferenceRequest.update_forward_refs()
CreateTransitGatewayPrefixListReferenceResult.update_forward_refs()
CreateTransitGatewayRequest.update_forward_refs()
CreateTransitGatewayResult.update_forward_refs()
CreateTransitGatewayRouteRequest.update_forward_refs()
CreateTransitGatewayRouteResult.update_forward_refs()
CreateTransitGatewayRouteTableAnnouncementRequest.update_forward_refs()
CreateTransitGatewayRouteTableAnnouncementResult.update_forward_refs()
CreateTransitGatewayRouteTableRequest.update_forward_refs()
CreateTransitGatewayRouteTableResult.update_forward_refs()
CreateTransitGatewayVpcAttachmentRequest.update_forward_refs()
CreateTransitGatewayVpcAttachmentRequestOptions.update_forward_refs()
CreateTransitGatewayVpcAttachmentResult.update_forward_refs()
CreateVerifiedAccessEndpointEniOptions.update_forward_refs()
CreateVerifiedAccessEndpointLoadBalancerOptions.update_forward_refs()
CreateVerifiedAccessEndpointRequest.update_forward_refs()
CreateVerifiedAccessEndpointResult.update_forward_refs()
CreateVerifiedAccessGroupRequest.update_forward_refs()
CreateVerifiedAccessGroupResult.update_forward_refs()
CreateVerifiedAccessInstanceRequest.update_forward_refs()
CreateVerifiedAccessInstanceResult.update_forward_refs()
CreateVerifiedAccessTrustProviderDeviceOptions.update_forward_refs()
CreateVerifiedAccessTrustProviderOidcOptions.update_forward_refs()
CreateVerifiedAccessTrustProviderRequest.update_forward_refs()
CreateVerifiedAccessTrustProviderResult.update_forward_refs()
CreateVolumePermission.update_forward_refs()
CreateVolumePermissionModifications.update_forward_refs()
CreateVolumeRequest.update_forward_refs()
CreateVpcEndpointConnectionNotificationRequest.update_forward_refs()
CreateVpcEndpointConnectionNotificationResult.update_forward_refs()
CreateVpcEndpointRequest.update_forward_refs()
CreateVpcEndpointResult.update_forward_refs()
CreateVpcEndpointServiceConfigurationRequest.update_forward_refs()
CreateVpcEndpointServiceConfigurationResult.update_forward_refs()
CreateVpcPeeringConnectionRequest.update_forward_refs()
CreateVpcPeeringConnectionResult.update_forward_refs()
CreateVpcRequest.update_forward_refs()
CreateVpcResult.update_forward_refs()
CreateVpnConnectionRequest.update_forward_refs()
CreateVpnConnectionResult.update_forward_refs()
CreateVpnConnectionRouteRequest.update_forward_refs()
CreateVpnGatewayRequest.update_forward_refs()
CreateVpnGatewayResult.update_forward_refs()
CreditSpecification.update_forward_refs()
CreditSpecificationRequest.update_forward_refs()
CustomerGateway.update_forward_refs()
DataQuery.update_forward_refs()
DataResponse.update_forward_refs()
DeleteCarrierGatewayRequest.update_forward_refs()
DeleteCarrierGatewayResult.update_forward_refs()
DeleteClientVpnEndpointRequest.update_forward_refs()
DeleteClientVpnEndpointResult.update_forward_refs()
DeleteClientVpnRouteRequest.update_forward_refs()
DeleteClientVpnRouteResult.update_forward_refs()
DeleteCoipCidrRequest.update_forward_refs()
DeleteCoipCidrResult.update_forward_refs()
DeleteCoipPoolRequest.update_forward_refs()
DeleteCoipPoolResult.update_forward_refs()
DeleteCustomerGatewayRequest.update_forward_refs()
DeleteDhcpOptionsRequest.update_forward_refs()
DeleteEgressOnlyInternetGatewayRequest.update_forward_refs()
DeleteEgressOnlyInternetGatewayResult.update_forward_refs()
DeleteFleetError.update_forward_refs()
DeleteFleetErrorItem.update_forward_refs()
DeleteFleetSuccessItem.update_forward_refs()
DeleteFleetsRequest.update_forward_refs()
DeleteFleetsResult.update_forward_refs()
DeleteFlowLogsRequest.update_forward_refs()
DeleteFlowLogsResult.update_forward_refs()
DeleteFpgaImageRequest.update_forward_refs()
DeleteFpgaImageResult.update_forward_refs()
DeleteInstanceEventWindowRequest.update_forward_refs()
DeleteInstanceEventWindowResult.update_forward_refs()
DeleteInternetGatewayRequest.update_forward_refs()
DeleteIpamPoolRequest.update_forward_refs()
DeleteIpamPoolResult.update_forward_refs()
DeleteIpamRequest.update_forward_refs()
DeleteIpamResourceDiscoveryRequest.update_forward_refs()
DeleteIpamResourceDiscoveryResult.update_forward_refs()
DeleteIpamResult.update_forward_refs()
DeleteIpamScopeRequest.update_forward_refs()
DeleteIpamScopeResult.update_forward_refs()
DeleteKeyPairRequest.update_forward_refs()
DeleteLaunchTemplateRequest.update_forward_refs()
DeleteLaunchTemplateResult.update_forward_refs()
DeleteLaunchTemplateVersionsRequest.update_forward_refs()
DeleteLaunchTemplateVersionsResponseErrorItem.update_forward_refs()
DeleteLaunchTemplateVersionsResponseSuccessItem.update_forward_refs()
DeleteLaunchTemplateVersionsResult.update_forward_refs()
DeleteLocalGatewayRouteRequest.update_forward_refs()
DeleteLocalGatewayRouteResult.update_forward_refs()
DeleteLocalGatewayRouteTableRequest.update_forward_refs()
DeleteLocalGatewayRouteTableResult.update_forward_refs()
DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest.update_forward_refs()
DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult.update_forward_refs()
DeleteLocalGatewayRouteTableVpcAssociationRequest.update_forward_refs()
DeleteLocalGatewayRouteTableVpcAssociationResult.update_forward_refs()
DeleteManagedPrefixListRequest.update_forward_refs()
DeleteManagedPrefixListResult.update_forward_refs()
DeleteNatGatewayRequest.update_forward_refs()
DeleteNatGatewayResult.update_forward_refs()
DeleteNetworkAclEntryRequest.update_forward_refs()
DeleteNetworkAclRequest.update_forward_refs()
DeleteNetworkInsightsAccessScopeAnalysisRequest.update_forward_refs()
DeleteNetworkInsightsAccessScopeAnalysisResult.update_forward_refs()
DeleteNetworkInsightsAccessScopeRequest.update_forward_refs()
DeleteNetworkInsightsAccessScopeResult.update_forward_refs()
DeleteNetworkInsightsAnalysisRequest.update_forward_refs()
DeleteNetworkInsightsAnalysisResult.update_forward_refs()
DeleteNetworkInsightsPathRequest.update_forward_refs()
DeleteNetworkInsightsPathResult.update_forward_refs()
DeleteNetworkInterfacePermissionRequest.update_forward_refs()
DeleteNetworkInterfacePermissionResult.update_forward_refs()
DeleteNetworkInterfaceRequest.update_forward_refs()
DeletePlacementGroupRequest.update_forward_refs()
DeletePublicIpv4PoolRequest.update_forward_refs()
DeletePublicIpv4PoolResult.update_forward_refs()
DeleteQueuedReservedInstancesError.update_forward_refs()
DeleteQueuedReservedInstancesRequest.update_forward_refs()
DeleteQueuedReservedInstancesResult.update_forward_refs()
DeleteRouteRequest.update_forward_refs()
DeleteRouteTableRequest.update_forward_refs()
DeleteSecurityGroupRequest.update_forward_refs()
DeleteSnapshotRequest.update_forward_refs()
DeleteSpotDatafeedSubscriptionRequest.update_forward_refs()
DeleteSubnetCidrReservationRequest.update_forward_refs()
DeleteSubnetCidrReservationResult.update_forward_refs()
DeleteSubnetRequest.update_forward_refs()
DeleteTagsRequest.update_forward_refs()
DeleteTrafficMirrorFilterRequest.update_forward_refs()
DeleteTrafficMirrorFilterResult.update_forward_refs()
DeleteTrafficMirrorFilterRuleRequest.update_forward_refs()
DeleteTrafficMirrorFilterRuleResult.update_forward_refs()
DeleteTrafficMirrorSessionRequest.update_forward_refs()
DeleteTrafficMirrorSessionResult.update_forward_refs()
DeleteTrafficMirrorTargetRequest.update_forward_refs()
DeleteTrafficMirrorTargetResult.update_forward_refs()
DeleteTransitGatewayConnectPeerRequest.update_forward_refs()
DeleteTransitGatewayConnectPeerResult.update_forward_refs()
DeleteTransitGatewayConnectRequest.update_forward_refs()
DeleteTransitGatewayConnectResult.update_forward_refs()
DeleteTransitGatewayMulticastDomainRequest.update_forward_refs()
DeleteTransitGatewayMulticastDomainResult.update_forward_refs()
DeleteTransitGatewayPeeringAttachmentRequest.update_forward_refs()
DeleteTransitGatewayPeeringAttachmentResult.update_forward_refs()
DeleteTransitGatewayPolicyTableRequest.update_forward_refs()
DeleteTransitGatewayPolicyTableResult.update_forward_refs()
DeleteTransitGatewayPrefixListReferenceRequest.update_forward_refs()
DeleteTransitGatewayPrefixListReferenceResult.update_forward_refs()
DeleteTransitGatewayRequest.update_forward_refs()
DeleteTransitGatewayResult.update_forward_refs()
DeleteTransitGatewayRouteRequest.update_forward_refs()
DeleteTransitGatewayRouteResult.update_forward_refs()
DeleteTransitGatewayRouteTableAnnouncementRequest.update_forward_refs()
DeleteTransitGatewayRouteTableAnnouncementResult.update_forward_refs()
DeleteTransitGatewayRouteTableRequest.update_forward_refs()
DeleteTransitGatewayRouteTableResult.update_forward_refs()
DeleteTransitGatewayVpcAttachmentRequest.update_forward_refs()
DeleteTransitGatewayVpcAttachmentResult.update_forward_refs()
DeleteVerifiedAccessEndpointRequest.update_forward_refs()
DeleteVerifiedAccessEndpointResult.update_forward_refs()
DeleteVerifiedAccessGroupRequest.update_forward_refs()
DeleteVerifiedAccessGroupResult.update_forward_refs()
DeleteVerifiedAccessInstanceRequest.update_forward_refs()
DeleteVerifiedAccessInstanceResult.update_forward_refs()
DeleteVerifiedAccessTrustProviderRequest.update_forward_refs()
DeleteVerifiedAccessTrustProviderResult.update_forward_refs()
DeleteVolumeRequest.update_forward_refs()
DeleteVpcEndpointConnectionNotificationsRequest.update_forward_refs()
DeleteVpcEndpointConnectionNotificationsResult.update_forward_refs()
DeleteVpcEndpointServiceConfigurationsRequest.update_forward_refs()
DeleteVpcEndpointServiceConfigurationsResult.update_forward_refs()
DeleteVpcEndpointsRequest.update_forward_refs()
DeleteVpcEndpointsResult.update_forward_refs()
DeleteVpcPeeringConnectionRequest.update_forward_refs()
DeleteVpcPeeringConnectionResult.update_forward_refs()
DeleteVpcRequest.update_forward_refs()
DeleteVpnConnectionRequest.update_forward_refs()
DeleteVpnConnectionRouteRequest.update_forward_refs()
DeleteVpnGatewayRequest.update_forward_refs()
DeprovisionByoipCidrRequest.update_forward_refs()
DeprovisionByoipCidrResult.update_forward_refs()
DeprovisionIpamPoolCidrRequest.update_forward_refs()
DeprovisionIpamPoolCidrResult.update_forward_refs()
DeprovisionPublicIpv4PoolCidrRequest.update_forward_refs()
DeprovisionPublicIpv4PoolCidrResult.update_forward_refs()
DeregisterImageRequest.update_forward_refs()
DeregisterInstanceEventNotificationAttributesRequest.update_forward_refs()
DeregisterInstanceEventNotificationAttributesResult.update_forward_refs()
DeregisterInstanceTagAttributeRequest.update_forward_refs()
DeregisterTransitGatewayMulticastGroupMembersRequest.update_forward_refs()
DeregisterTransitGatewayMulticastGroupMembersResult.update_forward_refs()
DeregisterTransitGatewayMulticastGroupSourcesRequest.update_forward_refs()
DeregisterTransitGatewayMulticastGroupSourcesResult.update_forward_refs()
DescribeAccountAttributesRequest.update_forward_refs()
DescribeAccountAttributesResult.update_forward_refs()
DescribeAddressTransfersRequest.update_forward_refs()
DescribeAddressTransfersResult.update_forward_refs()
DescribeAddressesAttributeRequest.update_forward_refs()
DescribeAddressesAttributeResult.update_forward_refs()
DescribeAddressesRequest.update_forward_refs()
DescribeAddressesResult.update_forward_refs()
DescribeAggregateIdFormatRequest.update_forward_refs()
DescribeAggregateIdFormatResult.update_forward_refs()
DescribeAvailabilityZonesRequest.update_forward_refs()
DescribeAvailabilityZonesResult.update_forward_refs()
DescribeAwsNetworkPerformanceMetricSubscriptionsRequest.update_forward_refs()
DescribeAwsNetworkPerformanceMetricSubscriptionsResult.update_forward_refs()
DescribeBundleTasksRequest.update_forward_refs()
DescribeBundleTasksResult.update_forward_refs()
DescribeByoipCidrsRequest.update_forward_refs()
DescribeByoipCidrsResult.update_forward_refs()
DescribeCapacityReservationFleetsRequest.update_forward_refs()
DescribeCapacityReservationFleetsResult.update_forward_refs()
DescribeCapacityReservationsRequest.update_forward_refs()
DescribeCapacityReservationsResult.update_forward_refs()
DescribeCarrierGatewaysRequest.update_forward_refs()
DescribeCarrierGatewaysResult.update_forward_refs()
DescribeClassicLinkInstancesRequest.update_forward_refs()
DescribeClassicLinkInstancesResult.update_forward_refs()
DescribeClientVpnAuthorizationRulesRequest.update_forward_refs()
DescribeClientVpnAuthorizationRulesResult.update_forward_refs()
DescribeClientVpnConnectionsRequest.update_forward_refs()
DescribeClientVpnConnectionsResult.update_forward_refs()
DescribeClientVpnEndpointsRequest.update_forward_refs()
DescribeClientVpnEndpointsResult.update_forward_refs()
DescribeClientVpnRoutesRequest.update_forward_refs()
DescribeClientVpnRoutesResult.update_forward_refs()
DescribeClientVpnTargetNetworksRequest.update_forward_refs()
DescribeClientVpnTargetNetworksResult.update_forward_refs()
DescribeCoipPoolsRequest.update_forward_refs()
DescribeCoipPoolsResult.update_forward_refs()
DescribeConversionTasksRequest.update_forward_refs()
DescribeConversionTasksResult.update_forward_refs()
DescribeCustomerGatewaysRequest.update_forward_refs()
DescribeCustomerGatewaysResult.update_forward_refs()
DescribeDhcpOptionsRequest.update_forward_refs()
DescribeDhcpOptionsResult.update_forward_refs()
DescribeEgressOnlyInternetGatewaysRequest.update_forward_refs()
DescribeEgressOnlyInternetGatewaysResult.update_forward_refs()
DescribeElasticGpusRequest.update_forward_refs()
DescribeElasticGpusResult.update_forward_refs()
DescribeExportImageTasksRequest.update_forward_refs()
DescribeExportImageTasksResult.update_forward_refs()
DescribeExportTasksRequest.update_forward_refs()
DescribeExportTasksResult.update_forward_refs()
DescribeFastLaunchImagesRequest.update_forward_refs()
DescribeFastLaunchImagesResult.update_forward_refs()
DescribeFastLaunchImagesSuccessItem.update_forward_refs()
DescribeFastSnapshotRestoreSuccessItem.update_forward_refs()
DescribeFastSnapshotRestoresRequest.update_forward_refs()
DescribeFastSnapshotRestoresResult.update_forward_refs()
DescribeFleetError.update_forward_refs()
DescribeFleetHistoryRequest.update_forward_refs()
DescribeFleetHistoryResult.update_forward_refs()
DescribeFleetInstancesRequest.update_forward_refs()
DescribeFleetInstancesResult.update_forward_refs()
DescribeFleetsInstances.update_forward_refs()
DescribeFleetsRequest.update_forward_refs()
DescribeFleetsResult.update_forward_refs()
DescribeFlowLogsRequest.update_forward_refs()
DescribeFlowLogsResult.update_forward_refs()
DescribeFpgaImageAttributeRequest.update_forward_refs()
DescribeFpgaImageAttributeResult.update_forward_refs()
DescribeFpgaImagesRequest.update_forward_refs()
DescribeFpgaImagesResult.update_forward_refs()
DescribeHostReservationOfferingsRequest.update_forward_refs()
DescribeHostReservationOfferingsResult.update_forward_refs()
DescribeHostReservationsRequest.update_forward_refs()
DescribeHostReservationsResult.update_forward_refs()
DescribeHostsRequest.update_forward_refs()
DescribeHostsResult.update_forward_refs()
DescribeIamInstanceProfileAssociationsRequest.update_forward_refs()
DescribeIamInstanceProfileAssociationsResult.update_forward_refs()
DescribeIdFormatRequest.update_forward_refs()
DescribeIdFormatResult.update_forward_refs()
DescribeIdentityIdFormatRequest.update_forward_refs()
DescribeIdentityIdFormatResult.update_forward_refs()
DescribeImageAttributeRequest.update_forward_refs()
DescribeImagesRequest.update_forward_refs()
DescribeImagesResult.update_forward_refs()
DescribeImportImageTasksRequest.update_forward_refs()
DescribeImportImageTasksResult.update_forward_refs()
DescribeImportSnapshotTasksRequest.update_forward_refs()
DescribeImportSnapshotTasksResult.update_forward_refs()
DescribeInstanceAttributeRequest.update_forward_refs()
DescribeInstanceCreditSpecificationsRequest.update_forward_refs()
DescribeInstanceCreditSpecificationsResult.update_forward_refs()
DescribeInstanceEventNotificationAttributesRequest.update_forward_refs()
DescribeInstanceEventNotificationAttributesResult.update_forward_refs()
DescribeInstanceEventWindowsRequest.update_forward_refs()
DescribeInstanceEventWindowsResult.update_forward_refs()
DescribeInstanceStatusRequest.update_forward_refs()
DescribeInstanceStatusResult.update_forward_refs()
DescribeInstanceTypeOfferingsRequest.update_forward_refs()
DescribeInstanceTypeOfferingsResult.update_forward_refs()
DescribeInstanceTypesRequest.update_forward_refs()
DescribeInstanceTypesResult.update_forward_refs()
DescribeInstancesRequest.update_forward_refs()
DescribeInstancesResult.update_forward_refs()
DescribeInternetGatewaysRequest.update_forward_refs()
DescribeInternetGatewaysResult.update_forward_refs()
DescribeIpamPoolsRequest.update_forward_refs()
DescribeIpamPoolsResult.update_forward_refs()
DescribeIpamResourceDiscoveriesRequest.update_forward_refs()
DescribeIpamResourceDiscoveriesResult.update_forward_refs()
DescribeIpamResourceDiscoveryAssociationsRequest.update_forward_refs()
DescribeIpamResourceDiscoveryAssociationsResult.update_forward_refs()
DescribeIpamScopesRequest.update_forward_refs()
DescribeIpamScopesResult.update_forward_refs()
DescribeIpamsRequest.update_forward_refs()
DescribeIpamsResult.update_forward_refs()
DescribeIpv6PoolsRequest.update_forward_refs()
DescribeIpv6PoolsResult.update_forward_refs()
DescribeKeyPairsRequest.update_forward_refs()
DescribeKeyPairsResult.update_forward_refs()
DescribeLaunchTemplateVersionsRequest.update_forward_refs()
DescribeLaunchTemplateVersionsResult.update_forward_refs()
DescribeLaunchTemplatesRequest.update_forward_refs()
DescribeLaunchTemplatesResult.update_forward_refs()
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest.update_forward_refs()
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult.update_forward_refs()
DescribeLocalGatewayRouteTableVpcAssociationsRequest.update_forward_refs()
DescribeLocalGatewayRouteTableVpcAssociationsResult.update_forward_refs()
DescribeLocalGatewayRouteTablesRequest.update_forward_refs()
DescribeLocalGatewayRouteTablesResult.update_forward_refs()
DescribeLocalGatewayVirtualInterfaceGroupsRequest.update_forward_refs()
DescribeLocalGatewayVirtualInterfaceGroupsResult.update_forward_refs()
DescribeLocalGatewayVirtualInterfacesRequest.update_forward_refs()
DescribeLocalGatewayVirtualInterfacesResult.update_forward_refs()
DescribeLocalGatewaysRequest.update_forward_refs()
DescribeLocalGatewaysResult.update_forward_refs()
DescribeManagedPrefixListsRequest.update_forward_refs()
DescribeManagedPrefixListsResult.update_forward_refs()
DescribeMovingAddressesRequest.update_forward_refs()
DescribeMovingAddressesResult.update_forward_refs()
DescribeNatGatewaysRequest.update_forward_refs()
DescribeNatGatewaysResult.update_forward_refs()
DescribeNetworkAclsRequest.update_forward_refs()
DescribeNetworkAclsResult.update_forward_refs()
DescribeNetworkInsightsAccessScopeAnalysesRequest.update_forward_refs()
DescribeNetworkInsightsAccessScopeAnalysesResult.update_forward_refs()
DescribeNetworkInsightsAccessScopesRequest.update_forward_refs()
DescribeNetworkInsightsAccessScopesResult.update_forward_refs()
DescribeNetworkInsightsAnalysesRequest.update_forward_refs()
DescribeNetworkInsightsAnalysesResult.update_forward_refs()
DescribeNetworkInsightsPathsRequest.update_forward_refs()
DescribeNetworkInsightsPathsResult.update_forward_refs()
DescribeNetworkInterfaceAttributeRequest.update_forward_refs()
DescribeNetworkInterfaceAttributeResult.update_forward_refs()
DescribeNetworkInterfacePermissionsRequest.update_forward_refs()
DescribeNetworkInterfacePermissionsResult.update_forward_refs()
DescribeNetworkInterfacesRequest.update_forward_refs()
DescribeNetworkInterfacesResult.update_forward_refs()
DescribePlacementGroupsRequest.update_forward_refs()
DescribePlacementGroupsResult.update_forward_refs()
DescribePrefixListsRequest.update_forward_refs()
DescribePrefixListsResult.update_forward_refs()
DescribePrincipalIdFormatRequest.update_forward_refs()
DescribePrincipalIdFormatResult.update_forward_refs()
DescribePublicIpv4PoolsRequest.update_forward_refs()
DescribePublicIpv4PoolsResult.update_forward_refs()
DescribeRegionsRequest.update_forward_refs()
DescribeRegionsResult.update_forward_refs()
DescribeReplaceRootVolumeTasksRequest.update_forward_refs()
DescribeReplaceRootVolumeTasksResult.update_forward_refs()
DescribeReservedInstancesListingsRequest.update_forward_refs()
DescribeReservedInstancesListingsResult.update_forward_refs()
DescribeReservedInstancesModificationsRequest.update_forward_refs()
DescribeReservedInstancesModificationsResult.update_forward_refs()
DescribeReservedInstancesOfferingsRequest.update_forward_refs()
DescribeReservedInstancesOfferingsResult.update_forward_refs()
DescribeReservedInstancesRequest.update_forward_refs()
DescribeReservedInstancesResult.update_forward_refs()
DescribeRouteTablesRequest.update_forward_refs()
DescribeRouteTablesResult.update_forward_refs()
DescribeScheduledInstanceAvailabilityRequest.update_forward_refs()
DescribeScheduledInstanceAvailabilityResult.update_forward_refs()
DescribeScheduledInstancesRequest.update_forward_refs()
DescribeScheduledInstancesResult.update_forward_refs()
DescribeSecurityGroupReferencesRequest.update_forward_refs()
DescribeSecurityGroupReferencesResult.update_forward_refs()
DescribeSecurityGroupRulesRequest.update_forward_refs()
DescribeSecurityGroupRulesResult.update_forward_refs()
DescribeSecurityGroupsRequest.update_forward_refs()
DescribeSecurityGroupsResult.update_forward_refs()
DescribeSnapshotAttributeRequest.update_forward_refs()
DescribeSnapshotAttributeResult.update_forward_refs()
DescribeSnapshotTierStatusRequest.update_forward_refs()
DescribeSnapshotTierStatusResult.update_forward_refs()
DescribeSnapshotsRequest.update_forward_refs()
DescribeSnapshotsResult.update_forward_refs()
DescribeSpotDatafeedSubscriptionRequest.update_forward_refs()
DescribeSpotDatafeedSubscriptionResult.update_forward_refs()
DescribeSpotFleetInstancesRequest.update_forward_refs()
DescribeSpotFleetInstancesResponse.update_forward_refs()
DescribeSpotFleetRequestHistoryRequest.update_forward_refs()
DescribeSpotFleetRequestHistoryResponse.update_forward_refs()
DescribeSpotFleetRequestsRequest.update_forward_refs()
DescribeSpotFleetRequestsResponse.update_forward_refs()
DescribeSpotInstanceRequestsRequest.update_forward_refs()
DescribeSpotInstanceRequestsResult.update_forward_refs()
DescribeSpotPriceHistoryRequest.update_forward_refs()
DescribeSpotPriceHistoryResult.update_forward_refs()
DescribeStaleSecurityGroupsRequest.update_forward_refs()
DescribeStaleSecurityGroupsResult.update_forward_refs()
DescribeStoreImageTasksRequest.update_forward_refs()
DescribeStoreImageTasksResult.update_forward_refs()
DescribeSubnetsRequest.update_forward_refs()
DescribeSubnetsResult.update_forward_refs()
DescribeTagsRequest.update_forward_refs()
DescribeTagsResult.update_forward_refs()
DescribeTrafficMirrorFiltersRequest.update_forward_refs()
DescribeTrafficMirrorFiltersResult.update_forward_refs()
DescribeTrafficMirrorSessionsRequest.update_forward_refs()
DescribeTrafficMirrorSessionsResult.update_forward_refs()
DescribeTrafficMirrorTargetsRequest.update_forward_refs()
DescribeTrafficMirrorTargetsResult.update_forward_refs()
DescribeTransitGatewayAttachmentsRequest.update_forward_refs()
DescribeTransitGatewayAttachmentsResult.update_forward_refs()
DescribeTransitGatewayConnectPeersRequest.update_forward_refs()
DescribeTransitGatewayConnectPeersResult.update_forward_refs()
DescribeTransitGatewayConnectsRequest.update_forward_refs()
DescribeTransitGatewayConnectsResult.update_forward_refs()
DescribeTransitGatewayMulticastDomainsRequest.update_forward_refs()
DescribeTransitGatewayMulticastDomainsResult.update_forward_refs()
DescribeTransitGatewayPeeringAttachmentsRequest.update_forward_refs()
DescribeTransitGatewayPeeringAttachmentsResult.update_forward_refs()
DescribeTransitGatewayPolicyTablesRequest.update_forward_refs()
DescribeTransitGatewayPolicyTablesResult.update_forward_refs()
DescribeTransitGatewayRouteTableAnnouncementsRequest.update_forward_refs()
DescribeTransitGatewayRouteTableAnnouncementsResult.update_forward_refs()
DescribeTransitGatewayRouteTablesRequest.update_forward_refs()
DescribeTransitGatewayRouteTablesResult.update_forward_refs()
DescribeTransitGatewayVpcAttachmentsRequest.update_forward_refs()
DescribeTransitGatewayVpcAttachmentsResult.update_forward_refs()
DescribeTransitGatewaysRequest.update_forward_refs()
DescribeTransitGatewaysResult.update_forward_refs()
DescribeTrunkInterfaceAssociationsRequest.update_forward_refs()
DescribeTrunkInterfaceAssociationsResult.update_forward_refs()
DescribeVerifiedAccessEndpointsRequest.update_forward_refs()
DescribeVerifiedAccessEndpointsResult.update_forward_refs()
DescribeVerifiedAccessGroupsRequest.update_forward_refs()
DescribeVerifiedAccessGroupsResult.update_forward_refs()
DescribeVerifiedAccessInstanceLoggingConfigurationsRequest.update_forward_refs()
DescribeVerifiedAccessInstanceLoggingConfigurationsResult.update_forward_refs()
DescribeVerifiedAccessInstancesRequest.update_forward_refs()
DescribeVerifiedAccessInstancesResult.update_forward_refs()
DescribeVerifiedAccessTrustProvidersRequest.update_forward_refs()
DescribeVerifiedAccessTrustProvidersResult.update_forward_refs()
DescribeVolumeAttributeRequest.update_forward_refs()
DescribeVolumeAttributeResult.update_forward_refs()
DescribeVolumeStatusRequest.update_forward_refs()
DescribeVolumeStatusResult.update_forward_refs()
DescribeVolumesModificationsRequest.update_forward_refs()
DescribeVolumesModificationsResult.update_forward_refs()
DescribeVolumesRequest.update_forward_refs()
DescribeVolumesResult.update_forward_refs()
DescribeVpcAttributeRequest.update_forward_refs()
DescribeVpcAttributeResult.update_forward_refs()
DescribeVpcClassicLinkDnsSupportRequest.update_forward_refs()
DescribeVpcClassicLinkDnsSupportResult.update_forward_refs()
DescribeVpcClassicLinkRequest.update_forward_refs()
DescribeVpcClassicLinkResult.update_forward_refs()
DescribeVpcEndpointConnectionNotificationsRequest.update_forward_refs()
DescribeVpcEndpointConnectionNotificationsResult.update_forward_refs()
DescribeVpcEndpointConnectionsRequest.update_forward_refs()
DescribeVpcEndpointConnectionsResult.update_forward_refs()
DescribeVpcEndpointServiceConfigurationsRequest.update_forward_refs()
DescribeVpcEndpointServiceConfigurationsResult.update_forward_refs()
DescribeVpcEndpointServicePermissionsRequest.update_forward_refs()
DescribeVpcEndpointServicePermissionsResult.update_forward_refs()
DescribeVpcEndpointServicesRequest.update_forward_refs()
DescribeVpcEndpointServicesResult.update_forward_refs()
DescribeVpcEndpointsRequest.update_forward_refs()
DescribeVpcEndpointsResult.update_forward_refs()
DescribeVpcPeeringConnectionsRequest.update_forward_refs()
DescribeVpcPeeringConnectionsResult.update_forward_refs()
DescribeVpcsRequest.update_forward_refs()
DescribeVpcsResult.update_forward_refs()
DescribeVpnConnectionsRequest.update_forward_refs()
DescribeVpnConnectionsResult.update_forward_refs()
DescribeVpnGatewaysRequest.update_forward_refs()
DescribeVpnGatewaysResult.update_forward_refs()
DestinationOptionsRequest.update_forward_refs()
DestinationOptionsResponse.update_forward_refs()
DetachClassicLinkVpcRequest.update_forward_refs()
DetachClassicLinkVpcResult.update_forward_refs()
DetachInternetGatewayRequest.update_forward_refs()
DetachNetworkInterfaceRequest.update_forward_refs()
DetachVerifiedAccessTrustProviderRequest.update_forward_refs()
DetachVerifiedAccessTrustProviderResult.update_forward_refs()
DetachVolumeRequest.update_forward_refs()
DetachVpnGatewayRequest.update_forward_refs()
DeviceOptions.update_forward_refs()
DhcpConfiguration.update_forward_refs()
DhcpOptions.update_forward_refs()
DirectoryServiceAuthentication.update_forward_refs()
DirectoryServiceAuthenticationRequest.update_forward_refs()
DisableAddressTransferRequest.update_forward_refs()
DisableAddressTransferResult.update_forward_refs()
DisableAwsNetworkPerformanceMetricSubscriptionRequest.update_forward_refs()
DisableAwsNetworkPerformanceMetricSubscriptionResult.update_forward_refs()
DisableEbsEncryptionByDefaultRequest.update_forward_refs()
DisableEbsEncryptionByDefaultResult.update_forward_refs()
DisableFastLaunchRequest.update_forward_refs()
DisableFastLaunchResult.update_forward_refs()
DisableFastSnapshotRestoreErrorItem.update_forward_refs()
DisableFastSnapshotRestoreStateError.update_forward_refs()
DisableFastSnapshotRestoreStateErrorItem.update_forward_refs()
DisableFastSnapshotRestoreSuccessItem.update_forward_refs()
DisableFastSnapshotRestoresRequest.update_forward_refs()
DisableFastSnapshotRestoresResult.update_forward_refs()
DisableImageDeprecationRequest.update_forward_refs()
DisableImageDeprecationResult.update_forward_refs()
DisableIpamOrganizationAdminAccountRequest.update_forward_refs()
DisableIpamOrganizationAdminAccountResult.update_forward_refs()
DisableSerialConsoleAccessRequest.update_forward_refs()
DisableSerialConsoleAccessResult.update_forward_refs()
DisableTransitGatewayRouteTablePropagationRequest.update_forward_refs()
DisableTransitGatewayRouteTablePropagationResult.update_forward_refs()
DisableVgwRoutePropagationRequest.update_forward_refs()
DisableVpcClassicLinkDnsSupportRequest.update_forward_refs()
DisableVpcClassicLinkDnsSupportResult.update_forward_refs()
DisableVpcClassicLinkRequest.update_forward_refs()
DisableVpcClassicLinkResult.update_forward_refs()
DisassociateAddressRequest.update_forward_refs()
DisassociateClientVpnTargetNetworkRequest.update_forward_refs()
DisassociateClientVpnTargetNetworkResult.update_forward_refs()
DisassociateEnclaveCertificateIamRoleRequest.update_forward_refs()
DisassociateEnclaveCertificateIamRoleResult.update_forward_refs()
DisassociateIamInstanceProfileRequest.update_forward_refs()
DisassociateIamInstanceProfileResult.update_forward_refs()
DisassociateInstanceEventWindowRequest.update_forward_refs()
DisassociateInstanceEventWindowResult.update_forward_refs()
DisassociateIpamResourceDiscoveryRequest.update_forward_refs()
DisassociateIpamResourceDiscoveryResult.update_forward_refs()
DisassociateNatGatewayAddressRequest.update_forward_refs()
DisassociateNatGatewayAddressResult.update_forward_refs()
DisassociateRouteTableRequest.update_forward_refs()
DisassociateSubnetCidrBlockRequest.update_forward_refs()
DisassociateSubnetCidrBlockResult.update_forward_refs()
DisassociateTransitGatewayMulticastDomainRequest.update_forward_refs()
DisassociateTransitGatewayMulticastDomainResult.update_forward_refs()
DisassociateTransitGatewayPolicyTableRequest.update_forward_refs()
DisassociateTransitGatewayPolicyTableResult.update_forward_refs()
DisassociateTransitGatewayRouteTableRequest.update_forward_refs()
DisassociateTransitGatewayRouteTableResult.update_forward_refs()
DisassociateTrunkInterfaceRequest.update_forward_refs()
DisassociateTrunkInterfaceResult.update_forward_refs()
DisassociateVpcCidrBlockRequest.update_forward_refs()
DisassociateVpcCidrBlockResult.update_forward_refs()
DiskImage.update_forward_refs()
DiskImageDescription.update_forward_refs()
DiskImageDetail.update_forward_refs()
DiskImageVolumeDescription.update_forward_refs()
DiskInfo.update_forward_refs()
DnsEntry.update_forward_refs()
DnsOptions.update_forward_refs()
DnsOptionsSpecification.update_forward_refs()
DnsServersOptionsModifyStructure.update_forward_refs()
EbsBlockDevice.update_forward_refs()
EbsInfo.update_forward_refs()
EbsInstanceBlockDevice.update_forward_refs()
EbsInstanceBlockDeviceSpecification.update_forward_refs()
EbsOptimizedInfo.update_forward_refs()
EfaInfo.update_forward_refs()
EgressOnlyInternetGateway.update_forward_refs()
ElasticGpuAssociation.update_forward_refs()
ElasticGpuHealth.update_forward_refs()
ElasticGpuSpecification.update_forward_refs()
ElasticGpuSpecificationResponse.update_forward_refs()
ElasticGpus.update_forward_refs()
ElasticInferenceAccelerator.update_forward_refs()
ElasticInferenceAcceleratorAssociation.update_forward_refs()
EnaSrdSpecification.update_forward_refs()
EnaSrdUdpSpecification.update_forward_refs()
EnableAddressTransferRequest.update_forward_refs()
EnableAddressTransferResult.update_forward_refs()
EnableAwsNetworkPerformanceMetricSubscriptionRequest.update_forward_refs()
EnableAwsNetworkPerformanceMetricSubscriptionResult.update_forward_refs()
EnableEbsEncryptionByDefaultRequest.update_forward_refs()
EnableEbsEncryptionByDefaultResult.update_forward_refs()
EnableFastLaunchRequest.update_forward_refs()
EnableFastLaunchResult.update_forward_refs()
EnableFastSnapshotRestoreErrorItem.update_forward_refs()
EnableFastSnapshotRestoreStateError.update_forward_refs()
EnableFastSnapshotRestoreStateErrorItem.update_forward_refs()
EnableFastSnapshotRestoreSuccessItem.update_forward_refs()
EnableFastSnapshotRestoresRequest.update_forward_refs()
EnableFastSnapshotRestoresResult.update_forward_refs()
EnableImageDeprecationRequest.update_forward_refs()
EnableImageDeprecationResult.update_forward_refs()
EnableIpamOrganizationAdminAccountRequest.update_forward_refs()
EnableIpamOrganizationAdminAccountResult.update_forward_refs()
EnableReachabilityAnalyzerOrganizationSharingRequest.update_forward_refs()
EnableReachabilityAnalyzerOrganizationSharingResult.update_forward_refs()
EnableSerialConsoleAccessRequest.update_forward_refs()
EnableSerialConsoleAccessResult.update_forward_refs()
EnableTransitGatewayRouteTablePropagationRequest.update_forward_refs()
EnableTransitGatewayRouteTablePropagationResult.update_forward_refs()
EnableVgwRoutePropagationRequest.update_forward_refs()
EnableVolumeIORequest.update_forward_refs()
EnableVpcClassicLinkDnsSupportRequest.update_forward_refs()
EnableVpcClassicLinkDnsSupportResult.update_forward_refs()
EnableVpcClassicLinkRequest.update_forward_refs()
EnableVpcClassicLinkResult.update_forward_refs()
EnclaveOptions.update_forward_refs()
EnclaveOptionsRequest.update_forward_refs()
EventInformation.update_forward_refs()
Explanation.update_forward_refs()
ExportClientVpnClientCertificateRevocationListRequest.update_forward_refs()
ExportClientVpnClientCertificateRevocationListResult.update_forward_refs()
ExportClientVpnClientConfigurationRequest.update_forward_refs()
ExportClientVpnClientConfigurationResult.update_forward_refs()
ExportImageRequest.update_forward_refs()
ExportImageResult.update_forward_refs()
ExportImageTask.update_forward_refs()
ExportTask.update_forward_refs()
ExportTaskS3Location.update_forward_refs()
ExportTaskS3LocationRequest.update_forward_refs()
ExportToS3Task.update_forward_refs()
ExportToS3TaskSpecification.update_forward_refs()
ExportTransitGatewayRoutesRequest.update_forward_refs()
ExportTransitGatewayRoutesResult.update_forward_refs()
FailedCapacityReservationFleetCancellationResult.update_forward_refs()
FailedQueuedPurchaseDeletion.update_forward_refs()
FastLaunchLaunchTemplateSpecificationRequest.update_forward_refs()
FastLaunchLaunchTemplateSpecificationResponse.update_forward_refs()
FastLaunchSnapshotConfigurationRequest.update_forward_refs()
FastLaunchSnapshotConfigurationResponse.update_forward_refs()
FederatedAuthentication.update_forward_refs()
FederatedAuthenticationRequest.update_forward_refs()
Filter.update_forward_refs()
FilterPortRange.update_forward_refs()
FirewallStatefulRule.update_forward_refs()
FirewallStatelessRule.update_forward_refs()
FleetCapacityReservation.update_forward_refs()
FleetData.update_forward_refs()
FleetLaunchTemplateConfig.update_forward_refs()
FleetLaunchTemplateConfigRequest.update_forward_refs()
FleetLaunchTemplateOverrides.update_forward_refs()
FleetLaunchTemplateOverridesRequest.update_forward_refs()
FleetLaunchTemplateSpecification.update_forward_refs()
FleetLaunchTemplateSpecificationRequest.update_forward_refs()
FleetSpotCapacityRebalance.update_forward_refs()
FleetSpotCapacityRebalanceRequest.update_forward_refs()
FleetSpotMaintenanceStrategies.update_forward_refs()
FleetSpotMaintenanceStrategiesRequest.update_forward_refs()
FlowLog.update_forward_refs()
FpgaDeviceInfo.update_forward_refs()
FpgaDeviceMemoryInfo.update_forward_refs()
FpgaImage.update_forward_refs()
FpgaImageAttribute.update_forward_refs()
FpgaImageState.update_forward_refs()
FpgaInfo.update_forward_refs()
GetAssociatedEnclaveCertificateIamRolesRequest.update_forward_refs()
GetAssociatedEnclaveCertificateIamRolesResult.update_forward_refs()
GetAssociatedIpv6PoolCidrsRequest.update_forward_refs()
GetAssociatedIpv6PoolCidrsResult.update_forward_refs()
GetAwsNetworkPerformanceDataRequest.update_forward_refs()
GetAwsNetworkPerformanceDataResult.update_forward_refs()
GetCapacityReservationUsageRequest.update_forward_refs()
GetCapacityReservationUsageResult.update_forward_refs()
GetCoipPoolUsageRequest.update_forward_refs()
GetCoipPoolUsageResult.update_forward_refs()
GetConsoleOutputRequest.update_forward_refs()
GetConsoleOutputResult.update_forward_refs()
GetConsoleScreenshotRequest.update_forward_refs()
GetConsoleScreenshotResult.update_forward_refs()
GetDefaultCreditSpecificationRequest.update_forward_refs()
GetDefaultCreditSpecificationResult.update_forward_refs()
GetEbsDefaultKmsKeyIdRequest.update_forward_refs()
GetEbsDefaultKmsKeyIdResult.update_forward_refs()
GetEbsEncryptionByDefaultRequest.update_forward_refs()
GetEbsEncryptionByDefaultResult.update_forward_refs()
GetFlowLogsIntegrationTemplateRequest.update_forward_refs()
GetFlowLogsIntegrationTemplateResult.update_forward_refs()
GetGroupsForCapacityReservationRequest.update_forward_refs()
GetGroupsForCapacityReservationResult.update_forward_refs()
GetHostReservationPurchasePreviewRequest.update_forward_refs()
GetHostReservationPurchasePreviewResult.update_forward_refs()
GetInstanceTypesFromInstanceRequirementsRequest.update_forward_refs()
GetInstanceTypesFromInstanceRequirementsResult.update_forward_refs()
GetInstanceUefiDataRequest.update_forward_refs()
GetInstanceUefiDataResult.update_forward_refs()
GetIpamAddressHistoryRequest.update_forward_refs()
GetIpamAddressHistoryResult.update_forward_refs()
GetIpamDiscoveredAccountsRequest.update_forward_refs()
GetIpamDiscoveredAccountsResult.update_forward_refs()
GetIpamDiscoveredResourceCidrsRequest.update_forward_refs()
GetIpamDiscoveredResourceCidrsResult.update_forward_refs()
GetIpamPoolAllocationsRequest.update_forward_refs()
GetIpamPoolAllocationsResult.update_forward_refs()
GetIpamPoolCidrsRequest.update_forward_refs()
GetIpamPoolCidrsResult.update_forward_refs()
GetIpamResourceCidrsRequest.update_forward_refs()
GetIpamResourceCidrsResult.update_forward_refs()
GetLaunchTemplateDataRequest.update_forward_refs()
GetLaunchTemplateDataResult.update_forward_refs()
GetManagedPrefixListAssociationsRequest.update_forward_refs()
GetManagedPrefixListAssociationsResult.update_forward_refs()
GetManagedPrefixListEntriesRequest.update_forward_refs()
GetManagedPrefixListEntriesResult.update_forward_refs()
GetNetworkInsightsAccessScopeAnalysisFindingsRequest.update_forward_refs()
GetNetworkInsightsAccessScopeAnalysisFindingsResult.update_forward_refs()
GetNetworkInsightsAccessScopeContentRequest.update_forward_refs()
GetNetworkInsightsAccessScopeContentResult.update_forward_refs()
GetPasswordDataRequest.update_forward_refs()
GetPasswordDataResult.update_forward_refs()
GetReservedInstancesExchangeQuoteRequest.update_forward_refs()
GetReservedInstancesExchangeQuoteResult.update_forward_refs()
GetSerialConsoleAccessStatusRequest.update_forward_refs()
GetSerialConsoleAccessStatusResult.update_forward_refs()
GetSpotPlacementScoresRequest.update_forward_refs()
GetSpotPlacementScoresResult.update_forward_refs()
GetSubnetCidrReservationsRequest.update_forward_refs()
GetSubnetCidrReservationsResult.update_forward_refs()
GetTransitGatewayAttachmentPropagationsRequest.update_forward_refs()
GetTransitGatewayAttachmentPropagationsResult.update_forward_refs()
GetTransitGatewayMulticastDomainAssociationsRequest.update_forward_refs()
GetTransitGatewayMulticastDomainAssociationsResult.update_forward_refs()
GetTransitGatewayPolicyTableAssociationsRequest.update_forward_refs()
GetTransitGatewayPolicyTableAssociationsResult.update_forward_refs()
GetTransitGatewayPolicyTableEntriesRequest.update_forward_refs()
GetTransitGatewayPolicyTableEntriesResult.update_forward_refs()
GetTransitGatewayPrefixListReferencesRequest.update_forward_refs()
GetTransitGatewayPrefixListReferencesResult.update_forward_refs()
GetTransitGatewayRouteTableAssociationsRequest.update_forward_refs()
GetTransitGatewayRouteTableAssociationsResult.update_forward_refs()
GetTransitGatewayRouteTablePropagationsRequest.update_forward_refs()
GetTransitGatewayRouteTablePropagationsResult.update_forward_refs()
GetVerifiedAccessEndpointPolicyRequest.update_forward_refs()
GetVerifiedAccessEndpointPolicyResult.update_forward_refs()
GetVerifiedAccessGroupPolicyRequest.update_forward_refs()
GetVerifiedAccessGroupPolicyResult.update_forward_refs()
GetVpnConnectionDeviceSampleConfigurationRequest.update_forward_refs()
GetVpnConnectionDeviceSampleConfigurationResult.update_forward_refs()
GetVpnConnectionDeviceTypesRequest.update_forward_refs()
GetVpnConnectionDeviceTypesResult.update_forward_refs()
GetVpnTunnelReplacementStatusRequest.update_forward_refs()
GetVpnTunnelReplacementStatusResult.update_forward_refs()
GpuDeviceInfo.update_forward_refs()
GpuDeviceMemoryInfo.update_forward_refs()
GpuInfo.update_forward_refs()
GroupIdentifier.update_forward_refs()
HibernationOptions.update_forward_refs()
HibernationOptionsRequest.update_forward_refs()
HistoryRecord.update_forward_refs()
HistoryRecordEntry.update_forward_refs()
Host.update_forward_refs()
HostInstance.update_forward_refs()
HostOffering.update_forward_refs()
HostProperties.update_forward_refs()
HostReservation.update_forward_refs()
IKEVersionsListValue.update_forward_refs()
IKEVersionsRequestListValue.update_forward_refs()
IamInstanceProfile.update_forward_refs()
IamInstanceProfileAssociation.update_forward_refs()
IamInstanceProfileSpecification.update_forward_refs()
IcmpTypeCode.update_forward_refs()
IdFormat.update_forward_refs()
Image.update_forward_refs()
ImageAttribute.update_forward_refs()
ImageDiskContainer.update_forward_refs()
ImageRecycleBinInfo.update_forward_refs()
ImportClientVpnClientCertificateRevocationListRequest.update_forward_refs()
ImportClientVpnClientCertificateRevocationListResult.update_forward_refs()
ImportImageLicenseConfigurationRequest.update_forward_refs()
ImportImageLicenseConfigurationResponse.update_forward_refs()
ImportImageRequest.update_forward_refs()
ImportImageResult.update_forward_refs()
ImportImageTask.update_forward_refs()
ImportInstanceLaunchSpecification.update_forward_refs()
ImportInstanceRequest.update_forward_refs()
ImportInstanceResult.update_forward_refs()
ImportInstanceTaskDetails.update_forward_refs()
ImportInstanceVolumeDetailItem.update_forward_refs()
ImportKeyPairRequest.update_forward_refs()
ImportKeyPairResult.update_forward_refs()
ImportSnapshotRequest.update_forward_refs()
ImportSnapshotResult.update_forward_refs()
ImportSnapshotTask.update_forward_refs()
ImportVolumeRequest.update_forward_refs()
ImportVolumeResult.update_forward_refs()
ImportVolumeTaskDetails.update_forward_refs()
InferenceAcceleratorInfo.update_forward_refs()
InferenceDeviceInfo.update_forward_refs()
Instance.update_forward_refs()
InstanceAttribute.update_forward_refs()
InstanceBlockDeviceMapping.update_forward_refs()
InstanceBlockDeviceMappingSpecification.update_forward_refs()
InstanceCapacity.update_forward_refs()
InstanceCount.update_forward_refs()
InstanceCreditSpecification.update_forward_refs()
InstanceCreditSpecificationRequest.update_forward_refs()
InstanceEventWindow.update_forward_refs()
InstanceEventWindowAssociationRequest.update_forward_refs()
InstanceEventWindowAssociationTarget.update_forward_refs()
InstanceEventWindowDisassociationRequest.update_forward_refs()
InstanceEventWindowStateChange.update_forward_refs()
InstanceEventWindowTimeRange.update_forward_refs()
InstanceEventWindowTimeRangeRequest.update_forward_refs()
InstanceExportDetails.update_forward_refs()
InstanceFamilyCreditSpecification.update_forward_refs()
InstanceIpv4Prefix.update_forward_refs()
InstanceIpv6Address.update_forward_refs()
InstanceIpv6AddressRequest.update_forward_refs()
InstanceIpv6Prefix.update_forward_refs()
InstanceMaintenanceOptions.update_forward_refs()
InstanceMaintenanceOptionsRequest.update_forward_refs()
InstanceMarketOptionsRequest.update_forward_refs()
InstanceMetadataOptionsRequest.update_forward_refs()
InstanceMetadataOptionsResponse.update_forward_refs()
InstanceMonitoring.update_forward_refs()
InstanceNetworkInterface.update_forward_refs()
InstanceNetworkInterfaceAssociation.update_forward_refs()
InstanceNetworkInterfaceAttachment.update_forward_refs()
InstanceNetworkInterfaceSpecification.update_forward_refs()
InstancePrivateIpAddress.update_forward_refs()
InstanceRequirements.update_forward_refs()
InstanceRequirementsRequest.update_forward_refs()
InstanceRequirementsWithMetadataRequest.update_forward_refs()
InstanceSpecification.update_forward_refs()
InstanceState.update_forward_refs()
InstanceStateChange.update_forward_refs()
InstanceStatus.update_forward_refs()
InstanceStatusDetails.update_forward_refs()
InstanceStatusEvent.update_forward_refs()
InstanceStatusSummary.update_forward_refs()
InstanceStorageInfo.update_forward_refs()
InstanceTagNotificationAttribute.update_forward_refs()
InstanceTypeInfo.update_forward_refs()
InstanceTypeInfoFromInstanceRequirements.update_forward_refs()
InstanceTypeOffering.update_forward_refs()
InstanceUsage.update_forward_refs()
IntegrateServices.update_forward_refs()
InternetGateway.update_forward_refs()
InternetGatewayAttachment.update_forward_refs()
IpPermission.update_forward_refs()
IpRange.update_forward_refs()
Ipam.update_forward_refs()
IpamAddressHistoryRecord.update_forward_refs()
IpamCidrAuthorizationContext.update_forward_refs()
IpamDiscoveredAccount.update_forward_refs()
IpamDiscoveredResourceCidr.update_forward_refs()
IpamDiscoveryFailureReason.update_forward_refs()
IpamOperatingRegion.update_forward_refs()
IpamPool.update_forward_refs()
IpamPoolAllocation.update_forward_refs()
IpamPoolCidr.update_forward_refs()
IpamPoolCidrFailureReason.update_forward_refs()
IpamResourceCidr.update_forward_refs()
IpamResourceDiscovery.update_forward_refs()
IpamResourceDiscoveryAssociation.update_forward_refs()
IpamResourceTag.update_forward_refs()
IpamScope.update_forward_refs()
Ipv4PrefixSpecification.update_forward_refs()
Ipv4PrefixSpecificationRequest.update_forward_refs()
Ipv4PrefixSpecificationResponse.update_forward_refs()
Ipv6CidrAssociation.update_forward_refs()
Ipv6CidrBlock.update_forward_refs()
Ipv6Pool.update_forward_refs()
Ipv6PrefixSpecification.update_forward_refs()
Ipv6PrefixSpecificationRequest.update_forward_refs()
Ipv6PrefixSpecificationResponse.update_forward_refs()
Ipv6Range.update_forward_refs()
KeyPair.update_forward_refs()
KeyPairInfo.update_forward_refs()
LastError.update_forward_refs()
LaunchPermission.update_forward_refs()
LaunchPermissionModifications.update_forward_refs()
LaunchSpecification.update_forward_refs()
LaunchTemplate.update_forward_refs()
LaunchTemplateAndOverridesResponse.update_forward_refs()
LaunchTemplateBlockDeviceMapping.update_forward_refs()
LaunchTemplateBlockDeviceMappingRequest.update_forward_refs()
LaunchTemplateCapacityReservationSpecificationRequest.update_forward_refs()
LaunchTemplateCapacityReservationSpecificationResponse.update_forward_refs()
LaunchTemplateConfig.update_forward_refs()
LaunchTemplateCpuOptions.update_forward_refs()
LaunchTemplateCpuOptionsRequest.update_forward_refs()
LaunchTemplateEbsBlockDevice.update_forward_refs()
LaunchTemplateEbsBlockDeviceRequest.update_forward_refs()
LaunchTemplateElasticInferenceAccelerator.update_forward_refs()
LaunchTemplateElasticInferenceAcceleratorResponse.update_forward_refs()
LaunchTemplateEnclaveOptions.update_forward_refs()
LaunchTemplateEnclaveOptionsRequest.update_forward_refs()
LaunchTemplateHibernationOptions.update_forward_refs()
LaunchTemplateHibernationOptionsRequest.update_forward_refs()
LaunchTemplateIamInstanceProfileSpecification.update_forward_refs()
LaunchTemplateIamInstanceProfileSpecificationRequest.update_forward_refs()
LaunchTemplateInstanceMaintenanceOptions.update_forward_refs()
LaunchTemplateInstanceMaintenanceOptionsRequest.update_forward_refs()
LaunchTemplateInstanceMarketOptions.update_forward_refs()
LaunchTemplateInstanceMarketOptionsRequest.update_forward_refs()
LaunchTemplateInstanceMetadataOptions.update_forward_refs()
LaunchTemplateInstanceMetadataOptionsRequest.update_forward_refs()
LaunchTemplateInstanceNetworkInterfaceSpecification.update_forward_refs()
LaunchTemplateInstanceNetworkInterfaceSpecificationRequest.update_forward_refs()
LaunchTemplateLicenseConfiguration.update_forward_refs()
LaunchTemplateLicenseConfigurationRequest.update_forward_refs()
LaunchTemplateOverrides.update_forward_refs()
LaunchTemplatePlacement.update_forward_refs()
LaunchTemplatePlacementRequest.update_forward_refs()
LaunchTemplatePrivateDnsNameOptions.update_forward_refs()
LaunchTemplatePrivateDnsNameOptionsRequest.update_forward_refs()
LaunchTemplateSpecification.update_forward_refs()
LaunchTemplateSpotMarketOptions.update_forward_refs()
LaunchTemplateSpotMarketOptionsRequest.update_forward_refs()
LaunchTemplateTagSpecification.update_forward_refs()
LaunchTemplateTagSpecificationRequest.update_forward_refs()
LaunchTemplateVersion.update_forward_refs()
LaunchTemplatesMonitoring.update_forward_refs()
LaunchTemplatesMonitoringRequest.update_forward_refs()
LicenseConfiguration.update_forward_refs()
LicenseConfigurationRequest.update_forward_refs()
ListImagesInRecycleBinRequest.update_forward_refs()
ListImagesInRecycleBinResult.update_forward_refs()
ListSnapshotsInRecycleBinRequest.update_forward_refs()
ListSnapshotsInRecycleBinResult.update_forward_refs()
LoadBalancersConfig.update_forward_refs()
LoadPermission.update_forward_refs()
LoadPermissionModifications.update_forward_refs()
LoadPermissionRequest.update_forward_refs()
LocalGateway.update_forward_refs()
LocalGatewayRoute.update_forward_refs()
LocalGatewayRouteTable.update_forward_refs()
LocalGatewayRouteTableVirtualInterfaceGroupAssociation.update_forward_refs()
LocalGatewayRouteTableVpcAssociation.update_forward_refs()
LocalGatewayVirtualInterface.update_forward_refs()
LocalGatewayVirtualInterfaceGroup.update_forward_refs()
MaintenanceDetails.update_forward_refs()
ManagedPrefixList.update_forward_refs()
MemoryGiBPerVCpu.update_forward_refs()
MemoryGiBPerVCpuRequest.update_forward_refs()
MemoryInfo.update_forward_refs()
MemoryMiB.update_forward_refs()
MemoryMiBRequest.update_forward_refs()
MetricPoint.update_forward_refs()
ModifyAddressAttributeRequest.update_forward_refs()
ModifyAddressAttributeResult.update_forward_refs()
ModifyAvailabilityZoneGroupRequest.update_forward_refs()
ModifyAvailabilityZoneGroupResult.update_forward_refs()
ModifyCapacityReservationFleetRequest.update_forward_refs()
ModifyCapacityReservationFleetResult.update_forward_refs()
ModifyCapacityReservationRequest.update_forward_refs()
ModifyCapacityReservationResult.update_forward_refs()
ModifyClientVpnEndpointRequest.update_forward_refs()
ModifyClientVpnEndpointResult.update_forward_refs()
ModifyDefaultCreditSpecificationRequest.update_forward_refs()
ModifyDefaultCreditSpecificationResult.update_forward_refs()
ModifyEbsDefaultKmsKeyIdRequest.update_forward_refs()
ModifyEbsDefaultKmsKeyIdResult.update_forward_refs()
ModifyFleetRequest.update_forward_refs()
ModifyFleetResult.update_forward_refs()
ModifyFpgaImageAttributeRequest.update_forward_refs()
ModifyFpgaImageAttributeResult.update_forward_refs()
ModifyHostsRequest.update_forward_refs()
ModifyHostsResult.update_forward_refs()
ModifyIdFormatRequest.update_forward_refs()
ModifyIdentityIdFormatRequest.update_forward_refs()
ModifyImageAttributeRequest.update_forward_refs()
ModifyInstanceAttributeRequest.update_forward_refs()
ModifyInstanceCapacityReservationAttributesRequest.update_forward_refs()
ModifyInstanceCapacityReservationAttributesResult.update_forward_refs()
ModifyInstanceCreditSpecificationRequest.update_forward_refs()
ModifyInstanceCreditSpecificationResult.update_forward_refs()
ModifyInstanceEventStartTimeRequest.update_forward_refs()
ModifyInstanceEventStartTimeResult.update_forward_refs()
ModifyInstanceEventWindowRequest.update_forward_refs()
ModifyInstanceEventWindowResult.update_forward_refs()
ModifyInstanceMaintenanceOptionsRequest.update_forward_refs()
ModifyInstanceMaintenanceOptionsResult.update_forward_refs()
ModifyInstanceMetadataOptionsRequest.update_forward_refs()
ModifyInstanceMetadataOptionsResult.update_forward_refs()
ModifyInstancePlacementRequest.update_forward_refs()
ModifyInstancePlacementResult.update_forward_refs()
ModifyIpamPoolRequest.update_forward_refs()
ModifyIpamPoolResult.update_forward_refs()
ModifyIpamRequest.update_forward_refs()
ModifyIpamResourceCidrRequest.update_forward_refs()
ModifyIpamResourceCidrResult.update_forward_refs()
ModifyIpamResourceDiscoveryRequest.update_forward_refs()
ModifyIpamResourceDiscoveryResult.update_forward_refs()
ModifyIpamResult.update_forward_refs()
ModifyIpamScopeRequest.update_forward_refs()
ModifyIpamScopeResult.update_forward_refs()
ModifyLaunchTemplateRequest.update_forward_refs()
ModifyLaunchTemplateResult.update_forward_refs()
ModifyLocalGatewayRouteRequest.update_forward_refs()
ModifyLocalGatewayRouteResult.update_forward_refs()
ModifyManagedPrefixListRequest.update_forward_refs()
ModifyManagedPrefixListResult.update_forward_refs()
ModifyNetworkInterfaceAttributeRequest.update_forward_refs()
ModifyPrivateDnsNameOptionsRequest.update_forward_refs()
ModifyPrivateDnsNameOptionsResult.update_forward_refs()
ModifyReservedInstancesRequest.update_forward_refs()
ModifyReservedInstancesResult.update_forward_refs()
ModifySecurityGroupRulesRequest.update_forward_refs()
ModifySecurityGroupRulesResult.update_forward_refs()
ModifySnapshotAttributeRequest.update_forward_refs()
ModifySnapshotTierRequest.update_forward_refs()
ModifySnapshotTierResult.update_forward_refs()
ModifySpotFleetRequestRequest.update_forward_refs()
ModifySpotFleetRequestResponse.update_forward_refs()
ModifySubnetAttributeRequest.update_forward_refs()
ModifyTrafficMirrorFilterNetworkServicesRequest.update_forward_refs()
ModifyTrafficMirrorFilterNetworkServicesResult.update_forward_refs()
ModifyTrafficMirrorFilterRuleRequest.update_forward_refs()
ModifyTrafficMirrorFilterRuleResult.update_forward_refs()
ModifyTrafficMirrorSessionRequest.update_forward_refs()
ModifyTrafficMirrorSessionResult.update_forward_refs()
ModifyTransitGatewayOptions.update_forward_refs()
ModifyTransitGatewayPrefixListReferenceRequest.update_forward_refs()
ModifyTransitGatewayPrefixListReferenceResult.update_forward_refs()
ModifyTransitGatewayRequest.update_forward_refs()
ModifyTransitGatewayResult.update_forward_refs()
ModifyTransitGatewayVpcAttachmentRequest.update_forward_refs()
ModifyTransitGatewayVpcAttachmentRequestOptions.update_forward_refs()
ModifyTransitGatewayVpcAttachmentResult.update_forward_refs()
ModifyVerifiedAccessEndpointEniOptions.update_forward_refs()
ModifyVerifiedAccessEndpointLoadBalancerOptions.update_forward_refs()
ModifyVerifiedAccessEndpointPolicyRequest.update_forward_refs()
ModifyVerifiedAccessEndpointPolicyResult.update_forward_refs()
ModifyVerifiedAccessEndpointRequest.update_forward_refs()
ModifyVerifiedAccessEndpointResult.update_forward_refs()
ModifyVerifiedAccessGroupPolicyRequest.update_forward_refs()
ModifyVerifiedAccessGroupPolicyResult.update_forward_refs()
ModifyVerifiedAccessGroupRequest.update_forward_refs()
ModifyVerifiedAccessGroupResult.update_forward_refs()
ModifyVerifiedAccessInstanceLoggingConfigurationRequest.update_forward_refs()
ModifyVerifiedAccessInstanceLoggingConfigurationResult.update_forward_refs()
ModifyVerifiedAccessInstanceRequest.update_forward_refs()
ModifyVerifiedAccessInstanceResult.update_forward_refs()
ModifyVerifiedAccessTrustProviderOidcOptions.update_forward_refs()
ModifyVerifiedAccessTrustProviderRequest.update_forward_refs()
ModifyVerifiedAccessTrustProviderResult.update_forward_refs()
ModifyVolumeAttributeRequest.update_forward_refs()
ModifyVolumeRequest.update_forward_refs()
ModifyVolumeResult.update_forward_refs()
ModifyVpcAttributeRequest.update_forward_refs()
ModifyVpcEndpointConnectionNotificationRequest.update_forward_refs()
ModifyVpcEndpointConnectionNotificationResult.update_forward_refs()
ModifyVpcEndpointRequest.update_forward_refs()
ModifyVpcEndpointResult.update_forward_refs()
ModifyVpcEndpointServiceConfigurationRequest.update_forward_refs()
ModifyVpcEndpointServiceConfigurationResult.update_forward_refs()
ModifyVpcEndpointServicePayerResponsibilityRequest.update_forward_refs()
ModifyVpcEndpointServicePayerResponsibilityResult.update_forward_refs()
ModifyVpcEndpointServicePermissionsRequest.update_forward_refs()
ModifyVpcEndpointServicePermissionsResult.update_forward_refs()
ModifyVpcPeeringConnectionOptionsRequest.update_forward_refs()
ModifyVpcPeeringConnectionOptionsResult.update_forward_refs()
ModifyVpcTenancyRequest.update_forward_refs()
ModifyVpcTenancyResult.update_forward_refs()
ModifyVpnConnectionOptionsRequest.update_forward_refs()
ModifyVpnConnectionOptionsResult.update_forward_refs()
ModifyVpnConnectionRequest.update_forward_refs()
ModifyVpnConnectionResult.update_forward_refs()
ModifyVpnTunnelCertificateRequest.update_forward_refs()
ModifyVpnTunnelCertificateResult.update_forward_refs()
ModifyVpnTunnelOptionsRequest.update_forward_refs()
ModifyVpnTunnelOptionsResult.update_forward_refs()
ModifyVpnTunnelOptionsSpecification.update_forward_refs()
MonitorInstancesRequest.update_forward_refs()
MonitorInstancesResult.update_forward_refs()
Monitoring.update_forward_refs()
MoveAddressToVpcRequest.update_forward_refs()
MoveAddressToVpcResult.update_forward_refs()
MoveByoipCidrToIpamRequest.update_forward_refs()
MoveByoipCidrToIpamResult.update_forward_refs()
MovingAddressStatus.update_forward_refs()
NatGateway.update_forward_refs()
NatGatewayAddress.update_forward_refs()
NetworkAcl.update_forward_refs()
NetworkAclAssociation.update_forward_refs()
NetworkAclEntry.update_forward_refs()
NetworkBandwidthGbps.update_forward_refs()
NetworkBandwidthGbpsRequest.update_forward_refs()
NetworkCardInfo.update_forward_refs()
NetworkInfo.update_forward_refs()
NetworkInsightsAccessScope.update_forward_refs()
NetworkInsightsAccessScopeAnalysis.update_forward_refs()
NetworkInsightsAccessScopeContent.update_forward_refs()
NetworkInsightsAnalysis.update_forward_refs()
NetworkInsightsPath.update_forward_refs()
NetworkInterface.update_forward_refs()
NetworkInterfaceAssociation.update_forward_refs()
NetworkInterfaceAttachment.update_forward_refs()
NetworkInterfaceAttachmentChanges.update_forward_refs()
NetworkInterfaceCount.update_forward_refs()
NetworkInterfaceCountRequest.update_forward_refs()
NetworkInterfaceIpv6Address.update_forward_refs()
NetworkInterfacePermission.update_forward_refs()
NetworkInterfacePermissionState.update_forward_refs()
NetworkInterfacePrivateIpAddress.update_forward_refs()
NewDhcpConfiguration.update_forward_refs()
OidcOptions.update_forward_refs()
OnDemandOptions.update_forward_refs()
OnDemandOptionsRequest.update_forward_refs()
PacketHeaderStatement.update_forward_refs()
PacketHeaderStatementRequest.update_forward_refs()
PathComponent.update_forward_refs()
PathFilter.update_forward_refs()
PathRequestFilter.update_forward_refs()
PathStatement.update_forward_refs()
PathStatementRequest.update_forward_refs()
PciId.update_forward_refs()
PeeringAttachmentStatus.update_forward_refs()
PeeringConnectionOptions.update_forward_refs()
PeeringConnectionOptionsRequest.update_forward_refs()
PeeringTgwInfo.update_forward_refs()
Phase1DHGroupNumbersListValue.update_forward_refs()
Phase1DHGroupNumbersRequestListValue.update_forward_refs()
Phase1EncryptionAlgorithmsListValue.update_forward_refs()
Phase1EncryptionAlgorithmsRequestListValue.update_forward_refs()
Phase1IntegrityAlgorithmsListValue.update_forward_refs()
Phase1IntegrityAlgorithmsRequestListValue.update_forward_refs()
Phase2DHGroupNumbersListValue.update_forward_refs()
Phase2DHGroupNumbersRequestListValue.update_forward_refs()
Phase2EncryptionAlgorithmsListValue.update_forward_refs()
Phase2EncryptionAlgorithmsRequestListValue.update_forward_refs()
Phase2IntegrityAlgorithmsListValue.update_forward_refs()
Phase2IntegrityAlgorithmsRequestListValue.update_forward_refs()
Placement.update_forward_refs()
PlacementGroup.update_forward_refs()
PlacementGroupInfo.update_forward_refs()
PlacementResponse.update_forward_refs()
PoolCidrBlock.update_forward_refs()
PortRange.update_forward_refs()
PrefixList.update_forward_refs()
PrefixListAssociation.update_forward_refs()
PrefixListEntry.update_forward_refs()
PrefixListId.update_forward_refs()
PriceSchedule.update_forward_refs()
PriceScheduleSpecification.update_forward_refs()
PricingDetail.update_forward_refs()
PrincipalIdFormat.update_forward_refs()
PrivateDnsDetails.update_forward_refs()
PrivateDnsNameConfiguration.update_forward_refs()
PrivateDnsNameOptionsOnLaunch.update_forward_refs()
PrivateDnsNameOptionsRequest.update_forward_refs()
PrivateDnsNameOptionsResponse.update_forward_refs()
PrivateIpAddressSpecification.update_forward_refs()
ProcessorInfo.update_forward_refs()
ProductCode.update_forward_refs()
PropagatingVgw.update_forward_refs()
ProvisionByoipCidrRequest.update_forward_refs()
ProvisionByoipCidrResult.update_forward_refs()
ProvisionIpamPoolCidrRequest.update_forward_refs()
ProvisionIpamPoolCidrResult.update_forward_refs()
ProvisionPublicIpv4PoolCidrRequest.update_forward_refs()
ProvisionPublicIpv4PoolCidrResult.update_forward_refs()
ProvisionedBandwidth.update_forward_refs()
PtrUpdateStatus.update_forward_refs()
PublicIpv4Pool.update_forward_refs()
PublicIpv4PoolRange.update_forward_refs()
Purchase.update_forward_refs()
PurchaseHostReservationRequest.update_forward_refs()
PurchaseHostReservationResult.update_forward_refs()
PurchaseRequest.update_forward_refs()
PurchaseReservedInstancesOfferingRequest.update_forward_refs()
PurchaseReservedInstancesOfferingResult.update_forward_refs()
PurchaseScheduledInstancesRequest.update_forward_refs()
PurchaseScheduledInstancesResult.update_forward_refs()
RebootInstancesRequest.update_forward_refs()
RecurringCharge.update_forward_refs()
ReferencedSecurityGroup.update_forward_refs()
Region.update_forward_refs()
RegisterImageRequest.update_forward_refs()
RegisterImageResult.update_forward_refs()
RegisterInstanceEventNotificationAttributesRequest.update_forward_refs()
RegisterInstanceEventNotificationAttributesResult.update_forward_refs()
RegisterInstanceTagAttributeRequest.update_forward_refs()
RegisterTransitGatewayMulticastGroupMembersRequest.update_forward_refs()
RegisterTransitGatewayMulticastGroupMembersResult.update_forward_refs()
RegisterTransitGatewayMulticastGroupSourcesRequest.update_forward_refs()
RegisterTransitGatewayMulticastGroupSourcesResult.update_forward_refs()
RejectTransitGatewayMulticastDomainAssociationsRequest.update_forward_refs()
RejectTransitGatewayMulticastDomainAssociationsResult.update_forward_refs()
RejectTransitGatewayPeeringAttachmentRequest.update_forward_refs()
RejectTransitGatewayPeeringAttachmentResult.update_forward_refs()
RejectTransitGatewayVpcAttachmentRequest.update_forward_refs()
RejectTransitGatewayVpcAttachmentResult.update_forward_refs()
RejectVpcEndpointConnectionsRequest.update_forward_refs()
RejectVpcEndpointConnectionsResult.update_forward_refs()
RejectVpcPeeringConnectionRequest.update_forward_refs()
RejectVpcPeeringConnectionResult.update_forward_refs()
ReleaseAddressRequest.update_forward_refs()
ReleaseHostsRequest.update_forward_refs()
ReleaseHostsResult.update_forward_refs()
ReleaseIpamPoolAllocationRequest.update_forward_refs()
ReleaseIpamPoolAllocationResult.update_forward_refs()
RemoveIpamOperatingRegion.update_forward_refs()
RemovePrefixListEntry.update_forward_refs()
ReplaceIamInstanceProfileAssociationRequest.update_forward_refs()
ReplaceIamInstanceProfileAssociationResult.update_forward_refs()
ReplaceNetworkAclAssociationRequest.update_forward_refs()
ReplaceNetworkAclAssociationResult.update_forward_refs()
ReplaceNetworkAclEntryRequest.update_forward_refs()
ReplaceRootVolumeTask.update_forward_refs()
ReplaceRouteRequest.update_forward_refs()
ReplaceRouteTableAssociationRequest.update_forward_refs()
ReplaceRouteTableAssociationResult.update_forward_refs()
ReplaceTransitGatewayRouteRequest.update_forward_refs()
ReplaceTransitGatewayRouteResult.update_forward_refs()
ReplaceVpnTunnelRequest.update_forward_refs()
ReplaceVpnTunnelResult.update_forward_refs()
ReportInstanceStatusRequest.update_forward_refs()
RequestFilterPortRange.update_forward_refs()
RequestIpamResourceTag.update_forward_refs()
RequestLaunchTemplateData.update_forward_refs()
RequestSpotFleetRequest.update_forward_refs()
RequestSpotFleetResponse.update_forward_refs()
RequestSpotInstancesRequest.update_forward_refs()
RequestSpotInstancesResult.update_forward_refs()
RequestSpotLaunchSpecification.update_forward_refs()
Reservation.update_forward_refs()
ReservationFleetInstanceSpecification.update_forward_refs()
ReservationValue.update_forward_refs()
ReservedInstanceLimitPrice.update_forward_refs()
ReservedInstanceReservationValue.update_forward_refs()
ReservedInstances.update_forward_refs()
ReservedInstancesConfiguration.update_forward_refs()
ReservedInstancesId.update_forward_refs()
ReservedInstancesListing.update_forward_refs()
ReservedInstancesModification.update_forward_refs()
ReservedInstancesModificationResult.update_forward_refs()
ReservedInstancesOffering.update_forward_refs()
ResetAddressAttributeRequest.update_forward_refs()
ResetAddressAttributeResult.update_forward_refs()
ResetEbsDefaultKmsKeyIdRequest.update_forward_refs()
ResetEbsDefaultKmsKeyIdResult.update_forward_refs()
ResetFpgaImageAttributeRequest.update_forward_refs()
ResetFpgaImageAttributeResult.update_forward_refs()
ResetImageAttributeRequest.update_forward_refs()
ResetInstanceAttributeRequest.update_forward_refs()
ResetNetworkInterfaceAttributeRequest.update_forward_refs()
ResetSnapshotAttributeRequest.update_forward_refs()
ResourceStatement.update_forward_refs()
ResourceStatementRequest.update_forward_refs()
ResponseError.update_forward_refs()
ResponseLaunchTemplateData.update_forward_refs()
RestoreAddressToClassicRequest.update_forward_refs()
RestoreAddressToClassicResult.update_forward_refs()
RestoreImageFromRecycleBinRequest.update_forward_refs()
RestoreImageFromRecycleBinResult.update_forward_refs()
RestoreManagedPrefixListVersionRequest.update_forward_refs()
RestoreManagedPrefixListVersionResult.update_forward_refs()
RestoreSnapshotFromRecycleBinRequest.update_forward_refs()
RestoreSnapshotFromRecycleBinResult.update_forward_refs()
RestoreSnapshotTierRequest.update_forward_refs()
RestoreSnapshotTierResult.update_forward_refs()
RevokeClientVpnIngressRequest.update_forward_refs()
RevokeClientVpnIngressResult.update_forward_refs()
RevokeSecurityGroupEgressRequest.update_forward_refs()
RevokeSecurityGroupEgressResult.update_forward_refs()
RevokeSecurityGroupIngressRequest.update_forward_refs()
RevokeSecurityGroupIngressResult.update_forward_refs()
Route.update_forward_refs()
RouteTable.update_forward_refs()
RouteTableAssociation.update_forward_refs()
RouteTableAssociationState.update_forward_refs()
RuleGroupRuleOptionsPair.update_forward_refs()
RuleGroupTypePair.update_forward_refs()
RuleOption.update_forward_refs()
RunInstancesMonitoringEnabled.update_forward_refs()
RunInstancesRequest.update_forward_refs()
RunScheduledInstancesRequest.update_forward_refs()
RunScheduledInstancesResult.update_forward_refs()
S3ObjectTag.update_forward_refs()
S3Storage.update_forward_refs()
ScheduledInstance.update_forward_refs()
ScheduledInstanceAvailability.update_forward_refs()
ScheduledInstanceRecurrence.update_forward_refs()
ScheduledInstanceRecurrenceRequest.update_forward_refs()
ScheduledInstancesBlockDeviceMapping.update_forward_refs()
ScheduledInstancesEbs.update_forward_refs()
ScheduledInstancesIamInstanceProfile.update_forward_refs()
ScheduledInstancesIpv6Address.update_forward_refs()
ScheduledInstancesLaunchSpecification.update_forward_refs()
ScheduledInstancesMonitoring.update_forward_refs()
ScheduledInstancesNetworkInterface.update_forward_refs()
ScheduledInstancesPlacement.update_forward_refs()
ScheduledInstancesPrivateIpAddressConfig.update_forward_refs()
SearchLocalGatewayRoutesRequest.update_forward_refs()
SearchLocalGatewayRoutesResult.update_forward_refs()
SearchTransitGatewayMulticastGroupsRequest.update_forward_refs()
SearchTransitGatewayMulticastGroupsResult.update_forward_refs()
SearchTransitGatewayRoutesRequest.update_forward_refs()
SearchTransitGatewayRoutesResult.update_forward_refs()
SecurityGroup.update_forward_refs()
SecurityGroupIdentifier.update_forward_refs()
SecurityGroupReference.update_forward_refs()
SecurityGroupRule.update_forward_refs()
SecurityGroupRuleDescription.update_forward_refs()
SecurityGroupRuleRequest.update_forward_refs()
SecurityGroupRuleUpdate.update_forward_refs()
SendDiagnosticInterruptRequest.update_forward_refs()
ServiceConfiguration.update_forward_refs()
ServiceDetail.update_forward_refs()
ServiceTypeDetail.update_forward_refs()
SlotDateTimeRangeRequest.update_forward_refs()
SlotStartTimeRangeRequest.update_forward_refs()
Snapshot.update_forward_refs()
SnapshotDetail.update_forward_refs()
SnapshotDiskContainer.update_forward_refs()
SnapshotInfo.update_forward_refs()
SnapshotRecycleBinInfo.update_forward_refs()
SnapshotTaskDetail.update_forward_refs()
SnapshotTierStatus.update_forward_refs()
SpotCapacityRebalance.update_forward_refs()
SpotDatafeedSubscription.update_forward_refs()
SpotFleetLaunchSpecification.update_forward_refs()
SpotFleetMonitoring.update_forward_refs()
SpotFleetRequestConfig.update_forward_refs()
SpotFleetRequestConfigData.update_forward_refs()
SpotFleetTagSpecification.update_forward_refs()
SpotInstanceRequest.update_forward_refs()
SpotInstanceStateFault.update_forward_refs()
SpotInstanceStatus.update_forward_refs()
SpotMaintenanceStrategies.update_forward_refs()
SpotMarketOptions.update_forward_refs()
SpotOptions.update_forward_refs()
SpotOptionsRequest.update_forward_refs()
SpotPlacement.update_forward_refs()
SpotPlacementScore.update_forward_refs()
SpotPrice.update_forward_refs()
StaleIpPermission.update_forward_refs()
StaleSecurityGroup.update_forward_refs()
StartInstancesRequest.update_forward_refs()
StartInstancesResult.update_forward_refs()
StartNetworkInsightsAccessScopeAnalysisRequest.update_forward_refs()
StartNetworkInsightsAccessScopeAnalysisResult.update_forward_refs()
StartNetworkInsightsAnalysisRequest.update_forward_refs()
StartNetworkInsightsAnalysisResult.update_forward_refs()
StartVpcEndpointServicePrivateDnsVerificationRequest.update_forward_refs()
StartVpcEndpointServicePrivateDnsVerificationResult.update_forward_refs()
StateReason.update_forward_refs()
StopInstancesRequest.update_forward_refs()
StopInstancesResult.update_forward_refs()
Storage.update_forward_refs()
StorageLocation.update_forward_refs()
StoreImageTaskResult.update_forward_refs()
Subnet.update_forward_refs()
SubnetAssociation.update_forward_refs()
SubnetCidrBlockState.update_forward_refs()
SubnetCidrReservation.update_forward_refs()
SubnetIpv6CidrBlockAssociation.update_forward_refs()
Subscription.update_forward_refs()
SuccessfulInstanceCreditSpecificationItem.update_forward_refs()
SuccessfulQueuedPurchaseDeletion.update_forward_refs()
Tag.update_forward_refs()
TagDescription.update_forward_refs()
TagSpecification.update_forward_refs()
TargetCapacitySpecification.update_forward_refs()
TargetCapacitySpecificationRequest.update_forward_refs()
TargetConfiguration.update_forward_refs()
TargetConfigurationRequest.update_forward_refs()
TargetGroup.update_forward_refs()
TargetGroupsConfig.update_forward_refs()
TargetNetwork.update_forward_refs()
TargetReservationValue.update_forward_refs()
TerminateClientVpnConnectionsRequest.update_forward_refs()
TerminateClientVpnConnectionsResult.update_forward_refs()
TerminateConnectionStatus.update_forward_refs()
TerminateInstancesRequest.update_forward_refs()
TerminateInstancesResult.update_forward_refs()
ThroughResourcesStatement.update_forward_refs()
ThroughResourcesStatementRequest.update_forward_refs()
TotalLocalStorageGB.update_forward_refs()
TotalLocalStorageGBRequest.update_forward_refs()
TrafficMirrorFilter.update_forward_refs()
TrafficMirrorFilterRule.update_forward_refs()
TrafficMirrorPortRange.update_forward_refs()
TrafficMirrorPortRangeRequest.update_forward_refs()
TrafficMirrorSession.update_forward_refs()
TrafficMirrorTarget.update_forward_refs()
TransitGateway.update_forward_refs()
TransitGatewayAssociation.update_forward_refs()
TransitGatewayAttachment.update_forward_refs()
TransitGatewayAttachmentAssociation.update_forward_refs()
TransitGatewayAttachmentBgpConfiguration.update_forward_refs()
TransitGatewayAttachmentPropagation.update_forward_refs()
TransitGatewayConnect.update_forward_refs()
TransitGatewayConnectOptions.update_forward_refs()
TransitGatewayConnectPeer.update_forward_refs()
TransitGatewayConnectPeerConfiguration.update_forward_refs()
TransitGatewayConnectRequestBgpOptions.update_forward_refs()
TransitGatewayMulticastDeregisteredGroupMembers.update_forward_refs()
TransitGatewayMulticastDeregisteredGroupSources.update_forward_refs()
TransitGatewayMulticastDomain.update_forward_refs()
TransitGatewayMulticastDomainAssociation.update_forward_refs()
TransitGatewayMulticastDomainAssociations.update_forward_refs()
TransitGatewayMulticastDomainOptions.update_forward_refs()
TransitGatewayMulticastGroup.update_forward_refs()
TransitGatewayMulticastRegisteredGroupMembers.update_forward_refs()
TransitGatewayMulticastRegisteredGroupSources.update_forward_refs()
TransitGatewayOptions.update_forward_refs()
TransitGatewayPeeringAttachment.update_forward_refs()
TransitGatewayPeeringAttachmentOptions.update_forward_refs()
TransitGatewayPolicyRule.update_forward_refs()
TransitGatewayPolicyRuleMetaData.update_forward_refs()
TransitGatewayPolicyTable.update_forward_refs()
TransitGatewayPolicyTableAssociation.update_forward_refs()
TransitGatewayPolicyTableEntry.update_forward_refs()
TransitGatewayPrefixListAttachment.update_forward_refs()
TransitGatewayPrefixListReference.update_forward_refs()
TransitGatewayPropagation.update_forward_refs()
TransitGatewayRequestOptions.update_forward_refs()
TransitGatewayRoute.update_forward_refs()
TransitGatewayRouteAttachment.update_forward_refs()
TransitGatewayRouteTable.update_forward_refs()
TransitGatewayRouteTableAnnouncement.update_forward_refs()
TransitGatewayRouteTableAssociation.update_forward_refs()
TransitGatewayRouteTablePropagation.update_forward_refs()
TransitGatewayRouteTableRoute.update_forward_refs()
TransitGatewayVpcAttachment.update_forward_refs()
TransitGatewayVpcAttachmentOptions.update_forward_refs()
TrunkInterfaceAssociation.update_forward_refs()
TunnelOption.update_forward_refs()
UnassignIpv6AddressesRequest.update_forward_refs()
UnassignIpv6AddressesResult.update_forward_refs()
UnassignPrivateIpAddressesRequest.update_forward_refs()
UnassignPrivateNatGatewayAddressRequest.update_forward_refs()
UnassignPrivateNatGatewayAddressResult.update_forward_refs()
UnmonitorInstancesRequest.update_forward_refs()
UnmonitorInstancesResult.update_forward_refs()
UnsuccessfulInstanceCreditSpecificationItem.update_forward_refs()
UnsuccessfulInstanceCreditSpecificationItemError.update_forward_refs()
UnsuccessfulItem.update_forward_refs()
UnsuccessfulItemError.update_forward_refs()
UpdateSecurityGroupRuleDescriptionsEgressRequest.update_forward_refs()
UpdateSecurityGroupRuleDescriptionsEgressResult.update_forward_refs()
UpdateSecurityGroupRuleDescriptionsIngressRequest.update_forward_refs()
UpdateSecurityGroupRuleDescriptionsIngressResult.update_forward_refs()
UserBucket.update_forward_refs()
UserBucketDetails.update_forward_refs()
UserData.update_forward_refs()
UserIdGroupPair.update_forward_refs()
VCpuCountRange.update_forward_refs()
VCpuCountRangeRequest.update_forward_refs()
VCpuInfo.update_forward_refs()
ValidationError.update_forward_refs()
ValidationWarning.update_forward_refs()
VerifiedAccessEndpoint.update_forward_refs()
VerifiedAccessEndpointEniOptions.update_forward_refs()
VerifiedAccessEndpointLoadBalancerOptions.update_forward_refs()
VerifiedAccessEndpointStatus.update_forward_refs()
VerifiedAccessGroup.update_forward_refs()
VerifiedAccessInstance.update_forward_refs()
VerifiedAccessInstanceLoggingConfiguration.update_forward_refs()
VerifiedAccessLogCloudWatchLogsDestination.update_forward_refs()
VerifiedAccessLogCloudWatchLogsDestinationOptions.update_forward_refs()
VerifiedAccessLogDeliveryStatus.update_forward_refs()
VerifiedAccessLogKinesisDataFirehoseDestination.update_forward_refs()
VerifiedAccessLogKinesisDataFirehoseDestinationOptions.update_forward_refs()
VerifiedAccessLogOptions.update_forward_refs()
VerifiedAccessLogS3Destination.update_forward_refs()
VerifiedAccessLogS3DestinationOptions.update_forward_refs()
VerifiedAccessLogs.update_forward_refs()
VerifiedAccessTrustProvider.update_forward_refs()
VerifiedAccessTrustProviderCondensed.update_forward_refs()
VgwTelemetry.update_forward_refs()
Volume.update_forward_refs()
VolumeAttachment.update_forward_refs()
VolumeDetail.update_forward_refs()
VolumeModification.update_forward_refs()
VolumeStatusAction.update_forward_refs()
VolumeStatusAttachmentStatus.update_forward_refs()
VolumeStatusDetails.update_forward_refs()
VolumeStatusEvent.update_forward_refs()
VolumeStatusInfo.update_forward_refs()
VolumeStatusItem.update_forward_refs()
Vpc.update_forward_refs()
VpcAttachment.update_forward_refs()
VpcCidrBlockAssociation.update_forward_refs()
VpcCidrBlockState.update_forward_refs()
VpcClassicLink.update_forward_refs()
VpcEndpoint.update_forward_refs()
VpcEndpointConnection.update_forward_refs()
VpcIpv6CidrBlockAssociation.update_forward_refs()
VpcPeeringConnection.update_forward_refs()
VpcPeeringConnectionOptionsDescription.update_forward_refs()
VpcPeeringConnectionStateReason.update_forward_refs()
VpcPeeringConnectionVpcInfo.update_forward_refs()
VpnConnection.update_forward_refs()
VpnConnectionDeviceType.update_forward_refs()
VpnConnectionOptions.update_forward_refs()
VpnConnectionOptionsSpecification.update_forward_refs()
VpnGateway.update_forward_refs()
VpnStaticRoute.update_forward_refs()
VpnTunnelLogOptions.update_forward_refs()
VpnTunnelLogOptionsSpecification.update_forward_refs()
VpnTunnelOptionsSpecification.update_forward_refs()
WithdrawByoipCidrRequest.update_forward_refs()
WithdrawByoipCidrResult.update_forward_refs()
