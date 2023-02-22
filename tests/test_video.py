from os import environ
from typing import Optional, Union
import unittest

from biggo_api.clients import VideoClient
from biggo_api.model import EditedVideo, NewVideo, Video
from biggo_api.enum import Limit


CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
TEST_HOST = environ.get('TEST_HOST')
FILENAME = './sample_video/BigGoDecoration2.mp4'
NOTFOUND_FILENAME = './sample_video/NotExistVideo.mp4'
RUNTIME_DATA: dict[str, Union[VideoClient, str]] = {
    'client': None,
    'video_id': None,
    'comment_id': None,
}


class TestVideoClient(unittest.TestCase):
    def __get_video_client(self) -> VideoClient:
        if RUNTIME_DATA['client'] is None:
            if TEST_HOST is not None:
                RUNTIME_DATA['client'] = VideoClient(
                    client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    host_url=TEST_HOST,
                )
            else:
                RUNTIME_DATA['client'] = VideoClient(
                    client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                )
            pass
        return RUNTIME_DATA['client']

    def __upload_video(self, file: str) -> str:
        video_client = self.__get_video_client()
        video_id = video_client.upload(file=file)
        self.assertNotEqual(video_id, '')
        return video_id

    def __setup_video(self, new_video: NewVideo) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.setup_new_video(new_video=new_video))
        pass

    def __get_video(self, video_id: str) -> Optional[Video]:
        video_client = self.__get_video_client()
        video = video_client.get(video_id=video_id)
        return video

    def __update_video(self, edited_video: EditedVideo) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.update(edited_video=edited_video))
        pass

    def __delete_video(self, video_id: str) -> None:
        video_client = self.__get_video_client()
        self.assertTrue(video_client.delete(video_id=video_id))
        pass

    def test_authorized(self):
        video_client = self.__get_video_client()
        self.assertTrue(video_client.authorized)
        pass

    def test_video_auth(self):
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
        self.assertIsInstance(video, Video)
        self.assertEqual(video.video_id, video_id)
        self.__delete_video(video_id=video_id)
        deleted_video = self.__get_video(video_id=video_id)
        self.assertIsNone(deleted_video)
        pass

    def __test_upload_duplicate_video(self):
        return
        video_id = self.__upload_video(file=FILENAME)
        with self.assertRaises(()):
            self.__upload_video(file=FILENAME)
            pass
        pass

    def test_setup_new_video(self):
        video_id = self.__upload_video(file=FILENAME)
        new_video = NewVideo(
            video_id=video_id,
            description='test setup',
            limit=Limit.everyone.name,
            product_list=[],
            thumbnail_ts=5000,
        )
        self.__setup_video(new_video=new_video)
        video = self.__get_video(video_id=video_id)
        self.assertEqual(video.video_id, new_video.video_id)
        self.assertEqual(video.description, new_video.description)
        self.assertEqual(video.limit, Limit[new_video.limit].value)
        self.assertEqual(video.product_list, None)
        self.__delete_video(video_id=video_id)
        pass

    def test_update_video(self):
        video_id = self.__upload_video(file=FILENAME)
        new_video = NewVideo(
            video_id=video_id,
            description='test setup',
            limit=Limit.everyone.name,
            product_list=[],
            thumbnail_ts=5000,
        )
        self.__setup_video(new_video=new_video)
        edited_video = EditedVideo(
            video_id=video_id,
            limit=Limit.non_public.name,
        )
        self.__update_video(edited_video=edited_video)
        updated_video = self.__get_video(video_id=video_id)
        self.assertIsNotNone(updated_video)
        self.assertEqual(updated_video.limit, Limit[edited_video.limit].value)
        self.__delete_video(video_id=video_id)
        pass
    pass
