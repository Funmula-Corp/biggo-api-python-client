# biggo_api.data_models package

## Submodules

## biggo_api.data_models.user module

This module defines data classes of user


### _class_ biggo_api.data_models.user.VideoUserInfo(\*\*data)
Bases: `BaseModel`


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

This module defines data classes of video


### _class_ biggo_api.data_models.video.BigGoVideo(\*\*data)
Bases: `BaseModel`

This class represents a video


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

#### meta(_: `BigGoVideoMeta_ )

#### name(_: `str_ )

#### product_count(_: `int_ )

#### product_list(_: `Optional`[`list`_ )

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

This class represents meta data of video


#### aspect_ratio(_: `Optional`[`str`_ )

#### cover_image(_: `str_ )

#### download(_: `Union`[`ConstrainedListValue`[`Any`], `BigGoVideoMetaDownload`_ )

#### iso8601_length(_: `str_ )

#### length(_: `float_ )

#### thumbnails(_: `list`[`str`_ )

### _class_ biggo_api.data_models.video.BigGoVideoMetaDownload(\*\*data)
Bases: `BaseModel`

This class represents specific format’s download path of video


#### mp4(_: `str_ )

### _class_ biggo_api.data_models.video.BigGoVideoProcessStatus(\*\*data)
Bases: `BaseModel`

This class represents status of processing video


#### process_status(_: [`ProcessStatus`](biggo_api.enum.md#biggo_api.enum.process_status.ProcessStatus_ )

#### process_status_kw(_: `list`[`str`_ )

#### processing(_: `bool_ )

### _class_ biggo_api.data_models.video.VideoParams(\*\*data)
Bases: `BaseModel`

This class is used for post/patch video settings


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
