# coding: utf-8

"""
    CloudAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.location_vpn import LocationVPN
from openapi_client.models.private_cloud2_boxwise_version import PrivateCloud2BoxwiseVersion
from openapi_client.models.private_cloud2_cloud_size import PrivateCloud2CloudSize
from openapi_client.models.private_cloud2_deployment_profile import PrivateCloud2DeploymentProfile
from openapi_client.models.private_cloud2_environment_id import PrivateCloud2EnvironmentId
from openapi_client.models.private_cloud2_subscription import PrivateCloud2Subscription
from openapi_client.models.subnet import Subnet
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PrivateCloud2(BaseModel):
    """
    PrivateCloud2
    """ # noqa: E501
    cloud_status: Optional[StrictStr] = Field(default=None, alias="CloudStatus")
    vm_name: Optional[StrictStr] = Field(default=None, alias="VM_Name")
    vm_user: Optional[StrictStr] = Field(default=None, alias="VM_User")
    vm_password: Optional[StrictStr] = Field(default=None, alias="VM_Password")
    database_user: Optional[StrictStr] = Field(default=None, alias="Database_User")
    database_password: Optional[StrictStr] = Field(default=None, alias="Database_Password")
    shared_secret: Optional[StrictStr] = Field(default=None, alias="SharedSecret")
    public_ip: Optional[StrictStr] = Field(default=None, alias="Public_IP")
    internal_ip: Optional[StrictStr] = Field(default=None, alias="Internal_IP")
    subnet: Optional[StrictStr] = Field(default=None, alias="Subnet")
    vpn_gateway: Optional[StrictStr] = Field(default=None, alias="VPN_Gateway")
    region: Optional[StrictStr] = Field(default=None, alias="Region")
    boxwise_url: Optional[StrictStr] = Field(default=None, alias="Boxwise_url")
    whitelist: Optional[StrictStr] = Field(default=None, alias="Whitelist")
    boxwise_version: Optional[PrivateCloud2BoxwiseVersion] = Field(default=None, alias="BoxwiseVersion")
    deployment_profile: Optional[PrivateCloud2DeploymentProfile] = Field(default=None, alias="DeploymentProfile")
    environment_id: Optional[PrivateCloud2EnvironmentId] = Field(default=None, alias="EnvironmentId")
    location_vpns: Optional[List[LocationVPN]] = Field(default=None, alias="Location_VPNs")
    cloud_size: Optional[PrivateCloud2CloudSize] = Field(default=None, alias="CloudSize")
    subnets: Optional[List[Subnet]] = Field(default=None, alias="Subnets")
    subscription: Optional[PrivateCloud2Subscription] = Field(default=None, alias="Subscription")
    github_access_token_url: Optional[StrictStr] = Field(default=None, alias="GithubAccessToken_url")
    __properties: ClassVar[List[str]] = ["CloudStatus", "VM_Name", "VM_User", "VM_Password", "Database_User", "Database_Password", "SharedSecret", "Public_IP", "Internal_IP", "Subnet", "VPN_Gateway", "Region", "Boxwise_url", "Whitelist", "BoxwiseVersion", "DeploymentProfile", "EnvironmentId", "Location_VPNs", "CloudSize", "Subnets", "Subscription", "GithubAccessToken_url"]

    @field_validator('cloud_status')
    def cloud_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BlockedForEdit', 'WaitForCreation', 'InProgress', 'Active', 'Error', 'WaitForDeletion', 'Deleted', 'WaitForEdit'):
            raise ValueError("must be one of enum values ('BlockedForEdit', 'WaitForCreation', 'InProgress', 'Active', 'Error', 'WaitForDeletion', 'Deleted', 'WaitForEdit')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PrivateCloud2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of boxwise_version
        if self.boxwise_version:
            _dict['BoxwiseVersion'] = self.boxwise_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deployment_profile
        if self.deployment_profile:
            _dict['DeploymentProfile'] = self.deployment_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of environment_id
        if self.environment_id:
            _dict['EnvironmentId'] = self.environment_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in location_vpns (list)
        _items = []
        if self.location_vpns:
            for _item in self.location_vpns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Location_VPNs'] = _items
        # override the default output from pydantic by calling `to_dict()` of cloud_size
        if self.cloud_size:
            _dict['CloudSize'] = self.cloud_size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subnets (list)
        _items = []
        if self.subnets:
            for _item in self.subnets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Subnets'] = _items
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['Subscription'] = self.subscription.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PrivateCloud2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CloudStatus": obj.get("CloudStatus"),
            "VM_Name": obj.get("VM_Name"),
            "VM_User": obj.get("VM_User"),
            "VM_Password": obj.get("VM_Password"),
            "Database_User": obj.get("Database_User"),
            "Database_Password": obj.get("Database_Password"),
            "SharedSecret": obj.get("SharedSecret"),
            "Public_IP": obj.get("Public_IP"),
            "Internal_IP": obj.get("Internal_IP"),
            "Subnet": obj.get("Subnet"),
            "VPN_Gateway": obj.get("VPN_Gateway"),
            "Region": obj.get("Region"),
            "Boxwise_url": obj.get("Boxwise_url"),
            "Whitelist": obj.get("Whitelist"),
            "BoxwiseVersion": PrivateCloud2BoxwiseVersion.from_dict(obj.get("BoxwiseVersion")) if obj.get("BoxwiseVersion") is not None else None,
            "DeploymentProfile": PrivateCloud2DeploymentProfile.from_dict(obj.get("DeploymentProfile")) if obj.get("DeploymentProfile") is not None else None,
            "EnvironmentId": PrivateCloud2EnvironmentId.from_dict(obj.get("EnvironmentId")) if obj.get("EnvironmentId") is not None else None,
            "Location_VPNs": [LocationVPN.from_dict(_item) for _item in obj.get("Location_VPNs")] if obj.get("Location_VPNs") is not None else None,
            "CloudSize": PrivateCloud2CloudSize.from_dict(obj.get("CloudSize")) if obj.get("CloudSize") is not None else None,
            "Subnets": [Subnet.from_dict(_item) for _item in obj.get("Subnets")] if obj.get("Subnets") is not None else None,
            "Subscription": PrivateCloud2Subscription.from_dict(obj.get("Subscription")) if obj.get("Subscription") is not None else None,
            "GithubAccessToken_url": obj.get("GithubAccessToken_url")
        })
        return _obj


