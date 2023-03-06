# biggo_api.clients package

## Submodules

## biggo_api.clients._auth module

This module contains classes of OAuth 2.0 grant type and their authorization functions.


### _class_ biggo_api.clients._auth.ClientCredentials(client_id: str, client_secret: str)
Bases: `NamedTuple`

The namedtuple class for client credentials.


* **Parameters**

    
    * **client_id** – Client identifier given by the OAuth provider upon registration.


    * **client_secret** – The secret paired to the client_id.



#### client_id(_: `str_ )
Alias for field number 0


#### client_secret(_: `str_ )
Alias for field number 1


### biggo_api.clients._auth.auth_client_credentials(url, client_credentials, verify=True, refresh_url=None)
Authorize client by client credentials grant.


* **Parameters**

    
    * **url** (`str`) – The url address used to fetch token.


    * **client_credentials** (`ClientCredentials`) – A NamedTuple contains client_id and client_secret.


    * **verify** (`bool`) – Verify SSL certificate.


    * **refresh_url** (`Optional`[`str`]) – The url address used to refresh access token.



* **Return type**

    `OAuth2Session`


### Examples

Call this function to get an OAuth2Session using client credentials grant.
Verify its authorization status.

```python
>>> credentials = ClientCredentials(
...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET'
... )
>>> oauth2_session = auth_client_credentials(
...     url='https://api.biggo.com/auth/v1/token',
...     client_credentials=credentials,
... )
>>> oauth2_session.authorized
True
```

## biggo_api.clients._base module

This module define Base Instance Client of BigGo API.


### _class_ biggo_api.clients._base.BaseInstanceClient(oauth2_session, host_url, verify, region=None)
Bases: `object`

Base class of BigGo API Instance Client.

