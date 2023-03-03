# Usage Guide
- [Usage Guide](#usage-guide)
  - [Clients](#clients)
  - [Initialize API Client](#initialize-api-client)
    - [Client Credentials](#client-credentials)

---
## Clients
- [Video Client](video.md)
- [User Client](user.md)

## Initialize API Client
Initialize API Client for different grant type.  
Currently support: [client credentials](#client-credentials).
### Client Credentials  
Grant client using client credentials.
```Python
>>> from biggo_api.clients import APIClient, ClientCredentials
>>> credentials = ClientCredentials(
...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
... )
>>> api_client = APIClient(client_credentials=credentials)
```