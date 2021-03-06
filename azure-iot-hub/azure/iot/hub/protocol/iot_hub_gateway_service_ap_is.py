# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations.configuration_operations import ConfigurationOperations
from .operations.registry_manager_operations import RegistryManagerOperations
from .operations.job_client_operations import JobClientOperations
from .operations.fault_injection_operations import FaultInjectionOperations
from .operations.twin_operations import TwinOperations
from .operations.http_runtime_operations import HttpRuntimeOperations
from .operations.device_method_operations import DeviceMethodOperations
from . import models


class IotHubGatewayServiceAPIsConfiguration(Configuration):
    """Configuration for IotHubGatewayServiceAPIs
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = "https://fully-qualified-iothubname.azure-devices.net"

        super(IotHubGatewayServiceAPIsConfiguration, self).__init__(base_url)

        self.add_user_agent("iothubgatewayserviceapis/{}".format(VERSION))

        self.credentials = credentials


class IotHubGatewayServiceAPIs(SDKClient):
    """IotHubGatewayServiceAPIs

    :ivar config: Configuration for client.
    :vartype config: IotHubGatewayServiceAPIsConfiguration

    :ivar configuration: Configuration operations
    :vartype configuration: protocol.operations.ConfigurationOperations
    :ivar registry_manager: RegistryManager operations
    :vartype registry_manager: protocol.operations.RegistryManagerOperations
    :ivar job_client: JobClient operations
    :vartype job_client: protocol.operations.JobClientOperations
    :ivar fault_injection: FaultInjection operations
    :vartype fault_injection: protocol.operations.FaultInjectionOperations
    :ivar twin: Twin operations
    :vartype twin: protocol.operations.TwinOperations
    :ivar http_runtime: HttpRuntime operations
    :vartype http_runtime: protocol.operations.HttpRuntimeOperations
    :ivar device_method: DeviceMethod operations
    :vartype device_method: protocol.operations.DeviceMethodOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(self, credentials, base_url=None):

        self.config = IotHubGatewayServiceAPIsConfiguration(credentials, base_url)
        super(IotHubGatewayServiceAPIs, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = "2020-03-13"
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.configuration = ConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize
        )
        self.registry_manager = RegistryManagerOperations(
            self._client, self.config, self._serialize, self._deserialize
        )
        self.job_client = JobClientOperations(
            self._client, self.config, self._serialize, self._deserialize
        )
        self.fault_injection = FaultInjectionOperations(
            self._client, self.config, self._serialize, self._deserialize
        )
        self.twin = TwinOperations(self._client, self.config, self._serialize, self._deserialize)
        self.http_runtime = HttpRuntimeOperations(
            self._client, self.config, self._serialize, self._deserialize
        )
        self.device_method = DeviceMethodOperations(
            self._client, self.config, self._serialize, self._deserialize
        )
