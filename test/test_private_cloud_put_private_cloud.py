# coding: utf-8

"""
    CloudAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.private_cloud_put_private_cloud import PrivateCloudPUTPrivateCloud

class TestPrivateCloudPUTPrivateCloud(unittest.TestCase):
    """PrivateCloudPUTPrivateCloud unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateCloudPUTPrivateCloud:
        """Test PrivateCloudPUTPrivateCloud
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateCloudPUTPrivateCloud`
        """
        model = PrivateCloudPUTPrivateCloud()
        if include_optional:
            return PrivateCloudPUTPrivateCloud(
                cloud_status = 'BlockedForEdit',
                vm_name = '',
                vm_user = '',
                vm_password = '',
                database_user = '',
                public_ip = '',
                internal_ip = '',
                subnet = '',
                vpn_gateway = '',
                region = '',
                boxwise_url = '',
                whitelist = '',
                github_access_token_url = '',
                worker_status = ''
            )
        else:
            return PrivateCloudPUTPrivateCloud(
        )
        """

    def testPrivateCloudPUTPrivateCloud(self):
        """Test PrivateCloudPUTPrivateCloud"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()