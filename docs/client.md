# API Client Usage
- [Initialize and Authorize API Client](#initialize-and-authorize-api-client)
  - [Client Credentials](#client-credentials)

## Initialize and Authorize API Client
### Client Credentials  
Grant client using client credentials.
```Python
>>> from biggo_api.clients import APIClient, ClientCredentials
>>> credentials = ClientCredentials(
...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
... )
>>> api_client = APIClient(client_credentials=credentials)
```
---
[ :arrow_left: Back to docs](../docs)
[ :arrow_up: Back to top](#api-client-usage)