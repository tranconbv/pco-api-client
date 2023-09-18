# PrivateCloud2


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
**whitelist** | **str** |  | [optional] 
**boxwise_version** | [**PrivateCloud2BoxwiseVersion**](PrivateCloud2BoxwiseVersion.md) |  | [optional] 
**deployment_profile** | [**PrivateCloud2DeploymentProfile**](PrivateCloud2DeploymentProfile.md) |  | [optional] 
**environment_id** | [**PrivateCloud2EnvironmentId**](PrivateCloud2EnvironmentId.md) |  | [optional] 
**location_vpns** | [**List[LocationVPN]**](LocationVPN.md) |  | [optional] 
**cloud_size** | [**PrivateCloud2CloudSize**](PrivateCloud2CloudSize.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) |  | [optional] 
**subscription** | [**PrivateCloud2Subscription**](PrivateCloud2Subscription.md) |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud2 import PrivateCloud2

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloud2 from a JSON string
private_cloud2_instance = PrivateCloud2.from_json(json)
# print the JSON string representation of the object
print PrivateCloud2.to_json()

# convert the object into a dict
private_cloud2_dict = private_cloud2_instance.to_dict()
# create an instance of PrivateCloud2 from a dict
private_cloud2_form_dict = private_cloud2.from_dict(private_cloud2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


