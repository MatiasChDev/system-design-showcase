import asyncio
import time

import aiohttp
import requests
from django.http import HttpResponse
from loguru import logger

# Create your views here.


async def print_ip(session):
    async with session.get("https://api.ipify.org?format=json") as resp:
        logger.info(await resp.text())


async def async_view(request):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[print_ip(session) for i in range(10)])
    end = time.time()
    logger.info(end - start)
    return HttpResponse("Test")


def sync(request):
    start = time.time()
    for i in range(10):
        x = requests.get("https://api.ipify.org?format=json")
        logger.info(x.json())
    end = time.time()
    logger.info(end - start)
    return HttpResponse("Hello, world. You're at the polls index.")
