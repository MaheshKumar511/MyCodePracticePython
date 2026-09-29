import os

from playwright.async_api import APIRequestContext

from api.client.auth_api import AuthApi
from api.client.order_api import OrderApi
from api.client.product_api import ProductApi


class ApiFixture:

    def __init__(self, request: APIRequestContext):
        self.request = request
        self._auth_api = None
        self._product_api = None
        self._order_api = None
        self._token = None

    @property
    def auth_api(self) -> AuthApi:
        if self._auth_api is None:
            self._auth_api = AuthApi(self.request)
        return self._auth_api

    async def login(self):
        response = await self.auth_api.login(
            os.getenv("USER_EMAIL"),
            os.getenv("USER_PASSWORD")
        )
        self._token = response["token"]
        return response

    @property
    def product_api(self) -> ProductApi:
        if not self._token:
            raise RuntimeError("API login required")

        if self._product_api is None:
            self._product_api = ProductApi(
                self.request,
                self._token
            )

        return self._product_api

    @property
    def order_api(self) -> OrderApi:
        if not self._token:
            raise RuntimeError("API login required")

        if self._order_api is None:
            self._order_api = OrderApi(
                self.request,
                self._token
            )

        return self._order_api