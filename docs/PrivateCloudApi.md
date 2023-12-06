# openapi_client.PrivateCloudApi

All URIs are relative to *https://tranconcloud.mendixcloud.com/rest/cloudapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_cloud_delete**](PrivateCloudApi.md#private_cloud_delete) | **DELETE** /PrivateCloud | 
[**private_cloud_get**](PrivateCloudApi.md#private_cloud_get) | **GET** /PrivateCloud | 
[**private_cloud_location_delete**](PrivateCloudApi.md#private_cloud_location_delete) | **DELETE** /PrivateCloud/Location | 
[**private_cloud_location_post**](PrivateCloudApi.md#private_cloud_location_post) | **POST** /PrivateCloud/Location | 
[**private_cloud_location_put**](PrivateCloudApi.md#private_cloud_location_put) | **PUT** /PrivateCloud/Location | 
[**private_cloud_post**](PrivateCloudApi.md#private_cloud_post) | **POST** /PrivateCloud | 
[**private_cloud_put**](PrivateCloudApi.md#private_cloud_put) | **PUT** /PrivateCloud | 


# **private_cloud_delete**
> object private_cloud_delete(environment_id=environment_id)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    environment_id = 'environment_id_example' # str |  (optional)

    try:
        api_response = api_instance.private_cloud_delete(environment_id=environment_id)
        print("The response of PrivateCloudApi->private_cloud_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | [optional] 

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

# **private_cloud_get**
> List[PrivateCloud] private_cloud_get(environment_id=environment_id, status=status, type=type)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud import PrivateCloud
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    environment_id = 'environment_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        api_response = api_instance.private_cloud_get(environment_id=environment_id, status=status, type=type)
        print("The response of PrivateCloudApi->private_cloud_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

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

# **private_cloud_location_delete**
> object private_cloud_location_delete(environment_id=environment_id, location=location)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    environment_id = 'environment_id_example' # str |  (optional)
    location = 'location_example' # str |  (optional)

    try:
        api_response = api_instance.private_cloud_location_delete(environment_id=environment_id, location=location)
        print("The response of PrivateCloudApi->private_cloud_location_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_location_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | [optional] 
 **location** | **str**|  | [optional] 

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

# **private_cloud_location_post**
> object private_cloud_location_post(environment_id=environment_id, location=location)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.models.location import Location
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    environment_id = 'environment_id_example' # str |  (optional)
    location = openapi_client.Location() # Location |  (optional)

    try:
        api_response = api_instance.private_cloud_location_post(environment_id=environment_id, location=location)
        print("The response of PrivateCloudApi->private_cloud_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | [optional] 
 **location** | [**Location**](Location.md)|  | [optional] 

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

# **private_cloud_location_put**
> object private_cloud_location_put(environment_id=environment_id, location=location)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.models.location import Location
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    environment_id = 'environment_id_example' # str |  (optional)
    location = openapi_client.Location() # Location |  (optional)

    try:
        api_response = api_instance.private_cloud_location_put(environment_id=environment_id, location=location)
        print("The response of PrivateCloudApi->private_cloud_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | [optional] 
 **location** | [**Location**](Location.md)|  | [optional] 

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

# **private_cloud_post**
> object private_cloud_post(private_cloud=private_cloud)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud2 import PrivateCloud2
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    private_cloud = openapi_client.PrivateCloud2() # PrivateCloud2 |  (optional)

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
 **private_cloud** | [**PrivateCloud2**](PrivateCloud2.md)|  | [optional] 

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
> object private_cloud_put(private_cloud=private_cloud)



### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import openapi_client
from openapi_client.models.private_cloud2 import PrivateCloud2
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tranconcloud.mendixcloud.com/rest/cloudapi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tranconcloud.mendixcloud.com/rest/cloudapi/v1"
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
    private_cloud = openapi_client.PrivateCloud2() # PrivateCloud2 |  (optional)

    try:
        api_response = api_instance.private_cloud_put(private_cloud=private_cloud)
        print("The response of PrivateCloudApi->private_cloud_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateCloudApi->private_cloud_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_cloud** | [**PrivateCloud2**](PrivateCloud2.md)|  | [optional] 

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

