# PrivateCloud


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**whitelist** | **str** |  | [optional] 
**ike_version** | [**PrivateCloudIKEVersion**](PrivateCloudIKEVersion.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud import PrivateCloud

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloud from a JSON string
private_cloud_instance = PrivateCloud.from_json(json)
# print the JSON string representation of the object
print PrivateCloud.to_json()

# convert the object into a dict
private_cloud_dict = private_cloud_instance.to_dict()
# create an instance of PrivateCloud from a dict
private_cloud_form_dict = private_cloud.from_dict(private_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


