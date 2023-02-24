"""This module contains classes of OAuth 2.0 grant type and their authorization function"""

from typing import Optional, NamedTuple

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class ClientCredentials(NamedTuple):
    """The namedtuple class for client credentials"""
    client_id: str
    client_secret: str
    pass


def auth_client_credentials(
    url: str,
    client_credentials: ClientCredentials,
    verify: bool = True,
    refresh_url: Optional[str] = None,
) -> OAuth2Session:
    """Authorize client by client credentials
    
    Args:
        url: The url address to fetch token
        client_credentials: A `NamedTuple` contains client_id and client_secret used for authorization
        verify: Verify SSL certificate
        refresh_url: The url address to refresh access token

    Returns:
        A  `requests_oauthlib.OAuth2Session` object
    """
    # initialize client for client credentials
    client = BackendApplicationClient(client_id=client_credentials.client_id)
    # initialize an OAuth2Session object
    oauth2_session = OAuth2Session(client=client, auto_refresh_url=refresh_url)
    params = {
        'token_url': url,
        'auth': client_credentials,
        'verify': verify,
    }
    # fetch JWT token
    oauth2_session.fetch_token(**params)
    return oauth2_session
