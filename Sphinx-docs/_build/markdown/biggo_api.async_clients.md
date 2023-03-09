# biggo_api.async_clients package

## Submodules

## biggo_api.async_clients._auth module

This module contains asynchronous authorization functions of OAuth 2.0 grant type.


### _async_ biggo_api.async_clients._auth.auth_client_credentials(url, client_credentials, verify_ssl=True, refresh_url=None)
Authorize client by client credentials grant asynchronously.


* **Parameters**

    
    * **url** (`str`) – The url address used to fetch token.


    * **client_credentials** ([`ClientCredentials`](biggo_api.clients.md#biggo_api.clients._auth.ClientCredentials)) – A NamedTuple contains client_id and client_secret.


    * **verify_ssl** (`bool`) – Verify SSL certificate.


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
>>> oauth2_session = await auth_client_credentials(
...     url='https://api.biggo.com/auth/v1/token',
...     client_credentials=credentials,
... )
>>> oauth2_session.authorized
True
```

## biggo_api.async_clients._base module

This module define asynchronous Base Instance Client of BigGo API.


### _class_ biggo_api.async_clients._base.BaseInstanceClient(oauth2_session, host_url, verify_ssl, region=None)
Bases: `object`

Base class of Async BigGo API Instance Client.

BigGo API Client using OAuth 2.0 ([https://oauth.net/2/](https://oauth.net/2/)).


* **Variables**

    
    * **oauth2_session** – An authorized OAuth2Session object.


    * **host_url** – API host.


    * **region** – Region of client.


    * **verify_ssl** – Verify SSL certificate.



#### _async_ request(method, path, headers={}, \*\*kwargs)
Send request asynchronously to /api/v1/{path} using given method, headers and other keyword arguments.


* **Parameters**

    
    * **method** (`str`) – The method of this request.


    * **path** (`str`) – The sub path of request url.



* **Raises**

    
    * [**BigGoAPIError**](biggo_api.md#biggo_api.exception.BigGoAPIError)**(****response status 4xx****, ****error in response body****)** – Client error.


    * **ClientResponseError****(****response status 4xx**** or ****5xx****)** – Parse failed client error or server error.


    * **ClientResponseError****(****response status 2xx**** or ****3xx****)** – Result in response body is False.



* **Return type**

    `dict`


### Examples

Send a GET request to ‘[https://api.biggo.com/api/v1/example](https://api.biggo.com/api/v1/example)’.

```python
>>> await client.request(method='GET', path='example')
{ "result": True, ... }
```

## biggo_api.async_clients._user module

The asynchronous API client of user.


### _class_ biggo_api.async_clients._user.UserClient(oauth2_session, host_url, verify_ssl, region=None)
Bases: `BaseInstanceClient`

Async client to access user API.


#### _async_ get_own_videos(page=1)
Get client’s own videos asynchronously.


* **Parameters**

    **page** (`int`) – The page of user videos. (20 videos in one page)



* **Return type**

    [`UserVideoResponse`](biggo_api.md#biggo_api.responses.UserVideoResponse)


### Examples

Assume user has 22 videos, get videos from page 1 to page 3.

```python
>>> await user_client.get_user_videos(page=1)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...), ...], size=22))
>>> await user_client.get_user_videos(page=2)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...)], size=22))
>>> await user_client.get_user_videos(page=3)
UserVideoResponse(result=True, user_video=UserVideo(data=[], size=22))
```


#### _async_ get_user_videos(userid, page=1)
Get user’s videos asynchronously.


* **Parameters**

    
    * **user_id** – The id of user.


    * **page** (`int`) – The page of user videos. (20 videos in one page)



* **Return type**

    [`UserVideoResponse`](biggo_api.md#biggo_api.responses.UserVideoResponse)


### Examples

Assume user has 22 videos, get videos from page 1 to page 3.

```python
>>> await user_client.get_user_videos(userid='USERID', page=1)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...), ...], size=22))
>>> await user_client.get_user_videos(userid='USERID', page=2)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...)], size=22))
>>> await user_client.get_user_videos(userid='USERID', page=3)
UserVideoResponse(result=True, user_video=UserVideo(data=[], size=22))
```

## biggo_api.async_clients._video module

The asynchronous API client of video.


### _class_ biggo_api.async_clients._video.VideoClient(oauth2_session, host_url, verify_ssl, region=None)
Bases: `BaseInstanceClient`

Async client to access video API.


#### _async_ delete(video_id)
Delete video asynchronously by its id.


* **Parameters**

    **video_id** (`str`) – The id of video.



* **Return type**

    [`VideoDeleteResponse`](biggo_api.md#biggo_api.responses.VideoDeleteResponse)


### Examples

```python
>>> await video_client.delete(video_id='VIDEO_ID')
VideoDeleteResponse(result=True)
```


#### _async_ get(video_id)
Get video asynchronously by its id.


* **Parameters**

    **video_id** (`str`) – The id of video.



* **Return type**

    [`VideoResponse`](biggo_api.md#biggo_api.responses.VideoResponse)


### Examples

```python
>>> video_response = await video_client.get(video_id='VIDEO_ID')
>>> video_response
VideoResponse(result=True, user=VideoUserInfo(...), video=[BigGoVideo(...)], size=1)
>>> video_response.video
BigGoVideo(video_id='VIDEO_ID', ...)
```


#### _async_ has_permission()
Verify permission of client to upload video asynchronously.


* **Return type**

    [`VideoPermissionResponse`](biggo_api.md#biggo_api.responses.VideoPermissionResponse)


### Examples

```python
>>> await video_client.has_permission()
VideoPermissionResponse(result=True, at_userid='BigGoUserID', region='tw', userid='USERID')
```


#### _async_ partial_update(video_params)
Update video parameters asynchronously using PATCH method.


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
>>> await video_client.partial_update(video_params=video_params)
VideoUpdateResponse(result=True)
```


