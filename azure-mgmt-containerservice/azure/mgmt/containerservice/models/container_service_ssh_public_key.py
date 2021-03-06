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


class ContainerServiceSshPublicKey(Model):
    """Contains information about SSH certificate public key data.

    All required parameters must be populated in order to send to Azure.

    :param key_data: Required. Certificate public key used to authenticate
     with VMs through SSH. The certificate must be in PEM format with or
     without headers.
    :type key_data: str
    """

    _validation = {
        'key_data': {'required': True},
    }

    _attribute_map = {
        'key_data': {'key': 'keyData', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceSshPublicKey, self).__init__(**kwargs)
        self.key_data = kwargs.get('key_data', None)
