# PrivateCloudSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.private_cloud_subscription import PrivateCloudSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCloudSubscription from a JSON string
private_cloud_subscription_instance = PrivateCloudSubscription.from_json(json)
# print the JSON string representation of the object
print PrivateCloudSubscription.to_json()

# convert the object into a dict
private_cloud_subscription_dict = private_cloud_subscription_instance.to_dict()
# create an instance of PrivateCloudSubscription from a dict
private_cloud_subscription_form_dict = private_cloud_subscription.from_dict(private_cloud_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


