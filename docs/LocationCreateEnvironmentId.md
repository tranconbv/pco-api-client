# LocationCreateEnvironmentId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_id** | **str** |  | [optional] 
**private_cloud** | [**LocationCreateEnvironmentIdPrivateCloud**](LocationCreateEnvironmentIdPrivateCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_create_environment_id import LocationCreateEnvironmentId

# TODO update the JSON string below
json = "{}"
# create an instance of LocationCreateEnvironmentId from a JSON string
location_create_environment_id_instance = LocationCreateEnvironmentId.from_json(json)
# print the JSON string representation of the object
print LocationCreateEnvironmentId.to_json()

# convert the object into a dict
location_create_environment_id_dict = location_create_environment_id_instance.to_dict()
# create an instance of LocationCreateEnvironmentId from a dict
location_create_environment_id_form_dict = location_create_environment_id.from_dict(location_create_environment_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


