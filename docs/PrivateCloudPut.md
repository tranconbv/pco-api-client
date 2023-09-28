# PrivateCloudPut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_id** | **str** |  | [optional] 
**private_cloud** | [**PrivateCloudPutPrivateCloud**](PrivateCloudPutPrivateCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud_put import PrivateCloudPut

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloudPut from a JSON string
private_cloud_put_instance = PrivateCloudPut.from_json(json)
# print the JSON string representation of the object
print PrivateCloudPut.to_json()

# convert the object into a dict
private_cloud_put_dict = private_cloud_put_instance.to_dict()
# create an instance of PrivateCloudPut from a dict
private_cloud_put_form_dict = private_cloud_put.from_dict(private_cloud_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


