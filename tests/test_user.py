from os import environ
from time import sleep
from typing import Union
import unittest

from biggo_api.clients import APIClient, ClientCredentials
from biggo_api.clients._user import UserClient
from biggo_api.clients._video import VideoClient
from biggo_api.model import VideoResponse


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
        video_client = self.__get_video_client()
        video_id = video_client.upload(file=file)
        self.assertNotEqual(video_id, '')
        return video_id

    def __delete_video(self, video_id: str) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.delete(video_id=video_id))
        pass

    def test_get_own_video_list(self):
        video_id = self.__upload_video(file=FILENAME)
        user_client = self.__get_user_client()
        retry = 0
        my_videos = []
        while retry <= 5 and not my_videos:
            retry += 1
            sleep(5*retry)
            my_videos = user_client.get_own_video_list()
            pass
        if retry > 5:
            self.__delete_video(video_id=video_id)
            raise TimeoutError
        found = video_id in [video.video_id for video in my_videos]
        self.assertTrue(found)
        self.__delete_video(video_id=video_id)
        pass
    pass
