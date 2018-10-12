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


class ChargesOperations(object):
    """ChargesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. The current version is 2018-08-31. Constant value: "2018-08-31".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-08-31"

        self.config = config

    def list_by_enrollment_account(
            self, billing_account_id, enrollment_account_id, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists the charges by enrollmentAccountId.

        :param billing_account_id: BillingAccount ID
        :type billing_account_id: str
        :param enrollment_account_id: EnrollmentAccount ID
        :type enrollment_account_id: str
        :param filter: May be used to filter charges by properties/usageEnd
         (Utc time), properties/usageStart (Utc time). The filter supports
         'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support
         'ne', 'or', or 'not'. Tag filter is a key value pair string where key
         and value is separated by a colon (:).
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ChargesListResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.consumption.models.ChargesListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.consumption.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_by_enrollment_account.metadata['url']
        path_format_arguments = {
            'billingAccountId': self._serialize.url("billing_account_id", billing_account_id, 'str'),
            'enrollmentAccountId': self._serialize.url("enrollment_account_id", enrollment_account_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

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
            deserialized = self._deserialize('ChargesListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_by_enrollment_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.Consumption/charges'}

    def list_for_billing_period_by_enrollment_account(
            self, billing_account_id, enrollment_account_id, billing_period_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists the charges based on enrollmentAccountId by billing period.

        :param billing_account_id: BillingAccount ID
        :type billing_account_id: str
        :param enrollment_account_id: EnrollmentAccount ID
        :type enrollment_account_id: str
        :param billing_period_name: Billing Period Name.
        :type billing_period_name: str
        :param filter: May be used to filter charges by properties/usageEnd
         (Utc time), properties/usageStart (Utc time). The filter supports
         'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support
         'ne', 'or', or 'not'. Tag filter is a key value pair string where key
         and value is separated by a colon (:).
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ChargeSummary or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.consumption.models.ChargeSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.consumption.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_for_billing_period_by_enrollment_account.metadata['url']
        path_format_arguments = {
            'billingAccountId': self._serialize.url("billing_account_id", billing_account_id, 'str'),
            'enrollmentAccountId': self._serialize.url("enrollment_account_id", enrollment_account_id, 'str'),
            'billingPeriodName': self._serialize.url("billing_period_name", billing_period_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

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
            deserialized = self._deserialize('ChargeSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_for_billing_period_by_enrollment_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/charges'}

    def list_by_department(
            self, billing_account_id, department_id, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists the charges by departmentId.

        :param billing_account_id: BillingAccount ID
        :type billing_account_id: str
        :param department_id: Department ID
        :type department_id: str
        :param filter: May be used to filter charges by properties/usageEnd
         (Utc time), properties/usageStart (Utc time). The filter supports
         'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support
         'ne', 'or', or 'not'. Tag filter is a key value pair string where key
         and value is separated by a colon (:).
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ChargesListResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.consumption.models.ChargesListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.consumption.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_by_department.metadata['url']
        path_format_arguments = {
            'billingAccountId': self._serialize.url("billing_account_id", billing_account_id, 'str'),
            'departmentId': self._serialize.url("department_id", department_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

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
            deserialized = self._deserialize('ChargesListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_by_department.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Consumption/charges'}

    def list_for_billing_period_by_department(
            self, billing_account_id, department_id, billing_period_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists the charges based on departmentId by billing period.

        :param billing_account_id: BillingAccount ID
        :type billing_account_id: str
        :param department_id: Department ID
        :type department_id: str
        :param billing_period_name: Billing Period Name.
        :type billing_period_name: str
        :param filter: May be used to filter charges by properties/usageEnd
         (Utc time), properties/usageStart (Utc time). The filter supports
         'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support
         'ne', 'or', or 'not'. Tag filter is a key value pair string where key
         and value is separated by a colon (:).
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ChargeSummary or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.consumption.models.ChargeSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.consumption.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_for_billing_period_by_department.metadata['url']
        path_format_arguments = {
            'billingAccountId': self._serialize.url("billing_account_id", billing_account_id, 'str'),
            'departmentId': self._serialize.url("department_id", department_id, 'str'),
            'billingPeriodName': self._serialize.url("billing_period_name", billing_period_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

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
            deserialized = self._deserialize('ChargeSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_for_billing_period_by_department.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/charges'}
