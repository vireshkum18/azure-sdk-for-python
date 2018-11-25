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


class EventsAvailabilityResultInfo(Model):
    """The availability result info.

    :param name: The name of the availability result
    :type name: str
    :param success: Indicates if the availability result was successful
    :type success: str
    :param duration: The duration of the availability result
    :type duration: long
    :param performance_bucket: The performance bucket of the availability
     result
    :type performance_bucket: str
    :param message: The message of the availability result
    :type message: str
    :param location: The location of the availability result
    :type location: str
    :param id: The ID of the availability result
    :type id: str
    :param size: The size of the availability result
    :type size: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'success': {'key': 'success', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'long'},
        'performance_bucket': {'key': 'performanceBucket', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventsAvailabilityResultInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.success = kwargs.get('success', None)
        self.duration = kwargs.get('duration', None)
        self.performance_bucket = kwargs.get('performance_bucket', None)
        self.message = kwargs.get('message', None)
        self.location = kwargs.get('location', None)
        self.id = kwargs.get('id', None)
        self.size = kwargs.get('size', None)
