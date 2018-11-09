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
    from .recoverable_database_py3 import RecoverableDatabase
    from .restorable_dropped_database_py3 import RestorableDroppedDatabase
    from .tracked_resource_py3 import TrackedResource
    from .resource_py3 import Resource
    from .proxy_resource_py3 import ProxyResource
    from .check_name_availability_request_py3 import CheckNameAvailabilityRequest
    from .check_name_availability_response_py3 import CheckNameAvailabilityResponse
    from .server_connection_policy_py3 import ServerConnectionPolicy
    from .database_security_alert_policy_py3 import DatabaseSecurityAlertPolicy
    from .data_masking_policy_py3 import DataMaskingPolicy
    from .data_masking_rule_py3 import DataMaskingRule
    from .firewall_rule_py3 import FirewallRule
    from .geo_backup_policy_py3 import GeoBackupPolicy
    from .import_extension_request_py3 import ImportExtensionRequest
    from .import_export_response_py3 import ImportExportResponse
    from .import_request_py3 import ImportRequest
    from .export_request_py3 import ExportRequest
    from .metric_value_py3 import MetricValue
    from .metric_name_py3 import MetricName
    from .metric_py3 import Metric
    from .metric_availability_py3 import MetricAvailability
    from .metric_definition_py3 import MetricDefinition
    from .recommended_elastic_pool_metric_py3 import RecommendedElasticPoolMetric
    from .recommended_elastic_pool_py3 import RecommendedElasticPool
    from .replication_link_py3 import ReplicationLink
    from .server_azure_ad_administrator_py3 import ServerAzureADAdministrator
    from .server_communication_link_py3 import ServerCommunicationLink
    from .service_objective_py3 import ServiceObjective
    from .elastic_pool_activity_py3 import ElasticPoolActivity
    from .elastic_pool_database_activity_py3 import ElasticPoolDatabaseActivity
    from .operation_impact_py3 import OperationImpact
    from .recommended_index_py3 import RecommendedIndex
    from .transparent_data_encryption_py3 import TransparentDataEncryption
    from .slo_usage_metric_py3 import SloUsageMetric
    from .service_tier_advisor_py3 import ServiceTierAdvisor
    from .transparent_data_encryption_activity_py3 import TransparentDataEncryptionActivity
    from .server_usage_py3 import ServerUsage
    from .database_usage_py3 import DatabaseUsage
    from .automatic_tuning_options_py3 import AutomaticTuningOptions
    from .database_automatic_tuning_py3 import DatabaseAutomaticTuning
    from .encryption_protector_py3 import EncryptionProtector
    from .failover_group_read_write_endpoint_py3 import FailoverGroupReadWriteEndpoint
    from .failover_group_read_only_endpoint_py3 import FailoverGroupReadOnlyEndpoint
    from .partner_info_py3 import PartnerInfo
    from .failover_group_py3 import FailoverGroup
    from .failover_group_update_py3 import FailoverGroupUpdate
    from .resource_identity_py3 import ResourceIdentity
    from .sku_py3 import Sku
    from .managed_instance_py3 import ManagedInstance
    from .managed_instance_update_py3 import ManagedInstanceUpdate
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .server_key_py3 import ServerKey
    from .server_py3 import Server
    from .server_update_py3 import ServerUpdate
    from .sync_agent_py3 import SyncAgent
    from .sync_agent_key_properties_py3 import SyncAgentKeyProperties
    from .sync_agent_linked_database_py3 import SyncAgentLinkedDatabase
    from .sync_database_id_properties_py3 import SyncDatabaseIdProperties
    from .sync_full_schema_table_column_py3 import SyncFullSchemaTableColumn
    from .sync_full_schema_table_py3 import SyncFullSchemaTable
    from .sync_full_schema_properties_py3 import SyncFullSchemaProperties
    from .sync_group_log_properties_py3 import SyncGroupLogProperties
    from .sync_group_schema_table_column_py3 import SyncGroupSchemaTableColumn
    from .sync_group_schema_table_py3 import SyncGroupSchemaTable
    from .sync_group_schema_py3 import SyncGroupSchema
    from .sync_group_py3 import SyncGroup
    from .sync_member_py3 import SyncMember
    from .subscription_usage_py3 import SubscriptionUsage
    from .virtual_network_rule_py3 import VirtualNetworkRule
    from .extended_database_blob_auditing_policy_py3 import ExtendedDatabaseBlobAuditingPolicy
    from .extended_server_blob_auditing_policy_py3 import ExtendedServerBlobAuditingPolicy
    from .server_blob_auditing_policy_py3 import ServerBlobAuditingPolicy
    from .database_blob_auditing_policy_py3 import DatabaseBlobAuditingPolicy
    from .database_vulnerability_assessment_rule_baseline_item_py3 import DatabaseVulnerabilityAssessmentRuleBaselineItem
    from .database_vulnerability_assessment_rule_baseline_py3 import DatabaseVulnerabilityAssessmentRuleBaseline
    from .vulnerability_assessment_recurring_scans_properties_py3 import VulnerabilityAssessmentRecurringScansProperties
    from .database_vulnerability_assessment_py3 import DatabaseVulnerabilityAssessment
    from .job_agent_py3 import JobAgent
    from .job_agent_update_py3 import JobAgentUpdate
    from .job_credential_py3 import JobCredential
    from .job_execution_target_py3 import JobExecutionTarget
    from .job_execution_py3 import JobExecution
    from .job_schedule_py3 import JobSchedule
    from .job_py3 import Job
    from .job_step_action_py3 import JobStepAction
    from .job_step_output_py3 import JobStepOutput
    from .job_step_execution_options_py3 import JobStepExecutionOptions
    from .job_step_py3 import JobStep
    from .job_target_py3 import JobTarget
    from .job_target_group_py3 import JobTargetGroup
    from .job_version_py3 import JobVersion
    from .long_term_retention_backup_py3 import LongTermRetentionBackup
    from .backup_long_term_retention_policy_py3 import BackupLongTermRetentionPolicy
    from .managed_backup_short_term_retention_policy_py3 import ManagedBackupShortTermRetentionPolicy
    from .complete_database_restore_definition_py3 import CompleteDatabaseRestoreDefinition
    from .managed_database_py3 import ManagedDatabase
    from .managed_database_update_py3 import ManagedDatabaseUpdate
    from .automatic_tuning_server_options_py3 import AutomaticTuningServerOptions
    from .server_automatic_tuning_py3 import ServerAutomaticTuning
    from .server_dns_alias_py3 import ServerDnsAlias
    from .server_dns_alias_acquisition_py3 import ServerDnsAliasAcquisition
    from .server_security_alert_policy_py3 import ServerSecurityAlertPolicy
    from .restore_point_py3 import RestorePoint
    from .create_database_restore_point_definition_py3 import CreateDatabaseRestorePointDefinition
    from .database_operation_py3 import DatabaseOperation
    from .elastic_pool_operation_py3 import ElasticPoolOperation
    from .max_size_capability_py3 import MaxSizeCapability
    from .log_size_capability_py3 import LogSizeCapability
    from .max_size_range_capability_py3 import MaxSizeRangeCapability
    from .performance_level_capability_py3 import PerformanceLevelCapability
    from .license_type_capability_py3 import LicenseTypeCapability
    from .service_objective_capability_py3 import ServiceObjectiveCapability
    from .edition_capability_py3 import EditionCapability
    from .elastic_pool_per_database_min_performance_level_capability_py3 import ElasticPoolPerDatabaseMinPerformanceLevelCapability
    from .elastic_pool_per_database_max_performance_level_capability_py3 import ElasticPoolPerDatabaseMaxPerformanceLevelCapability
    from .elastic_pool_performance_level_capability_py3 import ElasticPoolPerformanceLevelCapability
    from .elastic_pool_edition_capability_py3 import ElasticPoolEditionCapability
    from .server_version_capability_py3 import ServerVersionCapability
    from .managed_instance_vcores_capability_py3 import ManagedInstanceVcoresCapability
    from .managed_instance_family_capability_py3 import ManagedInstanceFamilyCapability
    from .managed_instance_edition_capability_py3 import ManagedInstanceEditionCapability
    from .managed_instance_version_capability_py3 import ManagedInstanceVersionCapability
    from .location_capabilities_py3 import LocationCapabilities
    from .database_py3 import Database
    from .database_update_py3 import DatabaseUpdate
    from .resource_move_definition_py3 import ResourceMoveDefinition
    from .elastic_pool_per_database_settings_py3 import ElasticPoolPerDatabaseSettings
    from .elastic_pool_py3 import ElasticPool
    from .elastic_pool_update_py3 import ElasticPoolUpdate
    from .vulnerability_assessment_scan_error_py3 import VulnerabilityAssessmentScanError
    from .vulnerability_assessment_scan_record_py3 import VulnerabilityAssessmentScanRecord
    from .database_vulnerability_assessment_scans_export_py3 import DatabaseVulnerabilityAssessmentScansExport
    from .instance_failover_group_read_write_endpoint_py3 import InstanceFailoverGroupReadWriteEndpoint
    from .instance_failover_group_read_only_endpoint_py3 import InstanceFailoverGroupReadOnlyEndpoint
    from .partner_region_info_py3 import PartnerRegionInfo
    from .managed_instance_pair_info_py3 import ManagedInstancePairInfo
    from .instance_failover_group_py3 import InstanceFailoverGroup
    from .backup_short_term_retention_policy_py3 import BackupShortTermRetentionPolicy
    from .tde_certificate_py3 import TdeCertificate
    from .managed_instance_key_py3 import ManagedInstanceKey
    from .managed_instance_encryption_protector_py3 import ManagedInstanceEncryptionProtector
    from .managed_instance_vulnerability_assessment_py3 import ManagedInstanceVulnerabilityAssessment
    from .server_vulnerability_assessment_py3 import ServerVulnerabilityAssessment
