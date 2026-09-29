import os

import pytest


@pytest.mark.RahulShetty
@pytest.mark.asyncio
async def test_place_order_successfully(
    mahesh_custom_fixture
):
    rahul_shetty = mahesh_custom_fixture.rahul_shetty

    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")

    await rahul_shetty.login_page.navigate()
    await rahul_shetty.login_page.enter_email(email)
    await rahul_shetty.login_page.enter_password(password)
    await rahul_shetty.login_page.click_login("Login Successfully")
    await rahul_shetty.login_page.validate_url("/dashboard")
    await rahul_shetty.login_page.validate_toast_message(
        "Login Successfully"
    )

    await rahul_shetty.dashboard_page.click_first_product()
    await rahul_shetty.dashboard_page.add_to_cart()
    await rahul_shetty.dashboard_page.validate_toast_message(
        "Product Added To Cart"
    )
    await rahul_shetty.dashboard_page.go_to_cart()

    await rahul_shetty.cart_page.verify_cart_price1()
    await rahul_shetty.cart_page.verify_cart_price2()
    await rahul_shetty.cart_page.verify_product_id()
    await rahul_shetty.cart_page.checkout()

    await rahul_shetty.checkout_page.select_expiry()
    await rahul_shetty.checkout_page.enter_cvv("485")
    await rahul_shetty.checkout_page.enter_card_holder_name("Playwright")
    await rahul_shetty.checkout_page.enter_country("India")
    await rahul_shetty.checkout_page.select_country("India")
    await rahul_shetty.checkout_page.place_order()

    await rahul_shetty.confirmation_page.validate_toast_message(
        "Order Placed Successfully"
    )
    await rahul_shetty.confirmation_page.verify_order_amount()