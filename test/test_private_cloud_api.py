# coding: utf-8

"""
    CloudAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501
import os
import unittest
import openapi_client

from openapi_client.api.private_cloud_api import PrivateCloudApi  # noqa: E501


class TestPrivateCloudApi(unittest.TestCase):
    """PrivateCloudApi unit test stubs"""

    def setUp(self) -> None:
        # Configure HTTP basic authorization: basicAuth
        configuration = openapi_client.Configuration(
            username=os.environ["PCO_API_USERNAME"],
            password=os.environ["PCO_API_PASSWORD"]
        )
        api_client = openapi_client.ApiClient(configuration)
        api_client.default_headers["Accept"] = "application/json"

        self.api = PrivateCloudApi(api_client)
        PrivateCloudApi()

    def tearDown(self) -> None:
        del self.api

    def test_private_cloud_get(self) -> None:
        """Test case for private_cloud_get

        """
        result = self.api.private_cloud_get()
        self.assertIsNotNone(result)

    def test_private_cloud_id_locations_name_delete(self) -> None:
        """Test case for private_cloud_id_locations_name_delete

        """
        pass

    def test_private_cloud_id_locations_put(self) -> None:
        """Test case for private_cloud_id_locations_put

        """
        pass

    def test_private_cloud_id_whitelist_post(self) -> None:
        """Test case for private_cloud_id_whitelist_post

        """
        pass

    def test_private_cloud_locations_get(self) -> None:
        """Test case for private_cloud_locations_get

        """
        pass

    def test_private_cloud_post(self) -> None:
        """Test case for private_cloud_post

        """
        pass

    def test_private_cloud_put(self) -> None:
        """Test case for private_cloud_put

        """
        pass


if __name__ == '__main__':
    unittest.main()