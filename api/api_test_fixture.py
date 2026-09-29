import pytest
from playwright.async_api import APIRequestContext

from api.api_fixture import ApiFixture


@pytest.fixture
async def api(request: APIRequestContext):
    yield ApiFixture(request)