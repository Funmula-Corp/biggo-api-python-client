# biggo_api.model package

## Submodules

## biggo_api.model._base module

This module defines the base class of all models


### _class_ biggo_api.model._base.Base()
Bases: `object`

Base class of all models

This class can convert data between dict and class with custom aliases and exclude fields


* **Variables**

    
    * **_ALIASES** – A dict object for aliases mapping. Convert attribute name to server’s field name


    * **_EXCLUDE_FIELDS** – A list of attribute name to exclude in function to_dict



#### _classmethod_ from_dict(dict_data)
Declare a class object from dict object


* **Parameters**

    **dict_data** (`dict`) – The dict object to convert



#### to_dict(exclude_none=True)
Convert this class to dict object

This function convert attribute to its alias and remove key with None value


* **Parameters**

    **exclude_none** (`bool`) – set to False will keep keys with None value



* **Return type**

    `dict`


## biggo_api.model.comment module

The models of video comment


### _class_ biggo_api.model.comment.CommentHistory(content, comment_owner_id, comment_to_user_id, date, is_owner, time, video_id, comment_owner_name=None, comment_to_user_name=None)
Bases: `Base`

This class represents a comment log


#### comment_owner_id(_: `str_ )

#### comment_owner_name(_: `Optional`[`str`_ _ = Non_ )

#### comment_to_user_id(_: `str_ )

#### comment_to_user_name(_: `Optional`[`str`_ _ = Non_ )

#### content(_: `str_ )

#### date(_: `str_ )

#### is_owner(_: `bool_ )

#### time(_: `str_ )

#### video_id(_: `str_ )

### _class_ biggo_api.model.comment.CommentRequest(comment_id, content, type_='text')
Bases: `Base`

This class is used for updating comment


* **Variables**

    
    * **comment_id** – The id of comment


    * **content** – New content of comment


    * **type** – The type of comment



#### comment_id(_: `str_ )

#### content(_: `str_ )

#### type_(_: `str_ _ = 'text_ )

### _class_ biggo_api.model.comment.CommentResponse(child_comment_count, comment, comment_id, createtime, createtime_timestamp, genelogy, is_liked, level_count, like_count, has_more_comments, parent_id, parent_user_id, type_, user_id, video_id, has_owner_comment=None, is_owner=None, at_user_id=None, can_delete=None, can_report=None, is_verify_ecomm=None, is_verify_user=None, name=None, user_profile=None, is_delete=None, child_comments=None)
Bases: `Base`

This class represents a comment


#### at_user_id(_: `Optional`[`str`_ _ = Non_ )

#### can_delete(_: `Optional`[`bool`_ _ = Non_ )

#### can_report(_: `Optional`[`bool`_ _ = Non_ )

#### child_comment_count(_: `int_ )

#### child_comments(_: `Optional`[`list`[`CommentResponse`]_ _ = Non_ )

#### comment(_: `str_ )

#### comment_id(_: `str_ )

#### createtime(_: `str_ )

#### createtime_timestamp(_: `int_ )

#### genelogy(_: `list`[`str`_ )

#### has_more_comments(_: `bool_ )

#### has_owner_comment(_: `Optional`[`bool`_ _ = Non_ )

#### is_delete(_: `Optional`[`bool`_ _ = Non_ )

#### is_liked(_: `bool_ )

#### is_owner(_: `Optional`[`bool`_ _ = Non_ )

#### is_verify_ecomm(_: `Optional`[`bool`_ _ = Non_ )

#### is_verify_user(_: `Optional`[`bool`_ _ = Non_ )

#### level_count(_: `int_ )

#### like_count(_: `int_ )

#### name(_: `Optional`[`str`_ _ = Non_ )

#### parent_id(_: `str_ )

#### parent_user_id(_: `str_ )

#### type_(_: `str_ )

#### user_id(_: `str_ )

#### user_profile(_: `Optional`[`str`_ _ = Non_ )

#### video_id(_: `str_ )

### _class_ biggo_api.model.comment.NewComment(content, parent_id, video_id, type_='text')
Bases: `Base`

This class is used for creating new comment.


* **Variables**

    
    * **video_id** – The id of video


    * **parent_id** – The id of parent, could be video id or comment id


    * **content** – The content of comment


    * **type** – comment type, default is text



#### content(_: `str_ )

#### parent_id(_: `str_ )

#### type_(_: `str_ _ = 'text_ )

#### video_id(_: `str_ )
## biggo_api.model.product module

The models of video product


### _class_ biggo_api.model.product.ProductRequest(nindex, oid)
Bases: `Base`

This class is used for setting up or updating video product list


#### nindex(_: `str_ )

#### oid(_: `str_ )