except (SyntaxError, ImportError):
    from .recoverable_database import RecoverableDatabase
    from .restorable_dropped_database import RestorableDroppedDatabase
    from .tracked_resource import TrackedResource
    from .resource import Resource
    from .proxy_resource import ProxyResource
    from .check_name_availability_request import CheckNameAvailabilityRequest
    from .check_name_availability_response import CheckNameAvailabilityResponse
    from .server_connection_policy import ServerConnectionPolicy
    from .database_security_alert_policy import DatabaseSecurityAlertPolicy
    from .data_masking_policy import DataMaskingPolicy
    from .data_masking_rule import DataMaskingRule
    from .firewall_rule import FirewallRule
    from .geo_backup_policy import GeoBackupPolicy
    from .import_extension_request import ImportExtensionRequest
    from .import_export_response import ImportExportResponse
    from .import_request import ImportRequest
    from .export_request import ExportRequest
    from .metric_value import MetricValue
    from .metric_name import MetricName
    from .metric import Metric
    from .metric_availability import MetricAvailability
    from .metric_definition import MetricDefinition
    from .recommended_elastic_pool_metric import RecommendedElasticPoolMetric
    from .recommended_elastic_pool import RecommendedElasticPool
    from .replication_link import ReplicationLink
    from .server_azure_ad_administrator import ServerAzureADAdministrator
    from .server_communication_link import ServerCommunicationLink
    from .service_objective import ServiceObjective
    from .elastic_pool_activity import ElasticPoolActivity
    from .elastic_pool_database_activity import ElasticPoolDatabaseActivity
    from .operation_impact import OperationImpact
    from .recommended_index import RecommendedIndex
    from .transparent_data_encryption import TransparentDataEncryption
    from .slo_usage_metric import SloUsageMetric
    from .service_tier_advisor import ServiceTierAdvisor
    from .transparent_data_encryption_activity import TransparentDataEncryptionActivity
    from .server_usage import ServerUsage
    from .database_usage import DatabaseUsage
    from .automatic_tuning_options import AutomaticTuningOptions
    from .database_automatic_tuning import DatabaseAutomaticTuning
    from .encryption_protector import EncryptionProtector
    from .failover_group_read_write_endpoint import FailoverGroupReadWriteEndpoint
    from .failover_group_read_only_endpoint import FailoverGroupReadOnlyEndpoint
    from .partner_info import PartnerInfo
    from .failover_group import FailoverGroup
    from .failover_group_update import FailoverGroupUpdate
    from .resource_identity import ResourceIdentity
    from .sku import Sku
    from .managed_instance import ManagedInstance
    from .managed_instance_update import ManagedInstanceUpdate
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .server_key import ServerKey
    from .server import Server
    from .server_update import ServerUpdate
    from .sync_agent import SyncAgent
    from .sync_agent_key_properties import SyncAgentKeyProperties
    from .sync_agent_linked_database import SyncAgentLinkedDatabase
    from .sync_database_id_properties import SyncDatabaseIdProperties
    from .sync_full_schema_table_column import SyncFullSchemaTableColumn
    from .sync_full_schema_table import SyncFullSchemaTable
    from .sync_full_schema_properties import SyncFullSchemaProperties
    from .sync_group_log_properties import SyncGroupLogProperties
    from .sync_group_schema_table_column import SyncGroupSchemaTableColumn
    from .sync_group_schema_table import SyncGroupSchemaTable
    from .sync_group_schema import SyncGroupSchema
    from .sync_group import SyncGroup
    from .sync_member import SyncMember
    from .subscription_usage import SubscriptionUsage
    from .virtual_network_rule import VirtualNetworkRule
    from .extended_database_blob_auditing_policy import ExtendedDatabaseBlobAuditingPolicy
    from .extended_server_blob_auditing_policy import ExtendedServerBlobAuditingPolicy
    from .server_blob_auditing_policy import ServerBlobAuditingPolicy
    from .database_blob_auditing_policy import DatabaseBlobAuditingPolicy
    from .database_vulnerability_assessment_rule_baseline_item import DatabaseVulnerabilityAssessmentRuleBaselineItem
    from .database_vulnerability_assessment_rule_baseline import DatabaseVulnerabilityAssessmentRuleBaseline
    from .vulnerability_assessment_recurring_scans_properties import VulnerabilityAssessmentRecurringScansProperties
    from .database_vulnerability_assessment import DatabaseVulnerabilityAssessment
    from .job_agent import JobAgent
    from .job_agent_update import JobAgentUpdate
    from .job_credential import JobCredential
    from .job_execution_target import JobExecutionTarget
    from .job_execution import JobExecution
    from .job_schedule import JobSchedule
    from .job import Job
    from .job_step_action import JobStepAction
    from .job_step_output import JobStepOutput
    from .job_step_execution_options import JobStepExecutionOptions
    from .job_step import JobStep
    from .job_target import JobTarget
    from .job_target_group import JobTargetGroup
    from .job_version import JobVersion
    from .long_term_retention_backup import LongTermRetentionBackup
    from .backup_long_term_retention_policy import BackupLongTermRetentionPolicy
    from .managed_backup_short_term_retention_policy import ManagedBackupShortTermRetentionPolicy
    from .complete_database_restore_definition import CompleteDatabaseRestoreDefinition
    from .managed_database import ManagedDatabase
    from .managed_database_update import ManagedDatabaseUpdate
    from .automatic_tuning_server_options import AutomaticTuningServerOptions
    from .server_automatic_tuning import ServerAutomaticTuning
    from .server_dns_alias import ServerDnsAlias
    from .server_dns_alias_acquisition import ServerDnsAliasAcquisition
    from .server_security_alert_policy import ServerSecurityAlertPolicy
    from .restore_point import RestorePoint
    from .create_database_restore_point_definition import CreateDatabaseRestorePointDefinition
    from .database_operation import DatabaseOperation
    from .elastic_pool_operation import ElasticPoolOperation
    from .max_size_capability import MaxSizeCapability
    from .log_size_capability import LogSizeCapability
    from .max_size_range_capability import MaxSizeRangeCapability
    from .performance_level_capability import PerformanceLevelCapability
    from .license_type_capability import LicenseTypeCapability
    from .service_objective_capability import ServiceObjectiveCapability
    from .edition_capability import EditionCapability
    from .elastic_pool_per_database_min_performance_level_capability import ElasticPoolPerDatabaseMinPerformanceLevelCapability
    from .elastic_pool_per_database_max_performance_level_capability import ElasticPoolPerDatabaseMaxPerformanceLevelCapability
    from .elastic_pool_performance_level_capability import ElasticPoolPerformanceLevelCapability
    from .elastic_pool_edition_capability import ElasticPoolEditionCapability
    from .server_version_capability import ServerVersionCapability
    from .managed_instance_vcores_capability import ManagedInstanceVcoresCapability
    from .managed_instance_family_capability import ManagedInstanceFamilyCapability
    from .managed_instance_edition_capability import ManagedInstanceEditionCapability
    from .managed_instance_version_capability import ManagedInstanceVersionCapability
    from .location_capabilities import LocationCapabilities
    from .database import Database
    from .database_update import DatabaseUpdate
    from .resource_move_definition import ResourceMoveDefinition
    from .elastic_pool_per_database_settings import ElasticPoolPerDatabaseSettings
    from .elastic_pool import ElasticPool
    from .elastic_pool_update import ElasticPoolUpdate
    from .vulnerability_assessment_scan_error import VulnerabilityAssessmentScanError
    from .vulnerability_assessment_scan_record import VulnerabilityAssessmentScanRecord
    from .database_vulnerability_assessment_scans_export import DatabaseVulnerabilityAssessmentScansExport
    from .instance_failover_group_read_write_endpoint import InstanceFailoverGroupReadWriteEndpoint
    from .instance_failover_group_read_only_endpoint import InstanceFailoverGroupReadOnlyEndpoint
    from .partner_region_info import PartnerRegionInfo
    from .managed_instance_pair_info import ManagedInstancePairInfo
    from .instance_failover_group import InstanceFailoverGroup
    from .backup_short_term_retention_policy import BackupShortTermRetentionPolicy
    from .tde_certificate import TdeCertificate
    from .managed_instance_key import ManagedInstanceKey
    from .managed_instance_encryption_protector import ManagedInstanceEncryptionProtector
    from .managed_instance_vulnerability_assessment import ManagedInstanceVulnerabilityAssessment
    from .server_vulnerability_assessment import ServerVulnerabilityAssessment
