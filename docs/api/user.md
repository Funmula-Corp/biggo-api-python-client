# User Client Usage
- [Get Own Videos](#get-own-videos)
- [Get User's Video](#get-users-video)
## Get Own Videos
Get client's own videos
```Python
>>> api_client.user.get_own_videos()
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...)], size=1))
>>> api_client.user.get_own_videos(page=2)
UserVideoResponse(result=True, user_video=UserVideo(data=[], size=1))
```
## Get User's Video
Get user's videos
```Python
>>> api_client.user.get_user_videos(userid='example_userid')
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), ...], size=21))
>>> api_client.user.get_user_videos(userid='example_userid', page=2)
UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...)], size=21))
```

---
[ :arrow_up: Back to top](#user-client-usage)  
[ :leftwards_arrow_with_hook: Back to docs](../../docs)