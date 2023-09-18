# PrivateCloud2Subscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] 
**license_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud2_subscription import PrivateCloud2Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloud2Subscription from a JSON string
private_cloud2_subscription_instance = PrivateCloud2Subscription.from_json(json)
# print the JSON string representation of the object
print PrivateCloud2Subscription.to_json()

# convert the object into a dict
private_cloud2_subscription_dict = private_cloud2_subscription_instance.to_dict()
# create an instance of PrivateCloud2Subscription from a dict
private_cloud2_subscription_form_dict = private_cloud2_subscription.from_dict(private_cloud2_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


