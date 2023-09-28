# PrivateCloudCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_status** | **str** |  | [optional] 
**vm_name** | **str** |  | [optional] 
**vm_user** | **str** |  | [optional] 
**vm_password** | **str** |  | [optional] 
**database_user** | **str** |  | [optional] 
**database_password** | **str** |  | [optional] 
**shared_secret** | **str** |  | [optional] 
**public_ip** | **str** |  | [optional] 
**internal_ip** | **str** |  | [optional] 
**subnet** | **str** |  | [optional] 
**vpn_gateway** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**boxwise_url** | **str** |  | [optional] 
**boxwise_version** | [**PrivateCloudBoxwiseVersion**](PrivateCloudBoxwiseVersion.md) |  | [optional] 
**deployment_profile** | [**PrivateCloudDeploymentProfile**](PrivateCloudDeploymentProfile.md) |  | [optional] 
**environment_id** | [**PrivateCloudEnvironmentId**](PrivateCloudEnvironmentId.md) |  | [optional] 
**cloud_size** | [**PrivateCloudCreateCloudSize**](PrivateCloudCreateCloudSize.md) |  | [optional] 
**subscription** | [**PrivateCloudCreateSubscription**](PrivateCloudCreateSubscription.md) |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud_create import PrivateCloudCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloudCreate from a JSON string
private_cloud_create_instance = PrivateCloudCreate.from_json(json)
# print the JSON string representation of the object
print PrivateCloudCreate.to_json()

# convert the object into a dict
private_cloud_create_dict = private_cloud_create_instance.to_dict()
# create an instance of PrivateCloudCreate from a dict
private_cloud_create_form_dict = private_cloud_create.from_dict(private_cloud_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


