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

from openapi_client.models.private_cloud2_cloud_size import PrivateCloud2CloudSize  # noqa: E501

class TestPrivateCloud2CloudSize(unittest.TestCase):
    """PrivateCloud2CloudSize unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateCloud2CloudSize:
        """Test PrivateCloud2CloudSize
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateCloud2CloudSize`
        """
        model = PrivateCloud2CloudSize()  # noqa: E501
        if include_optional:
            return PrivateCloud2CloudSize(
                description = '',
                code = ''
            )
        else:
            return PrivateCloud2CloudSize(
        )
        """

    def testPrivateCloud2CloudSize(self):
        """Test PrivateCloud2CloudSize"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