from .recoverable_database_paged import RecoverableDatabasePaged
from .restorable_dropped_database_paged import RestorableDroppedDatabasePaged
from .server_paged import ServerPaged
from .data_masking_rule_paged import DataMaskingRulePaged
from .firewall_rule_paged import FirewallRulePaged
from .geo_backup_policy_paged import GeoBackupPolicyPaged
from .metric_paged import MetricPaged
from .metric_definition_paged import MetricDefinitionPaged
from .database_paged import DatabasePaged
from .elastic_pool_paged import ElasticPoolPaged
from .recommended_elastic_pool_paged import RecommendedElasticPoolPaged
from .recommended_elastic_pool_metric_paged import RecommendedElasticPoolMetricPaged
from .replication_link_paged import ReplicationLinkPaged
from .server_azure_ad_administrator_paged import ServerAzureADAdministratorPaged
from .server_communication_link_paged import ServerCommunicationLinkPaged
from .service_objective_paged import ServiceObjectivePaged
from .elastic_pool_activity_paged import ElasticPoolActivityPaged
from .elastic_pool_database_activity_paged import ElasticPoolDatabaseActivityPaged
from .service_tier_advisor_paged import ServiceTierAdvisorPaged
from .transparent_data_encryption_activity_paged import TransparentDataEncryptionActivityPaged
from .server_usage_paged import ServerUsagePaged
from .database_usage_paged import DatabaseUsagePaged
from .encryption_protector_paged import EncryptionProtectorPaged
from .failover_group_paged import FailoverGroupPaged
from .managed_instance_paged import ManagedInstancePaged
from .operation_paged import OperationPaged
from .server_key_paged import ServerKeyPaged
from .sync_agent_paged import SyncAgentPaged
from .sync_agent_linked_database_paged import SyncAgentLinkedDatabasePaged
from .sync_database_id_properties_paged import SyncDatabaseIdPropertiesPaged
from .sync_full_schema_properties_paged import SyncFullSchemaPropertiesPaged
from .sync_group_log_properties_paged import SyncGroupLogPropertiesPaged
from .sync_group_paged import SyncGroupPaged
from .sync_member_paged import SyncMemberPaged
from .subscription_usage_paged import SubscriptionUsagePaged
from .virtual_network_rule_paged import VirtualNetworkRulePaged
from .database_vulnerability_assessment_paged import DatabaseVulnerabilityAssessmentPaged
from .job_agent_paged import JobAgentPaged
from .job_credential_paged import JobCredentialPaged
from .job_execution_paged import JobExecutionPaged
from .job_paged import JobPaged
from .job_step_paged import JobStepPaged
from .job_target_group_paged import JobTargetGroupPaged
from .job_version_paged import JobVersionPaged
from .long_term_retention_backup_paged import LongTermRetentionBackupPaged
from .managed_backup_short_term_retention_policy_paged import ManagedBackupShortTermRetentionPolicyPaged
from .managed_database_paged import ManagedDatabasePaged
from .server_dns_alias_paged import ServerDnsAliasPaged
from .restore_point_paged import RestorePointPaged
from .database_operation_paged import DatabaseOperationPaged
from .elastic_pool_operation_paged import ElasticPoolOperationPaged
from .vulnerability_assessment_scan_record_paged import VulnerabilityAssessmentScanRecordPaged
from .instance_failover_group_paged import InstanceFailoverGroupPaged
from .backup_short_term_retention_policy_paged import BackupShortTermRetentionPolicyPaged
from .managed_instance_key_paged import ManagedInstanceKeyPaged
from .managed_instance_encryption_protector_paged import ManagedInstanceEncryptionProtectorPaged
from .managed_instance_vulnerability_assessment_paged import ManagedInstanceVulnerabilityAssessmentPaged
from .server_vulnerability_assessment_paged import ServerVulnerabilityAssessmentPaged
from .sql_management_client_enums import (
    CheckNameAvailabilityReason,
    ServerConnectionType,
    SecurityAlertPolicyState,
    SecurityAlertPolicyEmailAccountAdmins,
    SecurityAlertPolicyUseServerDefault,
    DataMaskingState,
    DataMaskingRuleState,
    DataMaskingFunction,
    GeoBackupPolicyState,
    DatabaseEdition,
    ServiceObjectiveName,
    StorageKeyType,
    AuthenticationType,
    UnitType,
    PrimaryAggregationType,
    UnitDefinitionType,
    ElasticPoolEdition,
    ReplicationRole,
    ReplicationState,
    RecommendedIndexAction,
    RecommendedIndexState,
    RecommendedIndexType,
    TransparentDataEncryptionStatus,
    TransparentDataEncryptionActivityStatus,
    AutomaticTuningMode,
    AutomaticTuningOptionModeDesired,
    AutomaticTuningOptionModeActual,
    AutomaticTuningDisabledReason,
    ServerKeyType,
    ReadWriteEndpointFailoverPolicy,
    ReadOnlyEndpointFailoverPolicy,
    FailoverGroupReplicationRole,
    IdentityType,
    OperationOrigin,
    SyncAgentState,
    SyncMemberDbType,
    SyncGroupLogType,
    SyncConflictResolutionPolicy,
    SyncGroupState,
    SyncDirection,
    SyncMemberState,
    VirtualNetworkRuleState,
    BlobAuditingPolicyState,
    JobAgentState,
    JobExecutionLifecycle,
    ProvisioningState,
    JobTargetType,
    JobScheduleType,
    JobStepActionType,
    JobStepActionSource,
    JobStepOutputType,
    JobTargetGroupMembershipType,
    ManagedDatabaseStatus,
    CatalogCollationType,
    ManagedDatabaseCreateMode,
    AutomaticTuningServerMode,
    AutomaticTuningServerReason,
    RestorePointType,
    ManagementOperationState,
    MaxSizeUnit,
    LogSizeUnit,
    CapabilityStatus,
    PerformanceLevelUnit,
    CreateMode,
    SampleName,
    DatabaseStatus,
    DatabaseLicenseType,
    DatabaseReadScale,
    ElasticPoolState,
    ElasticPoolLicenseType,
    VulnerabilityAssessmentScanTriggerType,
    VulnerabilityAssessmentScanState,
    InstanceFailoverGroupReplicationRole,
    LongTermRetentionDatabaseState,
    VulnerabilityAssessmentPolicyBaselineName,
    CapabilityGroup,
)

