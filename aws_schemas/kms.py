from datetime import datetime
import typing
import enum

import pydantic


class _KMSModelBase(
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


AWSAccountIdType: str = pydantic.constr()
AlgorithmSpec: str = pydantic.constr()
AliasNameType: str = pydantic.constr(
    min_length=1, max_length=256, regex=r"^[a-zA-Z0-9:/_-]+$"
)
ArnType: str = pydantic.constr(min_length=20, max_length=2048)
AttestationDocumentType: bytes = pydantic.conbytes()
BooleanType: bool = pydantic.conbool()
CiphertextType: bytes = pydantic.conbytes()
CloudHsmClusterIdType: str = pydantic.constr(
    min_length=19, max_length=24, regex=r"cluster-[2-7a-zA-Z]{11,16}"
)
ConnectionErrorCodeType: str = pydantic.constr()
ConnectionStateType: str = pydantic.constr()
CustomKeyStoreIdType: str = pydantic.constr(min_length=1, max_length=64)
CustomKeyStoreNameType: str = pydantic.constr(min_length=1, max_length=256)
CustomKeyStoreType: str = pydantic.constr()
CustomerMasterKeySpec: str = pydantic.constr()
DataKeyPairSpec: str = pydantic.constr()
DataKeySpec: str = pydantic.constr()
DateType: datetime = pydantic.condate()
DescriptionType: str = pydantic.constr(max_length=8192)
EncryptionAlgorithmSpec: str = pydantic.constr()
EncryptionContextKey: str = pydantic.constr()
EncryptionContextType: dict = pydantic.condict()
EncryptionContextValue: str = pydantic.constr()
ErrorMessageType: str = pydantic.constr()
ExpirationModelType: str = pydantic.constr()
GrantIdType: str = pydantic.constr(min_length=1, max_length=128)
GrantNameType: str = pydantic.constr(
    min_length=1, max_length=256, regex=r"^[a-zA-Z0-9:/_-]+$"
)
GrantOperation: str = pydantic.constr()
GrantTokenType: str = pydantic.constr(min_length=1, max_length=8192)
KeyEncryptionMechanism: str = pydantic.constr()
KeyIdType: str = pydantic.constr(min_length=1, max_length=2048)
KeyManagerType: str = pydantic.constr()
KeySpec: str = pydantic.constr()
KeyState: str = pydantic.constr()
KeyStorePasswordType: str = pydantic.constr(min_length=7, max_length=32)
KeyUsageType: str = pydantic.constr()
LimitType: int = pydantic.conint(ge=1, le=1000)
MacAlgorithmSpec: str = pydantic.constr()
MarkerType: str = pydantic.constr(
    min_length=1, max_length=1024, regex=r"[\u0020-\u00FF]*"
)
MessageType: str = pydantic.constr()
MultiRegionKeyType: str = pydantic.constr()
NullableBooleanType: bool = pydantic.conbool()
NumberOfBytesType: int = pydantic.conint(ge=1, le=1024)
OriginType: str = pydantic.constr()
PendingWindowInDaysType: int = pydantic.conint(ge=1, le=365)
PlaintextType: bytes = pydantic.conbytes()
PolicyNameType: str = pydantic.constr(min_length=1, max_length=128, regex=r"[\w]+")
PolicyType: str = pydantic.constr(
    min_length=1, max_length=131072, regex=r"[\u0009\u000A\u000D\u0020-\u00FF]+"
)
PrincipalIdType: str = pydantic.constr(
    min_length=1, max_length=256, regex=r"^[\w+=,.@:/-]+$"
)
PublicKeyType: bytes = pydantic.conbytes()
RegionType: str = pydantic.constr(
    min_length=1, max_length=32, regex=r"^([a-z]+-){2,3}\d+$"
)
SigningAlgorithmSpec: str = pydantic.constr()
TagKeyType: str = pydantic.constr(min_length=1, max_length=128)
TagValueType: str = pydantic.constr(max_length=256)
TrustAnchorCertificateType: str = pydantic.constr(min_length=1, max_length=5000)
WrappingKeySpec: str = pydantic.constr()
XksKeyIdType: str = pydantic.constr(
    min_length=1, max_length=128, regex=r"^[a-zA-Z0-9-_.]+$"
)
XksProxyAuthenticationAccessKeyIdType: str = pydantic.constr(
    min_length=20, max_length=30, regex=r"^[A-Z2-7]+$"
)
XksProxyAuthenticationRawSecretAccessKeyType: str = pydantic.constr(
    min_length=43, max_length=64, regex=r"^[a-zA-Z0-9\/+=]+$"
)
XksProxyConnectivityType: str = pydantic.constr()
XksProxyUriEndpointType: str = pydantic.constr(
    min_length=10, max_length=128, regex=r"^https://[a-zA-Z0-9.-]+$"
)
XksProxyUriPathType: str = pydantic.constr(
    min_length=10,
    max_length=128,
    regex=r"^(/[a-zA-Z0-9\/_-]+/kms/xks/v\d{1,2})$|^(/kms/xks/v\d{1,2})$",
)
XksProxyVpcEndpointServiceNameType: str = pydantic.constr(
    min_length=20,
    max_length=64,
    regex=r"^com\.amazonaws\.vpce\.([a-z]+-){2,3}\d+\.vpce-svc-[0-9a-z]+$",
)

AliasList = typing.List["AliasListEntry"]
CustomKeyStoresList = typing.List["CustomKeyStoresListEntry"]
EncryptionAlgorithmSpecList = typing.List["EncryptionAlgorithmSpec"]
GrantList = typing.List["GrantListEntry"]
GrantOperationList = typing.List["GrantOperation"]
GrantTokenList = typing.List["GrantTokenType"]
KeyList = typing.List["KeyListEntry"]
MacAlgorithmSpecList = typing.List["MacAlgorithmSpec"]
MultiRegionKeyList = typing.List["MultiRegionKey"]
PolicyNameList = typing.List["PolicyNameType"]
SigningAlgorithmSpecList = typing.List["SigningAlgorithmSpec"]
TagKeyList = typing.List["TagKeyType"]
TagList = typing.List["Tag"]


class AlgorithmSpec(enum.Enum):
    RSAES_PKCS1_V1_5 = "RSAES_PKCS1_V1_5"
    RSAES_OAEP_SHA_1 = "RSAES_OAEP_SHA_1"
    RSAES_OAEP_SHA_256 = "RSAES_OAEP_SHA_256"
    RSA_AES_KEY_WRAP_SHA_1 = "RSA_AES_KEY_WRAP_SHA_1"
    RSA_AES_KEY_WRAP_SHA_256 = "RSA_AES_KEY_WRAP_SHA_256"


class ConnectionErrorCodeType(enum.Enum):
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    CLUSTER_NOT_FOUND = "CLUSTER_NOT_FOUND"
    NETWORK_ERRORS = "NETWORK_ERRORS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INSUFFICIENT_CLOUDHSM_HSMS = "INSUFFICIENT_CLOUDHSM_HSMS"
    USER_LOCKED_OUT = "USER_LOCKED_OUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_LOGGED_IN = "USER_LOGGED_IN"
    SUBNET_NOT_FOUND = "SUBNET_NOT_FOUND"
    INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET = "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET"
    XKS_PROXY_ACCESS_DENIED = "XKS_PROXY_ACCESS_DENIED"
    XKS_PROXY_NOT_REACHABLE = "XKS_PROXY_NOT_REACHABLE"
    XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND = "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND"
    XKS_PROXY_INVALID_RESPONSE = "XKS_PROXY_INVALID_RESPONSE"
    XKS_PROXY_INVALID_CONFIGURATION = "XKS_PROXY_INVALID_CONFIGURATION"
    XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION = (
        "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION"
    )
    XKS_PROXY_TIMED_OUT = "XKS_PROXY_TIMED_OUT"
    XKS_PROXY_INVALID_TLS_CONFIGURATION = "XKS_PROXY_INVALID_TLS_CONFIGURATION"


class ConnectionStateType(enum.Enum):
    CONNECTED = "CONNECTED"
    CONNECTING = "CONNECTING"
    FAILED = "FAILED"
    DISCONNECTED = "DISCONNECTED"
    DISCONNECTING = "DISCONNECTING"


class CustomKeyStoreType(enum.Enum):
    AWS_CLOUDHSM = "AWS_CLOUDHSM"
    EXTERNAL_KEY_STORE = "EXTERNAL_KEY_STORE"


class CustomerMasterKeySpec(enum.Enum):
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"
    ECC_NIST_P256 = "ECC_NIST_P256"
    ECC_NIST_P384 = "ECC_NIST_P384"
    ECC_NIST_P521 = "ECC_NIST_P521"
    ECC_SECG_P256K1 = "ECC_SECG_P256K1"
    SYMMETRIC_DEFAULT = "SYMMETRIC_DEFAULT"
    HMAC_224 = "HMAC_224"
    HMAC_256 = "HMAC_256"
    HMAC_384 = "HMAC_384"
    HMAC_512 = "HMAC_512"
    SM2 = "SM2"


class DataKeyPairSpec(enum.Enum):
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"
    ECC_NIST_P256 = "ECC_NIST_P256"
    ECC_NIST_P384 = "ECC_NIST_P384"
    ECC_NIST_P521 = "ECC_NIST_P521"
    ECC_SECG_P256K1 = "ECC_SECG_P256K1"
    SM2 = "SM2"


class DataKeySpec(enum.Enum):
    AES_256 = "AES_256"
    AES_128 = "AES_128"


class EncryptionAlgorithmSpec(enum.Enum):
    SYMMETRIC_DEFAULT = "SYMMETRIC_DEFAULT"
    RSAES_OAEP_SHA_1 = "RSAES_OAEP_SHA_1"
    RSAES_OAEP_SHA_256 = "RSAES_OAEP_SHA_256"
    SM2PKE = "SM2PKE"


class ExpirationModelType(enum.Enum):
    KEY_MATERIAL_EXPIRES = "KEY_MATERIAL_EXPIRES"
    KEY_MATERIAL_DOES_NOT_EXPIRE = "KEY_MATERIAL_DOES_NOT_EXPIRE"


class GrantOperation(enum.Enum):
    DECRYPT = "Decrypt"
    ENCRYPT = "Encrypt"
    GENERATEDATAKEY = "GenerateDataKey"
    GENERATEDATAKEYWITHOUTPLAINTEXT = "GenerateDataKeyWithoutPlaintext"
    REENCRYPTFROM = "ReEncryptFrom"
    REENCRYPTTO = "ReEncryptTo"
    SIGN = "Sign"
    VERIFY = "Verify"
    GETPUBLICKEY = "GetPublicKey"
    CREATEGRANT = "CreateGrant"
    RETIREGRANT = "RetireGrant"
    DESCRIBEKEY = "DescribeKey"
    GENERATEDATAKEYPAIR = "GenerateDataKeyPair"
    GENERATEDATAKEYPAIRWITHOUTPLAINTEXT = "GenerateDataKeyPairWithoutPlaintext"
    GENERATEMAC = "GenerateMac"
    VERIFYMAC = "VerifyMac"


class KeyEncryptionMechanism(enum.Enum):
    RSAES_OAEP_SHA_256 = "RSAES_OAEP_SHA_256"


class KeyManagerType(enum.Enum):
    AWS = "AWS"
    CUSTOMER = "CUSTOMER"


class KeySpec(enum.Enum):
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"
    ECC_NIST_P256 = "ECC_NIST_P256"
    ECC_NIST_P384 = "ECC_NIST_P384"
    ECC_NIST_P521 = "ECC_NIST_P521"
    ECC_SECG_P256K1 = "ECC_SECG_P256K1"
    SYMMETRIC_DEFAULT = "SYMMETRIC_DEFAULT"
    HMAC_224 = "HMAC_224"
    HMAC_256 = "HMAC_256"
    HMAC_384 = "HMAC_384"
    HMAC_512 = "HMAC_512"
    SM2 = "SM2"


class KeyState(enum.Enum):
    CREATING = "Creating"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    PENDINGDELETION = "PendingDeletion"
    PENDINGIMPORT = "PendingImport"
    PENDINGREPLICADELETION = "PendingReplicaDeletion"
    UNAVAILABLE = "Unavailable"
    UPDATING = "Updating"


class KeyUsageType(enum.Enum):
    SIGN_VERIFY = "SIGN_VERIFY"
    ENCRYPT_DECRYPT = "ENCRYPT_DECRYPT"
    GENERATE_VERIFY_MAC = "GENERATE_VERIFY_MAC"


class MacAlgorithmSpec(enum.Enum):
    HMAC_SHA_224 = "HMAC_SHA_224"
    HMAC_SHA_256 = "HMAC_SHA_256"
    HMAC_SHA_384 = "HMAC_SHA_384"
    HMAC_SHA_512 = "HMAC_SHA_512"


class MessageType(enum.Enum):
    RAW = "RAW"
    DIGEST = "DIGEST"


class MultiRegionKeyType(enum.Enum):
    PRIMARY = "PRIMARY"
    REPLICA = "REPLICA"


class OriginType(enum.Enum):
    AWS_KMS = "AWS_KMS"
    EXTERNAL = "EXTERNAL"
    AWS_CLOUDHSM = "AWS_CLOUDHSM"
    EXTERNAL_KEY_STORE = "EXTERNAL_KEY_STORE"


class SigningAlgorithmSpec(enum.Enum):
    RSASSA_PSS_SHA_256 = "RSASSA_PSS_SHA_256"
    RSASSA_PSS_SHA_384 = "RSASSA_PSS_SHA_384"
    RSASSA_PSS_SHA_512 = "RSASSA_PSS_SHA_512"
    RSASSA_PKCS1_V1_5_SHA_256 = "RSASSA_PKCS1_V1_5_SHA_256"
    RSASSA_PKCS1_V1_5_SHA_384 = "RSASSA_PKCS1_V1_5_SHA_384"
    RSASSA_PKCS1_V1_5_SHA_512 = "RSASSA_PKCS1_V1_5_SHA_512"
    ECDSA_SHA_256 = "ECDSA_SHA_256"
    ECDSA_SHA_384 = "ECDSA_SHA_384"
    ECDSA_SHA_512 = "ECDSA_SHA_512"
    SM2DSA = "SM2DSA"


class WrappingKeySpec(enum.Enum):
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"


class XksProxyConnectivityType(enum.Enum):
    PUBLIC_ENDPOINT = "PUBLIC_ENDPOINT"
    VPC_ENDPOINT_SERVICE = "VPC_ENDPOINT_SERVICE"


class AliasListEntry(_KMSModelBase):
    alias_name: AliasNameType = pydantic.Field(None, alias="AliasName")
    alias_arn: ArnType = pydantic.Field(None, alias="AliasArn")
    target_key_id: KeyIdType = pydantic.Field(None, alias="TargetKeyId")
    creation_date: DateType = pydantic.Field(None, alias="CreationDate")
    last_updated_date: DateType = pydantic.Field(None, alias="LastUpdatedDate")


class CancelKeyDeletionRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class CancelKeyDeletionResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class ConnectCustomKeyStoreRequest(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )


class ConnectCustomKeyStoreResponse(_KMSModelBase):
    pass


class CreateAliasRequest(_KMSModelBase):
    alias_name: AliasNameType = pydantic.Field(None, alias="AliasName")
    target_key_id: KeyIdType = pydantic.Field(None, alias="TargetKeyId")


class CreateCustomKeyStoreRequest(_KMSModelBase):
    custom_key_store_name: CustomKeyStoreNameType = pydantic.Field(
        None, alias="CustomKeyStoreName"
    )
    cloud_hsm_cluster_id: CloudHsmClusterIdType = pydantic.Field(
        None, alias="CloudHsmClusterId"
    )
    trust_anchor_certificate: TrustAnchorCertificateType = pydantic.Field(
        None, alias="TrustAnchorCertificate"
    )
    key_store_password: KeyStorePasswordType = pydantic.Field(
        None, alias="KeyStorePassword"
    )
    custom_key_store_type: CustomKeyStoreType = pydantic.Field(
        None, alias="CustomKeyStoreType"
    )
    xks_proxy_uri_endpoint: XksProxyUriEndpointType = pydantic.Field(
        None, alias="XksProxyUriEndpoint"
    )
    xks_proxy_uri_path: XksProxyUriPathType = pydantic.Field(
        None, alias="XksProxyUriPath"
    )
    xks_proxy_vpc_endpoint_service_name: XksProxyVpcEndpointServiceNameType = (
        pydantic.Field(None, alias="XksProxyVpcEndpointServiceName")
    )
    xks_proxy_authentication_credential: "XksProxyAuthenticationCredentialType" = (
        pydantic.Field(None, alias="XksProxyAuthenticationCredential")
    )
    xks_proxy_connectivity: XksProxyConnectivityType = pydantic.Field(
        None, alias="XksProxyConnectivity"
    )


class CreateCustomKeyStoreResponse(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )


class CreateGrantRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grantee_principal: PrincipalIdType = pydantic.Field(None, alias="GranteePrincipal")
    retiring_principal: PrincipalIdType = pydantic.Field(
        None, alias="RetiringPrincipal"
    )
    operations: GrantOperationList = pydantic.Field(None, alias="Operations")
    constraints: "GrantConstraints" = pydantic.Field(None, alias="Constraints")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")
    name: GrantNameType = pydantic.Field(None, alias="Name")


class CreateGrantResponse(_KMSModelBase):
    grant_token: GrantTokenType = pydantic.Field(None, alias="GrantToken")
    grant_id: GrantIdType = pydantic.Field(None, alias="GrantId")


class CreateKeyRequest(_KMSModelBase):
    policy: PolicyType = pydantic.Field(None, alias="Policy")
    description: DescriptionType = pydantic.Field(None, alias="Description")
    key_usage: KeyUsageType = pydantic.Field(None, alias="KeyUsage")
    customer_master_key_spec: CustomerMasterKeySpec = pydantic.Field(
        None, alias="CustomerMasterKeySpec"
    )
    key_spec: KeySpec = pydantic.Field(None, alias="KeySpec")
    origin: OriginType = pydantic.Field(None, alias="Origin")
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )
    bypass_policy_lockout_safety_check: BooleanType = pydantic.Field(
        None, alias="BypassPolicyLockoutSafetyCheck"
    )
    tags: TagList = pydantic.Field(None, alias="Tags")
    multi_region: NullableBooleanType = pydantic.Field(None, alias="MultiRegion")
    xks_key_id: XksKeyIdType = pydantic.Field(None, alias="XksKeyId")


