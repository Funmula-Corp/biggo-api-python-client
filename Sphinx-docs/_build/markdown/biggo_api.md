# biggo_api package

## Subpackages


* [biggo_api.clients package](biggo_api.clients.md)


    * [Submodules](biggo_api.clients.md#submodules)


    * [biggo_api.clients._auth module](biggo_api.clients.md#module-biggo_api.clients._auth)


        * [`ClientCredentials`](biggo_api.clients.md#biggo_api.clients._auth.ClientCredentials)


            * [`ClientCredentials.client_id`](biggo_api.clients.md#biggo_api.clients._auth.ClientCredentials.client_id)


            * [`ClientCredentials.client_secret`](biggo_api.clients.md#biggo_api.clients._auth.ClientCredentials.client_secret)


        * [`auth_client_credentials()`](biggo_api.clients.md#biggo_api.clients._auth.auth_client_credentials)


    * [biggo_api.clients._base module](biggo_api.clients.md#module-biggo_api.clients._base)


        * [`BaseInstanceClient`](biggo_api.clients.md#biggo_api.clients._base.BaseInstanceClient)


            * [`BaseInstanceClient.request()`](biggo_api.clients.md#biggo_api.clients._base.BaseInstanceClient.request)


    * [biggo_api.clients._user module](biggo_api.clients.md#module-biggo_api.clients._user)


        * [`UserClient`](biggo_api.clients.md#biggo_api.clients._user.UserClient)


            * [`UserClient.get_own_videos()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_own_videos)


            * [`UserClient.get_user_videos()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_user_videos)


    * [biggo_api.clients._video module](biggo_api.clients.md#module-biggo_api.clients._video)


        * [`VideoClient`](biggo_api.clients.md#biggo_api.clients._video.VideoClient)


            * [`VideoClient.delete()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.delete)


            * [`VideoClient.get()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.get)


            * [`VideoClient.has_permission()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.has_permission)


            * [`VideoClient.partial_update()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.partial_update)


            * [`VideoClient.update()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.update)


            * [`VideoClient.upload()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.upload)


    * [biggo_api.clients.api module](biggo_api.clients.md#module-biggo_api.clients.api)


        * [`APIClient`](biggo_api.clients.md#biggo_api.clients.api.APIClient)


            * [`APIClient.user`](biggo_api.clients.md#biggo_api.clients.api.APIClient.user)


            * [`APIClient.video`](biggo_api.clients.md#biggo_api.clients.api.APIClient.video)


    * [Module contents](biggo_api.clients.md#module-biggo_api.clients)


* [biggo_api.data_models package](biggo_api.data_models.md)


    * [Submodules](biggo_api.data_models.md#submodules)


    * [biggo_api.data_models.product module](biggo_api.data_models.md#module-biggo_api.data_models.product)


        * [`BigGoVideoProduct`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct)


            * [`BigGoVideoProduct.currency`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.currency)


            * [`BigGoVideoProduct.discount`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.discount)


            * [`BigGoVideoProduct.gallery_count`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.gallery_count)


            * [`BigGoVideoProduct.gallery_images`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.gallery_images)


            * [`BigGoVideoProduct.has_shop`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.has_shop)


            * [`BigGoVideoProduct.has_store_page`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.has_store_page)


            * [`BigGoVideoProduct.history_id`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.history_id)


            * [`BigGoVideoProduct.id`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.id)


            * [`BigGoVideoProduct.index`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.index)


            * [`BigGoVideoProduct.is_ad`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.is_ad)


            * [`BigGoVideoProduct.is_adult`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.is_adult)


            * [`BigGoVideoProduct.is_multiple_product`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.is_multiple_product)


            * [`BigGoVideoProduct.is_not_found`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.is_not_found)


            * [`BigGoVideoProduct.is_offline`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.is_offline)


            * [`BigGoVideoProduct.location`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.location)


            * [`BigGoVideoProduct.m_max_price`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.m_max_price)


            * [`BigGoVideoProduct.m_text`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.m_text)


            * [`BigGoVideoProduct.more`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.more)


            * [`BigGoVideoProduct.online_notify`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.online_notify)


            * [`BigGoVideoProduct.original_image`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.original_image)


            * [`BigGoVideoProduct.original_price`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.original_price)


            * [`BigGoVideoProduct.original_symbol`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.original_symbol)


            * [`BigGoVideoProduct.price_diff_real`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.price_diff_real)


            * [`BigGoVideoProduct.provide`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.provide)


            * [`BigGoVideoProduct.purl`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.purl)


            * [`BigGoVideoProduct.seller_credit`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.seller_credit)


            * [`BigGoVideoProduct.subscribe`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.subscribe)


            * [`BigGoVideoProduct.type_`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.type_)


            * [`BigGoVideoProduct.uid`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.uid)


            * [`BigGoVideoProduct.url`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.url)


            * [`BigGoVideoProduct.username`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProduct.username)


        * [`BigGoVideoProductBase`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProductBase)


            * [`BigGoVideoProductBase.image`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProductBase.image)


            * [`BigGoVideoProductBase.price`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProductBase.price)


            * [`BigGoVideoProductBase.symbol`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProductBase.symbol)


            * [`BigGoVideoProductBase.title`](biggo_api.data_models.md#biggo_api.data_models.product.BigGoVideoProductBase.title)


    * [biggo_api.data_models.user module](biggo_api.data_models.md#module-biggo_api.data_models.user)


        * [`VideoUserInfo`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo)


            * [`VideoUserInfo.all_like_count`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.all_like_count)


            * [`VideoUserInfo.at_userid`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.at_userid)


            * [`VideoUserInfo.description`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.description)


            * [`VideoUserInfo.follow_count`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.follow_count)


            * [`VideoUserInfo.follower_count`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.follower_count)


            * [`VideoUserInfo.is_follow`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.is_follow)


            * [`VideoUserInfo.is_myvideo`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.is_myvideo)


            * [`VideoUserInfo.is_verify_ecomm`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.is_verify_ecomm)


            * [`VideoUserInfo.is_verify_user`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.is_verify_user)


            * [`VideoUserInfo.name`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.name)


            * [`VideoUserInfo.personal_url`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.personal_url)


            * [`VideoUserInfo.profileimg`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.profileimg)


            * [`VideoUserInfo.userid`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo.userid)


    * [biggo_api.data_models.video module](biggo_api.data_models.md#module-biggo_api.data_models.video)


        * [`BigGoVideo`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo)


            * [`BigGoVideo.access`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.access)


            * [`BigGoVideo.at_userid`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.at_userid)


            * [`BigGoVideo.created_at`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.created_at)


            * [`BigGoVideo.description`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.description)


            * [`BigGoVideo.has_product`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.has_product)


            * [`BigGoVideo.is_edited`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_edited)


            * [`BigGoVideo.is_follow`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_follow)


            * [`BigGoVideo.is_like`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_like)


            * [`BigGoVideo.is_myvideo`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_myvideo)


            * [`BigGoVideo.is_private`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_private)


            * [`BigGoVideo.is_verify_ecomm`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_verify_ecomm)


            * [`BigGoVideo.is_verify_user`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.is_verify_user)


            * [`BigGoVideo.like_list`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.like_list)


            * [`BigGoVideo.limit`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.limit)


            * [`BigGoVideo.meta`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.meta)


            * [`BigGoVideo.name`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.name)


            * [`BigGoVideo.product_count`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.product_count)


            * [`BigGoVideo.product_list`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.product_list)


            * [`BigGoVideo.profile_image`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.profile_image)


            * [`BigGoVideo.status`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.status)


            * [`BigGoVideo.str_datetime`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.str_datetime)


            * [`BigGoVideo.timestamp`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.timestamp)


            * [`BigGoVideo.url`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.url)


            * [`BigGoVideo.userid`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.userid)


            * [`BigGoVideo.video_comment_count`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.video_comment_count)


            * [`BigGoVideo.video_id`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.video_id)


            * [`BigGoVideo.video_like_count`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.video_like_count)


            * [`BigGoVideo.view_count`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo.view_count)


        * [`BigGoVideoMeta`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta)


            * [`BigGoVideoMeta.aspect_ratio`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta.aspect_ratio)


            * [`BigGoVideoMeta.cover_image`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta.cover_image)


            * [`BigGoVideoMeta.download`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta.download)


            * [`BigGoVideoMeta.iso8601_length`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta.iso8601_length)


            * [`BigGoVideoMeta.length`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta.length)


            * [`BigGoVideoMeta.thumbnails`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMeta.thumbnails)


        * [`BigGoVideoMetaDownload`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMetaDownload)


            * [`BigGoVideoMetaDownload.mp4`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoMetaDownload.mp4)


        * [`BigGoVideoProcessStatus`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoProcessStatus)


            * [`BigGoVideoProcessStatus.process_status`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoProcessStatus.process_status)


            * [`BigGoVideoProcessStatus.process_status_kw`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoProcessStatus.process_status_kw)


            * [`BigGoVideoProcessStatus.processing`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideoProcessStatus.processing)


        * [`VideoParams`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams)


            * [`VideoParams.Config`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.Config)


            * [`VideoParams.access`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.access)


            * [`VideoParams.description`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.description)


            * [`VideoParams.product_list`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.product_list)


            * [`VideoParams.thumbnail_time`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.thumbnail_time)


            * [`VideoParams.title`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.title)


            * [`VideoParams.video_id`](biggo_api.data_models.md#biggo_api.data_models.video.VideoParams.video_id)


    * [Module contents](biggo_api.data_models.md#module-biggo_api.data_models)


* [biggo_api.enum package](biggo_api.enum.md)


    * [Submodules](biggo_api.enum.md#submodules)


    * [biggo_api.enum.access module](biggo_api.enum.md#module-biggo_api.enum.access)


        * [`Access`](biggo_api.enum.md#biggo_api.enum.access.Access)


            * [`Access.PRIVATE`](biggo_api.enum.md#biggo_api.enum.access.Access.PRIVATE)


            * [`Access.PUBLIC`](biggo_api.enum.md#biggo_api.enum.access.Access.PUBLIC)


            * [`Access.UNLISTED`](biggo_api.enum.md#biggo_api.enum.access.Access.UNLISTED)


    * [biggo_api.enum.process_status module](biggo_api.enum.md#module-biggo_api.enum.process_status)


        * [`ProcessStatus`](biggo_api.enum.md#biggo_api.enum.process_status.ProcessStatus)


            * [`ProcessStatus.COMPLETE`](biggo_api.enum.md#biggo_api.enum.process_status.ProcessStatus.COMPLETE)


            * [`ProcessStatus.INQUEUE`](biggo_api.enum.md#biggo_api.enum.process_status.ProcessStatus.INQUEUE)


    * [Module contents](biggo_api.enum.md#module-biggo_api.enum)


## Submodules

## biggo_api.exception module

This module defind error of BigGo API.


### _exception_ biggo_api.exception.BigGoAPIError(response)
Bases: `Exception`

BigGo API Error object for all 4xx responses with error in response body.


* **Variables**

    **response** – The error response.



#### response(_: `ErrorResponse_ )
## biggo_api.responses module

This module defines formats of response bodies.


### _class_ biggo_api.responses.BaseResponse(\*\*data)
Bases: `BaseModel`

Base format of response.


#### result(_: `bool_ )

### _class_ biggo_api.responses.Error(\*\*data)
Bases: `BaseModel`

Detailed error code and reason.


#### code(_: `int_ )

#### message(_: `str_ )

### _class_ biggo_api.responses.ErrorResponse(\*\*data)
Bases: `BaseResponse`

Response of API error.


#### error(_: `Error_ )

### _class_ biggo_api.responses.UserVideo(\*\*data)
Bases: `BaseModel`

User video dataset.


#### data(_: `list`[[`BigGoVideo`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo)_ )

#### size(_: `int_ )

### _class_ biggo_api.responses.UserVideoResponse(\*\*data)
Bases: `BaseResponse`

Response of getting user’s videos.


#### user_video(_: `UserVideo_ )

### _class_ biggo_api.responses.VideoDeleteResponse(\*\*data)
Bases: `BaseResponse`

Response of deleting video.


### _class_ biggo_api.responses.VideoPermissionResponse(\*\*data)
Bases: `BaseResponse`

Response of getting video permission.


#### at_userid(_: `str_ )

#### region(_: `str_ )

#### userid(_: `str_ )

### _class_ biggo_api.responses.VideoResponse(\*\*data)
Bases: `BaseResponse`

Response of getting video.


#### size(_: `int_ )

#### user(_: [`VideoUserInfo`](biggo_api.data_models.md#biggo_api.data_models.user.VideoUserInfo_ )

#### video(_: `list`[[`BigGoVideo`](biggo_api.data_models.md#biggo_api.data_models.video.BigGoVideo)_ )

### _class_ biggo_api.responses.VideoUpdateResponse(\*\*data)
Bases: `BaseResponse`

Response of posting/patching video params.


#### data()
alias of `ConstrainedListValue`


### _class_ biggo_api.responses.VideoUploadResponse(\*\*data)
Bases: `BaseResponse`

Response of uploading video.


#### video_id(_: `str_ )
## Module contents
