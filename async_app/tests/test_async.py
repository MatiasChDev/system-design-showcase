import asyncio
import time

import aiohttp
from django.test import TestCase
from loguru import logger

from system_design_project.client_session import get_client_session


async def print_ip(session):
    async with session.get("https://api.ipify.org?format=json") as resp:
        x = await resp.text()


class AsyncTestCase(TestCase):
    async def test_async(self):
        session = await get_client_session()
        start = time.time()
        # async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[print_ip(session) for i in range(10)])
        end = time.time()
        logger.info(end - start)
