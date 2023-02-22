# B!gGo API Python Client

The official Python client library for BigGo API.

## Documentation
---
See usage guide in [docs folder](docs)

## Installaiton
---
Install `biggo-api` in virtual environment.
1. create and activate virtual environment
```
python3 -m venv <venv-name>
source <venv-name>/bin/activate
```
2. install `biggo-api`
```
pip install biggo-api
```

## Usage
---
### Quick Example
```Python
from biggo_api.clients import APIClient
from biggo_api.enum import Limit
from biggo_api.model import DraftProduct, NewVideo

# inititalize api client
api_client = APIClient(client_id=<client_id>, client_secret=<client_secret>)
# upload video
video_id = api_client.video.upload(file=<file>)

# setup video settings
new_video = NewVideo(
    video_id=video_id,
    limit=Limit.everyone.name,
    product_list=[DraftProduct(nindex=<nindex>, oid=<product_oid>)],
    thumbnail_ts=5000,
)
api_client.video.setup_new_video(new_video=new_video)

# get video
video = api_client.video.get(video_id=video_id)

# update video settings partially
edited_video = EditedVideo(
    video_id=video_id,
    limit=Limit.limit_myself.name,
)
api_client.video.update(edited_video=edited_video)
```

## Supported Python Versions
Python 3.9+

