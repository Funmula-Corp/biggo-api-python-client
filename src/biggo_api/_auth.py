"""This module authorize functions for supporting grant types"""

from typing import Optional
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def auth_client_credentials(
    url: str,
    client_id: str,
    client_secret: str,
    verify: bool = True,
    refresh_url: Optional[str] = None,
) -> OAuth2Session:
    """Authorize client by client credentials

    Raises:
        InvalidClientIdError: authorization failed
    """
    # init oauth 2.0 session
    oauth2_session = OAuth2Session(
        client=BackendApplicationClient(client_id=client_id),
        auto_refresh_url=refresh_url,
    )
    # setup params: token url, auth(id & secret)
    params = {
        'token_url': url,
        'auth': (client_id, client_secret),
        'verify': verify,
    }
    # get access token from authorized server
    oauth2_session.fetch_token(**params)
    return oauth2_session
