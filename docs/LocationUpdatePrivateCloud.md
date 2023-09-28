# LocationUpdatePrivateCloud


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_vpns** | [**LocationUpdatePrivateCloudLocationVPNs**](LocationUpdatePrivateCloudLocationVPNs.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_update_private_cloud import LocationUpdatePrivateCloud

# TODO update the JSON string below
json = "{}"
# create an instance of LocationUpdatePrivateCloud from a JSON string
location_update_private_cloud_instance = LocationUpdatePrivateCloud.from_json(json)
# print the JSON string representation of the object
print LocationUpdatePrivateCloud.to_json()

# convert the object into a dict
location_update_private_cloud_dict = location_update_private_cloud_instance.to_dict()
# create an instance of LocationUpdatePrivateCloud from a dict
location_update_private_cloud_form_dict = location_update_private_cloud.from_dict(location_update_private_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


