# LocationUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_id** | **str** |  | [optional] 
**private_cloud** | [**LocationUpdatePrivateCloud**](LocationUpdatePrivateCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_update import LocationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of LocationUpdate from a JSON string
location_update_instance = LocationUpdate.from_json(json)
# print the JSON string representation of the object
print LocationUpdate.to_json()

# convert the object into a dict
location_update_dict = location_update_instance.to_dict()
# create an instance of LocationUpdate from a dict
location_update_form_dict = location_update.from_dict(location_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


