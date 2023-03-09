# Async API Client Usage
- [Initialize Async API Client](#initialize-async-api-client)
- [Authorize Async API Client](#authorize-async-api-client)
  - [Client Credentials](#client-credentials)
- [Async Instance Client Method Usage](#async-instance-client-method-usage)

## Initialize Async API Client
```Python
>>> from biggo_api.async_clients import APIClient
>>> api_client = APIClient()
```
## Authorize Async API Client
### Client Credentials  
Grant client using client credentials.
```Python
>>> from biggo_api.clients import ClientCredentials
>>> credentials = ClientCredentials(
...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
... )
>>> api_client.authorize(client_credentials=credentials)
```
## Async Instance Client Method Usage
All the asynchronous instance clients' methods are the same as synchornous instance clients'.
The only difference is that async method returns coroutine, remember to await it.
For example:
```Python
>>> video_upload_resp = await api_client.video.upload(file='FILENAME')
>>> video_upload_resp.video_id
'example_video_id'
```
---
[ :arrow_left: Back to docs](../docs)
[ :arrow_up: Back to top](#async-api-client-usage)