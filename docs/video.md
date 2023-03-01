# Video Client Usage
- [Video Client Usage](#video-client-usage)
  - [Check Upload Permission of Client](#check-upload-permission-of-client)
  - [Upload Video](#upload-video)
  - [Setup Video Settings](#setup-video-settings)
  - [Get Video](#get-video)
  - [Update Video Settings](#update-video-settings)
  - [Delete Video](#delete-video)
## Check Upload Permission of Client
To Check if client has permission to upload video.
```python
api_client.video.has_permission()
```
## Upload Video
Upload video from local file and get its id.
```python
video_id = api_client.video.upload(file='FILENAME')
```
## Setup Video Settings
Setup video settings.  
Settings include description, visibility, product list and thumbnail timestmp in microseconds.  
Filled video settings in a [NewVideo](/src/biggo_api/model/video.py) object.
```python
from biggo_api.enum import Limit
from biggo_api.model import NewVideo, DraftProduct

new_video = NewVideo(
    video_id=video_id,
    description='DESCRIPTION',
    limit=Limit.everyone.name,
    product_list=[DraftProduct(nindex='tw_pec_biggo', oid='1')],
    thumbnail_ts=5000,
)
api_client.video.setup_new_video(new_video=new_video)
```
## Get Video
Get the [Video](/src/biggo_api/model/video.py) by its id.
```python
video = api_client.video.get(video_id=video_id)
```
## Update Video Settings
Update partial settings of video.  
Filled video settings (at least one) in an [EditedVideo](/src/biggo_api/model/video.py) object.
```python
from biggo_api.model import EditedVideo

edited_video = EditedVideo(
    video_id=video_id,
    limit=Limit.non_public.name,
)
api_client.video.update(edited_video=edited_video)
```
## Delete Video
Delete the video by its id.
```python
api_client.video.delete(video_id=video_id)
```
