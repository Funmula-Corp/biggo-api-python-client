# User Client Usage
- [User Client Usage](#user-client-usage)
  - [Get Own Videos](#get-own-videos)
  - [Get User's Video](#get-users-video)
## Get Own Videos
Get client's own videos
```Python
>>> api_client.user.get_own_videos()
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...)], size=1))
```
## Get User's Video
Get user's videos
```Python
>>> api_client.user.get_user_videos(userid='example_userid')
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...)], size=1))
```