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


    * **client_credentials** (`ClientCredentials`) – A NamedTuple contains client_id and client_secret used for authorization.


    * **verify** (`bool`) – Verify SSL certificate.


    * **refresh_url** (`Optional`[`str`]) – The url address used to refresh access token.



* **Return type**

    `OAuth2Session`


### Examples

Call this function to get an OAuth2Session object using client credentials grant then verify its authorization status.

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
Send request to /api/v1/{path} using given method with headers and other keyword arguments.


* **Parameters**

    
    * **method** (`str`) – The method of this request.


    * **path** (`str`) – The sub path of request url.



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


#### get_own_videos()
Get client’s own videos


* **Return type**

    [`UserVideoResponse`](biggo_api.md#biggo_api.responses.UserVideoResponse)



#### get_user_videos(userid)
Get user’s videos


* **Parameters**

    **user_id** – The id of user



* **Return type**

    [`UserVideoResponse`](biggo_api.md#biggo_api.responses.UserVideoResponse)


## biggo_api.clients._video module

The API client of video.


### _class_ biggo_api.clients._video.VideoClient(oauth2_session, host_url, verify, region=None)
Bases: `BaseInstanceClient`

Client to access video API.


#### delete(video_id)
Delete video.


* **Parameters**

    **video_id** (`str`) – The id of video.



* **Return type**

    [`BaseResponse`](biggo_api.md#biggo_api.responses.BaseResponse)



#### get(video_id)
Get video.


* **Parameters**

    **video_id** (`str`) – The id of video.



* **Return type**

    [`VideoResponse`](biggo_api.md#biggo_api.responses.VideoResponse)



#### has_permission()
Verify permission of client to upload video.


* **Return type**

    [`VideoPermissionResponse`](biggo_api.md#biggo_api.responses.VideoPermissionResponse)



#### patch_video_params(video_params)
Update video parameters using PATCH method.


* **Parameters**

    **video_params** ([`VideoParams`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams)) – Parameters of video.



* **Return type**

    [`VideoUpdateResponse`](biggo_api.md#biggo_api.responses.VideoUpdateResponse)



#### post_video_params(video_params)
Update video parameters using POST method.


* **Parameters**

    **video_params** ([`VideoParams`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams)) – Parameters of video.



* **Return type**

    [`VideoUpdateResponse`](biggo_api.md#biggo_api.responses.VideoUpdateResponse)



#### upload(file)
Upload video from local file.


* **Parameters**

    **file** (`str`) – The file path & name of video file.



* **Return type**

    [`VideoUploadResponse`](biggo_api.md#biggo_api.responses.VideoUploadResponse)


## biggo_api.clients.api module

This module define a general api client contains clients for instances


### _class_ biggo_api.clients.api.APIClient(client_credentials, host_url='https://api.biggo.com', region=None, verify=True, \*\*kwargs)
Bases: `object`

The API Client wraps all types of client


* **Variables**

    
    * **user** – See `biggo_api.clients.user.UserClient`


    * **video** – See `biggo_api.clients.video.VideoClient`


## Module contents
