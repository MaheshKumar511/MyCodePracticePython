from playwright.async_api import APIRequestContext

from api.client.api_client import ApiClient


class OrderApi:

    def __init__(self, request: APIRequestContext, token: str):
        self.api_client = ApiClient(request)
        self.token = token

    async def create_order(
        self,
        country: str,
        product_ordered_id: str
    ) -> dict:
        response = await self.api_client.post(
            "/api/ecom/order/create-order",
            {
                "orders": [
                    {
                        "country": country,
                        "productOrderedId": product_ordered_id
                    }
                ]
            },
            self.token
        )
        return await response.json()

    async def get_orders_for_customer(
        self,
        user_id: str
    ) -> dict:
        response = await self.api_client.get(
            f"/api/ecom/order/get-orders-for-customer/{user_id}",
            self.token
        )
        return await response.json()