class CreateKeyResponse(_KMSModelBase):
    key_metadata: "KeyMetadata" = pydantic.Field(None, alias="KeyMetadata")


class CustomKeyStoresListEntry(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )
    custom_key_store_name: CustomKeyStoreNameType = pydantic.Field(
        None, alias="CustomKeyStoreName"
    )
    cloud_hsm_cluster_id: CloudHsmClusterIdType = pydantic.Field(
        None, alias="CloudHsmClusterId"
    )
    trust_anchor_certificate: TrustAnchorCertificateType = pydantic.Field(
        None, alias="TrustAnchorCertificate"
    )
    connection_state: ConnectionStateType = pydantic.Field(
        None, alias="ConnectionState"
    )
    connection_error_code: ConnectionErrorCodeType = pydantic.Field(
        None, alias="ConnectionErrorCode"
    )
    creation_date: DateType = pydantic.Field(None, alias="CreationDate")
    custom_key_store_type: CustomKeyStoreType = pydantic.Field(
        None, alias="CustomKeyStoreType"
    )
    xks_proxy_configuration: "XksProxyConfigurationType" = pydantic.Field(
        None, alias="XksProxyConfiguration"
    )


class DecryptRequest(_KMSModelBase):
    ciphertext_blob: CiphertextType = pydantic.Field(None, alias="CiphertextBlob")
    encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContext"
    )
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="EncryptionAlgorithm"
    )
    recipient: "RecipientInfo" = pydantic.Field(None, alias="Recipient")


class DecryptResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    plaintext: PlaintextType = pydantic.Field(None, alias="Plaintext")
    encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="EncryptionAlgorithm"
    )
    ciphertext_for_recipient: CiphertextType = pydantic.Field(
        None, alias="CiphertextForRecipient"
    )


class DeleteAliasRequest(_KMSModelBase):
    alias_name: AliasNameType = pydantic.Field(None, alias="AliasName")


class DeleteCustomKeyStoreRequest(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )


class DeleteCustomKeyStoreResponse(_KMSModelBase):
    pass


class DeleteImportedKeyMaterialRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class DescribeCustomKeyStoresRequest(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )
    custom_key_store_name: CustomKeyStoreNameType = pydantic.Field(
        None, alias="CustomKeyStoreName"
    )
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")


class DescribeCustomKeyStoresResponse(_KMSModelBase):
    custom_key_stores: CustomKeyStoresList = pydantic.Field(
        None, alias="CustomKeyStores"
    )
    next_marker: MarkerType = pydantic.Field(None, alias="NextMarker")
    truncated: BooleanType = pydantic.Field(None, alias="Truncated")


class DescribeKeyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class DescribeKeyResponse(_KMSModelBase):
    key_metadata: "KeyMetadata" = pydantic.Field(None, alias="KeyMetadata")


class DisableKeyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class DisableKeyRotationRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class DisconnectCustomKeyStoreRequest(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )


class DisconnectCustomKeyStoreResponse(_KMSModelBase):
    pass


class EnableKeyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class EnableKeyRotationRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class EncryptRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    plaintext: PlaintextType = pydantic.Field(None, alias="Plaintext")
    encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContext"
    )
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")
    encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="EncryptionAlgorithm"
    )


class EncryptResponse(_KMSModelBase):
    ciphertext_blob: CiphertextType = pydantic.Field(None, alias="CiphertextBlob")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="EncryptionAlgorithm"
    )


class GenerateDataKeyPairRequest(_KMSModelBase):
    encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContext"
    )
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    key_pair_spec: DataKeyPairSpec = pydantic.Field(None, alias="KeyPairSpec")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")
    recipient: "RecipientInfo" = pydantic.Field(None, alias="Recipient")


class GenerateDataKeyPairResponse(_KMSModelBase):
    private_key_ciphertext_blob: CiphertextType = pydantic.Field(
        None, alias="PrivateKeyCiphertextBlob"
    )
    private_key_plaintext: PlaintextType = pydantic.Field(
        None, alias="PrivateKeyPlaintext"
    )
    public_key: PublicKeyType = pydantic.Field(None, alias="PublicKey")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    key_pair_spec: DataKeyPairSpec = pydantic.Field(None, alias="KeyPairSpec")
    ciphertext_for_recipient: CiphertextType = pydantic.Field(
        None, alias="CiphertextForRecipient"
    )


class GenerateDataKeyPairWithoutPlaintextRequest(_KMSModelBase):
    encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContext"
    )
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    key_pair_spec: DataKeyPairSpec = pydantic.Field(None, alias="KeyPairSpec")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class GenerateDataKeyPairWithoutPlaintextResponse(_KMSModelBase):
    private_key_ciphertext_blob: CiphertextType = pydantic.Field(
        None, alias="PrivateKeyCiphertextBlob"
    )
    public_key: PublicKeyType = pydantic.Field(None, alias="PublicKey")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    key_pair_spec: DataKeyPairSpec = pydantic.Field(None, alias="KeyPairSpec")


class GenerateDataKeyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContext"
    )
    number_of_bytes: NumberOfBytesType = pydantic.Field(None, alias="NumberOfBytes")
    key_spec: DataKeySpec = pydantic.Field(None, alias="KeySpec")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")
    recipient: "RecipientInfo" = pydantic.Field(None, alias="Recipient")


class GenerateDataKeyResponse(_KMSModelBase):
    ciphertext_blob: CiphertextType = pydantic.Field(None, alias="CiphertextBlob")
    plaintext: PlaintextType = pydantic.Field(None, alias="Plaintext")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    ciphertext_for_recipient: CiphertextType = pydantic.Field(
        None, alias="CiphertextForRecipient"
    )


class GenerateDataKeyWithoutPlaintextRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContext"
    )
    key_spec: DataKeySpec = pydantic.Field(None, alias="KeySpec")
    number_of_bytes: NumberOfBytesType = pydantic.Field(None, alias="NumberOfBytes")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class GenerateDataKeyWithoutPlaintextResponse(_KMSModelBase):
    ciphertext_blob: CiphertextType = pydantic.Field(None, alias="CiphertextBlob")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class GenerateMacRequest(_KMSModelBase):
    message: PlaintextType = pydantic.Field(None, alias="Message")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    mac_algorithm: MacAlgorithmSpec = pydantic.Field(None, alias="MacAlgorithm")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class GenerateMacResponse(_KMSModelBase):
    mac: CiphertextType = pydantic.Field(None, alias="Mac")
    mac_algorithm: MacAlgorithmSpec = pydantic.Field(None, alias="MacAlgorithm")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class GenerateRandomRequest(_KMSModelBase):
    number_of_bytes: NumberOfBytesType = pydantic.Field(None, alias="NumberOfBytes")
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )
    recipient: "RecipientInfo" = pydantic.Field(None, alias="Recipient")


class GenerateRandomResponse(_KMSModelBase):
    plaintext: PlaintextType = pydantic.Field(None, alias="Plaintext")
    ciphertext_for_recipient: CiphertextType = pydantic.Field(
        None, alias="CiphertextForRecipient"
    )


class GetKeyPolicyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    policy_name: PolicyNameType = pydantic.Field(None, alias="PolicyName")


class GetKeyPolicyResponse(_KMSModelBase):
    policy: PolicyType = pydantic.Field(None, alias="Policy")


class GetKeyRotationStatusRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")


class GetKeyRotationStatusResponse(_KMSModelBase):
    key_rotation_enabled: BooleanType = pydantic.Field(None, alias="KeyRotationEnabled")


class GetParametersForImportRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    wrapping_algorithm: AlgorithmSpec = pydantic.Field(None, alias="WrappingAlgorithm")
    wrapping_key_spec: WrappingKeySpec = pydantic.Field(None, alias="WrappingKeySpec")


class GetParametersForImportResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    import_token: CiphertextType = pydantic.Field(None, alias="ImportToken")
    public_key: PlaintextType = pydantic.Field(None, alias="PublicKey")
    parameters_valid_to: DateType = pydantic.Field(None, alias="ParametersValidTo")


class GetPublicKeyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class GetPublicKeyResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    public_key: PublicKeyType = pydantic.Field(None, alias="PublicKey")
    customer_master_key_spec: CustomerMasterKeySpec = pydantic.Field(
        None, alias="CustomerMasterKeySpec"
    )
    key_spec: KeySpec = pydantic.Field(None, alias="KeySpec")
    key_usage: KeyUsageType = pydantic.Field(None, alias="KeyUsage")
    encryption_algorithms: EncryptionAlgorithmSpecList = pydantic.Field(
        None, alias="EncryptionAlgorithms"
    )
    signing_algorithms: SigningAlgorithmSpecList = pydantic.Field(
        None, alias="SigningAlgorithms"
    )


class GrantConstraints(_KMSModelBase):
    encryption_context_subset: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContextSubset"
    )
    encryption_context_equals: EncryptionContextType = pydantic.Field(
        None, alias="EncryptionContextEquals"
    )


