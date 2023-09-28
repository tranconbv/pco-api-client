# LocationCreateEnvironmentIdPrivateCloudLocationVPN


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**peer_ip** | **str** |  | [optional] 
**gate_way_ip** | **str** |  | [optional] 
**subnet** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**ike_version** | [**LocationCreateEnvironmentIdPrivateCloudLocationVPNIKEVersion**](LocationCreateEnvironmentIdPrivateCloudLocationVPNIKEVersion.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_create_environment_id_private_cloud_location_vpn import LocationCreateEnvironmentIdPrivateCloudLocationVPN

# TODO update the JSON string below
json = "{}"
# create an instance of LocationCreateEnvironmentIdPrivateCloudLocationVPN from a JSON string
location_create_environment_id_private_cloud_location_vpn_instance = LocationCreateEnvironmentIdPrivateCloudLocationVPN.from_json(json)
# print the JSON string representation of the object
print LocationCreateEnvironmentIdPrivateCloudLocationVPN.to_json()

# convert the object into a dict
location_create_environment_id_private_cloud_location_vpn_dict = location_create_environment_id_private_cloud_location_vpn_instance.to_dict()
# create an instance of LocationCreateEnvironmentIdPrivateCloudLocationVPN from a dict
location_create_environment_id_private_cloud_location_vpn_form_dict = location_create_environment_id_private_cloud_location_vpn.from_dict(location_create_environment_id_private_cloud_location_vpn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


