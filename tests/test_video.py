from os import environ
from typing import Optional, Union
import unittest

from requests.exceptions import HTTPError

from biggo_api.clients import APIClient, ClientCredentials
from biggo_api.clients._video import VideoClient
from biggo_api.enum import Limit
from biggo_api.exception import BigGoAPIException
from biggo_api.model import VideoSettings, VideoSettings, VideoResponse


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

    def __upload_video(self, file: str) -> str:
        video_client = self.__get_video_client()
        video_id = video_client.upload(file=file)
        self.assertNotEqual(video_id, '')
        return video_id

    def __post_video_settings(self, video_settings: VideoSettings) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.patch_settings(video_settings=video_settings))
        pass

    def __get_video(self, video_id: str) -> Optional[VideoResponse]:
        video_client = self.__get_video_client()
        video = video_client.get(video_id=video_id)
        return video

    def __patch_video_settings(self, video_settings: VideoSettings) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.patch_settings(video_settings=video_settings))
        pass

    def __delete_video(self, video_id: str) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.delete(video_id=video_id))
        pass

    def test_has_permission(self):
        video_client = self.__get_video_client()
        self.assertTrue(video_client.has_permission())
        pass

    def test_upload_notfound(self):
        with self.assertRaises(FileNotFoundError):
            self.__upload_video(file=NOTFOUND_FILENAME)
            pass
        pass

    def test_upload_get_and_delete_video(self):
        video_id = self.__upload_video(file=FILENAME)
        video = self.__get_video(video_id=video_id)
        self.assertIsInstance(video, VideoResponse)
        self.assertEqual(video.video_id, video_id)
        self.__delete_video(video_id=video_id)
        with self.assertRaises(BigGoAPIException) as ex:
            deleted_video = self.__get_video(video_id=video_id)
            pass
        raised_exc = ex.exception
        self.assertEqual(raised_exc.code, 1004)
        pass

    def test_upload_duplicate_video(self):
        video_id = self.__upload_video(file=FILENAME)
        with self.assertRaises((HTTPError, BigGoAPIException)) as ex:
            self.__upload_video(file=FILENAME)
            pass
        raised_exc = ex.exception
        if isinstance(raised_exc, BigGoAPIException):
            self.assertEqual(ex.exception.code == 1002)
            pass
        self.__delete_video(video_id=video_id)
        pass

    def test_post_video_settings(self):
        video_id = self.__upload_video(file=FILENAME)
        video_settings = VideoSettings(
            video_id=video_id,
            description='test setup',
            limit=Limit.everyone.name,
        )
        self.__post_video_settings(video_settings=video_settings)
        video = self.__get_video(video_id=video_id)
        self.assertEqual(video.video_id, video_settings.video_id)
        self.assertEqual(video.description, video_settings.description)
        self.assertEqual(video.limit, Limit[video_settings.limit].value)
        self.__delete_video(video_id=video_id)
        pass

    def test_update_video(self):
        video_id = self.__upload_video(file=FILENAME)
        video_settings = VideoSettings(
            video_id=video_id,
            description='test post',
            limit=Limit.everyone.name,
        )
        self.__post_video_settings(video_settings=video_settings)
        video_settings_v2 = VideoSettings(
            video_id=video_id,
            limit=Limit.non_public.name,
        )
        self.__patch_video_settings(video_settings=video_settings_v2)
        updated_video = self.__get_video(video_id=video_id)
        self.assertIsNotNone(updated_video)
        self.assertEqual(updated_video.limit, Limit[video_settings_v2.limit].value)
        self.__delete_video(video_id=video_id)
        pass
    pass
