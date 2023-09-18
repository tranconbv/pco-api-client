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

from openapi_client.models.private_cloud2 import PrivateCloud2  # noqa: E501

class TestPrivateCloud2(unittest.TestCase):
    """PrivateCloud2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateCloud2:
        """Test PrivateCloud2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateCloud2`
        """
        model = PrivateCloud2()  # noqa: E501
        if include_optional:
            return PrivateCloud2(
                cloud_status = 'BlockedForEdit',
                vm_name = '',
                vm_user = '',
                vm_password = '',
                database_user = '',
                database_password = '',
                shared_secret = '',
                public_ip = '',
                internal_ip = '',
                subnet = '',
                vpn_gateway = '',
                region = '',
                boxwise_url = '',
                whitelist = '',
                boxwise_version = openapi_client.models.private_cloud_2_boxwise_version.PrivateCloud_2_BoxwiseVersion(
                    version = '', 
                    name = '', 
                    _id = 56, ),
                deployment_profile = openapi_client.models.private_cloud_2_deployment_profile.PrivateCloud_2_DeploymentProfile(
                    description = '', ),
                environment_id = openapi_client.models.private_cloud_2_environment_id.PrivateCloud_2_EnvironmentId(
                    env_id = '', ),
                location_vpns = [
                    openapi_client.models.location_vpn.Location_VPN(
                        location = '', 
                        peer_ip = '', 
                        gate_way_ip = '', 
                        subnet = '', 
                        status = 'BlockedForEdit', 
                        shared_secret = '', 
                        whitelist = '', )
                    ],
                cloud_size = openapi_client.models.private_cloud_2_cloud_size.PrivateCloud_2_CloudSize(
                    description = '', 
                    code = '', ),
                subnets = [
                    openapi_client.models.subnet.Subnet(
                        subnet = '', 
                        cidr_notation = '', 
                        first_assignable_host = '', 
                        last_assignable_host = '', )
                    ],
                subscription = openapi_client.models.private_cloud_2_subscription.PrivateCloud_2_Subscription(
                    subscription_id = 56, 
                    license_id = 56, )
            )
        else:
            return PrivateCloud2(
        )
        """

    def testPrivateCloud2(self):
        """Test PrivateCloud2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
