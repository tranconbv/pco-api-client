# PrivateCloud


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | [optional] 
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
**github_access_token_url** | **str** |  | [optional] 
**worker_status** | **str** |  | [optional] 
**boxwise_version** | [**PrivateCloudBoxwiseVersion**](PrivateCloudBoxwiseVersion.md) |  | [optional] 
**deployment_profile** | [**PrivateCloudDeploymentProfile**](PrivateCloudDeploymentProfile.md) |  | [optional] 
**cloud_size** | [**PrivateCloudCloudSize**](PrivateCloudCloudSize.md) |  | [optional] 
**subscription** | [**PrivateCloudSubscription**](PrivateCloudSubscription.md) |  | [optional] 
**location_vpns** | [**List[LocationVPN]**](LocationVPN.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) |  | [optional] 
**whitelist** | **str** |  | [optional] 

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


