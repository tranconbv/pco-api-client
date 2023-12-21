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

from openapi_client.models.private_cloud import PrivateCloud

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
        model = PrivateCloud()
        if include_optional:
            return PrivateCloud(
                environment_id = '',
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
                github_access_token_url = '',
                worker_status = '',
                boxwise_version = openapi_client.models.private_cloud_boxwise_version.PrivateCloud_BoxwiseVersion(
                    version = '', 
                    _id = 56, ),
                deployment_profile = openapi_client.models.private_cloud_deployment_profile.PrivateCloud_DeploymentProfile(
                    description = '', ),
                cloud_size = openapi_client.models.private_cloud_cloud_size.PrivateCloud_CloudSize(
                    code = '', ),
                subscription = openapi_client.models.private_cloud_subscription.PrivateCloud_Subscription(
                    subscription_id = 56, 
                    license_id = 56, ),
                location_vpns = [
                    openapi_client.models.location_vpn.Location_VPN(
                        location = '', 
                        status = 'BlockedForEdit', 
                        whitelist = '', 
                        ike_version = openapi_client.models.location_vpn_ike_version.Location_VPN_IKE_Version(
                            version = '', ), 
                        subnets = [
                            openapi_client.models.subnet.Subnet(
                                subnet = '', 
                                cidr_notation = '', )
                            ], 
                        peer_ip = '', )
                    ],
                subnets = [
                    openapi_client.models.subnet.Subnet(
                        subnet = '', 
                        cidr_notation = '', )
                    ],
                whitelist = ''
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
