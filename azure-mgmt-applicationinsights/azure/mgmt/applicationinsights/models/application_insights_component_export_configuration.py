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

from msrest.serialization import Model


class ApplicationInsightsComponentExportConfiguration(Model):
    """Properties that define a Continuous Export configuration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar export_id: The unique ID of the export configuration inside an
     Application Insights component. It is auto generated when the Continuous
     Export configuration is created.
    :vartype export_id: str
    :ivar instrumentation_key: The instrumentation key of the Application
     Insights component.
    :vartype instrumentation_key: str
    :param record_types: This comma separated list of document types that will
     be exported. The possible values include 'Requests', 'Event',
     'Exceptions', 'Metrics', 'PageViews', 'PageViewPerformance', 'Rdd',
     'PerformanceCounters', 'Availability', 'Messages'.
    :type record_types: str
    :ivar application_name: The name of the Application Insights component.
    :vartype application_name: str
    :ivar subscription_id: The subscription of the Application Insights
     component.
    :vartype subscription_id: str
    :ivar resource_group: The resource group of the Application Insights
     component.
    :vartype resource_group: str
    :ivar destination_storage_subscription_id: The destination storage account
     subscription ID.
    :vartype destination_storage_subscription_id: str
    :ivar destination_storage_location_id: The destination account location
     ID.
    :vartype destination_storage_location_id: str
    :ivar destination_account_id: The name of destination account.
    :vartype destination_account_id: str
    :ivar destination_type: The destination type.
    :vartype destination_type: str
    :ivar is_user_enabled: This will be 'true' if the Continuous Export
     configuration is enabled, otherwise it will be 'false'.
    :vartype is_user_enabled: str
    :ivar last_user_update: Last time the Continuous Export configuration was
     updated.
    :vartype last_user_update: str
    :param notification_queue_enabled: Deprecated
    :type notification_queue_enabled: str
    :ivar export_status: This indicates current Continuous Export
     configuration status. The possible values are 'Preparing', 'Success',
     'Failure'.
    :vartype export_status: str
    :ivar last_success_time: The last time data was successfully delivered to
     the destination storage container for this Continuous Export
     configuration.
    :vartype last_success_time: str
    :ivar last_gap_time: The last time the Continuous Export configuration
     started failing.
    :vartype last_gap_time: str
    :ivar permanent_error_reason: This is the reason the Continuous Export
     configuration started failing. It can be 'AzureStorageNotFound' or
     'AzureStorageAccessDenied'.
    :vartype permanent_error_reason: str
    :ivar storage_name: The name of the destination storage account.
    :vartype storage_name: str
    :ivar container_name: The name of the destination storage container.
    :vartype container_name: str
    """

    _validation = {
        'export_id': {'readonly': True},
        'instrumentation_key': {'readonly': True},
        'application_name': {'readonly': True},
        'subscription_id': {'readonly': True},
        'resource_group': {'readonly': True},
        'destination_storage_subscription_id': {'readonly': True},
        'destination_storage_location_id': {'readonly': True},
        'destination_account_id': {'readonly': True},
        'destination_type': {'readonly': True},
        'is_user_enabled': {'readonly': True},
        'last_user_update': {'readonly': True},
        'export_status': {'readonly': True},
        'last_success_time': {'readonly': True},
        'last_gap_time': {'readonly': True},
        'permanent_error_reason': {'readonly': True},
        'storage_name': {'readonly': True},
        'container_name': {'readonly': True},
    }

    _attribute_map = {
        'export_id': {'key': 'ExportId', 'type': 'str'},
        'instrumentation_key': {'key': 'InstrumentationKey', 'type': 'str'},
        'record_types': {'key': 'RecordTypes', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'subscription_id': {'key': 'SubscriptionId', 'type': 'str'},
        'resource_group': {'key': 'ResourceGroup', 'type': 'str'},
        'destination_storage_subscription_id': {'key': 'DestinationStorageSubscriptionId', 'type': 'str'},
        'destination_storage_location_id': {'key': 'DestinationStorageLocationId', 'type': 'str'},
        'destination_account_id': {'key': 'DestinationAccountId', 'type': 'str'},
        'destination_type': {'key': 'DestinationType', 'type': 'str'},
        'is_user_enabled': {'key': 'IsUserEnabled', 'type': 'str'},
        'last_user_update': {'key': 'LastUserUpdate', 'type': 'str'},
        'notification_queue_enabled': {'key': 'NotificationQueueEnabled', 'type': 'str'},
        'export_status': {'key': 'ExportStatus', 'type': 'str'},
        'last_success_time': {'key': 'LastSuccessTime', 'type': 'str'},
        'last_gap_time': {'key': 'LastGapTime', 'type': 'str'},
        'permanent_error_reason': {'key': 'PermanentErrorReason', 'type': 'str'},
        'storage_name': {'key': 'StorageName', 'type': 'str'},
        'container_name': {'key': 'ContainerName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationInsightsComponentExportConfiguration, self).__init__(**kwargs)
        self.export_id = None
        self.instrumentation_key = None
        self.record_types = kwargs.get('record_types', None)
        self.application_name = None
        self.subscription_id = None
        self.resource_group = None
        self.destination_storage_subscription_id = None
        self.destination_storage_location_id = None
        self.destination_account_id = None
        self.destination_type = None
        self.is_user_enabled = None
        self.last_user_update = None
        self.notification_queue_enabled = kwargs.get('notification_queue_enabled', None)
        self.export_status = None
        self.last_success_time = None
        self.last_gap_time = None
        self.permanent_error_reason = None
        self.storage_name = None
        self.container_name = None
