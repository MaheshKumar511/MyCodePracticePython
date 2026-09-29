import pytest


@pytest.mark.api
async def test_get_product_details(api):
    await api.login()

    response = await api.product_api.get_product_details(
        "6960eae1c941646b7a8b3ed3"
    )

    assert response["message"] == "Product Details fetched Successfully"
    assert response["data"]["_id"] == "6960eae1c941646b7a8b3ed3"
    assert response["data"]["productName"] == "ADIDAS ORIGINAL"
    assert response["data"]["productPrice"] == 11500
    assert response["data"]["productCategory"] == "electronics"
    assert response["data"]["productSubCategory"] == "mobiles"
    assert response["data"]["productDescription"] == "Apple phone"