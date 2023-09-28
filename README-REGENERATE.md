# Regenerate this package using this command

This package was generated using the command below. To regenerate it use the same command and commit the new version.

*powershell*
```shell
docker run --rm -v "./:/local" openapitools/openapi-generator-cli generate `
  -i https://static.app.boxwise.nl/pco/swagger.json `
  -g python `
  -o /local 
```
