# Usage Guide
- [Clients](#clients)
- [Initialize and Authorize API Client](#initialize-and-authorize-api-client)
  - [Client Credentials](#client-credentials)

---
## Clients
- [Video Client](video.md)
- [User Client](user.md)

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
[ :arrow_up: Back to top](#usage-guide)