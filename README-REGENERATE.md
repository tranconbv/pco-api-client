# Regenerate this package using this command

This package was generated using the command below. To regenerate it use the same command and commit the new version.

*Production*
```shell
# production
docker run --rm -v "D:/pco-api-client/:/local" openapitools/openapi-generator-cli:v7.3.0 generate `
  -i https://boxwise.mendixcloud.com/rest-doc/rest/cloudapi/v1/openapi.json `
  -g python `
  -o /local
```


*Accept*
```shell
docker run --rm -v "D:/pco-api-client/:/local" openapitools/openapi-generator-cli:v7.3.0 generate `
  -i https://boxwise-accp.mendixcloud.com/rest-doc/rest/cloudapi/v1/openapi.json `
  -g python `
  -o /local 
```
