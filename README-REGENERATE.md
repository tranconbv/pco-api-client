# Regenerate this package using this command

This package was generated using the command below. To regenerate it use the same command and commit the new version.

*Production*
```shell
# production
docker run --rm -v "C:/Dev/pco-api-client/:/local" openapitools/openapi-generator-cli generate `
  -i https://static.app.boxwise.nl/pco/swagger.json `
  -g python `
  -o /local
```


*Accept*
```shell
docker run --rm -v "C:/Dev/pco-api-client/:/local" openapitools/openapi-generator-cli generate `
  -i https://tranconcloud-accp.mendixcloud.com/rest-doc/rest/cloudapi/v1/swagger.json `
  -g python `
  -o /local 
```