#### _async_ update(video_params)
Update video parameters asynchronously using POST method.

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
>>> await video_client.update(video_params=video_params)
VideoUpdateResponse(result=True)
```


#### _async_ upload(file)
Upload video asynchronously from local file.


* **Parameters**

    **file** (`str`) – The file path & name of video file.



* **Return type**

    [`VideoUploadResponse`](biggo_api.md#biggo_api.responses.VideoUploadResponse)


### Examples

Upload local video file at current working directory.

```python
>>> await video_client.upload(file='./SAMPLE_VIDEO.mp4')
VideoUploadResponse(result=True, video_id='VIDEO_ID')
```

## biggo_api.async_clients.api module

This module define a general async api client contains async clients of instances.


### _class_ biggo_api.async_clients.api.APIClient(host_url='https://api.biggo.com', region=None, verify_ssl=True, \*\*kwargs)
Bases: `object`

The async API client wraps all types of async clients.

The API client will be authorized by passing grant type into authorize method.


* **Variables**

    
    * **params** – Parameters of API client, including oauth_session, host_url, region and verify_ssl.


    * **user** – User client.


    * **video** – Video client.



#### _async_ authorize(client_credentials)
Authorize client asynchronously using given grant type.


* **Parameters**

    **client_credentials** (`Optional`[[`ClientCredentials`](biggo_api.clients.md#biggo_api.clients._auth.ClientCredentials)]) – Parameters for client credentials grant type.


### Examples

```python
>>> client_credentials = ClientCredentials(
...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
... )
>>> api_client = APIClient()
>>> await api_client.authorize(client_credentials=client_credentials)
```


#### _async_ close()
Close OAuth2Session.

### Examples

```python
>>> await api_client.close()
```


#### params(_: `dict_ _ = {_ )

#### user(_: `UserClient_ _ = Non_ )

#### video(_: `VideoClient_ _ = Non_ )
## Module contents
