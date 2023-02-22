# Usage Guide
- [Usage Guide](#usage-guide)
  - [Clients](#clients)
  - [Client Initialization](#client-initialization)
    - [Grant Type](#grant-type)
  - [Check Client Authorization](#check-client-authorization)

---
## Clients
- [Video Client](video.md)
- [Comment Client](comment.md)
- [User Client](user.md)

## Client Initialization
use VideoClient for example
### Grant Type
1. Client Credentials  
Grant client using client credentials.
```
from biggo_api.clients import VideoClient

video_client = VideoClient(
    client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
)
```
## Check Client Authorization
Check if client's OAuth2 Session has OAuth token.
```
video_client.authorized
```