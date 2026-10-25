from aiohttp import ClientResponse, ClientSession

class Auth:
    """Make authenticated requests to the API."""

    def __init__(self, session: ClientSession, host: str,
                 access_token: str) -> None:
        """Initialize the auth."""
        self.session = session
        self.host = host
        self.access_token = access_token

    async def update_token(self, username: str, password: str) -> None:
        response = await self.session.request("post",
                                              f"https://{self.host}/auth/login",
                                              json={'username': username,
                                                    'password': password})
        response.raise_for_status()
        data = await response.json()
        if (data['code'] != 200):
            raise AuthError(str(data))
        self.access_token = data['data']['access_token']

    async def request(
            self, method: str, path: str, **kwargs
            ) -> ClientResponse:
        """Make a request."""
        headers = dict(kwargs.pop("headers", None) or {})
        headers["authorization"] = f"Bearer {self.access_token}"

        return await self.session.request(
                method, f"https://{self.host}/{path}", **kwargs, headers=headers
                )

class AuthError(Exception):
    pass
