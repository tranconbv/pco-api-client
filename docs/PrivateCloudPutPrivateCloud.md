# PrivateCloudPutPrivateCloud


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_status** | **str** |  | [optional] 
**public_ip** | **str** |  | [optional] 
**internal_ip** | **str** |  | [optional] 
**subnet** | **str** |  | [optional] 
**vpn_gateway_ip** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**whitelist** | **str** |  | [optional] 
**vm_name** | **str** |  | [optional] 
**vm_user** | **str** |  | [optional] 
**vm_password** | **str** |  | [optional] 
**database_user** | **str** |  | [optional] 
**boxwise_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud_put_private_cloud import PrivateCloudPutPrivateCloud

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloudPutPrivateCloud from a JSON string
private_cloud_put_private_cloud_instance = PrivateCloudPutPrivateCloud.from_json(json)
# print the JSON string representation of the object
print PrivateCloudPutPrivateCloud.to_json()

# convert the object into a dict
private_cloud_put_private_cloud_dict = private_cloud_put_private_cloud_instance.to_dict()
# create an instance of PrivateCloudPutPrivateCloud from a dict
private_cloud_put_private_cloud_form_dict = private_cloud_put_private_cloud.from_dict(private_cloud_put_private_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


