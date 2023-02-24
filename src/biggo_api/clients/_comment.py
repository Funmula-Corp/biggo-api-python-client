"""The API client of video comment"""

from biggo_api.model import CommentResponse, CommentHistory, CommentRequest, NewComment
from biggo_api.clients._base import BaseInstanceClient


class CommentClient(BaseInstanceClient):
    """Client to access video comment API"""

    def create(self, new_comment: NewComment) -> CommentResponse:
        """Create new comment

        Args:
            new_comment: A `biggo_api.model.NewComment` object

        Returns:
            A `biggo_api.model.Comment` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='POST',
            path='video/comment/',
            json=new_comment.to_dict(),
        )
        dict_created_comment = response_json['created_comment']
        created_comment = CommentResponse.from_dict(dict_data=dict_created_comment)
        return created_comment

    def update(self, edited_comment: CommentRequest) -> bool:
        """Update comment

        Args:
            edited_comment: A `biggo_api.model.EditedComment` object

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='PATCH',
            path=f'video/comment/{edited_comment.comment_id}',
            json=edited_comment.to_dict()
        )
        return response_json is not None

    def delete(self, comment_id: str) -> bool:
        """Delete comment

        Args:
            comment_id: The id of comment

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'video/comment/{comment_id}',
        )
        return response_json is not None

    def like(self, comment_id: str) -> bool:
        """Like comment

        Args:
            comment_id: The id of comment

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='POST',
            path=f'video/comment/{comment_id}/like',
        )
        return response_json is not None

    def unlike(self, comment_id: str):
        """Unlike comment

        Args:
            comment_id: The id of comment

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'video/comment/{comment_id}/like',
        )
        return response_json is not None

    def get_list(self, video_id: str, parent_id: str = None) -> list[CommentResponse]:
        """Get list of comments

        Args:
            video_id: The id of video
            parent_id: The id of parent id (video or comment)

        Returns:
            A list of `biggo_api.model.Comment` object
        """
        raise NotImplementedError
        if parent_id is None:
            parent_id = video_id
            pass
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}/{parent_id}'
        )
        comments = [
            CommentResponse.from_dict(dict_data=dict_comment)
            for dict_comment in response_json['comments']
        ]
        return comments

    def get_comment_history(self) -> list[CommentHistory]:
        """Get comment log

        Returns:
            A list of `biggo_api.model.CommentHistory` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path='video/comment_log/',
        )
        comment_history = [
            CommentHistory.from_dict(comment_history)
            for comment_history in response_json['comment_logs']
        ]
        return comment_history
    pass
