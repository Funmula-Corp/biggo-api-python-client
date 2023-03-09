"""This module contains asynchronous authorization functions of OAuth 2.0 grant type."""

from aiohttp import BasicAuth
from typing import Optional

from async_oauthlib.oauth2_session import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

from biggo_api.clients._auth import ClientCredentials


async def auth_client_credentials(
    url: str,
    client_credentials: ClientCredentials,
    verify_ssl: bool = True,
    refresh_url: Optional[str] = None,
) -> OAuth2Session:
    """Authorize client by client credentials grant asynchronously.

    Args:
        url: The url address used to fetch token.
        client_credentials: A `NamedTuple` contains client_id and client_secret.
        verify_ssl: Verify SSL certificate.
        refresh_url: The url address used to refresh access token.

    Examples:
        Call this function to get an `OAuth2Session` using client credentials grant.
        Verify its authorization status.

        >>> credentials = ClientCredentials(
        ...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET'
        ... )
        >>> oauth2_session = await auth_client_credentials(
        ...     url='https://api.biggo.com/auth/v1/token',
        ...     client_credentials=credentials,
        ... )
        >>> oauth2_session.authorized
        True
    """
    # initialize client for client credentials
    client = BackendApplicationClient(client_id=client_credentials.client_id)
    # initialize an OAuth2Session object
    oauth2_session = OAuth2Session(client=client, auto_refresh_url=refresh_url)
    params = {
        'token_url': url,
        'auth': BasicAuth(*client_credentials),
        'verify_ssl': verify_ssl,
    }
    # fetch JWT token
    await oauth2_session.fetch_token(**params)
    return oauth2_session
