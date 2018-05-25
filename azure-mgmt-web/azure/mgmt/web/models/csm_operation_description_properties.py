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


class CsmOperationDescriptionProperties(Model):
    """Properties available for a Microsoft.Web resource provider operation.

    :param service_specification:
    :type service_specification: ~azure.mgmt.web.models.ServiceSpecification
    """

    _attribute_map = {
        'service_specification': {'key': 'serviceSpecification', 'type': 'ServiceSpecification'},
    }

    def __init__(self, service_specification=None):
        super(CsmOperationDescriptionProperties, self).__init__()
        self.service_specification = service_specification