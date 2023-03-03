from os import environ
from time import sleep
from typing import Union
import unittest

from biggo_api.clients import APIClient, ClientCredentials
from biggo_api.clients._user import UserClient
from biggo_api.clients._video import VideoClient


CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
TEST_HOST = environ.get('TEST_HOST')
FILENAME = './sample_video/BigGoDecoration2.mp4'
NOTFOUND_FILENAME = './sample_video/NotExistVideo.mp4'
RUNTIME_DATA: dict[str, Union[APIClient, str]] = {
    'client': None,
    'video_id': None,
    'comment_id': None,
}


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
        video_id = self.__upload_video(file=FILENAME)
        user_client = self.__get_user_client()
        retry = 0
        my_videos = []
        while retry <= 5 and not my_videos:
            retry += 1
            sleep(5*retry)
            get_own_videos_response = user_client.get_own_videos()
            self.assertTrue(get_own_videos_response.result)
            my_videos = get_own_videos_response.user_video.data
            pass
        if retry > 5:
            self.__delete_video(video_id=video_id)
            raise TimeoutError
        self.assertIn(video_id, [video.video_id for video in my_videos])
        self.__delete_video(video_id=video_id)
        pass

    def test_get_user_videos(self):
        video_id = self.__upload_video(file=FILENAME)
        userid = self.__get_video_client().has_permission().userid
        user_client = self.__get_user_client()
        retry = 0
        user_videos = []
        while retry <= 5 and not user_videos:
            retry += 1
            sleep(5*retry)
            get_user_videos_response = \
                user_client.get_user_videos(userid=userid)
            self.assertTrue(get_user_videos_response.result)
            user_videos = get_user_videos_response.user_video.data
            pass
        if retry > 5:
            self.__delete_video(video_id=video_id)
            raise TimeoutError
        self.assertIn(video_id, [video.video_id for video in user_videos])
        self.__delete_video(video_id=video_id)
        pass
    pass
