# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**whitelist** | **str** |  | [optional] 
**ike_version** | [**LocationVPNIKEVersion**](LocationVPNIKEVersion.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) |  | [optional] 
**peer_ip** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print Location.to_json()

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_form_dict = location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


