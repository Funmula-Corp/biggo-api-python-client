Tutorial
===
In this tutorial, we will use the video api to upload, get, update and delete an example video.  
First, try to upload a local video file:
```Python
>>> video_upload_resp = api_client.video.upload(file='./my_video.mp4')
>>> video_upload_resp
VideoUploadResponse(result=True, video_id='example_id')
```
The id of this newly uploaded video is `example_id`.
Next, try to get the video from APIClient:
```Python
>>> video_get_resp = api_client.video.get(video_id='example_id')
>>> video_get_resp
VideoResponse(result=True, user=VideoUserInfo(...), video=[BigGoVideo(...)], size=1)
```
The data we need is in the attribute `video`:
```Python
>>> video = video_get_resp.video[0]
```
Now, we have a BigGoVideo object called video. We can get all the information we need from this object.
```Python
>>> video.video_id
'example_id'
>>> video.created_at
'2023-03-01T00:00:00.0000'
>>> video.is_myvideo
True
>>> video.description
#None
```
The description of this video is `None`, we should add some text to it.  
Import the data model `VideoParams` first:
```Python
>>> from biggo_api.data_models import VideoParams
```
Initialize the object by filling video_id and description into it:
```Python
>>> video_params = VideoParams(
...     video_id='example_id',
...     description='my first video',
... )
>>> video_params
VideoParams(access=None, description='my first video', product_list=None, thumbnail_time=None, title=None, video_id='example_id')
```
There is a lot of `None` value in the object `video_params`, just ignore them because the `partial_update` function will remove all the fields whose value is `None` when sending request.  
Now, call the update function to update the description of video:
```Python
>>> api_client.video.partial_update(video_params=video_params)
VideoUpdateResponse(result=True)
```
Get the video again, the description is updated.
```Python3
>>> updated_video = api_client.video.get(video_id='example_id').video[0]
>>> updated_video.description
'my first video'
```
Let's take a look of your own videos before deleting the example video:
```Python
>>> api_client.user.get_own_videos()
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(video_id='example_id', ...)], size=1))
```
Finally, delete this example video:
```Python
>>> api_client.video.delete(video_id='example_id')
VideoDeleteResponse(result=True)
```
When you try to get the deleted video, it will raise an BigGoAPIError:
```Python
>>> api_client.video.get(video_id='example_id')
Traceback (most recent call last):
  ...
biggo_api.exception.BigGoAPIError: result=False error=Error(code=1004, message='The video does not exist.')
```

---
[ :arrow_up: Back to top](#tutorial)  
[ :leftwards_arrow_with_hook: Back to docs](../docs)