class GrantListEntry(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grant_id: GrantIdType = pydantic.Field(None, alias="GrantId")
    name: GrantNameType = pydantic.Field(None, alias="Name")
    creation_date: DateType = pydantic.Field(None, alias="CreationDate")
    grantee_principal: PrincipalIdType = pydantic.Field(None, alias="GranteePrincipal")
    retiring_principal: PrincipalIdType = pydantic.Field(
        None, alias="RetiringPrincipal"
    )
    issuing_account: PrincipalIdType = pydantic.Field(None, alias="IssuingAccount")
    operations: GrantOperationList = pydantic.Field(None, alias="Operations")
    constraints: "GrantConstraints" = pydantic.Field(None, alias="Constraints")


class ImportKeyMaterialRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    import_token: CiphertextType = pydantic.Field(None, alias="ImportToken")
    encrypted_key_material: CiphertextType = pydantic.Field(
        None, alias="EncryptedKeyMaterial"
    )
    valid_to: DateType = pydantic.Field(None, alias="ValidTo")
    expiration_model: ExpirationModelType = pydantic.Field(
        None, alias="ExpirationModel"
    )


class ImportKeyMaterialResponse(_KMSModelBase):
    pass


class KeyListEntry(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    key_arn: ArnType = pydantic.Field(None, alias="KeyArn")


class KeyMetadata(_KMSModelBase):
    aws_account_id: AWSAccountIdType = pydantic.Field(None, alias="AWSAccountId")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    arn: ArnType = pydantic.Field(None, alias="Arn")
    creation_date: DateType = pydantic.Field(None, alias="CreationDate")
    enabled: BooleanType = pydantic.Field(None, alias="Enabled")
    description: DescriptionType = pydantic.Field(None, alias="Description")
    key_usage: KeyUsageType = pydantic.Field(None, alias="KeyUsage")
    key_state: KeyState = pydantic.Field(None, alias="KeyState")
    deletion_date: DateType = pydantic.Field(None, alias="DeletionDate")
    valid_to: DateType = pydantic.Field(None, alias="ValidTo")
    origin: OriginType = pydantic.Field(None, alias="Origin")
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )
    cloud_hsm_cluster_id: CloudHsmClusterIdType = pydantic.Field(
        None, alias="CloudHsmClusterId"
    )
    expiration_model: ExpirationModelType = pydantic.Field(
        None, alias="ExpirationModel"
    )
    key_manager: KeyManagerType = pydantic.Field(None, alias="KeyManager")
    customer_master_key_spec: CustomerMasterKeySpec = pydantic.Field(
        None, alias="CustomerMasterKeySpec"
    )
    key_spec: KeySpec = pydantic.Field(None, alias="KeySpec")
    encryption_algorithms: EncryptionAlgorithmSpecList = pydantic.Field(
        None, alias="EncryptionAlgorithms"
    )
    signing_algorithms: SigningAlgorithmSpecList = pydantic.Field(
        None, alias="SigningAlgorithms"
    )
    multi_region: NullableBooleanType = pydantic.Field(None, alias="MultiRegion")
    multi_region_configuration: "MultiRegionConfiguration" = pydantic.Field(
        None, alias="MultiRegionConfiguration"
    )
    pending_deletion_window_in_days: PendingWindowInDaysType = pydantic.Field(
        None, alias="PendingDeletionWindowInDays"
    )
    mac_algorithms: MacAlgorithmSpecList = pydantic.Field(None, alias="MacAlgorithms")
    xks_key_configuration: "XksKeyConfigurationType" = pydantic.Field(
        None, alias="XksKeyConfiguration"
    )


class ListAliasesRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")


class ListAliasesResponse(_KMSModelBase):
    aliases: AliasList = pydantic.Field(None, alias="Aliases")
    next_marker: MarkerType = pydantic.Field(None, alias="NextMarker")
    truncated: BooleanType = pydantic.Field(None, alias="Truncated")


class ListGrantsRequest(_KMSModelBase):
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grant_id: GrantIdType = pydantic.Field(None, alias="GrantId")
    grantee_principal: PrincipalIdType = pydantic.Field(None, alias="GranteePrincipal")


class ListGrantsResponse(_KMSModelBase):
    grants: GrantList = pydantic.Field(None, alias="Grants")
    next_marker: MarkerType = pydantic.Field(None, alias="NextMarker")
    truncated: BooleanType = pydantic.Field(None, alias="Truncated")


class ListKeyPoliciesRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")


class ListKeyPoliciesResponse(_KMSModelBase):
    policy_names: PolicyNameList = pydantic.Field(None, alias="PolicyNames")
    next_marker: MarkerType = pydantic.Field(None, alias="NextMarker")
    truncated: BooleanType = pydantic.Field(None, alias="Truncated")


class ListKeysRequest(_KMSModelBase):
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")


class ListKeysResponse(_KMSModelBase):
    keys: KeyList = pydantic.Field(None, alias="Keys")
    next_marker: MarkerType = pydantic.Field(None, alias="NextMarker")
    truncated: BooleanType = pydantic.Field(None, alias="Truncated")


class ListResourceTagsRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")


class ListResourceTagsResponse(_KMSModelBase):
    tags: TagList = pydantic.Field(None, alias="Tags")
    next_marker: MarkerType = pydantic.Field(None, alias="NextMarker")
    truncated: BooleanType = pydantic.Field(None, alias="Truncated")


class ListRetirableGrantsRequest(_KMSModelBase):
    limit: LimitType = pydantic.Field(None, alias="Limit")
    marker: MarkerType = pydantic.Field(None, alias="Marker")
    retiring_principal: PrincipalIdType = pydantic.Field(
        None, alias="RetiringPrincipal"
    )


class MultiRegionConfiguration(_KMSModelBase):
    multi_region_key_type: MultiRegionKeyType = pydantic.Field(
        None, alias="MultiRegionKeyType"
    )
    primary_key: "MultiRegionKey" = pydantic.Field(None, alias="PrimaryKey")
    replica_keys: MultiRegionKeyList = pydantic.Field(None, alias="ReplicaKeys")


class MultiRegionKey(_KMSModelBase):
    arn: ArnType = pydantic.Field(None, alias="Arn")
    region: RegionType = pydantic.Field(None, alias="Region")


class PutKeyPolicyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    policy_name: PolicyNameType = pydantic.Field(None, alias="PolicyName")
    policy: PolicyType = pydantic.Field(None, alias="Policy")
    bypass_policy_lockout_safety_check: BooleanType = pydantic.Field(
        None, alias="BypassPolicyLockoutSafetyCheck"
    )


class ReEncryptRequest(_KMSModelBase):
    ciphertext_blob: CiphertextType = pydantic.Field(None, alias="CiphertextBlob")
    source_encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="SourceEncryptionContext"
    )
    source_key_id: KeyIdType = pydantic.Field(None, alias="SourceKeyId")
    destination_key_id: KeyIdType = pydantic.Field(None, alias="DestinationKeyId")
    destination_encryption_context: EncryptionContextType = pydantic.Field(
        None, alias="DestinationEncryptionContext"
    )
    source_encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="SourceEncryptionAlgorithm"
    )
    destination_encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="DestinationEncryptionAlgorithm"
    )
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class ReEncryptResponse(_KMSModelBase):
    ciphertext_blob: CiphertextType = pydantic.Field(None, alias="CiphertextBlob")
    source_key_id: KeyIdType = pydantic.Field(None, alias="SourceKeyId")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    source_encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="SourceEncryptionAlgorithm"
    )
    destination_encryption_algorithm: EncryptionAlgorithmSpec = pydantic.Field(
        None, alias="DestinationEncryptionAlgorithm"
    )


class RecipientInfo(_KMSModelBase):
    key_encryption_algorithm: KeyEncryptionMechanism = pydantic.Field(
        None, alias="KeyEncryptionAlgorithm"
    )
    attestation_document: AttestationDocumentType = pydantic.Field(
        None, alias="AttestationDocument"
    )


class ReplicateKeyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    replica_region: RegionType = pydantic.Field(None, alias="ReplicaRegion")
    policy: PolicyType = pydantic.Field(None, alias="Policy")
    bypass_policy_lockout_safety_check: BooleanType = pydantic.Field(
        None, alias="BypassPolicyLockoutSafetyCheck"
    )
    description: DescriptionType = pydantic.Field(None, alias="Description")
    tags: TagList = pydantic.Field(None, alias="Tags")


class ReplicateKeyResponse(_KMSModelBase):
    replica_key_metadata: "KeyMetadata" = pydantic.Field(
        None, alias="ReplicaKeyMetadata"
    )
    replica_policy: PolicyType = pydantic.Field(None, alias="ReplicaPolicy")
    replica_tags: TagList = pydantic.Field(None, alias="ReplicaTags")


class RetireGrantRequest(_KMSModelBase):
    grant_token: GrantTokenType = pydantic.Field(None, alias="GrantToken")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grant_id: GrantIdType = pydantic.Field(None, alias="GrantId")


class RevokeGrantRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    grant_id: GrantIdType = pydantic.Field(None, alias="GrantId")


class ScheduleKeyDeletionRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    pending_window_in_days: PendingWindowInDaysType = pydantic.Field(
        None, alias="PendingWindowInDays"
    )


class ScheduleKeyDeletionResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    deletion_date: DateType = pydantic.Field(None, alias="DeletionDate")
    key_state: KeyState = pydantic.Field(None, alias="KeyState")
    pending_window_in_days: PendingWindowInDaysType = pydantic.Field(
        None, alias="PendingWindowInDays"
    )


class SignRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    message: PlaintextType = pydantic.Field(None, alias="Message")
    message_type: MessageType = pydantic.Field(None, alias="MessageType")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")
    signing_algorithm: SigningAlgorithmSpec = pydantic.Field(
        None, alias="SigningAlgorithm"
    )


class SignResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    signature: CiphertextType = pydantic.Field(None, alias="Signature")
    signing_algorithm: SigningAlgorithmSpec = pydantic.Field(
        None, alias="SigningAlgorithm"
    )


class Tag(_KMSModelBase):
    tag_key: TagKeyType = pydantic.Field(None, alias="TagKey")
    tag_value: TagValueType = pydantic.Field(None, alias="TagValue")


class TagResourceRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    tags: TagList = pydantic.Field(None, alias="Tags")


class UntagResourceRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    tag_keys: TagKeyList = pydantic.Field(None, alias="TagKeys")


class UpdateAliasRequest(_KMSModelBase):
    alias_name: AliasNameType = pydantic.Field(None, alias="AliasName")
    target_key_id: KeyIdType = pydantic.Field(None, alias="TargetKeyId")


class UpdateCustomKeyStoreRequest(_KMSModelBase):
    custom_key_store_id: CustomKeyStoreIdType = pydantic.Field(
        None, alias="CustomKeyStoreId"
    )
    new_custom_key_store_name: CustomKeyStoreNameType = pydantic.Field(
        None, alias="NewCustomKeyStoreName"
    )
    key_store_password: KeyStorePasswordType = pydantic.Field(
        None, alias="KeyStorePassword"
    )
    cloud_hsm_cluster_id: CloudHsmClusterIdType = pydantic.Field(
        None, alias="CloudHsmClusterId"
    )
    xks_proxy_uri_endpoint: XksProxyUriEndpointType = pydantic.Field(
        None, alias="XksProxyUriEndpoint"
    )
    xks_proxy_uri_path: XksProxyUriPathType = pydantic.Field(
        None, alias="XksProxyUriPath"
    )
    xks_proxy_vpc_endpoint_service_name: XksProxyVpcEndpointServiceNameType = (
        pydantic.Field(None, alias="XksProxyVpcEndpointServiceName")
    )
    xks_proxy_authentication_credential: "XksProxyAuthenticationCredentialType" = (
        pydantic.Field(None, alias="XksProxyAuthenticationCredential")
    )
    xks_proxy_connectivity: XksProxyConnectivityType = pydantic.Field(
        None, alias="XksProxyConnectivity"
    )


class UpdateCustomKeyStoreResponse(_KMSModelBase):
    pass


class UpdateKeyDescriptionRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    description: DescriptionType = pydantic.Field(None, alias="Description")


class UpdatePrimaryRegionRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    primary_region: RegionType = pydantic.Field(None, alias="PrimaryRegion")


class VerifyMacRequest(_KMSModelBase):
    message: PlaintextType = pydantic.Field(None, alias="Message")
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    mac_algorithm: MacAlgorithmSpec = pydantic.Field(None, alias="MacAlgorithm")
    mac: CiphertextType = pydantic.Field(None, alias="Mac")
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class VerifyMacResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    mac_valid: BooleanType = pydantic.Field(None, alias="MacValid")
    mac_algorithm: MacAlgorithmSpec = pydantic.Field(None, alias="MacAlgorithm")


