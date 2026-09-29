import pytest


@pytest.mark.api
async def test_get_all_products(api):
    await api.login()

    response = await api.product_api.get_products()

    assert response["message"] == "All Products fetched Successfully"
    assert len(response["data"]) > 0
    assert response["data"][0]["productName"]
    assert response["data"][0]["productPrice"] > 0