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
from msrestazure.azure_exceptions import CloudError

from .. import models


class AnalyticsItemsOperations(object):
    """AnalyticsItemsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2015-05-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2015-05-01"

        self.config = config

    def list(
            self, resource_group_name, resource_name, scope_path, scope="shared", type="none", include_content=None, custom_headers=None, raw=False, **operation_config):
        """Gets a list of Analytics Items defined within an Application Insights
        component.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component
         resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by
         a specific user or is shared between all users with access to the
         Application Insights component. Possible values include:
         'analyticsItems', 'myanalyticsItems'
        :type scope_path: str or
         ~azure.mgmt.applicationinsights.models.ItemScopePath
        :param scope: Enum indicating if this item definition is owned by a
         specific user or is shared between all users with access to the
         Application Insights component. Possible values include: 'shared',
         'user'
        :type scope: str or ~azure.mgmt.applicationinsights.models.ItemScope
        :param type: Enum indicating the type of the Analytics item. Possible
         values include: 'none', 'query', 'function', 'folder', 'recent'
        :type type: str or
         ~azure.mgmt.applicationinsights.models.ItemTypeParameter
        :param include_content: Flag indicating whether or not to return the
         content of each applicable item. If false, only return the item
         information.
        :type include_content: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.mgmt.applicationinsights.models.ApplicationInsightsComponentAnalyticsItem]
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'scopePath': self._serialize.url("scope_path", scope_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        if type is not None:
            query_parameters['type'] = self._serialize.query("type", type, 'str')
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query("include_content", include_content, 'bool')

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
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[ApplicationInsightsComponentAnalyticsItem]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}'}

    def get(
            self, resource_group_name, resource_name, scope_path, id=None, name=None, custom_headers=None, raw=False, **operation_config):
        """Gets a specific Analytics Items defined within an Application Insights
        component.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component
         resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by
         a specific user or is shared between all users with access to the
         Application Insights component. Possible values include:
         'analyticsItems', 'myanalyticsItems'
        :type scope_path: str or
         ~azure.mgmt.applicationinsights.models.ItemScopePath
        :param id: The Id of a specific item defined in the Application
         Insights component
        :type id: str
        :param name: The name of a specific item defined in the Application
         Insights component
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ApplicationInsightsComponentAnalyticsItem or
         ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.applicationinsights.models.ApplicationInsightsComponentAnalyticsItem
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'scopePath': self._serialize.url("scope_path", scope_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if id is not None:
            query_parameters['id'] = self._serialize.query("id", id, 'str')
        if name is not None:
            query_parameters['name'] = self._serialize.query("name", name, 'str')

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
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ApplicationInsightsComponentAnalyticsItem', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item'}

    def put(
            self, resource_group_name, resource_name, scope_path, item_properties, override_item=None, custom_headers=None, raw=False, **operation_config):
        """Adds or Updates a specific Analytics Item within an Application
        Insights component.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component
         resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by
         a specific user or is shared between all users with access to the
         Application Insights component. Possible values include:
         'analyticsItems', 'myanalyticsItems'
        :type scope_path: str or
         ~azure.mgmt.applicationinsights.models.ItemScopePath
        :param item_properties: Properties that need to be specified to create
         a new item and add it to an Application Insights component.
        :type item_properties:
         ~azure.mgmt.applicationinsights.models.ApplicationInsightsComponentAnalyticsItem
        :param override_item: Flag indicating whether or not to force save an
         item. This allows overriding an item if it already exists.
        :type override_item: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ApplicationInsightsComponentAnalyticsItem or
         ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.applicationinsights.models.ApplicationInsightsComponentAnalyticsItem
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.put.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'scopePath': self._serialize.url("scope_path", scope_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if override_item is not None:
            query_parameters['overrideItem'] = self._serialize.query("override_item", override_item, 'bool')

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
        body_content = self._serialize.body(item_properties, 'ApplicationInsightsComponentAnalyticsItem')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ApplicationInsightsComponentAnalyticsItem', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    put.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item'}

    def delete(
            self, resource_group_name, resource_name, scope_path, id=None, name=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a specific Analytics Items defined within an Application
        Insights component.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component
         resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by
         a specific user or is shared between all users with access to the
         Application Insights component. Possible values include:
         'analyticsItems', 'myanalyticsItems'
        :type scope_path: str or
         ~azure.mgmt.applicationinsights.models.ItemScopePath
        :param id: The Id of a specific item defined in the Application
         Insights component
        :type id: str
        :param name: The name of a specific item defined in the Application
         Insights component
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'scopePath': self._serialize.url("scope_path", scope_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if id is not None:
            query_parameters['id'] = self._serialize.query("id", id, 'str')
        if name is not None:
            query_parameters['name'] = self._serialize.query("name", name, 'str')

        # Construct headers
        header_parameters = {}
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
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item'}
