# Regenerate this package using this command

This package was generated using the command below. To regenerate it use the same command and commit the new version.

*powershell*
```shell
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate `
  -i https://tranconcloud.mendixcloud.com/rest-doc/rest/cloudapi/v1/swagger.json `
  -g python `
  -o /local/out/python 
```
