# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.namespaces_operations import NamespacesOperations
from .operations.hybrid_connections_operations import HybridConnectionsOperations
from .operations.wcf_relays_operations import WCFRelaysOperations
from . import models


class RelayManagementClientConfiguration(AzureConfiguration):
    """Configuration for RelayManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     the Microsoft Azure subscription. The subscription ID forms part of the
     URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(RelayManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-relay/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class RelayManagementClient(object):
    """Use these API to manage Azure Relay resources through Azure Resource Manager.

    :ivar config: Configuration for client.
    :vartype config: RelayManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.relay.operations.Operations
    :ivar namespaces: Namespaces operations
    :vartype namespaces: azure.mgmt.relay.operations.NamespacesOperations
    :ivar hybrid_connections: HybridConnections operations
    :vartype hybrid_connections: azure.mgmt.relay.operations.HybridConnectionsOperations
    :ivar wcf_relays: WCFRelays operations
    :vartype wcf_relays: azure.mgmt.relay.operations.WCFRelaysOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     the Microsoft Azure subscription. The subscription ID forms part of the
     URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = RelayManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.namespaces = NamespacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hybrid_connections = HybridConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.wcf_relays = WCFRelaysOperations(
            self._client, self.config, self._serialize, self._deserialize)
