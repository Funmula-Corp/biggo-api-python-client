# BigGo API Python Client

The official Python client library for BigGo API.

## Installaiton
Install `biggo-api` in virtual environment.
1. create and activate virtual environment
```bash
python3 -m venv <venv-name>
source <venv-name>/bin/activate
```
2. install `biggo-api` using pip
```bash
python3 -m pip install biggo-api
```

## Supported Python Versions
Python 3.9+

## Usage
Begin by importing the APIClient and ClientCredentials from biggo_api module:
```Python
>>> from biggo_api.clients import APIClient, ClientCredentials
```
Next, initialize an authorized API client using client credentials:
```Python
>>> credentials = ClientCredentials(
...     client_id='my_client_id', client_secret='my_client_secret',
... )
>>> api_client = APIClient(client_credentials=credentials)
```
### Video
You can use the video api to upload, get, update and delete the video.  
Let's take a look at the usage of these four basic functions.
#### Upload Video
First, try to upload a local video file:
```Python
>>> video_upload_resp = api_client.video.upload(file='./my_video.mp4')
>>> video_upload_resp
VideoUploadResponse(result=True, video_id='example_id')
```
The id of this newly uploaded video is `example_id`.
#### Get Video
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
#### Update Video Settings
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
#### Delete the video
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
### User
#### Get your own videos
The user api allows you to get your own videos:
```Python
>>> api_client.user.get_own_videos()
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...)], size=1))
```

## Document
See full user guide in [docs folder](docs)  

## API Reference
See [Sphinx-docs folder](Sphinx-docs/_build/markdown/index.md)  

## LICENSE
[MIT](LICENSE)

---
[ :arrow_up: Back to top](#biggo-api-python-client)  