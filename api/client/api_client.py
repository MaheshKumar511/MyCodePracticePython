from typing import Any

from playwright.async_api import APIRequestContext


class ApiClient:

    def __init__(self, request: APIRequestContext):
        self.request = request

    async def get(self, endpoint: str, token: str | None = None):
        response = await self.request.get(
            endpoint,
            headers={"Authorization": token} if token else {}
        )

        assert response.ok
        return response

    async def post(
        self,
        endpoint: str,
        data: dict[str, Any],
        token: str | None = None
    ):
        response = await self.request.post(
            endpoint,
            data=data,
            headers={"Authorization": token} if token else {}
        )

        assert response.ok
        return response

    async def put(
        self,
        endpoint: str,
        data: dict[str, Any],
        token: str | None = None
    ):
        response = await self.request.put(
            endpoint,
            data=data,
            headers={"Authorization": token} if token else {}
        )

        assert response.ok
        return response

    async def delete(
        self,
        endpoint: str,
        token: str | None = None
    ):
        response = await self.request.delete(
            endpoint,
            headers={"Authorization": token} if token else {}
        )

        assert response.ok
        return response