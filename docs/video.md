# Video Client Usage
- [Video Client Usage](#video-client-usage)
  - [Check Upload Permission of Client](#check-upload-permission-of-client)
  - [Upload Video](#upload-video)
  - [Setup Video Settings](#setup-video-settings)
  - [Get Video](#get-video)
  - [Update Video Settings](#update-video-settings)
  - [Delete Video](#delete-video)
## Check Upload Permission of Client
Check client has permission to upload video.
```
video_client.has_permission()
```
## Upload Video
Upload video from local file and get its id.
```
video_id = video_client.upload(file='FILENAME')
```
## Setup Video Settings
Setup video settings.  
Settings include description, visibility, product list and thumbnail timestmp in microseconds.  
Filled video settings in a [NewVideo](/src/biggo_api/model/video.py) object.
```
from biggo_api.enum import Limit
from biggo_api.model import NewVideo, DraftProduct

new_video = NewVideo(
    video_id=video_id,
    description='DESCRIPTION',
    limit=Limit.everyone.name,
    product_list=[DraftProduct(nindex='tw_pec_biggo', oid='1')],
    thumbnail_ts=5000,
)
video_client.setup_new_video(new_video=new_video)
```
## Get Video
Get a [Video](/src/biggo_api/model/video.py) by its id.
```
video = video_client.get(video_id=video_id)
```
## Update Video Settings
Update partial settings of video.  
Filled video settings (at least one) in an [EditedVideo](/src/biggo_api/model/video.py) object.
```
from biggo_api.model import EditedVideo

edited_video = EditedVideo(
    video_id=video_id,
    limit=Limit.non_public.name,
)
video_client.update(edited_video=edited_video)
```
## Delete Video
Delete a video by its id.
```
video_client.delete(video_id=video_id)
```