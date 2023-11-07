# openapi_client.LocationsApi

All URIs are relative to *https://tranconcloud-accp.mendixcloud.com/rest/cloudapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_id_loc_whitelist_post**](LocationsApi.md#locations_id_loc_whitelist_post) | **POST** /Locations/{Id}/{Loc}/Whitelist | 
[**locations_post**](LocationsApi.md#locations_post) | **POST** /Locations | 


# **locations_id_loc_whitelist_post**
> object locations_id_loc_whitelist_post(id, loc)



### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud-accp.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud-accp.mendixcloud.com/rest/cloudapi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LocationsApi(api_client)
    id = 'id_example' # str | 
    loc = 'loc_example' # str | 

    try:
        api_response = api_instance.locations_id_loc_whitelist_post(id, loc)
        print("The response of LocationsApi->locations_id_loc_whitelist_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_id_loc_whitelist_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **loc** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Authentication information is missing or invalid |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_post**
> object locations_post()



### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud-accp.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud-accp.mendixcloud.com/rest/cloudapi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LocationsApi(api_client)

    try:
        api_response = api_instance.locations_post()
        print("The response of LocationsApi->locations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_post: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Authentication information is missing or invalid |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

