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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class DscNodeOperations(object):
    """DscNodeOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2018-01-15".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-01-15"

        self.config = config

    def delete(
            self, resource_group_name, automation_account_name, node_id, custom_headers=None, raw=False, **operation_config):
        """Delete the dsc node identified by node id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param node_id: The node id.
        :type node_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DscNode or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.automation.models.DscNode or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.automation.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'nodeId': self._serialize.url("node_id", node_id, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DscNode', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId}'}

    def get(
            self, resource_group_name, automation_account_name, node_id, custom_headers=None, raw=False, **operation_config):
        """Retrieve the dsc node identified by node id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param node_id: The node id.
        :type node_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DscNode or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.automation.models.DscNode or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.automation.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'nodeId': self._serialize.url("node_id", node_id, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DscNode', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId}'}

    def update(
            self, resource_group_name, automation_account_name, node_id, node_id1=None, properties=None, custom_headers=None, raw=False, **operation_config):
        """Update the dsc node.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param node_id: Parameters supplied to the update dsc node.
        :type node_id: str
        :param node_id1: Gets or sets the id of the dsc node.
        :type node_id1: str
        :param properties:
        :type properties:
         ~azure.mgmt.automation.models.DscNodeUpdateParametersProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DscNode or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.automation.models.DscNode or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.automation.models.ErrorResponseException>`
        """
        dsc_node_update_parameters = models.DscNodeUpdateParameters(node_id=node_id1, properties=properties)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'nodeId': self._serialize.url("node_id", node_id, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(dsc_node_update_parameters, 'DscNodeUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DscNode', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId}'}

    def list_by_automation_account(
            self, resource_group_name, automation_account_name, filter=None, skip=None, top=None, inlinecount=None, custom_headers=None, raw=False, **operation_config):
        """Retrieve a list of dsc nodes.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :param skip: The number of rows to skip.
        :type skip: int
        :param top: The the number of rows to take.
        :type top: int
        :param inlinecount: Return total rows.
        :type inlinecount: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DscNode
        :rtype:
         ~azure.mgmt.automation.models.DscNodePaged[~azure.mgmt.automation.models.DscNode]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.automation.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_automation_account.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
                    'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if inlinecount is not None:
                    query_parameters['$inlinecount'] = self._serialize.query("inlinecount", inlinecount, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.DscNodePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.DscNodePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_automation_account.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes'}
