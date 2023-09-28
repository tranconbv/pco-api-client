# PrivateCloudLocations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**whitelist** | **str** |  | [optional] 
**ike_version** | [**PrivateCloudLocationsIKEVersion**](PrivateCloudLocationsIKEVersion.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud_locations import PrivateCloudLocations

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloudLocations from a JSON string
private_cloud_locations_instance = PrivateCloudLocations.from_json(json)
# print the JSON string representation of the object
print PrivateCloudLocations.to_json()

# convert the object into a dict
private_cloud_locations_dict = private_cloud_locations_instance.to_dict()
# create an instance of PrivateCloudLocations from a dict
private_cloud_locations_form_dict = private_cloud_locations.from_dict(private_cloud_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


