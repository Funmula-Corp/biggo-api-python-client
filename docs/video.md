# Video Client Usage
- [Video Client Usage](#video-client-usage)
  - [Check Upload Permission of Client](#check-upload-permission-of-client)
  - [Upload Video](#upload-video)
  - [Get Video](#get-video)
  - [Post Video Parameters](#post-video-parameters)
  - [Patch Video Parameters](#patch-video-parameters)
  - [Delete Video](#delete-video)
## Check Upload Permission of Client
To Check if client has permission to upload video.
```Python
>>> api_client.video.has_permission()
VideoPermissionResponse(result=True, at_userid='example_at_userid', region='tw', userid='example_userid')
```
## Upload Video
Upload video from local file.
```Python
>>> api_client.video.upload(file='FILENAME')
VideoUploadResponse(result=True, video_id='example_video_id')
```
## Get Video
Get the [Video](/src/biggo_api/data_models/video.py) by its id.
```Python
>>> get_video_resp = api_client.video.get(video_id='example_video_id')
>>> get_video_resp.video
[BigGoVideo(...)]
```
## Post Video Parameters
Parameters include video_id, access, description, product list, thumbnail_time and title.  
Video parameters would be filled into the [VideoParams](/src/biggo_api/data_models/video.py) object.  
**All parameters are required**.  
(See available Access type [here](/src/biggo_api/enum/access.py))
```Python
>>> from biggo_api.enum import Access
>>> from biggo_api.data_models import VideoParams
>>> video_params = VideoParams(
...     video_id='example_video_id',
...     access=Access.PUBLIC,
...     description='DESCRIPTION',
...     title='TITLE',
... )
>>> api_client.video.update(video_params=video_params)
VideoUpdateResponse(result=True)
```
## Patch Video Parameters
Update partial parameters of the video.  
Video parameters would be filled into the [VideoParams](/src/biggo_api/data_models/video.py) object.  
**At least one parameter except video_id is required**.  
(See available Access type [here](/src/biggo_api/enum/access.py))
```Python
>>> from biggo_api.data_models import VideoParams
>>> video_params = VideoParams(
...     video_id='example_video_id',
...     access=Access.UNLISTED,
... )
>>> api_client.video.partial_update(video_params=video_params)
VideoUpdateResponse(result=True)
```
## Delete Video
Delete the video by its id.
```Python
>>> api_client.video.delete(video_id='example_video_id')
VideoDeleteResponse(result=True)
```
