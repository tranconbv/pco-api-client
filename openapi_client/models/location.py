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
from openapi_client.models.subnet import Subnet
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Location(BaseModel):
    """
    Location
    """ # noqa: E501
    location: Optional[StrictStr] = Field(default=None, alias="Location")
    status: Optional[StrictStr] = Field(default=None, alias="Status")
    whitelist: Optional[StrictStr] = Field(default=None, alias="Whitelist")
    ike_version: Optional[PrivateCloudBoxwiseVersion] = Field(default=None, alias="IKE_Version")
    subnets: Optional[List[Subnet]] = Field(default=None, alias="Subnets")
    __properties: ClassVar[List[str]] = ["Location", "Status", "Whitelist", "IKE_Version", "Subnets"]

    @field_validator('status')
    def status_validate_enum(cls, value):
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
        """Create an instance of Location from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ike_version
        if self.ike_version:
            _dict['IKE_Version'] = self.ike_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subnets (list)
        _items = []
        if self.subnets:
            for _item in self.subnets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Subnets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Location from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Location": obj.get("Location"),
            "Status": obj.get("Status"),
            "Whitelist": obj.get("Whitelist"),
            "IKE_Version": PrivateCloudBoxwiseVersion.from_dict(obj.get("IKE_Version")) if obj.get("IKE_Version") is not None else None,
            "Subnets": [Subnet.from_dict(_item) for _item in obj.get("Subnets")] if obj.get("Subnets") is not None else None
        })
        return _obj


