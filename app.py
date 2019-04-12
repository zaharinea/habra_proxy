import asyncio
import logging

import uvloop
from aiohttp import web
from proxy.config import Config, config
from proxy.routes import setup_routes

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def create_app(config: Config):
    app = web.Application()
    setattr(app, "config", config)

    setup_routes(app)
    return app


if __name__ == "__main__":
    app = create_app(config)
    web.run_app(app, host=config.HOST, port=config.PORT)
