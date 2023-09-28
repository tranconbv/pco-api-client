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

from openapi_client.models.private_cloud_put import PrivateCloudPut  # noqa: E501

class TestPrivateCloudPut(unittest.TestCase):
    """PrivateCloudPut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateCloudPut:
        """Test PrivateCloudPut
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateCloudPut`
        """
        model = PrivateCloudPut()  # noqa: E501
        if include_optional:
            return PrivateCloudPut(
                env_id = '',
                private_cloud = openapi_client.models.private_cloud_put_private_cloud.PrivateCloudPut_PrivateCloud(
                    cloud_status = '', 
                    public_ip = '', 
                    internal_ip = '', 
                    subnet = '', 
                    vpn_gateway_ip = '', 
                    region = '', 
                    whitelist = '', 
                    vm_name = '', 
                    vm_user = '', 
                    vm_password = '', 
                    database_user = '', 
                    boxwise_url = '', )
            )
        else:
            return PrivateCloudPut(
        )
        """

    def testPrivateCloudPut(self):
        """Test PrivateCloudPut"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
