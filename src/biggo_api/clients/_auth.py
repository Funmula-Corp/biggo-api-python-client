"""This module contains classes of OAuth 2.0 grant type and their authorization functions."""

from typing import Optional, NamedTuple

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class ClientCredentials(NamedTuple):
    """The namedtuple class for client credentials.

    Args:
        client_id: Client identifier given by the OAuth provider upon registration.
        client_secret: The secret paired to the client_id.
    """
    client_id: str
    client_secret: str
    pass


def auth_client_credentials(
    url: str,
    client_credentials: ClientCredentials,
    verify: bool = True,
    refresh_url: Optional[str] = None,
) -> OAuth2Session:
    """Authorize client by client credentials grant.

    Args:
        url: The url address used to fetch token.
        client_credentials: A `NamedTuple` contains client_id and client_secret.
        verify: Verify SSL certificate.
        refresh_url: The url address used to refresh access token.

    Examples:
        Call this function to get an `OAuth2Session` using client credentials grant.
        Verify its authorization status.

        >>> credentials = ClientCredentials(
        ...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET'
        ... )
        >>> oauth2_session = auth_client_credentials(
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
        'auth': client_credentials,
        'verify': verify,
    }
    # fetch JWT token
    oauth2_session.fetch_token(**params)
    return oauth2_session
