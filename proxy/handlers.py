import logging
import ssl
from typing import List
from urllib.parse import urljoin

import certifi
from aiohttp import ClientSession, web
from aiohttp.web import Request, Response

from .common import ServerResponse, UrlReplace
from .utils import processing_text

LOGGER = logging.getLogger(__name__)


def get_target_url(request: Request) -> str:
    return urljoin(request.app.config.TARGET_URL, request.path_qs)


def get_urls_replace(request: Request) -> List[UrlReplace]:
    urls = []
    for url in request.app.config.REPLACE_URLS:
        urls.append(UrlReplace(src=url, dst=f"{request.url.scheme}://{request.host}/"))
    return urls


async def fetch_response(request: Request) -> ServerResponse:
    target_url = get_target_url(request)
    request_body = await request.read()

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    timeout = request.app.config.HTTP_TIMEOUT

    async with ClientSession() as session:
        async with session.request(
            method=request.method,
            url=target_url,
            data=request_body,
            timeout=timeout,
            ssl=ssl_context,
        ) as resp:
            data = await resp.read()
            return ServerResponse(
                data=data,
                headers=resp.headers,
                status=resp.status,
                content_type=resp.content_type,
            )


async def proxy(request: Request) -> Response:
    """
    Данный handler проксирует поступающие запросы на url указанный в config.TARGET_URL.
    Полученный ответ от сервера преобразуется к следующему виду:
     - к словам из шести букв добавляется символ «™»;
     - urls из списка config.REPLACE_URLS, заменяются на url proxy-сервера.

    """
    resp = await fetch_response(request)

    exclude_headers = ("Transfer-Encoding", "Content-Encoding")
    headers = {
        key: val for key, val in resp.headers.items() if key not in exclude_headers
    }
    if resp.content_type == "text/html":
        data = processing_text(data=resp.data.decode(), urls=get_urls_replace(request))
        return web.Response(text=data, status=resp.status, headers=headers)

    return web.Response(body=resp.data, status=resp.status, headers=headers)