__all__ = [
    'RecoverableDatabase',
    'RestorableDroppedDatabase',
    'TrackedResource',
    'Resource',
    'ProxyResource',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'ServerConnectionPolicy',
    'DatabaseSecurityAlertPolicy',
    'DataMaskingPolicy',
    'DataMaskingRule',
    'FirewallRule',
    'GeoBackupPolicy',
    'ImportExtensionRequest',
    'ImportExportResponse',
    'ImportRequest',
    'ExportRequest',
    'MetricValue',
    'MetricName',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'RecommendedElasticPoolMetric',
    'RecommendedElasticPool',
    'ReplicationLink',
    'ServerAzureADAdministrator',
    'ServerCommunicationLink',
    'ServiceObjective',
    'ElasticPoolActivity',
    'ElasticPoolDatabaseActivity',
    'OperationImpact',
    'RecommendedIndex',
    'TransparentDataEncryption',
    'SloUsageMetric',
    'ServiceTierAdvisor',
    'TransparentDataEncryptionActivity',
    'ServerUsage',
    'DatabaseUsage',
    'AutomaticTuningOptions',
    'DatabaseAutomaticTuning',
    'EncryptionProtector',
    'FailoverGroupReadWriteEndpoint',
    'FailoverGroupReadOnlyEndpoint',
    'PartnerInfo',
    'FailoverGroup',
    'FailoverGroupUpdate',
    'ResourceIdentity',
    'Sku',
    'ManagedInstance',
    'ManagedInstanceUpdate',
    'OperationDisplay',
    'Operation',
    'ServerKey',
    'Server',
    'ServerUpdate',
    'SyncAgent',
    'SyncAgentKeyProperties',
    'SyncAgentLinkedDatabase',
    'SyncDatabaseIdProperties',
    'SyncFullSchemaTableColumn',
    'SyncFullSchemaTable',
    'SyncFullSchemaProperties',
    'SyncGroupLogProperties',
    'SyncGroupSchemaTableColumn',
    'SyncGroupSchemaTable',
    'SyncGroupSchema',
    'SyncGroup',
    'SyncMember',
    'SubscriptionUsage',
    'VirtualNetworkRule',
    'ExtendedDatabaseBlobAuditingPolicy',
    'ExtendedServerBlobAuditingPolicy',
    'ServerBlobAuditingPolicy',
    'DatabaseBlobAuditingPolicy',
    'DatabaseVulnerabilityAssessmentRuleBaselineItem',
    'DatabaseVulnerabilityAssessmentRuleBaseline',
    'VulnerabilityAssessmentRecurringScansProperties',
    'DatabaseVulnerabilityAssessment',
    'JobAgent',
    'JobAgentUpdate',
    'JobCredential',
    'JobExecutionTarget',
    'JobExecution',
    'JobSchedule',
    'Job',
    'JobStepAction',
    'JobStepOutput',
    'JobStepExecutionOptions',
    'JobStep',
    'JobTarget',
    'JobTargetGroup',
    'JobVersion',
    'LongTermRetentionBackup',
    'BackupLongTermRetentionPolicy',
    'ManagedBackupShortTermRetentionPolicy',
    'CompleteDatabaseRestoreDefinition',
    'ManagedDatabase',
    'ManagedDatabaseUpdate',
    'AutomaticTuningServerOptions',
    'ServerAutomaticTuning',
    'ServerDnsAlias',
    'ServerDnsAliasAcquisition',
    'ServerSecurityAlertPolicy',
    'RestorePoint',
    'CreateDatabaseRestorePointDefinition',
    'DatabaseOperation',
    'ElasticPoolOperation',
    'MaxSizeCapability',
    'LogSizeCapability',
    'MaxSizeRangeCapability',
    'PerformanceLevelCapability',
    'LicenseTypeCapability',
    'ServiceObjectiveCapability',
    'EditionCapability',
    'ElasticPoolPerDatabaseMinPerformanceLevelCapability',
    'ElasticPoolPerDatabaseMaxPerformanceLevelCapability',
    'ElasticPoolPerformanceLevelCapability',
    'ElasticPoolEditionCapability',
    'ServerVersionCapability',
    'ManagedInstanceVcoresCapability',
    'ManagedInstanceFamilyCapability',
    'ManagedInstanceEditionCapability',
    'ManagedInstanceVersionCapability',
    'LocationCapabilities',
    'Database',
    'DatabaseUpdate',
    'ResourceMoveDefinition',
    'ElasticPoolPerDatabaseSettings',
    'ElasticPool',
    'ElasticPoolUpdate',
    'VulnerabilityAssessmentScanError',
    'VulnerabilityAssessmentScanRecord',
    'DatabaseVulnerabilityAssessmentScansExport',
    'InstanceFailoverGroupReadWriteEndpoint',
    'InstanceFailoverGroupReadOnlyEndpoint',
    'PartnerRegionInfo',
    'ManagedInstancePairInfo',
    'InstanceFailoverGroup',
    'BackupShortTermRetentionPolicy',
    'TdeCertificate',
    'ManagedInstanceKey',
    'ManagedInstanceEncryptionProtector',
    'ManagedInstanceVulnerabilityAssessment',
    'ServerVulnerabilityAssessment',
    'RecoverableDatabasePaged',
    'RestorableDroppedDatabasePaged',
    'ServerPaged',
    'DataMaskingRulePaged',
    'FirewallRulePaged',
    'GeoBackupPolicyPaged',
    'MetricPaged',
    'MetricDefinitionPaged',
    'DatabasePaged',
    'ElasticPoolPaged',
    'RecommendedElasticPoolPaged',
    'RecommendedElasticPoolMetricPaged',
    'ReplicationLinkPaged',
    'ServerAzureADAdministratorPaged',
    'ServerCommunicationLinkPaged',
    'ServiceObjectivePaged',
    'ElasticPoolActivityPaged',
    'ElasticPoolDatabaseActivityPaged',
    'ServiceTierAdvisorPaged',
    'TransparentDataEncryptionActivityPaged',
    'ServerUsagePaged',
    'DatabaseUsagePaged',
    'EncryptionProtectorPaged',
    'FailoverGroupPaged',
    'ManagedInstancePaged',
    'OperationPaged',
    'ServerKeyPaged',
    'SyncAgentPaged',
    'SyncAgentLinkedDatabasePaged',
    'SyncDatabaseIdPropertiesPaged',
    'SyncFullSchemaPropertiesPaged',
    'SyncGroupLogPropertiesPaged',
    'SyncGroupPaged',
    'SyncMemberPaged',
    'SubscriptionUsagePaged',
    'VirtualNetworkRulePaged',
    'DatabaseVulnerabilityAssessmentPaged',
    'JobAgentPaged',
    'JobCredentialPaged',
    'JobExecutionPaged',
    'JobPaged',
    'JobStepPaged',
    'JobTargetGroupPaged',
    'JobVersionPaged',
    'LongTermRetentionBackupPaged',
    'ManagedBackupShortTermRetentionPolicyPaged',
    'ManagedDatabasePaged',
    'ServerDnsAliasPaged',
    'RestorePointPaged',
    'DatabaseOperationPaged',
    'ElasticPoolOperationPaged',
    'VulnerabilityAssessmentScanRecordPaged',
    'InstanceFailoverGroupPaged',
    'BackupShortTermRetentionPolicyPaged',
    'ManagedInstanceKeyPaged',
    'ManagedInstanceEncryptionProtectorPaged',
    'ManagedInstanceVulnerabilityAssessmentPaged',
    'ServerVulnerabilityAssessmentPaged',
    'CheckNameAvailabilityReason',
    'ServerConnectionType',
    'SecurityAlertPolicyState',
    'SecurityAlertPolicyEmailAccountAdmins',
    'SecurityAlertPolicyUseServerDefault',
    'DataMaskingState',
    'DataMaskingRuleState',
    'DataMaskingFunction',
    'GeoBackupPolicyState',
    'DatabaseEdition',
    'ServiceObjectiveName',
    'StorageKeyType',
    'AuthenticationType',
    'UnitType',
    'PrimaryAggregationType',
    'UnitDefinitionType',
    'ElasticPoolEdition',
    'ReplicationRole',
    'ReplicationState',
    'RecommendedIndexAction',
    'RecommendedIndexState',
    'RecommendedIndexType',
    'TransparentDataEncryptionStatus',
    'TransparentDataEncryptionActivityStatus',
    'AutomaticTuningMode',
    'AutomaticTuningOptionModeDesired',
    'AutomaticTuningOptionModeActual',
    'AutomaticTuningDisabledReason',
    'ServerKeyType',
    'ReadWriteEndpointFailoverPolicy',
    'ReadOnlyEndpointFailoverPolicy',
    'FailoverGroupReplicationRole',
    'IdentityType',
    'OperationOrigin',
    'SyncAgentState',
    'SyncMemberDbType',
    'SyncGroupLogType',
    'SyncConflictResolutionPolicy',
    'SyncGroupState',
    'SyncDirection',
    'SyncMemberState',
    'VirtualNetworkRuleState',
    'BlobAuditingPolicyState',
    'JobAgentState',
    'JobExecutionLifecycle',
    'ProvisioningState',
    'JobTargetType',
    'JobScheduleType',
    'JobStepActionType',
    'JobStepActionSource',
    'JobStepOutputType',
    'JobTargetGroupMembershipType',
    'ManagedDatabaseStatus',
    'CatalogCollationType',
    'ManagedDatabaseCreateMode',
    'AutomaticTuningServerMode',
    'AutomaticTuningServerReason',
    'RestorePointType',
    'ManagementOperationState',
    'MaxSizeUnit',
    'LogSizeUnit',
    'CapabilityStatus',
    'PerformanceLevelUnit',
    'CreateMode',
    'SampleName',
    'DatabaseStatus',
    'DatabaseLicenseType',
    'DatabaseReadScale',
    'ElasticPoolState',
    'ElasticPoolLicenseType',
    'VulnerabilityAssessmentScanTriggerType',
    'VulnerabilityAssessmentScanState',
    'InstanceFailoverGroupReplicationRole',
    'LongTermRetentionDatabaseState',
    'VulnerabilityAssessmentPolicyBaselineName',
    'CapabilityGroup',
]
