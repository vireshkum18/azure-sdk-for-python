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


class ModelDescription(Model):
    """An object describing supported model by name and categories.

    :param name:
    :type name: str
    :param categories:
    :type categories: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'categories': {'key': 'categories', 'type': '[str]'},
    }

    def __init__(self, name=None, categories=None):
        super(ModelDescription, self).__init__()
        self.name = name
        self.categories = categories