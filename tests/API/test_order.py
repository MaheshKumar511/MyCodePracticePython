import pytest


@pytest.mark.api
async def test_create_order_successfully(api):
    await api.login()

    response = await api.order_api.create_order(
        "India",
        "6960eae1c941646b7a8b3ed3"
    )

    assert response["message"] == "Order Placed Successfully"
    assert len(response["orders"]) > 0
    assert response["orders"][0]


@pytest.mark.api
async def test_get_orders_for_customer_successfully(api):
    login_response = await api.login()

    response = await api.order_api.get_orders_for_customer(
        login_response["userId"]
    )

    assert response["message"] == "Orders fetched for customer Successfully"
    assert response["count"] > 0
    assert len(response["data"]) == response["count"]
    assert response["data"][0]["productName"]
    assert response["data"][0]["orderPrice"]