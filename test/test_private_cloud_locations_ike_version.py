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

from openapi_client.models.private_cloud_locations_ike_version import PrivateCloudLocationsIKEVersion  # noqa: E501

class TestPrivateCloudLocationsIKEVersion(unittest.TestCase):
    """PrivateCloudLocationsIKEVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateCloudLocationsIKEVersion:
        """Test PrivateCloudLocationsIKEVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateCloudLocationsIKEVersion`
        """
        model = PrivateCloudLocationsIKEVersion()  # noqa: E501
        if include_optional:
            return PrivateCloudLocationsIKEVersion(
                version = ''
            )
        else:
            return PrivateCloudLocationsIKEVersion(
        )
        """

    def testPrivateCloudLocationsIKEVersion(self):
        """Test PrivateCloudLocationsIKEVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
