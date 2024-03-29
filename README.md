# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    except ApiException as e:
        print("Exception when calling PrivateCloudApi->private_cloud_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://tranconcloud.mendixcloud.com/rest/cloudapi/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PrivateCloudApi* | [**private_cloud_delete**](docs/PrivateCloudApi.md#private_cloud_delete) | **DELETE** /PrivateCloud | 
*PrivateCloudApi* | [**private_cloud_get**](docs/PrivateCloudApi.md#private_cloud_get) | **GET** /PrivateCloud | 
*PrivateCloudApi* | [**private_cloud_location_delete**](docs/PrivateCloudApi.md#private_cloud_location_delete) | **DELETE** /PrivateCloud/Location | 
*PrivateCloudApi* | [**private_cloud_location_post**](docs/PrivateCloudApi.md#private_cloud_location_post) | **POST** /PrivateCloud/Location | 
*PrivateCloudApi* | [**private_cloud_location_put**](docs/PrivateCloudApi.md#private_cloud_location_put) | **PUT** /PrivateCloud/Location | 
*PrivateCloudApi* | [**private_cloud_post**](docs/PrivateCloudApi.md#private_cloud_post) | **POST** /PrivateCloud | 
*PrivateCloudApi* | [**private_cloud_put**](docs/PrivateCloudApi.md#private_cloud_put) | **PUT** /PrivateCloud | 


## Documentation For Models

 - [Location](docs/Location.md)
 - [LocationVPN](docs/LocationVPN.md)
 - [LocationVPNIKEVersion](docs/LocationVPNIKEVersion.md)
 - [PrivateCloud](docs/PrivateCloud.md)
 - [PrivateCloud2](docs/PrivateCloud2.md)
 - [PrivateCloudBoxwiseVersion](docs/PrivateCloudBoxwiseVersion.md)
 - [PrivateCloudCloudSize](docs/PrivateCloudCloudSize.md)
 - [PrivateCloudDeploymentProfile](docs/PrivateCloudDeploymentProfile.md)
 - [PrivateCloudSubscription](docs/PrivateCloudSubscription.md)
 - [Subnets](docs/Subnets.md)
 - [WhitelistedSubnets](docs/WhitelistedSubnets.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication


## Author




