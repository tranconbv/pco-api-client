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
from openapi_client.models.private_cloud_boxwise_version import PrivateCloudBoxwiseVersion
from openapi_client.models.private_cloud_cloud_size import PrivateCloudCloudSize
from openapi_client.models.private_cloud_deployment_profile import PrivateCloudDeploymentProfile
from openapi_client.models.private_cloud_subscription import PrivateCloudSubscription
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PrivateCloud2(BaseModel):
    """
    PrivateCloud2
    """ # noqa: E501
    environment_id: Optional[StrictStr] = Field(default=None, alias="EnvironmentId")
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
    github_access_token_url: Optional[StrictStr] = Field(default=None, alias="GithubAccessToken_url")
    worker_status: Optional[StrictStr] = Field(default=None, alias="Worker_status")
    boxwise_version: Optional[PrivateCloudBoxwiseVersion] = Field(default=None, alias="BoxwiseVersion")
    deployment_profile: Optional[PrivateCloudDeploymentProfile] = Field(default=None, alias="DeploymentProfile")
    cloud_size: Optional[PrivateCloudCloudSize] = Field(default=None, alias="CloudSize")
    subscription: Optional[PrivateCloudSubscription] = Field(default=None, alias="Subscription")
    __properties: ClassVar[List[str]] = ["EnvironmentId", "CloudStatus", "VM_Name", "VM_User", "VM_Password", "Database_User", "Database_Password", "SharedSecret", "Public_IP", "Internal_IP", "Subnet", "VPN_Gateway", "Region", "Boxwise_url", "GithubAccessToken_url", "Worker_status", "BoxwiseVersion", "DeploymentProfile", "CloudSize", "Subscription"]

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
        "validate_assignment": True,
        "protected_namespaces": (),
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
        # override the default output from pydantic by calling `to_dict()` of cloud_size
        if self.cloud_size:
            _dict['CloudSize'] = self.cloud_size.to_dict()
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
            "EnvironmentId": obj.get("EnvironmentId"),
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
            "GithubAccessToken_url": obj.get("GithubAccessToken_url"),
            "Worker_status": obj.get("Worker_status"),
            "BoxwiseVersion": PrivateCloudBoxwiseVersion.from_dict(obj.get("BoxwiseVersion")) if obj.get("BoxwiseVersion") is not None else None,
            "DeploymentProfile": PrivateCloudDeploymentProfile.from_dict(obj.get("DeploymentProfile")) if obj.get("DeploymentProfile") is not None else None,
            "CloudSize": PrivateCloudCloudSize.from_dict(obj.get("CloudSize")) if obj.get("CloudSize") is not None else None,
            "Subscription": PrivateCloudSubscription.from_dict(obj.get("Subscription")) if obj.get("Subscription") is not None else None
        })
        return _obj


