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


class KeyOperationsParameters(Model):
    """The key operations parameters.

    All required parameters must be populated in order to send to Azure.

    :param algorithm: Required. algorithm identifier. Possible values include:
     'RSA-OAEP', 'RSA-OAEP-256', 'RSA1_5'
    :type algorithm: str or
     ~azure.keyvault.models.JsonWebKeyEncryptionAlgorithm
    :param value: Required.
    :type value: bytes
    """

    _validation = {
        'algorithm': {'required': True, 'min_length': 1},
        'value': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, **kwargs):
        super(KeyOperationsParameters, self).__init__(**kwargs)
        self.algorithm = kwargs.get('algorithm', None)
        self.value = kwargs.get('value', None)