class VerifyRequest(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    message: PlaintextType = pydantic.Field(None, alias="Message")
    message_type: MessageType = pydantic.Field(None, alias="MessageType")
    signature: CiphertextType = pydantic.Field(None, alias="Signature")
    signing_algorithm: SigningAlgorithmSpec = pydantic.Field(
        None, alias="SigningAlgorithm"
    )
    grant_tokens: GrantTokenList = pydantic.Field(None, alias="GrantTokens")


class VerifyResponse(_KMSModelBase):
    key_id: KeyIdType = pydantic.Field(None, alias="KeyId")
    signature_valid: BooleanType = pydantic.Field(None, alias="SignatureValid")
    signing_algorithm: SigningAlgorithmSpec = pydantic.Field(
        None, alias="SigningAlgorithm"
    )


class XksKeyConfigurationType(_KMSModelBase):
    id: XksKeyIdType = pydantic.Field(None, alias="Id")


class XksProxyAuthenticationCredentialType(_KMSModelBase):
    access_key_id: XksProxyAuthenticationAccessKeyIdType = pydantic.Field(
        None, alias="AccessKeyId"
    )
    raw_secret_access_key: XksProxyAuthenticationRawSecretAccessKeyType = (
        pydantic.Field(None, alias="RawSecretAccessKey")
    )


class XksProxyConfigurationType(_KMSModelBase):
    connectivity: XksProxyConnectivityType = pydantic.Field(None, alias="Connectivity")
    access_key_id: XksProxyAuthenticationAccessKeyIdType = pydantic.Field(
        None, alias="AccessKeyId"
    )
    uri_endpoint: XksProxyUriEndpointType = pydantic.Field(None, alias="UriEndpoint")
    uri_path: XksProxyUriPathType = pydantic.Field(None, alias="UriPath")
    vpc_endpoint_service_name: XksProxyVpcEndpointServiceNameType = pydantic.Field(
        None, alias="VpcEndpointServiceName"
    )


AliasListEntry.update_forward_refs()
CancelKeyDeletionRequest.update_forward_refs()
CancelKeyDeletionResponse.update_forward_refs()
ConnectCustomKeyStoreRequest.update_forward_refs()
ConnectCustomKeyStoreResponse.update_forward_refs()
CreateAliasRequest.update_forward_refs()
CreateCustomKeyStoreRequest.update_forward_refs()
CreateCustomKeyStoreResponse.update_forward_refs()
CreateGrantRequest.update_forward_refs()
CreateGrantResponse.update_forward_refs()
CreateKeyRequest.update_forward_refs()
CreateKeyResponse.update_forward_refs()
CustomKeyStoresListEntry.update_forward_refs()
DecryptRequest.update_forward_refs()
DecryptResponse.update_forward_refs()
DeleteAliasRequest.update_forward_refs()
DeleteCustomKeyStoreRequest.update_forward_refs()
DeleteCustomKeyStoreResponse.update_forward_refs()
DeleteImportedKeyMaterialRequest.update_forward_refs()
DescribeCustomKeyStoresRequest.update_forward_refs()
DescribeCustomKeyStoresResponse.update_forward_refs()
DescribeKeyRequest.update_forward_refs()
DescribeKeyResponse.update_forward_refs()
DisableKeyRequest.update_forward_refs()
DisableKeyRotationRequest.update_forward_refs()
DisconnectCustomKeyStoreRequest.update_forward_refs()
DisconnectCustomKeyStoreResponse.update_forward_refs()
EnableKeyRequest.update_forward_refs()
EnableKeyRotationRequest.update_forward_refs()
EncryptRequest.update_forward_refs()
EncryptResponse.update_forward_refs()
GenerateDataKeyPairRequest.update_forward_refs()
GenerateDataKeyPairResponse.update_forward_refs()
GenerateDataKeyPairWithoutPlaintextRequest.update_forward_refs()
GenerateDataKeyPairWithoutPlaintextResponse.update_forward_refs()
GenerateDataKeyRequest.update_forward_refs()
GenerateDataKeyResponse.update_forward_refs()
GenerateDataKeyWithoutPlaintextRequest.update_forward_refs()
GenerateDataKeyWithoutPlaintextResponse.update_forward_refs()
GenerateMacRequest.update_forward_refs()
GenerateMacResponse.update_forward_refs()
GenerateRandomRequest.update_forward_refs()
GenerateRandomResponse.update_forward_refs()
GetKeyPolicyRequest.update_forward_refs()
GetKeyPolicyResponse.update_forward_refs()
GetKeyRotationStatusRequest.update_forward_refs()
GetKeyRotationStatusResponse.update_forward_refs()
GetParametersForImportRequest.update_forward_refs()
GetParametersForImportResponse.update_forward_refs()
GetPublicKeyRequest.update_forward_refs()
GetPublicKeyResponse.update_forward_refs()
GrantConstraints.update_forward_refs()
GrantListEntry.update_forward_refs()
ImportKeyMaterialRequest.update_forward_refs()
ImportKeyMaterialResponse.update_forward_refs()
KeyListEntry.update_forward_refs()
KeyMetadata.update_forward_refs()
ListAliasesRequest.update_forward_refs()
ListAliasesResponse.update_forward_refs()
ListGrantsRequest.update_forward_refs()
ListGrantsResponse.update_forward_refs()
ListKeyPoliciesRequest.update_forward_refs()
ListKeyPoliciesResponse.update_forward_refs()
ListKeysRequest.update_forward_refs()
ListKeysResponse.update_forward_refs()
ListResourceTagsRequest.update_forward_refs()
ListResourceTagsResponse.update_forward_refs()
ListRetirableGrantsRequest.update_forward_refs()
MultiRegionConfiguration.update_forward_refs()
MultiRegionKey.update_forward_refs()
PutKeyPolicyRequest.update_forward_refs()
ReEncryptRequest.update_forward_refs()
ReEncryptResponse.update_forward_refs()
RecipientInfo.update_forward_refs()
ReplicateKeyRequest.update_forward_refs()
ReplicateKeyResponse.update_forward_refs()
RetireGrantRequest.update_forward_refs()
RevokeGrantRequest.update_forward_refs()
ScheduleKeyDeletionRequest.update_forward_refs()
ScheduleKeyDeletionResponse.update_forward_refs()
SignRequest.update_forward_refs()
SignResponse.update_forward_refs()
Tag.update_forward_refs()
TagResourceRequest.update_forward_refs()
UntagResourceRequest.update_forward_refs()
UpdateAliasRequest.update_forward_refs()
UpdateCustomKeyStoreRequest.update_forward_refs()
UpdateCustomKeyStoreResponse.update_forward_refs()
UpdateKeyDescriptionRequest.update_forward_refs()
UpdatePrimaryRegionRequest.update_forward_refs()
VerifyMacRequest.update_forward_refs()
VerifyMacResponse.update_forward_refs()
VerifyRequest.update_forward_refs()
VerifyResponse.update_forward_refs()
XksKeyConfigurationType.update_forward_refs()
XksProxyAuthenticationCredentialType.update_forward_refs()
XksProxyConfigurationType.update_forward_refs()
