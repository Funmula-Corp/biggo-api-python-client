# biggo_api.clients package

## Submodules

## biggo_api.clients._auth module

This module contains classes of OAuth 2.0 grant type and their authorization function


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
Authorize client by client credentials


* **Parameters**

    
    * **url** (`str`) – The url address to fetch token


    * **client_credentials** (`ClientCredentials`) – A NamedTuple contains client_id and client_secret used for authorization


    * **verify** (`bool`) – Verify SSL certificate


    * **refresh_url** (`Optional`[`str`]) – The url address to refresh access token



* **Return type**

    `OAuth2Session`


### Examples

Use this function to get an OAuth2Session object by client credentials then verify its authorization status.

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

Base API Instance Client


### _class_ biggo_api.clients._base.BaseInstanceClient(oauth2_session, host_url, verify, region=None)
Bases: `object`

Base class of BigGo API Instance Client

BigGo API Client using OAuth 2.0 ([https://oauth.net/2/](https://oauth.net/2/)).


* **Variables**

    
    * **oauth2_session** – An authorized requests_oauthlib.OAuth2Session object


    * **host_url** – API host


    * **region** – Region of client, leave it None will auto filled by server


    * **verify** – Verify SSL certificate



#### request(method, path, headers={}, \*\*kwargs)
Send request to /api/v1/{path} using given method with keyword arguments


* **Parameters**

    
    * **method** (`str`) – The method of this request


    * **path** (`str`) – The sub path of request url after {host}/{api_path}



* **Return type**

    `dict`


### Examples

send a GET request to ‘[https://api.biggo.com/api/v1/example](https://api.biggo.com/api/v1/example)’

```python
>>> client.request(method='GET', path='example')
{ "result": True, ... }
```

## biggo_api.clients._comment module

The API client of video comment


### _class_ biggo_api.clients._comment.CommentClient(oauth2_session, host_url, verify, region=None)
Bases: `BaseInstanceClient`

Client to access video comment API


#### create(new_comment)
Create new comment


* **Parameters**

    **new_comment** ([`NewComment`](biggo_api.model.md#biggo_api.model.comment.NewComment)) – A `biggo_api.model.NewComment` object



* **Return type**

    [`CommentResponse`](biggo_api.model.md#biggo_api.model.comment.CommentResponse)



#### delete(comment_id)
Delete comment


* **Parameters**

    **comment_id** (`str`) – The id of comment



* **Return type**

    `bool`



#### get_comment_history()
Get comment log


* **Return type**

    `list`[[`CommentHistory`](biggo_api.model.md#biggo_api.model.comment.CommentHistory)]



#### get_list(video_id, parent_id=None)
Get list of comments


* **Parameters**

    
    * **video_id** (`str`) – The id of video


    * **parent_id** (`str`) – The id of parent id (video or comment)



* **Return type**

    `list`[[`CommentResponse`](biggo_api.model.md#biggo_api.model.comment.CommentResponse)]



#### like(comment_id)
Like comment


* **Parameters**

    **comment_id** (`str`) – The id of comment



* **Return type**

    `bool`



#### unlike(comment_id)
Unlike comment


* **Parameters**

    **comment_id** (`str`) – The id of comment



#### update(edited_comment)
Update comment


* **Parameters**

    **edited_comment** ([`CommentRequest`](biggo_api.model.md#biggo_api.model.comment.CommentRequest)) – A `biggo_api.model.EditedComment` object



* **Return type**

    `bool`


## biggo_api.clients._user module

The API client of user


### _class_ biggo_api.clients._user.UserClient(oauth2_session, host_url, verify, region=None)
Bases: `BaseInstanceClient`

Client to access user API


#### block(user_id)
Block user


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `bool`



#### follow(user_id)
Follow user


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `bool`



#### get_block_list(user_id)
Get block list


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`UserResponse`](biggo_api.model.md#biggo_api.model.user.UserResponse)]



#### get_favorite_product_list(user_id)
Get user’s favorite products


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`ProductResponse`](biggo_api.model.md#biggo_api.model.product.ProductResponse)]



#### get_follow_user_list(user_id)
Get following users


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`UserResponse`](biggo_api.model.md#biggo_api.model.user.UserResponse)]



#### get_follower_count(user_id)
Get follower count


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `int`



#### get_follower_list(user_id)
Get followed users


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`UserResponse`](biggo_api.model.md#biggo_api.model.user.UserResponse)]



#### get_liked_video_list(user_id)
Get liked videos


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### get_own_video_list()
Get client’s own videos


* **Return type**

    `list`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### get_subscribed_video_list(user_id)
Get videos from user’s subscribed accounts


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### get_user_video_list(user_id)
Get user’s videos


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `list`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### is_following(user_id)
Check if following user


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `bool`



#### remove_follower(follower_id)
Unfollow user


* **Parameters**

    **follower_id** (`str`) – The user id of follower



#### unblock(user_id)
Unblock user


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `bool`



#### unfollow(user_id)
Unfollow user


* **Parameters**

    **user_id** (`str`) – The id of user



* **Return type**

    `bool`


## biggo_api.clients._video module

The API client of video


### _class_ biggo_api.clients._video.VideoClient(oauth2_session, host_url, verify, region=None)
Bases: `BaseInstanceClient`

Client to access video API


#### analyze(video_id)
Get video analyzation


* **Parameters**

    **video_id** (`str`) – The id of video



* **Return type**

    [`VideoAnalysis`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis)



#### delete(video_id)
Delete video


* **Parameters**

    **video_id** (`str`) – The id of video



* **Return type**

    `bool`



#### get(video_id)
Get video


* **Parameters**

    **video_id** (`str`) – The id of video



* **Return type**

    `Optional`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### get_like_list(video_id)
Get like list of video


* **Parameters**

    **video_id** (`str`) – The id of video



* **Return type**

    `list`[[`UserResponse`](biggo_api.model.md#biggo_api.model.user.UserResponse)]



#### has_permission()
Verify permission of client to upload video


* **Return type**

    `bool`



#### like(video_id)
Like video


* **Parameters**

    **video_id** (`str`) – The id of video



* **Return type**

    `bool`



#### patch_settings(video_settings)
Update video settings using PATCH method


* **Parameters**

    **video** – The `biggo_api.model.VideoSettings` object



* **Return type**

    `bool`



#### post_settings(video_settings)
Update video settings using POST method.


* **Parameters**

    **video** – The `biggo_api.model.VideoSettings` object



* **Return type**

    `bool`



#### recommend()
Get recommended videos


* **Return type**

    `list`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### search(keyword, tag_only=False)
Search videos by keyword or tag


* **Parameters**

    
    * **keyword** (`str`) – The keyword to search for


    * **tag_only** (`bool`) – Set to True will search #target



* **Return type**

    `list`[[`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)]



#### unlike(video_id)
Unlike video


* **Parameters**

    **video_id** (`str`) – The id of video



* **Return type**

    `bool`



#### upload(file)
Upload video from local file


* **Parameters**

    **file** (`str`) – The file path & name of video file



* **Return type**

    `str`


## biggo_api.clients.api module

This module define a general api client contains clients for instances


### _class_ biggo_api.clients.api.APIClient(client_credentials, host_url='https://api.biggo.com', region=None, verify=True, \*\*kwargs)
Bases: `object`

The API Client wraps all types of client


* **Variables**

    
    * **comment** – See `biggo_api.clients.comment.CommentClient`


    * **user** – See `biggo_api.clients.user.UserClient`


    * **video** – See `biggo_api.clients.video.VideoClient`


## Module contents