### _class_ biggo_api.model.product.ProductResponse(currency, gallery_count, gallery_images, has_shop, has_store_page, id, image, index, is_ad, is_adult, is_not_found, is_offline, more, online_notify, original_image, original_price, price_diff_real, provide, subscribe, title, type_, cata=None, count_result_product=None, count_result_store=None, discount=None, history_id=None, is_multiple_product=None, location=None, m_max_price=None, m_text=None, original_symbol=None, price=None, price_range_max=None, price_range_min=None, product_nindex_price=None, promo_btn=None, promo_title=None, promo_url=None, purl=None, seller_credit=None, symbol=None, target_app=None, uid=None, url=None, url_dynamic=None, url_scheme=None, user_name=None, view_counter=None)
Bases: `Base`

This class represents a product in video


#### cata(_: `Optional`[`list`_ _ = Non_ )

#### count_result_product(_: `Optional`[`int`_ _ = Non_ )

#### count_result_store(_: `Optional`[`int`_ _ = Non_ )

#### currency(_: `str_ )

#### discount(_: `Optional`[`list`_ _ = Non_ )

#### gallery_count(_: `int_ )

#### gallery_images(_: `list`[`str`_ )

#### has_shop(_: `bool_ )

#### has_store_page(_: `bool_ )

#### history_id(_: `Optional`[`str`_ _ = Non_ )

#### id(_: `str_ )

#### image(_: `str_ )

#### index(_: `str_ )

#### is_ad(_: `bool_ )

#### is_adult(_: `bool_ )

#### is_multiple_product(_: `Optional`[`bool`_ _ = Non_ )

#### is_not_found(_: `bool_ )

#### is_offline(_: `str_ )

#### location(_: `Optional`[`str`_ _ = Non_ )

#### m_max_price(_: `Optional`[`str`_ _ = Non_ )

#### m_text(_: `Optional`[`str`_ _ = Non_ )

#### more(_: `bool_ )

#### online_notify(_: `bool_ )

#### original_image(_: `str_ )

#### original_price(_: `float_ )

#### original_symbol(_: `Optional`[`str`_ _ = Non_ )

#### price(_: `Optional`[`float`_ _ = Non_ )

#### price_diff_real(_: `float_ )

#### price_range_max(_: `Optional`[`int`_ _ = Non_ )

#### price_range_min(_: `Optional`[`int`_ _ = Non_ )

#### product_nindex_price(_: `Optional`[`list`_ _ = Non_ )

#### promo_btn(_: `Optional`[`str`_ _ = Non_ )

#### promo_title(_: `Optional`[`str`_ _ = Non_ )

#### promo_url(_: `Optional`[`str`_ _ = Non_ )

#### provide(_: `str_ )

#### purl(_: `Optional`[`str`_ _ = Non_ )

#### seller_credit(_: `Optional`[`int`_ _ = Non_ )

#### subscribe(_: `bool_ )

#### symbol(_: `Optional`[`str`_ _ = Non_ )

#### target_app(_: `Optional`[`str`_ _ = Non_ )

#### title(_: `str_ )

#### type_(_: `str_ )

#### uid(_: `Optional`[`str`_ _ = Non_ )

#### url(_: `Optional`[`str`_ _ = Non_ )

#### url_dynamic(_: `Optional`[`str`_ _ = Non_ )

#### url_scheme(_: `Optional`[`str`_ _ = Non_ )

#### user_name(_: `Optional`[`str`_ _ = Non_ )

#### view_counter(_: `Optional`[`int`_ _ = Non_ )
## biggo_api.model.store module

The models of user store


### _class_ biggo_api.model.store.StoreResponse(name, nindex)
Bases: `Base`

This class represents a store


#### name(_: `str_ )

#### nindex(_: `str_ )
## biggo_api.model.user module

The models of user


### _class_ biggo_api.model.user.UserResponse(at_user_id, description, is_verify_ecomm, is_verify_user, name, personal_url, profile_image, user_id, all_like_count=None, follow_count=None, follower_count=None, is_follow=None, is_my_video=None, store_list=None)
Bases: `Base`

This class represents a user


#### all_like_count(_: `Optional`[`int`_ _ = Non_ )

#### at_user_id(_: `str_ )

#### description(_: `str_ )

#### follow_count(_: `Optional`[`int`_ _ = Non_ )

#### follower_count(_: `Optional`[`int`_ _ = Non_ )

#### is_follow(_: `Optional`[`bool`_ _ = Non_ )

#### is_my_video(_: `Optional`[`bool`_ _ = Non_ )

#### is_verify_ecomm(_: `bool_ )

#### is_verify_user(_: `bool_ )

#### name(_: `str_ )

#### personal_url(_: `Union`[`str`, `list`[`str`]_ )

#### profile_image(_: `list`[`str`_ )

#### store_list(_: `Optional`[`list`[`StoreResponse`]_ _ = Non_ )

#### user_id(_: `str_ )
## biggo_api.model.video module

