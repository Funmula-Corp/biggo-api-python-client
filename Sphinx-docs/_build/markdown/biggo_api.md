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


    * [biggo_api.clients._comment module](biggo_api.clients.md#module-biggo_api.clients._comment)


        * [`CommentClient`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient)


            * [`CommentClient.create()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.create)


            * [`CommentClient.delete()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.delete)


            * [`CommentClient.get_comment_history()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.get_comment_history)


            * [`CommentClient.get_list()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.get_list)


            * [`CommentClient.like()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.like)


            * [`CommentClient.unlike()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.unlike)


            * [`CommentClient.update()`](biggo_api.clients.md#biggo_api.clients._comment.CommentClient.update)


    * [biggo_api.clients._user module](biggo_api.clients.md#module-biggo_api.clients._user)


        * [`UserClient`](biggo_api.clients.md#biggo_api.clients._user.UserClient)


            * [`UserClient.block()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.block)


            * [`UserClient.follow()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.follow)


            * [`UserClient.get_block_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_block_list)


            * [`UserClient.get_favorite_product_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_favorite_product_list)


            * [`UserClient.get_follow_user_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_follow_user_list)


            * [`UserClient.get_follower_count()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_follower_count)


            * [`UserClient.get_follower_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_follower_list)


            * [`UserClient.get_liked_video_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_liked_video_list)


            * [`UserClient.get_own_video_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_own_video_list)


            * [`UserClient.get_subscribed_video_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_subscribed_video_list)


            * [`UserClient.get_user_video_list()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.get_user_video_list)


            * [`UserClient.is_following()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.is_following)


            * [`UserClient.remove_follower()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.remove_follower)


            * [`UserClient.unblock()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.unblock)


            * [`UserClient.unfollow()`](biggo_api.clients.md#biggo_api.clients._user.UserClient.unfollow)


    * [biggo_api.clients._video module](biggo_api.clients.md#module-biggo_api.clients._video)


        * [`VideoClient`](biggo_api.clients.md#biggo_api.clients._video.VideoClient)


            * [`VideoClient.analyze()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.analyze)


            * [`VideoClient.delete()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.delete)


            * [`VideoClient.get()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.get)


            * [`VideoClient.get_like_list()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.get_like_list)


            * [`VideoClient.has_permission()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.has_permission)


            * [`VideoClient.like()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.like)


            * [`VideoClient.patch_settings()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.patch_settings)


            * [`VideoClient.post_settings()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.post_settings)


            * [`VideoClient.recommend()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.recommend)


            * [`VideoClient.search()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.search)


            * [`VideoClient.unlike()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.unlike)


            * [`VideoClient.upload()`](biggo_api.clients.md#biggo_api.clients._video.VideoClient.upload)


    * [biggo_api.clients.api module](biggo_api.clients.md#module-biggo_api.clients.api)


        * [`APIClient`](biggo_api.clients.md#biggo_api.clients.api.APIClient)


    * [Module contents](biggo_api.clients.md#module-biggo_api.clients)


* [biggo_api.enum package](biggo_api.enum.md)


    * [Submodules](biggo_api.enum.md#submodules)


    * [biggo_api.enum.limit module](biggo_api.enum.md#module-biggo_api.enum.limit)


        * [`Limit`](biggo_api.enum.md#biggo_api.enum.limit.Limit)


            * [`Limit.everyone`](biggo_api.enum.md#biggo_api.enum.limit.Limit.everyone)


            * [`Limit.limit_myself`](biggo_api.enum.md#biggo_api.enum.limit.Limit.limit_myself)


            * [`Limit.non_public`](biggo_api.enum.md#biggo_api.enum.limit.Limit.non_public)


    * [Module contents](biggo_api.enum.md#module-biggo_api.enum)


* [biggo_api.model package](biggo_api.model.md)


    * [Submodules](biggo_api.model.md#submodules)


    * [biggo_api.model._base module](biggo_api.model.md#module-biggo_api.model._base)


        * [`Base`](biggo_api.model.md#biggo_api.model._base.Base)


            * [`Base.from_dict()`](biggo_api.model.md#biggo_api.model._base.Base.from_dict)


            * [`Base.to_dict()`](biggo_api.model.md#biggo_api.model._base.Base.to_dict)


    * [biggo_api.model.comment module](biggo_api.model.md#module-biggo_api.model.comment)


        * [`CommentHistory`](biggo_api.model.md#biggo_api.model.comment.CommentHistory)


            * [`CommentHistory.comment_owner_id`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.comment_owner_id)


            * [`CommentHistory.comment_owner_name`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.comment_owner_name)


            * [`CommentHistory.comment_to_user_id`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.comment_to_user_id)


            * [`CommentHistory.comment_to_user_name`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.comment_to_user_name)


            * [`CommentHistory.content`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.content)


            * [`CommentHistory.date`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.date)


            * [`CommentHistory.is_owner`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.is_owner)


            * [`CommentHistory.time`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.time)


            * [`CommentHistory.video_id`](biggo_api.model.md#biggo_api.model.comment.CommentHistory.video_id)


        * [`CommentRequest`](biggo_api.model.md#biggo_api.model.comment.CommentRequest)


            * [`CommentRequest.comment_id`](biggo_api.model.md#biggo_api.model.comment.CommentRequest.comment_id)


            * [`CommentRequest.content`](biggo_api.model.md#biggo_api.model.comment.CommentRequest.content)


            * [`CommentRequest.type_`](biggo_api.model.md#biggo_api.model.comment.CommentRequest.type_)


        * [`CommentResponse`](biggo_api.model.md#biggo_api.model.comment.CommentResponse)


            * [`CommentResponse.at_user_id`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.at_user_id)


            * [`CommentResponse.can_delete`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.can_delete)


            * [`CommentResponse.can_report`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.can_report)


            * [`CommentResponse.child_comment_count`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.child_comment_count)


            * [`CommentResponse.child_comments`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.child_comments)


            * [`CommentResponse.comment`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.comment)


            * [`CommentResponse.comment_id`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.comment_id)


            * [`CommentResponse.createtime`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.createtime)


            * [`CommentResponse.createtime_timestamp`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.createtime_timestamp)


            * [`CommentResponse.genelogy`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.genelogy)


            * [`CommentResponse.has_more_comments`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.has_more_comments)


            * [`CommentResponse.has_owner_comment`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.has_owner_comment)


            * [`CommentResponse.is_delete`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.is_delete)


            * [`CommentResponse.is_liked`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.is_liked)


            * [`CommentResponse.is_owner`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.is_owner)


            * [`CommentResponse.is_verify_ecomm`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.is_verify_ecomm)


            * [`CommentResponse.is_verify_user`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.is_verify_user)


            * [`CommentResponse.level_count`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.level_count)


            * [`CommentResponse.like_count`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.like_count)


            * [`CommentResponse.name`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.name)


            * [`CommentResponse.parent_id`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.parent_id)


            * [`CommentResponse.parent_user_id`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.parent_user_id)


            * [`CommentResponse.type_`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.type_)


            * [`CommentResponse.user_id`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.user_id)


            * [`CommentResponse.user_profile`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.user_profile)


            * [`CommentResponse.video_id`](biggo_api.model.md#biggo_api.model.comment.CommentResponse.video_id)


        * [`NewComment`](biggo_api.model.md#biggo_api.model.comment.NewComment)


            * [`NewComment.content`](biggo_api.model.md#biggo_api.model.comment.NewComment.content)


            * [`NewComment.parent_id`](biggo_api.model.md#biggo_api.model.comment.NewComment.parent_id)


            * [`NewComment.type_`](biggo_api.model.md#biggo_api.model.comment.NewComment.type_)


            * [`NewComment.video_id`](biggo_api.model.md#biggo_api.model.comment.NewComment.video_id)


    * [biggo_api.model.product module](biggo_api.model.md#module-biggo_api.model.product)


        * [`ProductRequest`](biggo_api.model.md#biggo_api.model.product.ProductRequest)


            * [`ProductRequest.nindex`](biggo_api.model.md#biggo_api.model.product.ProductRequest.nindex)


            * [`ProductRequest.oid`](biggo_api.model.md#biggo_api.model.product.ProductRequest.oid)


        * [`ProductResponse`](biggo_api.model.md#biggo_api.model.product.ProductResponse)


            * [`ProductResponse.cata`](biggo_api.model.md#biggo_api.model.product.ProductResponse.cata)


            * [`ProductResponse.count_result_product`](biggo_api.model.md#biggo_api.model.product.ProductResponse.count_result_product)


            * [`ProductResponse.count_result_store`](biggo_api.model.md#biggo_api.model.product.ProductResponse.count_result_store)


            * [`ProductResponse.currency`](biggo_api.model.md#biggo_api.model.product.ProductResponse.currency)


            * [`ProductResponse.discount`](biggo_api.model.md#biggo_api.model.product.ProductResponse.discount)


            * [`ProductResponse.gallery_count`](biggo_api.model.md#biggo_api.model.product.ProductResponse.gallery_count)


            * [`ProductResponse.gallery_images`](biggo_api.model.md#biggo_api.model.product.ProductResponse.gallery_images)


            * [`ProductResponse.has_shop`](biggo_api.model.md#biggo_api.model.product.ProductResponse.has_shop)


            * [`ProductResponse.has_store_page`](biggo_api.model.md#biggo_api.model.product.ProductResponse.has_store_page)


            * [`ProductResponse.history_id`](biggo_api.model.md#biggo_api.model.product.ProductResponse.history_id)


            * [`ProductResponse.id`](biggo_api.model.md#biggo_api.model.product.ProductResponse.id)


            * [`ProductResponse.image`](biggo_api.model.md#biggo_api.model.product.ProductResponse.image)


            * [`ProductResponse.index`](biggo_api.model.md#biggo_api.model.product.ProductResponse.index)


            * [`ProductResponse.is_ad`](biggo_api.model.md#biggo_api.model.product.ProductResponse.is_ad)


            * [`ProductResponse.is_adult`](biggo_api.model.md#biggo_api.model.product.ProductResponse.is_adult)


            * [`ProductResponse.is_multiple_product`](biggo_api.model.md#biggo_api.model.product.ProductResponse.is_multiple_product)


            * [`ProductResponse.is_not_found`](biggo_api.model.md#biggo_api.model.product.ProductResponse.is_not_found)


            * [`ProductResponse.is_offline`](biggo_api.model.md#biggo_api.model.product.ProductResponse.is_offline)


            * [`ProductResponse.location`](biggo_api.model.md#biggo_api.model.product.ProductResponse.location)


            * [`ProductResponse.m_max_price`](biggo_api.model.md#biggo_api.model.product.ProductResponse.m_max_price)


            * [`ProductResponse.m_text`](biggo_api.model.md#biggo_api.model.product.ProductResponse.m_text)


            * [`ProductResponse.more`](biggo_api.model.md#biggo_api.model.product.ProductResponse.more)


            * [`ProductResponse.online_notify`](biggo_api.model.md#biggo_api.model.product.ProductResponse.online_notify)


            * [`ProductResponse.original_image`](biggo_api.model.md#biggo_api.model.product.ProductResponse.original_image)


            * [`ProductResponse.original_price`](biggo_api.model.md#biggo_api.model.product.ProductResponse.original_price)


            * [`ProductResponse.original_symbol`](biggo_api.model.md#biggo_api.model.product.ProductResponse.original_symbol)


            * [`ProductResponse.price`](biggo_api.model.md#biggo_api.model.product.ProductResponse.price)


            * [`ProductResponse.price_diff_real`](biggo_api.model.md#biggo_api.model.product.ProductResponse.price_diff_real)


            * [`ProductResponse.price_range_max`](biggo_api.model.md#biggo_api.model.product.ProductResponse.price_range_max)


            * [`ProductResponse.price_range_min`](biggo_api.model.md#biggo_api.model.product.ProductResponse.price_range_min)


            * [`ProductResponse.product_nindex_price`](biggo_api.model.md#biggo_api.model.product.ProductResponse.product_nindex_price)


            * [`ProductResponse.promo_btn`](biggo_api.model.md#biggo_api.model.product.ProductResponse.promo_btn)


            * [`ProductResponse.promo_title`](biggo_api.model.md#biggo_api.model.product.ProductResponse.promo_title)


            * [`ProductResponse.promo_url`](biggo_api.model.md#biggo_api.model.product.ProductResponse.promo_url)


            * [`ProductResponse.provide`](biggo_api.model.md#biggo_api.model.product.ProductResponse.provide)


            * [`ProductResponse.purl`](biggo_api.model.md#biggo_api.model.product.ProductResponse.purl)


            * [`ProductResponse.seller_credit`](biggo_api.model.md#biggo_api.model.product.ProductResponse.seller_credit)


            * [`ProductResponse.subscribe`](biggo_api.model.md#biggo_api.model.product.ProductResponse.subscribe)


            * [`ProductResponse.symbol`](biggo_api.model.md#biggo_api.model.product.ProductResponse.symbol)


            * [`ProductResponse.target_app`](biggo_api.model.md#biggo_api.model.product.ProductResponse.target_app)


            * [`ProductResponse.title`](biggo_api.model.md#biggo_api.model.product.ProductResponse.title)


            * [`ProductResponse.type_`](biggo_api.model.md#biggo_api.model.product.ProductResponse.type_)


            * [`ProductResponse.uid`](biggo_api.model.md#biggo_api.model.product.ProductResponse.uid)


            * [`ProductResponse.url`](biggo_api.model.md#biggo_api.model.product.ProductResponse.url)


            * [`ProductResponse.url_dynamic`](biggo_api.model.md#biggo_api.model.product.ProductResponse.url_dynamic)


            * [`ProductResponse.url_scheme`](biggo_api.model.md#biggo_api.model.product.ProductResponse.url_scheme)


            * [`ProductResponse.user_name`](biggo_api.model.md#biggo_api.model.product.ProductResponse.user_name)


            * [`ProductResponse.view_counter`](biggo_api.model.md#biggo_api.model.product.ProductResponse.view_counter)


    * [biggo_api.model.store module](biggo_api.model.md#module-biggo_api.model.store)


        * [`StoreResponse`](biggo_api.model.md#biggo_api.model.store.StoreResponse)


            * [`StoreResponse.name`](biggo_api.model.md#biggo_api.model.store.StoreResponse.name)


            * [`StoreResponse.nindex`](biggo_api.model.md#biggo_api.model.store.StoreResponse.nindex)


    * [biggo_api.model.user module](biggo_api.model.md#module-biggo_api.model.user)


        * [`UserResponse`](biggo_api.model.md#biggo_api.model.user.UserResponse)


            * [`UserResponse.all_like_count`](biggo_api.model.md#biggo_api.model.user.UserResponse.all_like_count)


            * [`UserResponse.at_user_id`](biggo_api.model.md#biggo_api.model.user.UserResponse.at_user_id)


            * [`UserResponse.description`](biggo_api.model.md#biggo_api.model.user.UserResponse.description)


            * [`UserResponse.follow_count`](biggo_api.model.md#biggo_api.model.user.UserResponse.follow_count)


            * [`UserResponse.follower_count`](biggo_api.model.md#biggo_api.model.user.UserResponse.follower_count)


            * [`UserResponse.is_follow`](biggo_api.model.md#biggo_api.model.user.UserResponse.is_follow)


            * [`UserResponse.is_my_video`](biggo_api.model.md#biggo_api.model.user.UserResponse.is_my_video)


            * [`UserResponse.is_verify_ecomm`](biggo_api.model.md#biggo_api.model.user.UserResponse.is_verify_ecomm)


            * [`UserResponse.is_verify_user`](biggo_api.model.md#biggo_api.model.user.UserResponse.is_verify_user)


            * [`UserResponse.name`](biggo_api.model.md#biggo_api.model.user.UserResponse.name)


            * [`UserResponse.personal_url`](biggo_api.model.md#biggo_api.model.user.UserResponse.personal_url)


            * [`UserResponse.profile_image`](biggo_api.model.md#biggo_api.model.user.UserResponse.profile_image)


            * [`UserResponse.store_list`](biggo_api.model.md#biggo_api.model.user.UserResponse.store_list)


            * [`UserResponse.user_id`](biggo_api.model.md#biggo_api.model.user.UserResponse.user_id)


    * [biggo_api.model.video module](biggo_api.model.md#module-biggo_api.model.video)


        * [`VideoAnalysis`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis)


            * [`VideoAnalysis.cover_image`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.cover_image)


            * [`VideoAnalysis.createtime`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.createtime)


            * [`VideoAnalysis.createtime_ts`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.createtime_ts)


            * [`VideoAnalysis.last_timestamp`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.last_timestamp)


            * [`VideoAnalysis.last_timestamp_ts`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.last_timestamp_ts)


            * [`VideoAnalysis.length`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.length)


            * [`VideoAnalysis.share_count`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.share_count)


            * [`VideoAnalysis.statistics_last_day`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.statistics_last_day)


            * [`VideoAnalysis.statistics_total`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.statistics_total)


            * [`VideoAnalysis.thumbnails`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.thumbnails)


            * [`VideoAnalysis.updatetime`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.updatetime)


            * [`VideoAnalysis.updatetime_ts`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.updatetime_ts)


            * [`VideoAnalysis.video_comment_count`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.video_comment_count)


            * [`VideoAnalysis.video_like_count`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.video_like_count)


            * [`VideoAnalysis.view_count`](biggo_api.model.md#biggo_api.model.video.VideoAnalysis.view_count)


        * [`VideoResponse`](biggo_api.model.md#biggo_api.model.video.VideoResponse)


            * [`VideoResponse.at_user_id`](biggo_api.model.md#biggo_api.model.video.VideoResponse.at_user_id)


            * [`VideoResponse.created_at`](biggo_api.model.md#biggo_api.model.video.VideoResponse.created_at)


            * [`VideoResponse.description`](biggo_api.model.md#biggo_api.model.video.VideoResponse.description)


            * [`VideoResponse.has_product`](biggo_api.model.md#biggo_api.model.video.VideoResponse.has_product)


            * [`VideoResponse.is_edited`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_edited)


            * [`VideoResponse.is_follow`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_follow)


            * [`VideoResponse.is_like`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_like)


            * [`VideoResponse.is_myvideo`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_myvideo)


            * [`VideoResponse.is_private`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_private)


            * [`VideoResponse.is_verify_ecomm`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_verify_ecomm)


            * [`VideoResponse.is_verify_user`](biggo_api.model.md#biggo_api.model.video.VideoResponse.is_verify_user)


            * [`VideoResponse.like_list`](biggo_api.model.md#biggo_api.model.video.VideoResponse.like_list)


            * [`VideoResponse.limit`](biggo_api.model.md#biggo_api.model.video.VideoResponse.limit)


            * [`VideoResponse.meta`](biggo_api.model.md#biggo_api.model.video.VideoResponse.meta)


            * [`VideoResponse.name`](biggo_api.model.md#biggo_api.model.video.VideoResponse.name)


            * [`VideoResponse.product_count`](biggo_api.model.md#biggo_api.model.video.VideoResponse.product_count)


            * [`VideoResponse.product_list`](biggo_api.model.md#biggo_api.model.video.VideoResponse.product_list)


            * [`VideoResponse.profile_image`](biggo_api.model.md#biggo_api.model.video.VideoResponse.profile_image)


            * [`VideoResponse.status`](biggo_api.model.md#biggo_api.model.video.VideoResponse.status)


            * [`VideoResponse.str_datetime`](biggo_api.model.md#biggo_api.model.video.VideoResponse.str_datetime)


            * [`VideoResponse.timestamp`](biggo_api.model.md#biggo_api.model.video.VideoResponse.timestamp)


            * [`VideoResponse.url`](biggo_api.model.md#biggo_api.model.video.VideoResponse.url)


            * [`VideoResponse.user_id`](biggo_api.model.md#biggo_api.model.video.VideoResponse.user_id)


            * [`VideoResponse.video_comment_count`](biggo_api.model.md#biggo_api.model.video.VideoResponse.video_comment_count)


            * [`VideoResponse.video_id`](biggo_api.model.md#biggo_api.model.video.VideoResponse.video_id)


            * [`VideoResponse.video_like_count`](biggo_api.model.md#biggo_api.model.video.VideoResponse.video_like_count)


            * [`VideoResponse.view_count`](biggo_api.model.md#biggo_api.model.video.VideoResponse.view_count)


        * [`VideoResponseDownload`](biggo_api.model.md#biggo_api.model.video.VideoResponseDownload)


            * [`VideoResponseDownload.mp4`](biggo_api.model.md#biggo_api.model.video.VideoResponseDownload.mp4)


        * [`VideoResponseMeta`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta)


            * [`VideoResponseMeta.aspect_ratio`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta.aspect_ratio)


            * [`VideoResponseMeta.cover_image`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta.cover_image)


            * [`VideoResponseMeta.download`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta.download)


            * [`VideoResponseMeta.iso8601_length`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta.iso8601_length)


            * [`VideoResponseMeta.length`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta.length)


            * [`VideoResponseMeta.thumbnails`](biggo_api.model.md#biggo_api.model.video.VideoResponseMeta.thumbnails)


        * [`VideoResponseStatus`](biggo_api.model.md#biggo_api.model.video.VideoResponseStatus)


            * [`VideoResponseStatus.process_status`](biggo_api.model.md#biggo_api.model.video.VideoResponseStatus.process_status)


            * [`VideoResponseStatus.process_status_kw`](biggo_api.model.md#biggo_api.model.video.VideoResponseStatus.process_status_kw)


            * [`VideoResponseStatus.processing`](biggo_api.model.md#biggo_api.model.video.VideoResponseStatus.processing)


        * [`VideoSettings`](biggo_api.model.md#biggo_api.model.video.VideoSettings)


            * [`VideoSettings.description`](biggo_api.model.md#biggo_api.model.video.VideoSettings.description)


            * [`VideoSettings.limit`](biggo_api.model.md#biggo_api.model.video.VideoSettings.limit)


            * [`VideoSettings.product_list`](biggo_api.model.md#biggo_api.model.video.VideoSettings.product_list)


            * [`VideoSettings.thumbnail_ts`](biggo_api.model.md#biggo_api.model.video.VideoSettings.thumbnail_ts)


            * [`VideoSettings.video_id`](biggo_api.model.md#biggo_api.model.video.VideoSettings.video_id)


        * [`VideoStatistics`](biggo_api.model.md#biggo_api.model.video.VideoStatistics)


            * [`VideoStatistics.average_play_time`](biggo_api.model.md#biggo_api.model.video.VideoStatistics.average_play_time)


            * [`VideoStatistics.full_play_percentage`](biggo_api.model.md#biggo_api.model.video.VideoStatistics.full_play_percentage)


            * [`VideoStatistics.play_time`](biggo_api.model.md#biggo_api.model.video.VideoStatistics.play_time)


            * [`VideoStatistics.unique_user_count`](biggo_api.model.md#biggo_api.model.video.VideoStatistics.unique_user_count)


    * [Module contents](biggo_api.model.md#module-biggo_api.model)


## Submodules

## biggo_api.exception module

This module defind exceptions of BigGo API Client


### _exception_ biggo_api.exception.BigGoAPIException(code, message)
Bases: `Exception`

Base Exception, all the other exceptions are inherited from it

## Module contents
