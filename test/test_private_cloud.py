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

from openapi_client.models.private_cloud import PrivateCloud  # noqa: E501

class TestPrivateCloud(unittest.TestCase):
    """PrivateCloud unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateCloud:
        """Test PrivateCloud
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateCloud`
        """
        model = PrivateCloud()  # noqa: E501
        if include_optional:
            return PrivateCloud(
                location = '',
                status = 'BlockedForEdit',
                whitelist = '',
                ike_version = openapi_client.models.private_cloud_ike_version.PrivateCloud_IKE_Version(
                    version = '', ),
                subnets = [
                    openapi_client.models.subnet.Subnet(
                        subnet = '', 
                        cidr_notation = '', 
                        first_assignable_host = '', 
                        last_assignable_host = '', )
                    ]
            )
        else:
            return PrivateCloud(
        )
        """

    def testPrivateCloud(self):
        """Test PrivateCloud"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()