import asynctest
import pytest
from aiohttp import web
from proxy.config import config
from proxy.routes import setup_routes


def create_app(loop):
    app = web.Application(loop=loop)
    setattr(app, "config", config)
    setup_routes(app)
    return app


@pytest.fixture
def mocked_response(expected_html):
    mock_resp = asynctest.MagicMock()
    mock_resp.status = 200
    mock_resp.data = expected_html.encode()
    mock_resp.content_type = "text/html"
    return mock_resp


async def test_proxy(loop, aiohttp_client, get_expected_soup, mocked_response):
    expected_soup, _ = get_expected_soup
    client = await aiohttp_client(create_app)

    with asynctest.patch("proxy.handlers.fetch_response", return_value=mocked_response):
        resp = await client.get("/")

    assert resp.status == 200
    text = await resp.text()
    assert text == str(expected_soup)
