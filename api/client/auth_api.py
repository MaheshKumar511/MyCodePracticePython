from playwright.async_api import APIRequestContext

from api.client.api_client import ApiClient


class AuthApi:

    def __init__(self, request: APIRequestContext):
        self.api_client = ApiClient(request)

    async def login(
        self,
        user_email: str,
        user_password: str
    ) -> dict:
        response = await self.api_client.post(
            "/api/ecom/auth/login",
            {
                "userEmail": user_email,
                "userPassword": user_password
            }
        )
        return await response.json()