import asyncio

import aiohttp
import environ
from todoist_api_python.api_async import TodoistAPIAsync

from .asgi import application

CLIENT_SESSSION = None
TODOIST_API = None

_lock = asyncio.Lock()


async def get_client_session():
    global CLIENT_SESSSION

    async with _lock:
        if not CLIENT_SESSSION:
            CLIENT_SESSSION = aiohttp.ClientSession()
            application.on_shutdown.append(CLIENT_SESSSION.close)

    return CLIENT_SESSSION


async def get_todoist_api(todoist_token: str):
    global TODOIST_API

    async with _lock:
        if not TODOIST_API:
            TODOIST_API = TodoistAPIAsync(todoist_token)

    return TODOIST_API