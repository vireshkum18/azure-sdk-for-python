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

from .components_resource_py3 import ComponentsResource


class ApplicationInsightsComponent(ComponentsResource):
    """An Application Insights component definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param kind: Required. The kind of application that this component refers
     to, used to customize UI. This value is a freeform string, values should
     typically be one of the following: web, ios, other, store, java, phone.
    :type kind: str
    :ivar application_id: The unique ID of your application. This field
     mirrors the 'Name' field and cannot be changed.
    :vartype application_id: str
    :ivar app_id: Application Insights Unique ID for your Application.
    :vartype app_id: str
    :param application_type: Required. Type of application being monitored.
     Possible values include: 'web', 'other'. Default value: "web" .
    :type application_type: str or
     ~azure.mgmt.applicationinsights.models.ApplicationType
    :param flow_type: Used by the Application Insights system to determine
     what kind of flow this component was created by. This is to be set to
     'Bluefield' when creating/updating a component via the REST API. Possible
     values include: 'Bluefield'. Default value: "Bluefield" .
    :type flow_type: str or ~azure.mgmt.applicationinsights.models.FlowType
    :param request_source: Describes what tool created this Application
     Insights component. Customers using this API should set this to the
     default 'rest'. Possible values include: 'rest'. Default value: "rest" .
    :type request_source: str or
     ~azure.mgmt.applicationinsights.models.RequestSource
    :ivar instrumentation_key: Application Insights Instrumentation key. A
     read-only value that applications can use to identify the destination for
     all telemetry sent to Azure Application Insights. This value will be
     supplied upon construction of each new Application Insights component.
    :vartype instrumentation_key: str
    :ivar creation_date: Creation Date for the Application Insights component,
     in ISO 8601 format.
    :vartype creation_date: datetime
    :ivar tenant_id: Azure Tenant Id.
    :vartype tenant_id: str
    :param hockey_app_id: The unique application ID created when a new
     application is added to HockeyApp, used for communications with HockeyApp.
    :type hockey_app_id: str
    :ivar hockey_app_token: Token used to authenticate communications with
     between Application Insights and HockeyApp.
    :vartype hockey_app_token: str
    :ivar provisioning_state: Current state of this component: whether or not
     is has been provisioned within the resource group it is defined. Users
     cannot change this value but are able to read from it. Values will include
     Succeeded, Deploying, Canceled, and Failed.
    :vartype provisioning_state: str
    :param sampling_percentage: Percentage of the data produced by the
     application being monitored that is being sampled for Application Insights
     telemetry.
    :type sampling_percentage: float
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'kind': {'required': True},
        'application_id': {'readonly': True},
        'app_id': {'readonly': True},
        'application_type': {'required': True},
        'instrumentation_key': {'readonly': True},
        'creation_date': {'readonly': True},
        'tenant_id': {'readonly': True},
        'hockey_app_token': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'application_id': {'key': 'properties.ApplicationId', 'type': 'str'},
        'app_id': {'key': 'properties.AppId', 'type': 'str'},
        'application_type': {'key': 'properties.Application_Type', 'type': 'str'},
        'flow_type': {'key': 'properties.Flow_Type', 'type': 'str'},
        'request_source': {'key': 'properties.Request_Source', 'type': 'str'},
        'instrumentation_key': {'key': 'properties.InstrumentationKey', 'type': 'str'},
        'creation_date': {'key': 'properties.CreationDate', 'type': 'iso-8601'},
        'tenant_id': {'key': 'properties.TenantId', 'type': 'str'},
        'hockey_app_id': {'key': 'properties.HockeyAppId', 'type': 'str'},
        'hockey_app_token': {'key': 'properties.HockeyAppToken', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'sampling_percentage': {'key': 'properties.SamplingPercentage', 'type': 'float'},
    }

    def __init__(self, *, location: str, kind: str, tags=None, application_type="web", flow_type="Bluefield", request_source="rest", hockey_app_id: str=None, sampling_percentage: float=None, **kwargs) -> None:
        super(ApplicationInsightsComponent, self).__init__(location=location, tags=tags, **kwargs)
        self.kind = kind
        self.application_id = None
        self.app_id = None
        self.application_type = application_type
        self.flow_type = flow_type
        self.request_source = request_source
        self.instrumentation_key = None
        self.creation_date = None
        self.tenant_id = None
        self.hockey_app_id = hockey_app_id
        self.hockey_app_token = None
        self.provisioning_state = None
        self.sampling_percentage = sampling_percentage
