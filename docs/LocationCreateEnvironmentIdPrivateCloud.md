# LocationCreateEnvironmentIdPrivateCloud


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_vpn** | [**LocationCreateEnvironmentIdPrivateCloudLocationVPN**](LocationCreateEnvironmentIdPrivateCloudLocationVPN.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_create_environment_id_private_cloud import LocationCreateEnvironmentIdPrivateCloud

# TODO update the JSON string below
json = "{}"
# create an instance of LocationCreateEnvironmentIdPrivateCloud from a JSON string
location_create_environment_id_private_cloud_instance = LocationCreateEnvironmentIdPrivateCloud.from_json(json)
# print the JSON string representation of the object
print LocationCreateEnvironmentIdPrivateCloud.to_json()

# convert the object into a dict
location_create_environment_id_private_cloud_dict = location_create_environment_id_private_cloud_instance.to_dict()
# create an instance of LocationCreateEnvironmentIdPrivateCloud from a dict
location_create_environment_id_private_cloud_form_dict = location_create_environment_id_private_cloud.from_dict(location_create_environment_id_private_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