This module defines data class of video


### _class_ biggo_api.model.video.VideoAnalysis(cover_image, createtime, createtime_ts, last_timestamp, last_timestamp_ts, length, share_count, statistics_total, statistics_last_day, video_like_count, video_comment_count, view_count, thumbnails=None, updatetime=None, updatetime_ts=None)
Bases: `Base`

This class represents analysis of video


#### cover_image(_: `str_ )

#### createtime(_: `str_ )

#### createtime_ts(_: `int_ )

#### last_timestamp(_: `str_ )

#### last_timestamp_ts(_: `int_ )

#### length(_: `float_ )

#### share_count(_: `int_ )

#### statistics_last_day(_: `VideoStatistics_ )

#### statistics_total(_: `VideoStatistics_ )

#### thumbnails(_: `Optional`[`list`[`str`]_ _ = Non_ )

#### updatetime(_: `Optional`[`str`_ _ = Non_ )

#### updatetime_ts(_: `Optional`[`int`_ _ = Non_ )

#### video_comment_count(_: `int_ )

#### video_like_count(_: `int_ )

#### view_count(_: `int_ )

### _class_ biggo_api.model.video.VideoResponse(created_at, description, has_product, is_edited, is_like, is_myvideo, limit, meta, product_count, status, str_datetime, timestamp, url, user_id, video_comment_count, video_id, video_like_count, view_count, at_user_id=None, is_follow=None, is_private=None, is_verify_ecomm=None, is_verify_user=None, like_list=None, name=None, product_list=None, profile_image=None)
Bases: `Base`

This class represents a video


#### at_user_id(_: `Optional`[`str`_ _ = Non_ )

#### created_at(_: `str_ )

#### description(_: `str_ )

#### has_product(_: `bool_ )

#### is_edited(_: `bool_ )

#### is_follow(_: `Optional`[`bool`_ _ = Non_ )

#### is_like(_: `bool_ )

#### is_myvideo(_: `bool_ )

#### is_private(_: `Optional`[`bool`_ _ = Non_ )

#### is_verify_ecomm(_: `Optional`[`bool`_ _ = Non_ )

#### is_verify_user(_: `Optional`[`bool`_ _ = Non_ )

#### like_list(_: `Optional`[`list`[`str`]_ _ = Non_ )

#### limit(_: `int_ )

#### meta(_: `VideoResponseMeta_ )

#### name(_: `Optional`[`str`_ _ = Non_ )

#### product_count(_: `int_ )

#### product_list(_: `Optional`[`list`[`ProductResponse`]_ _ = Non_ )

#### profile_image(_: `Optional`[`str`_ _ = Non_ )

#### status(_: `VideoResponseStatus_ )

#### str_datetime(_: `str_ )

#### timestamp(_: `int_ )

#### url(_: `str_ )

#### user_id(_: `str_ )

#### video_comment_count(_: `int_ )

#### video_id(_: `str_ )

#### video_like_count(_: `int_ )

#### view_count(_: `int_ )

### _class_ biggo_api.model.video.VideoResponseDownload(mp4)
Bases: `Base`

This class represents specific format’s download path of video


#### mp4(_: `str_ )

### _class_ biggo_api.model.video.VideoResponseMeta(aspect_ratio, cover_image, download, iso8601_length, length, thumbnails)
Bases: `Base`

This class represents meta data of video


#### aspect_ratio(_: `Optional`[`str`_ )

#### cover_image(_: `str_ )

#### download(_: `VideoResponseDownload_ )

#### iso8601_length(_: `str_ )

#### length(_: `float_ )

#### thumbnails(_: `list`[`str`_ )

### _class_ biggo_api.model.video.VideoResponseStatus(process_status, process_status_kw, processing)
Bases: `Base`

This class represents status of processing video


#### process_status(_: `int_ )

#### process_status_kw(_: `list`[`str`_ )

#### processing(_: `bool_ )

### _class_ biggo_api.model.video.VideoSettings(video_id, description=None, limit=None, product_list=None, thumbnail_ts=None)
Bases: `Base`

This class is used for post/patch video settings


#### description(_: `Optional`[`str`_ _ = Non_ )

#### limit(_: `Optional`[`str`_ _ = Non_ )

#### product_list(_: `Optional`[`list`[`ProductRequest`]_ _ = Non_ )

#### thumbnail_ts(_: `Optional`[`int`_ _ = Non_ )

#### video_id(_: `str_ )

### _class_ biggo_api.model.video.VideoStatistics(average_play_time, full_play_percentage, play_time, unique_user_count)
Bases: `Base`

This class represents statistics of video


#### average_play_time(_: `float_ )

#### full_play_percentage(_: `float_ )

#### play_time(_: `float_ )

#### unique_user_count(_: `int_ )
## Module contents
