# openapi_client.PrivateCloudApi

All URIs are relative to *https://tranconcloud-accp.mendixcloud.com/rest/cloudapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_cloud_get**](PrivateCloudApi.md#private_cloud_get) | **GET** /PrivateCloud | 
[**private_cloud_id_locations_name_delete**](PrivateCloudApi.md#private_cloud_id_locations_name_delete) | **DELETE** /PrivateCloud/{Id}/Locations/{Name} | 
[**private_cloud_id_locations_put**](PrivateCloudApi.md#private_cloud_id_locations_put) | **PUT** /PrivateCloud/{Id}/Locations | 
[**private_cloud_id_whitelist_post**](PrivateCloudApi.md#private_cloud_id_whitelist_post) | **POST** /PrivateCloud/{Id}/Whitelist | 
[**private_cloud_locations_get**](PrivateCloudApi.md#private_cloud_locations_get) | **GET** /PrivateCloud/Locations | 
[**private_cloud_post**](PrivateCloudApi.md#private_cloud_post) | **POST** /PrivateCloud | 
[**private_cloud_put**](PrivateCloudApi.md#private_cloud_put) | **PUT** /PrivateCloud | 


# **private_cloud_get**
> List[PrivateCloud2] private_cloud_get(status=status, type=type, env_id=env_id)



### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud2 import PrivateCloud2
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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    status = 'status_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    env_id = 'env_id_example' # str |  (optional)

    try:
        api_response = api_instance.private_cloud_get(status=status, type=type, env_id=env_id)
        print("The response of PrivateCloudApi->private_cloud_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **env_id** | **str**|  | [optional] 

### Return type

[**List[PrivateCloud2]**](PrivateCloud2.md)

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

# **private_cloud_id_locations_name_delete**
> str private_cloud_id_locations_name_delete(id, name)



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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = api_instance.private_cloud_id_locations_name_delete(id, name)
        print("The response of PrivateCloudApi->private_cloud_id_locations_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_id_locations_name_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

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

# **private_cloud_id_locations_put**
> str private_cloud_id_locations_put(id, status=status)



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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    id = 'id_example' # str | 
    status = None # object |  (optional)

    try:
        api_response = api_instance.private_cloud_id_locations_put(id, status=status)
        print("The response of PrivateCloudApi->private_cloud_id_locations_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_id_locations_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **object**|  | [optional] 

### Return type

**str**

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

# **private_cloud_id_whitelist_post**
> str private_cloud_id_whitelist_post(id)



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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.private_cloud_id_whitelist_post(id)
        print("The response of PrivateCloudApi->private_cloud_id_whitelist_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_id_whitelist_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

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

# **private_cloud_locations_get**
> List[PrivateCloud] private_cloud_locations_get(env_id=env_id, status=status)



### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud import PrivateCloud
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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    env_id = 'env_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        api_response = api_instance.private_cloud_locations_get(env_id=env_id, status=status)
        print("The response of PrivateCloudApi->private_cloud_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_locations_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**List[PrivateCloud]**](PrivateCloud.md)

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

# **private_cloud_post**
> object private_cloud_post(private_cloud=private_cloud)



### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud_post import PrivateCloudPOST
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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    private_cloud = openapi_client.PrivateCloudPOST() # PrivateCloudPOST |  (optional)

    try:
        api_response = api_instance.private_cloud_post(private_cloud=private_cloud)
        print("The response of PrivateCloudApi->private_cloud_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_cloud** | [**PrivateCloudPOST**](PrivateCloudPOST.md)|  | [optional] 

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

# **private_cloud_put**
> str private_cloud_put(environment_id=environment_id)



### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud_put import PrivateCloudPUT
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
    api_instance = openapi_client.PrivateCloudApi(api_client)
    environment_id = openapi_client.PrivateCloudPUT() # PrivateCloudPUT |  (optional)

    try:
        api_response = api_instance.private_cloud_put(environment_id=environment_id)
        print("The response of PrivateCloudApi->private_cloud_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**PrivateCloudPUT**](PrivateCloudPUT.md)|  | [optional] 

### Return type

**str**

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

