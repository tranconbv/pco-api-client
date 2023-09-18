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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class LocationVPN(BaseModel):
    """
    LocationVPN
    """
    location: Optional[StrictStr] = Field(None, alias="Location")
    peer_ip: Optional[StrictStr] = Field(None, alias="Peer_Ip")
    gate_way_ip: Optional[StrictStr] = Field(None, alias="GateWay_IP")
    subnet: Optional[StrictStr] = Field(None, alias="Subnet")
    status: Optional[StrictStr] = Field(None, alias="Status")
    shared_secret: Optional[StrictStr] = Field(None, alias="SharedSecret")
    whitelist: Optional[StrictStr] = Field(None, alias="Whitelist")
    __properties = ["Location", "Peer_Ip", "GateWay_IP", "Subnet", "Status", "SharedSecret", "Whitelist"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BlockedForEdit', 'WaitForCreation', 'InProgress', 'Active', 'Error', 'WaitForDeletion', 'Deleted', 'WaitForEdit'):
            raise ValueError("must be one of enum values ('BlockedForEdit', 'WaitForCreation', 'InProgress', 'Active', 'Error', 'WaitForDeletion', 'Deleted', 'WaitForEdit')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LocationVPN:
        """Create an instance of LocationVPN from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocationVPN:
        """Create an instance of LocationVPN from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocationVPN.parse_obj(obj)

        _obj = LocationVPN.parse_obj({
            "location": obj.get("Location"),
            "peer_ip": obj.get("Peer_Ip"),
            "gate_way_ip": obj.get("GateWay_IP"),
            "subnet": obj.get("Subnet"),
            "status": obj.get("Status"),
            "shared_secret": obj.get("SharedSecret"),
            "whitelist": obj.get("Whitelist")
        })
        return _obj


