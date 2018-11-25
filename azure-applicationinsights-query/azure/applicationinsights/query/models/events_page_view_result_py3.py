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

from .events_result_data_py3 import EventsResultData


class EventsPageViewResult(EventsResultData):
    """A page view result.

    All required parameters must be populated in order to send to Azure.

    :param id: The unique ID for this event.
    :type id: str
    :param count: Count of the event
    :type count: long
    :param timestamp: Timestamp of the event
    :type timestamp: datetime
    :param custom_dimensions: Custom dimensions of the event
    :type custom_dimensions:
     ~azure.applicationinsights.query.models.EventsResultDataCustomDimensions
    :param custom_measurements: Custom measurements of the event
    :type custom_measurements:
     ~azure.applicationinsights.query.models.EventsResultDataCustomMeasurements
    :param operation: Operation info of the event
    :type operation:
     ~azure.applicationinsights.query.models.EventsOperationInfo
    :param session: Session info of the event
    :type session: ~azure.applicationinsights.query.models.EventsSessionInfo
    :param user: User info of the event
    :type user: ~azure.applicationinsights.query.models.EventsUserInfo
    :param cloud: Cloud info of the event
    :type cloud: ~azure.applicationinsights.query.models.EventsCloudInfo
    :param ai: AI info of the event
    :type ai: ~azure.applicationinsights.query.models.EventsAiInfo
    :param application: Application info of the event
    :type application:
     ~azure.applicationinsights.query.models.EventsApplicationInfo
    :param client: Client info of the event
    :type client: ~azure.applicationinsights.query.models.EventsClientInfo
    :param type: Required. Constant filled by server.
    :type type: str
    :param page_view:
    :type page_view:
     ~azure.applicationinsights.query.models.EventsPageViewInfo
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'count': {'key': 'count', 'type': 'long'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'custom_dimensions': {'key': 'customDimensions', 'type': 'EventsResultDataCustomDimensions'},
        'custom_measurements': {'key': 'customMeasurements', 'type': 'EventsResultDataCustomMeasurements'},
        'operation': {'key': 'operation', 'type': 'EventsOperationInfo'},
        'session': {'key': 'session', 'type': 'EventsSessionInfo'},
        'user': {'key': 'user', 'type': 'EventsUserInfo'},
        'cloud': {'key': 'cloud', 'type': 'EventsCloudInfo'},
        'ai': {'key': 'ai', 'type': 'EventsAiInfo'},
        'application': {'key': 'application', 'type': 'EventsApplicationInfo'},
        'client': {'key': 'client', 'type': 'EventsClientInfo'},
        'type': {'key': 'type', 'type': 'str'},
        'page_view': {'key': 'pageView', 'type': 'EventsPageViewInfo'},
    }

    def __init__(self, *, id: str=None, count: int=None, timestamp=None, custom_dimensions=None, custom_measurements=None, operation=None, session=None, user=None, cloud=None, ai=None, application=None, client=None, page_view=None, **kwargs) -> None:
        super(EventsPageViewResult, self).__init__(id=id, count=count, timestamp=timestamp, custom_dimensions=custom_dimensions, custom_measurements=custom_measurements, operation=operation, session=session, user=user, cloud=cloud, ai=ai, application=application, client=client, **kwargs)
        self.page_view = page_view
        self.type = 'pageView'
