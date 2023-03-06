# biggo_api.data_models package

## Submodules

## biggo_api.data_models.product module

This module defines data classes of video product


### _class_ biggo_api.data_models.product.BigGoVideoProduct(\*\*data)
Bases: `BigGoVideoProductBase`

This class represents a detailed product in video.


#### currency(_: `str_ )

#### discount(_: `list`[`str`_ )

#### gallery_count(_: `int_ )

#### gallery_images(_: `list`[`str`_ )

#### has_shop(_: `bool_ )

#### has_store_page(_: `bool_ )

#### history_id(_: `str_ )

#### id(_: `str_ )

#### index(_: `str_ )

#### is_ad(_: `bool_ )

#### is_adult(_: `bool_ )

#### is_multiple_product(_: `bool_ )

#### is_not_found(_: `bool_ )

#### is_offline(_: `bool_ )

#### location(_: `Optional`[`str`_ )

#### m_max_price(_: `Optional`[`str`_ )

#### m_text(_: `Optional`[`str`_ )

#### more(_: `bool_ )

#### online_notify(_: `bool_ )

#### original_image(_: `str_ )

#### original_price(_: `float_ )

#### original_symbol(_: `str_ )

#### price_diff_real(_: `float_ )

#### provide(_: `str_ )

#### purl(_: `str_ )

#### seller_credit(_: `Optional`[`int`_ )

#### subscribe(_: `bool_ )

#### type_(_: `str_ )

#### uid(_: `Optional`[`str`_ )

#### url(_: `str_ )

#### username(_: `Optional`[`str`_ )

### _class_ biggo_api.data_models.product.BigGoVideoProductBase(\*\*data)
Bases: `BaseModel`

This class represents a base product in video.


#### image(_: `str_ )

#### price(_: `float_ )

#### symbol(_: `str_ )

#### title(_: `str_ )
## biggo_api.data_models.user module

This module defines data classes of user.


### _class_ biggo_api.data_models.user.VideoUserInfo(\*\*data)
Bases: `BaseModel`

This class represents the user data in get video response.


#### all_like_count(_: `int_ )

#### at_userid(_: `str_ )

#### description(_: `str_ )

#### follow_count(_: `int_ )

#### follower_count(_: `int_ )

#### is_follow(_: `bool_ )

#### is_myvideo(_: `bool_ )

#### is_verify_ecomm(_: `bool_ )

#### is_verify_user(_: `bool_ )

#### name(_: `str_ )

#### personal_url(_: `Union`[`str`, `list`[`str`]_ )

#### profileimg(_: `str_ )

#### userid(_: `str_ )
## biggo_api.data_models.video module

This module defines data classes of video.


### _class_ biggo_api.data_models.video.BigGoVideo(\*\*data)
Bases: `BaseModel`

This class represents a video.


#### access(_: [`Access`](biggo_api.enum.md#biggo_api.enum.access.Access_ )

#### at_userid(_: `str_ )

#### created_at(_: `str_ )

#### description(_: `Optional`[`str`_ )

#### has_product(_: `bool_ )

#### is_edited(_: `bool_ )

#### is_follow(_: `bool_ )

#### is_like(_: `bool_ )

#### is_myvideo(_: `bool_ )

#### is_private(_: `Optional`[`bool`_ )

#### is_verify_ecomm(_: `bool_ )

#### is_verify_user(_: `bool_ )

#### like_list(_: `Optional`[`list`[`str`]_ )

#### limit(_: [`Access`](biggo_api.enum.md#biggo_api.enum.access.Access_ )

#### meta(_: `Optional`[`BigGoVideoMeta`_ )

#### name(_: `str_ )

#### product_count(_: `int_ )

#### product_list(_: `Union`[`list`[`BigGoVideoProduct`], `list`[`BigGoVideoProductBase`], `None`_ )

#### profile_image(_: `str_ )

#### status(_: `BigGoVideoProcessStatus_ )

#### str_datetime(_: `Optional`[`str`_ )

#### timestamp(_: `int_ )

#### url(_: `str_ )

#### userid(_: `str_ )

#### video_comment_count(_: `int_ )

#### video_id(_: `str_ )

#### video_like_count(_: `int_ )

#### view_count(_: `int_ )

### _class_ biggo_api.data_models.video.BigGoVideoMeta(\*\*data)
Bases: `BaseModel`

This class represents meta data of video.


#### aspect_ratio(_: `Optional`[`str`_ )

#### cover_image(_: `str_ )

#### download(_: `Union`[`ConstrainedListValue`[`Any`], `BigGoVideoMetaDownload`_ )

#### iso8601_length(_: `str_ )

#### length(_: `float_ )

#### thumbnails(_: `list`[`str`_ )

### _class_ biggo_api.data_models.video.BigGoVideoMetaDownload(\*\*data)
Bases: `BaseModel`

This class represents download path in specific format for the video.


#### mp4(_: `str_ )

### _class_ biggo_api.data_models.video.BigGoVideoProcessStatus(\*\*data)
Bases: `BaseModel`

This class represents status of processing video.


#### process_status(_: [`ProcessStatus`](biggo_api.enum.md#biggo_api.enum.process_status.ProcessStatus_ )

#### process_status_kw(_: `list`[`str`_ )

#### processing(_: `bool_ )

### _class_ biggo_api.data_models.video.VideoParams(\*\*data)
Bases: `BaseModel`

This class is used for post/patch video settings.


* **Variables**

    
    * **access** – Accessibility of video.


    * **description** – Description of video.


    * **title** – Title of video.


    * **video_id** – Id of video.



#### _class_ Config()
Bases: `object`


#### allow_population_by_field_name(_ = Tru_ )

#### access(_: `Optional`[[`Access`](biggo_api.enum.md#biggo_api.enum.access.Access)_ )

#### description(_: `Optional`[`str`_ )

#### product_list(_: `Optional`[`list`_ )

#### thumbnail_time(_: `Optional`[`int`_ )

#### title(_: `Optional`[`str`_ )

#### video_id(_: `str_ )
## Module contents
