# LocationVPN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**ike_version** | [**LocationVPNIKEVersion**](LocationVPNIKEVersion.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) |  | [optional] 
**peer_ip** | **str** |  | [optional] 
**shared_secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.location_vpn import LocationVPN

# TODO update the JSON string below
json = "{}"
# create an instance of LocationVPN from a JSON string
location_vpn_instance = LocationVPN.from_json(json)
# print the JSON string representation of the object
print LocationVPN.to_json()

# convert the object into a dict
location_vpn_dict = location_vpn_instance.to_dict()
# create an instance of LocationVPN from a dict
location_vpn_form_dict = location_vpn.from_dict(location_vpn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


