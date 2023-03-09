from os import environ
from typing import Union
import unittest

from aiohttp import ClientResponseError

from biggo_api.async_clients import APIClient, ClientCredentials
from biggo_api.async_clients._video import VideoClient
from biggo_api.enum import Access
from biggo_api.exception import BigGoAPIError
from biggo_api.data_models import BigGoVideo, VideoParams


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


class TestVideoClient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        await self.__init_api_client()
        pass

    async def asyncTearDown(self) -> None:
        if RUNTIME_DATA['api_client']:
            api_client: APIClient = RUNTIME_DATA['api_client']
            await api_client.close()
            pass
        pass

    async def __init_api_client(self) -> None:
        client_credentials = ClientCredentials(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
        )
        if TEST_HOST is not None:
            RUNTIME_DATA['api_client'] = APIClient(
                host_url=TEST_HOST,
                verify=False,
            )
            pass
        else:
            RUNTIME_DATA['api_client'] = APIClient()
            pass
        await RUNTIME_DATA['api_client'].authorize(client_credentials=client_credentials)
        pass

    async def __get_video_client(self) -> VideoClient:
        return RUNTIME_DATA['api_client'].video

    async def __upload_video(self, file: str) -> str:
        """Return video_id"""
        video_client = await self.__get_video_client()
        video_upload_response = await video_client.upload(file=file)
        self.assertTrue(video_upload_response.result)
        self.assertNotEqual(video_upload_response.video_id, '')
        return video_upload_response.video_id

    async def __update_video_params(self, video_params: VideoParams) -> None:
        video_client = await self.__get_video_client()
        update_response = \
            await video_client.update(video_params=video_params)
        self.assertTrue(update_response.result)
        pass

    async def __get_video(self, video_id: str) -> BigGoVideo:
        video_client = await self.__get_video_client()
        get_video_response = await video_client.get(video_id=video_id)
        self.assertTrue(get_video_response.result)
        video = get_video_response.video[0]
        return video

    async def __partial_update_video_params(self, video_params: VideoParams) -> None:
        video_client = await self.__get_video_client()
        partial_update_response = \
            await video_client.partial_update(video_params=video_params)
        self.assertTrue(partial_update_response.result)
        pass

    async def __delete_video(self, video_id: str) -> None:
        video_client = await self.__get_video_client()
        video_delete_response = await video_client.delete(video_id=video_id)
        self.assertTrue(video_delete_response.result)
        pass

    async def test_has_permission(self):
        video_client = await self.__get_video_client()
        
        self.assertTrue((await video_client.has_permission()).result)
        pass

    async def test_upload_notfound(self):
        with self.assertRaises(FileNotFoundError):
            await self.__upload_video(file=NOTFOUND_FILENAME)
            pass
        pass

    async def test_upload_get_and_delete_video(self):
        video_id = await self.__upload_video(file=FILENAME)
        video = await self.__get_video(video_id=video_id)
        self.assertEqual(video.video_id, video_id)
        await self.__delete_video(video_id=video_id)
        with self.assertRaises(BigGoAPIError) as ex:
            await self.__get_video(video_id=video_id)
            pass
        raised_exc = ex.exception
        self.assertEqual(raised_exc.response.error.code, 1004)
        pass

    async def test_upload_duplicate_video(self):
        video_id = await self.__upload_video(file=FILENAME)
        with self.assertRaises((ClientResponseError, BigGoAPIError)) as ex:
            await self.__upload_video(file=FILENAME)
            pass
        raised_exc = ex.exception
        if isinstance(raised_exc, BigGoAPIError):
            self.assertEqual(raised_exc.response.error.code, 1002)
            pass
        await self.__delete_video(video_id=video_id)
        pass

    async def test_update(self):
        video_id = await self.__upload_video(file=FILENAME)
        video_params = VideoParams(
            video_id=video_id,
            access=Access.PUBLIC,
            description='test setup',
            title='test post title',
        )
        await self.__update_video_params(video_params=video_params)
        video = await self.__get_video(video_id=video_id)
        self.assertEqual(video.video_id, video_params.video_id)
        self.assertEqual(video.description, video_params.description)
        self.assertEqual(video.access, video_params.access)
        await self.__delete_video(video_id=video_id)
        pass

    async def test_partial_update(self):
        video_id = await self.__upload_video(file=FILENAME)
        video_params = VideoParams(
            video_id=video_id,
            access=Access.PUBLIC,
            description='test post description',
            title='test post title',
        )
        await self.__partial_update_video_params(video_params=video_params)
        video_params_v2 = VideoParams(
            video_id=video_id,
            access=Access.UNLISTED,
        )
        await self.__partial_update_video_params(video_params=video_params_v2)
        updated_video = await self.__get_video(video_id=video_id)
        self.assertEqual(updated_video.access, video_params_v2.access)
        await self.__delete_video(video_id=video_id)
        pass
    pass
