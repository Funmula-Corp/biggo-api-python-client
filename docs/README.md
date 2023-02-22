# Usage Guide
- [Usage Guide](#usage-guide)
  - [Clients](#clients)
  - [Initialize API Client](#initialize-api-client)
    - [Client Credentials](#client-credentials)

---
## Clients
- [Video Client](video.md)
- [Comment Client](comment.md)
- [User Client](user.md)

## Initialize API Client
Initialize API Client for different grant type.  
Currently support: [client credentials](#client-credentials).
### Client Credentials  
Grant client using client credentials.
```
from biggo_api.clients import APIClient

api_client = APIClient(
    client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
)
```