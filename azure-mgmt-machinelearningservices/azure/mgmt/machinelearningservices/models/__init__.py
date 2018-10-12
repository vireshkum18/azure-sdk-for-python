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

try:
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .workspace_py3 import Workspace
    from .workspace_update_parameters_py3 import WorkspaceUpdateParameters
    from .identity_py3 import Identity
    from .resource_py3 import Resource
    from .password_py3 import Password
    from .registry_list_credentials_result_py3 import RegistryListCredentialsResult
    from .list_workspace_keys_result_py3 import ListWorkspaceKeysResult
    from .error_detail_py3 import ErrorDetail
    from .error_response_py3 import ErrorResponse
    from .machine_learning_service_error_py3 import MachineLearningServiceError, MachineLearningServiceErrorException
    from .compute_py3 import Compute
    from .compute_resource_py3 import ComputeResource
    from .system_service_py3 import SystemService
    from .ssl_configuration_py3 import SslConfiguration
    from .aks_properties_py3 import AKSProperties
    from .aks_py3 import AKS
    from .scale_settings_py3 import ScaleSettings
    from .batch_ai_properties_py3 import BatchAIProperties
    from .batch_ai_py3 import BatchAI
    from .virtual_machine_ssh_credentials_py3 import VirtualMachineSshCredentials
    from .virtual_machine_properties_py3 import VirtualMachineProperties
    from .virtual_machine_py3 import VirtualMachine
    from .hd_insight_properties_py3 import HDInsightProperties
    from .hd_insight_py3 import HDInsight
    from .data_factory_py3 import DataFactory
    from .service_principal_credentials_py3 import ServicePrincipalCredentials
    from .compute_secrets_py3 import ComputeSecrets
    from .aks_compute_secrets_py3 import AksComputeSecrets
    from .virtual_machine_secrets_py3 import VirtualMachineSecrets
except (SyntaxError, ImportError):
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .workspace import Workspace
    from .workspace_update_parameters import WorkspaceUpdateParameters
    from .identity import Identity
    from .resource import Resource
    from .password import Password
    from .registry_list_credentials_result import RegistryListCredentialsResult
    from .list_workspace_keys_result import ListWorkspaceKeysResult
    from .error_detail import ErrorDetail
    from .error_response import ErrorResponse
    from .machine_learning_service_error import MachineLearningServiceError, MachineLearningServiceErrorException
    from .compute import Compute
    from .compute_resource import ComputeResource
    from .system_service import SystemService
    from .ssl_configuration import SslConfiguration
    from .aks_properties import AKSProperties
    from .aks import AKS
    from .scale_settings import ScaleSettings
    from .batch_ai_properties import BatchAIProperties
    from .batch_ai import BatchAI
    from .virtual_machine_ssh_credentials import VirtualMachineSshCredentials
    from .virtual_machine_properties import VirtualMachineProperties
    from .virtual_machine import VirtualMachine
    from .hd_insight_properties import HDInsightProperties
    from .hd_insight import HDInsight
    from .data_factory import DataFactory
    from .service_principal_credentials import ServicePrincipalCredentials
    from .compute_secrets import ComputeSecrets
    from .aks_compute_secrets import AksComputeSecrets
    from .virtual_machine_secrets import VirtualMachineSecrets
from .operation_paged import OperationPaged
from .workspace_paged import WorkspacePaged
from .compute_resource_paged import ComputeResourcePaged
from .azure_machine_learning_workspaces_enums import (
    ProvisioningState,
    ResourceIdentityType,
    ComputeType,
)

__all__ = [
    'OperationDisplay',
    'Operation',
    'Workspace',
    'WorkspaceUpdateParameters',
    'Identity',
    'Resource',
    'Password',
    'RegistryListCredentialsResult',
    'ListWorkspaceKeysResult',
    'ErrorDetail',
    'ErrorResponse',
    'MachineLearningServiceError', 'MachineLearningServiceErrorException',
    'Compute',
    'ComputeResource',
    'SystemService',
    'SslConfiguration',
    'AKSProperties',
    'AKS',
    'ScaleSettings',
    'BatchAIProperties',
    'BatchAI',
    'VirtualMachineSshCredentials',
    'VirtualMachineProperties',
    'VirtualMachine',
    'HDInsightProperties',
    'HDInsight',
    'DataFactory',
    'ServicePrincipalCredentials',
    'ComputeSecrets',
    'AksComputeSecrets',
    'VirtualMachineSecrets',
    'OperationPaged',
    'WorkspacePaged',
    'ComputeResourcePaged',
    'ProvisioningState',
    'ResourceIdentityType',
    'ComputeType',
]
