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


class BackupStatusResponse(Model):
    """BackupStatus response.

    :param protection_status: Specifies whether the container is registered or
     not. Possible values include: 'Invalid', 'NotProtected', 'Protecting',
     'Protected', 'ProtectionFailed'
    :type protection_status: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param fabric_name: Specifies the fabric name - Azure or AD. Possible
     values include: 'Invalid', 'Azure'
    :type fabric_name: str or
     ~azure.mgmt.recoveryservicesbackup.models.FabricName
    :param container_name: Specifies the product specific container name. E.g.
     iaasvmcontainer;iaasvmcontainer;csname;vmname.
    :type container_name: str
    :param protected_item_name: Specifies the product specific ds name. E.g.
     vm;iaasvmcontainer;csname;vmname.
    :type protected_item_name: str
    :param error_code: ErrorCode in case of intent failed
    :type error_code: str
    :param error_message: ErrorMessage in case of intent failed.
    :type error_message: str
    :param policy_name: Specifies the policy name which is used for protection
    :type policy_name: str
    :param registration_status: Container registration status
    :type registration_status: str
    """

    _attribute_map = {
        'protection_status': {'key': 'protectionStatus', 'type': 'str'},
        'fabric_name': {'key': 'fabricName', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'protected_item_name': {'key': 'protectedItemName', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'},
        'registration_status': {'key': 'registrationStatus', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BackupStatusResponse, self).__init__(**kwargs)
        self.protection_status = kwargs.get('protection_status', None)
        self.fabric_name = kwargs.get('fabric_name', None)
        self.container_name = kwargs.get('container_name', None)
        self.protected_item_name = kwargs.get('protected_item_name', None)
        self.error_code = kwargs.get('error_code', None)
        self.error_message = kwargs.get('error_message', None)
        self.policy_name = kwargs.get('policy_name', None)
        self.registration_status = kwargs.get('registration_status', None)
