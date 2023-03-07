from os import environ
from time import sleep
from typing import Union
import unittest

from biggo_api.clients import APIClient, ClientCredentials
from biggo_api.clients._user import UserClient
from biggo_api.clients._video import VideoClient
from biggo_api.data_models import BigGoVideoProductBase
from biggo_api.enum import ProcessStatus


CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
TEST_HOST = environ.get('TEST_HOST')
FILENAME = './sample_video/test_video1.mp4'
NOTFOUND_FILENAME = './sample_video/NotExistVideo.mp4'
RUNTIME_DATA: dict[str, Union[APIClient, str]] = {
    'client': None,
    'video_id': None,
    'comment_id': None,
}
VIDEO_PER_PAGE = 20


class TestVideoClient(unittest.TestCase):
    def __get_video_client(self) -> VideoClient:
        if RUNTIME_DATA['client'] is None:
            client_credentials = ClientCredentials(
                client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
            )
            if TEST_HOST is not None:
                RUNTIME_DATA['client'] = APIClient(
                    client_credentials=client_credentials,
                    host_url=TEST_HOST,
                    verify=False,
                )
            else:
                RUNTIME_DATA['client'] = APIClient(
                    client_credentials=client_credentials,
                )
            pass
        return RUNTIME_DATA['client'].video

    def __get_user_client(self) -> UserClient:
        if RUNTIME_DATA['client'] is None:
            client_credentials = ClientCredentials(
                client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
            )
            if TEST_HOST is not None:
                RUNTIME_DATA['client'] = APIClient(
                    client_credentials=client_credentials,
                    host_url=TEST_HOST,
                    verify=False,
                )
            else:
                RUNTIME_DATA['client'] = APIClient(
                    client_credentials=client_credentials,
                )
            pass
        return RUNTIME_DATA['client'].user

    def __upload_video(self, file: str) -> str:
        """Return video_id"""
        video_client = self.__get_video_client()
        video_upload_response = video_client.upload(file=file)
        self.assertTrue(video_upload_response.result)
        self.assertNotEqual(video_upload_response.video_id, '')
        return video_upload_response.video_id

    def __delete_video(self, video_id: str) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.delete(video_id=video_id).result)
        pass

    def test_get_own_videos(self):
        user_client = self.__get_user_client()
        page = 1
        own_videos: set[str] = set()
        while True:
            get_own_videos_response = user_client.get_own_videos(page=page)
            videos = get_own_videos_response.user_video.data
            video_ids: list[str] = []
            for video in videos:
                video_ids.append(video.video_id)
                if video.product_list:
                    for product in video.product_list:
                        self.assertIsInstance(product, BigGoVideoProductBase)
                        pass
                    pass
                pass
            own_videos = own_videos.union(set(video_ids))
            total_video_count = get_own_videos_response.user_video.size
            if total_video_count <= VIDEO_PER_PAGE * page:
                break
            page += 1
            pass
        self.assertEqual(len(own_videos), total_video_count)
        pass

    def test_get_own_videos_upload(self):
        video_id = self.__upload_video(file=FILENAME)
        sleep(5)
        user_client = self.__get_user_client()
        page = 1
        own_videos: set[str] = set()
        while True:
            get_own_videos_response = user_client.get_own_videos(page=page)
            videos = get_own_videos_response.user_video.data
            #check processing video
            video0 = videos[0]
            if video0.status.process_status != ProcessStatus.COMPLETE:
                sleep(5)
                continue
            #finish check processing video
            video_ids: list[str] = []
            for video in videos:
                video_ids.append(video.video_id)
                if video.product_list:
                    for product in video.product_list:
                        self.assertIsInstance(product, BigGoVideoProductBase)
                        pass
                    pass
                pass
            own_videos = own_videos.union(set(video_ids))
            video_count = get_own_videos_response.user_video.size
            if video_count == len(own_videos):
                break
            page += 1
            pass
        self.assertIn(video_id, own_videos)
        self.__delete_video(video_id=video_id)
        pass

    def test_get_user_videos(self):
        user_client = self.__get_user_client()
        userid = self.__get_video_client().has_permission().userid
        page = 1
        user_videos: set[str] = set()
        while True:
            get_user_videos_response = user_client.get_user_videos(userid=userid, page=page)
            videos = get_user_videos_response.user_video.data
            video_ids: list[str] = []
            for video in videos:
                video_ids.append(video.video_id)
                if video.product_list:
                    for product in video.product_list:
                        self.assertIsInstance(product, BigGoVideoProductBase)
                        pass
                    pass
                pass
            user_videos = user_videos.union(set(video_ids))
            total_video_count = get_user_videos_response.user_video.size
            if total_video_count <= VIDEO_PER_PAGE * page:
                break
            page += 1
            pass
        self.assertEqual(len(user_videos), total_video_count)
        pass

    def test_get_user_videos_upload(self):
        video_id = self.__upload_video(file=FILENAME)
        sleep(5)
        userid = self.__get_video_client().has_permission().userid
        user_client = self.__get_user_client()
        page = 1
        user_videos: set[str] = set()
        while True:
            get_user_videos_response = \
                user_client.get_user_videos(userid=userid, page=page)
            videos = get_user_videos_response.user_video.data
            # check processing video
            video0 = videos[0]
            if video0.status.process_status != ProcessStatus.COMPLETE:
                sleep(5)
                continue
            #finish check processing video
            video_ids: list[str] = []
            for video in videos:
                video_ids.append(video.video_id)
                if video.product_list:
                    for product in video.product_list:
                        self.assertIsInstance(product, BigGoVideoProductBase)
                        pass
                    pass
                pass
            user_videos = user_videos.union(set(video_ids))
            video_count = get_user_videos_response.user_video.size
            if video_count <= len(user_videos):
                break
            page += 1
            pass
        self.assertIn(video_id, user_videos)
        self.__delete_video(video_id=video_id)
        pass
    pass
