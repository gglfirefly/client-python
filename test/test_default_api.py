# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubevirt
from kubevirt.rest import ApiException
from kubevirt.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = kubevirt.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_check_health(self):
        """
        Test case for check_health

        Health endpoint
        """
        pass

    def test_console(self):
        """
        Test case for console

        Open a websocket connection to a serial console on the specified VirtualMachineInstance.
        """
        pass

    def test_create_namespaced_virtual_machine(self):
        """
        Test case for create_namespaced_virtual_machine

        Create a VirtualMachine object.
        """
        pass

    def test_create_namespaced_virtual_machine_instance(self):
        """
        Test case for create_namespaced_virtual_machine_instance

        Create a VirtualMachineInstance object.
        """
        pass

    def test_create_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for create_namespaced_virtual_machine_instance_migration

        Create a VirtualMachineInstanceMigration object.
        """
        pass

    def test_create_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for create_namespaced_virtual_machine_instance_preset

        Create a VirtualMachineInstancePreset object.
        """
        pass

    def test_create_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for create_namespaced_virtual_machine_instance_replica_set

        Create a VirtualMachineInstanceReplicaSet object.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine(self):
        """
        Test case for delete_collection_namespaced_virtual_machine

        Delete a collection of VirtualMachine objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance

        Delete a collection of VirtualMachineInstance objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_migration

        Delete a collection of VirtualMachineInstanceMigration objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_preset

        Delete a collection of VirtualMachineInstancePreset objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_replica_set

        Delete a collection of VirtualMachineInstanceReplicaSet objects.
        """
        pass

    def test_delete_namespaced_virtual_machine(self):
        """
        Test case for delete_namespaced_virtual_machine

        Delete a VirtualMachine object.
        """
        pass

    def test_delete_namespaced_virtual_machine_instance(self):
        """
        Test case for delete_namespaced_virtual_machine_instance

        Delete a VirtualMachineInstance object.
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_migration

        Delete a VirtualMachineInstanceMigration object.
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_preset

        Delete a VirtualMachineInstancePreset object.
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_replica_set

        Delete a VirtualMachineInstanceReplicaSet object.
        """
        pass

    def test_func7(self):
        """
        Test case for func7

        
        """
        pass

    def test_get_api_group(self):
        """
        Test case for get_api_group

        Get a KubeVirt API group
        """
        pass

    def test_get_api_group_0(self):
        """
        Test case for get_api_group_0

        Get a KubeVirt API Group
        """
        pass

    def test_get_api_group_list(self):
        """
        Test case for get_api_group_list

        Get a KubeVirt API GroupList
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        Get KubeVirt API Resources
        """
        pass

    def test_get_api_resources_0(self):
        """
        Test case for get_api_resources_0

        Get a KubeVirt API resources
        """
        pass

    def test_list_namespaced_virtual_machine(self):
        """
        Test case for list_namespaced_virtual_machine

        Get a list of VirtualMachine objects.
        """
        pass

    def test_list_namespaced_virtual_machine_instance(self):
        """
        Test case for list_namespaced_virtual_machine_instance

        Get a list of VirtualMachineInstance objects.
        """
        pass

    def test_list_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for list_namespaced_virtual_machine_instance_migration

        Get a list of VirtualMachineInstanceMigration objects.
        """
        pass

    def test_list_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for list_namespaced_virtual_machine_instance_preset

        Get a list of VirtualMachineInstancePreset objects.
        """
        pass

    def test_list_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for list_namespaced_virtual_machine_instance_replica_set

        Get a list of VirtualMachineInstanceReplicaSet objects.
        """
        pass

    def test_list_virtual_machine_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_for_all_namespaces

        Get a list of all VirtualMachine objects.
        """
        pass

    def test_list_virtual_machine_instance_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_for_all_namespaces

        Get a list of all VirtualMachineInstance objects.
        """
        pass

    def test_list_virtual_machine_instance_migration_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_migration_for_all_namespaces

        Get a list of all VirtualMachineInstanceMigration objects.
        """
        pass

    def test_list_virtual_machine_instance_preset_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_preset_for_all_namespaces

        Get a list of all VirtualMachineInstancePreset objects.
        """
        pass

    def test_list_virtual_machine_instance_replica_set_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_replica_set_for_all_namespaces

        Get a list of all VirtualMachineInstanceReplicaSet objects.
        """
        pass

    def test_patch_namespaced_virtual_machine(self):
        """
        Test case for patch_namespaced_virtual_machine

        Patch a VirtualMachine object.
        """
        pass

    def test_patch_namespaced_virtual_machine_instance(self):
        """
        Test case for patch_namespaced_virtual_machine_instance

        Patch a VirtualMachineInstance object.
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_migration

        Patch a VirtualMachineInstanceMigration object.
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_preset

        Patch a VirtualMachineInstancePreset object.
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_replica_set

        Patch a VirtualMachineInstanceReplicaSet object.
        """
        pass

    def test_read_namespaced_virtual_machine(self):
        """
        Test case for read_namespaced_virtual_machine

        Get a VirtualMachine object.
        """
        pass

    def test_read_namespaced_virtual_machine_instance(self):
        """
        Test case for read_namespaced_virtual_machine_instance

        Get a VirtualMachineInstance object.
        """
        pass

    def test_read_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for read_namespaced_virtual_machine_instance_migration

        Get a VirtualMachineInstanceMigration object.
        """
        pass

    def test_read_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for read_namespaced_virtual_machine_instance_preset

        Get a VirtualMachineInstancePreset object.
        """
        pass

    def test_read_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for read_namespaced_virtual_machine_instance_replica_set

        Get a VirtualMachineInstanceReplicaSet object.
        """
        pass

    def test_replace_namespaced_virtual_machine(self):
        """
        Test case for replace_namespaced_virtual_machine

        Update a VirtualMachine object.
        """
        pass

    def test_replace_namespaced_virtual_machine_instance(self):
        """
        Test case for replace_namespaced_virtual_machine_instance

        Update a VirtualMachineInstance object.
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_migration

        Update a VirtualMachineInstanceMigration object.
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_preset

        Update a VirtualMachineInstancePreset object.
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_replica_set

        Update a VirtualMachineInstanceReplicaSet object.
        """
        pass

    def test_restart(self):
        """
        Test case for restart

        Restart a VirtualMachine object.
        """
        pass

    def test_start(self):
        """
        Test case for start

        Start a VirtualMachine object.
        """
        pass

    def test_stop(self):
        """
        Test case for stop

        Stop a VirtualMachine object.
        """
        pass

    def test_test(self):
        """
        Test case for test

        Test endpoint verifying apiserver connectivity.
        """
        pass

    def test_version(self):
        """
        Test case for version

        
        """
        pass

    def test_vnc(self):
        """
        Test case for vnc

        Open a websocket connection to connect to VNC on the specified VirtualMachineInstance.
        """
        pass

    def test_watch_namespaced_virtual_machine(self):
        """
        Test case for watch_namespaced_virtual_machine

        Watch a VirtualMachine object.
        """
        pass

    def test_watch_namespaced_virtual_machine_instance(self):
        """
        Test case for watch_namespaced_virtual_machine_instance

        Watch a VirtualMachineInstance object.
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_migration

        Watch a VirtualMachineInstanceMigration object.
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_preset

        Watch a VirtualMachineInstancePreset object.
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_replica_set

        Watch a VirtualMachineInstanceReplicaSet object.
        """
        pass

    def test_watch_virtual_machine_instance_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_list_for_all_namespaces

        Watch a VirtualMachineInstanceList object.
        """
        pass

    def test_watch_virtual_machine_instance_migration_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_migration_list_for_all_namespaces

        Watch a VirtualMachineInstanceMigrationList object.
        """
        pass

    def test_watch_virtual_machine_instance_preset_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_preset_list_for_all_namespaces

        Watch a VirtualMachineInstancePresetList object.
        """
        pass

    def test_watch_virtual_machine_instance_replica_set_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_replica_set_list_for_all_namespaces

        Watch a VirtualMachineInstanceReplicaSetList object.
        """
        pass

    def test_watch_virtual_machine_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_list_for_all_namespaces

        Watch a VirtualMachineList object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
