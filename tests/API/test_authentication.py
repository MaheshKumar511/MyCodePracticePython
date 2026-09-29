import pytest


@pytest.mark.api
async def test_login_successfully(api):
    response = await api.login()

    assert response["message"] == "Login Successfully"
    assert response["token"]
    assert response["userId"]