BigGo API Client using OAuth 2.0 ([https://oauth.net/2/](https://oauth.net/2/)).


* **Variables**

    
    * **oauth2_session** – An authorized OAuth2Session object.


    * **host_url** – API host.


    * **region** – Region of client.


    * **verify** – Verify SSL certificate.



#### request(method, path, headers={}, \*\*kwargs)
Send request to /api/v1/{path} using given method, headers and other keyword arguments.


* **Parameters**

    
    * **method** (`str`) – The method of this request.


    * **path** (`str`) – The sub path of request url.



* **Raises**

    
    * [**BigGoAPIError**](biggo_api.md#biggo_api.exception.BigGoAPIError)**(****response status 4xx****, ****error in response body****)** – Client error.


    * **HTTPError****(****response status 4xx**** or ****5xx****)** – Client(rarely) or server error.


    * **HTTPError****(****response status 2xx**** or ****3xx****)** – Result in response body is False.



* **Return type**

    `dict`


### Examples

Send a GET request to ‘[https://api.biggo.com/api/v1/example](https://api.biggo.com/api/v1/example)’.

```python
>>> client.request(method='GET', path='example')
{ "result": True, ... }
```

## biggo_api.clients._user module

The API client of user.


### _class_ biggo_api.clients._user.UserClient(oauth2_session, host_url, verify, region=None)
Bases: `BaseInstanceClient`

Client to access user API.


#### get_own_videos(page=1)
Get client’s own videos.


* **Parameters**

    **page** (`int`) – The page of user videos. (20 videos in one page)



* **Return type**

    [`UserVideoResponse`](biggo_api.md#biggo_api.responses.UserVideoResponse)


### Examples

Assume user has 22 videos, get videos from page 1 to page 3.

```python
>>> user_client.get_user_videos(page=1)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...), ...], size=22))
>>> user_client.get_user_videos(page=2)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...)], size=22))
>>> user_client.get_user_videos(page=3)
UserVideoResponse(result=True, user_video=UserVideo(data=[], size=22))
```


#### get_user_videos(userid, page=1)
Get user’s videos.


* **Parameters**

    
    * **user_id** – The id of user.


    * **page** (`int`) – The page of user videos. (20 videos in one page)



* **Return type**

    [`UserVideoResponse`](biggo_api.md#biggo_api.responses.UserVideoResponse)


### Examples

Assume user has 22 videos, get videos from page 1 to page 3.

```python
>>> user_client.get_user_videos(userid='USERID', page=1)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...), ...], size=22))
>>> user_client.get_user_videos(userid='USERID', page=2)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...)], size=22))
>>> user_client.get_user_videos(userid='USERID', page=3)
UserVideoResponse(result=True, user_video=UserVideo(data=[], size=22))
```

## biggo_api.clients._video module

The API client of video.


### _class_ biggo_api.clients._video.VideoClient(oauth2_session, host_url, verify, region=None)
Bases: `BaseInstanceClient`

Client to access video API.


#### delete(video_id)
Delete video by its id.


* **Parameters**

    **video_id** (`str`) – The id of video.



* **Return type**

    [`VideoDeleteResponse`](biggo_api.md#biggo_api.responses.VideoDeleteResponse)


### Examples

```python
>>> video_client.delete(video_id='VIDEO_ID')
VideoDeleteResponse(result=True)
```


#### get(video_id)
Get video by its id.


* **Parameters**

    **video_id** (`str`) – The id of video.



* **Return type**

    [`VideoResponse`](biggo_api.md#biggo_api.responses.VideoResponse)


### Examples

```python
>>> video_response = video_client.get(video_id='VIDEO_ID')
>>> video_response
VideoResponse(result=True, user=VideoUserInfo(...), video=[BigGoVideo(...)], size=1)
>>> video_response.video
BigGoVideo(video_id='VIDEO_ID', ...)
```


#### has_permission()
Verify permission of client to upload video.


* **Return type**

    [`VideoPermissionResponse`](biggo_api.md#biggo_api.responses.VideoPermissionResponse)


### Examples

```python
>>> video_client.has_permission()
VideoPermissionResponse(result=True, at_userid='BigGoUserID', region='tw', userid='USERID')
```


#### partial_update(video_params)
Update video parameters using PATCH method.


* **Parameters**

    **video_params** ([`VideoParams`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams)) – Parameters of video.



* **Return type**

    [`VideoUpdateResponse`](biggo_api.md#biggo_api.responses.VideoUpdateResponse)


### Examples

Initialize VideoParams object then patch it.

```python
>>> video_params = VideoParams(
...     video_id='VIDEO_ID',
...     access=Access.UNLISTED,
... )
>>> video_client.partial_update(video_params=video_params)
VideoUpdateResponse(result=True)
```


#### update(video_params)
Update video parameters using POST method.

In this method, video_id, access, description and title in VideoParams are required.
Use partial_update method to update partial parameters.


* **Parameters**

    **video_params** ([`VideoParams`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams)) – Parameters of video.



* **Return type**

    [`VideoUpdateResponse`](biggo_api.md#biggo_api.responses.VideoUpdateResponse)


### Examples

Initialize VideoParams object then post it.

```python
>>> video_params = VideoParams(
...     video_id='VIDEO_ID',
...     access=Access.PRIVATE,
...     description='DESCRIPTION',
...     title='TITLE',
... )
>>> video_client.update(video_params=video_params)
VideoUpdateResponse(result=True)
```


#### upload(file)
Upload video from local file.


* **Parameters**

    **file** (`str`) – The file path & name of video file.



* **Return type**

    [`VideoUploadResponse`](biggo_api.md#biggo_api.responses.VideoUploadResponse)


### Examples

Upload local video file at current working directory.

```python
>>> video_client.upload(file='./SAMPLE_VIDEO.mp4')
VideoUploadResponse(result=True, video_id='VIDEO_ID')
```

## biggo_api.clients.api module

This module define a general api client contains clients of instances.


### _class_ biggo_api.clients.api.APIClient(client_credentials, host_url='https://api.biggo.com', region=None, verify=True, \*\*kwargs)
Bases: `object`

The API client wraps all types of clients.

The API client will be authorized using given grant type.


* **Variables**

    
    * **params** – Parameters of API client, including oauth_session, host_url, region and verify.


    * **user** – User client.


    * **video** – Video client.



#### user(_: `UserClient_ )

#### video(_: `VideoClient_ )
## Module contents
