# PrivateCloudPOST


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
**boxwise_version** | [**PrivateCloudIKEVersion**](PrivateCloudIKEVersion.md) |  | [optional] 
**deployment_profile** | [**PrivateCloud2DeploymentProfile**](PrivateCloud2DeploymentProfile.md) |  | [optional] 
**environment_id** | [**PrivateCloud2EnvironmentId**](PrivateCloud2EnvironmentId.md) |  | [optional] 
**cloud_size** | [**PrivateCloudPOSTCloudSize**](PrivateCloudPOSTCloudSize.md) |  | [optional] 
**subscription** | [**PrivateCloudPOSTSubscription**](PrivateCloudPOSTSubscription.md) |  | [optional] 
**github_access_token_url** | **str** |  | [optional] 
**worker_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud_post import PrivateCloudPOST

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloudPOST from a JSON string
private_cloud_post_instance = PrivateCloudPOST.from_json(json)
# print the JSON string representation of the object
print PrivateCloudPOST.to_json()

# convert the object into a dict
private_cloud_post_dict = private_cloud_post_instance.to_dict()
# create an instance of PrivateCloudPOST from a dict
private_cloud_post_form_dict = private_cloud_post.from_dict(private_cloud_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


