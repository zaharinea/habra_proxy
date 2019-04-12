from typing import NamedTuple

from multidict import CIMultiDictProxy


class UrlReplace(NamedTuple):
    src: str
    dst: str


class ServerResponse(NamedTuple):
    data: bytes
    status: int
    headers: CIMultiDictProxy
    content_type: str
