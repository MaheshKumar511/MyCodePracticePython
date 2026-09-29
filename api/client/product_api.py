from playwright.async_api import APIRequestContext

from api.client.api_client import ApiClient


class ProductApi:

    def __init__(self, request: APIRequestContext, token: str):
        self.api_client = ApiClient(request)
        self.token = token

    async def get_products(self) -> dict:
        response = await self.api_client.post(
            "/api/ecom/product/get-all-products",
            {},
            self.token
        )
        return await response.json()

    async def get_product_details(
        self,
        product_id: str
    ) -> dict:
        response = await self.api_client.get(
            f"/api/ecom/product/get-product-detail/{product_id}",
            self.token
        )
        return await response.json()