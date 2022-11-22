"""
ASGI config for system_design_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import asyncio
import os

import django
from django.core.asgi import ASGIHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system_design_project.settings")


class MyASGIHandler(ASGIHandler):
    def __init__(self):
        super().__init__()
        self.on_shutdown = []

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            while True:
                message = await receive()
                if message["type"] == "lifespan.startup":
                    # Do some startup here!
                    await send({"type": "lifespan.startup.complete"})
                elif message["type"] == "lifespan.shutdown":
                    # Do some shutdown here!
                    await self.shutdown()
                    await send({"type": "lifespan.shutdown.complete"})
                    return
        await super().__call__(scope, receive, send)

    async def shutdown(self):
        for handler in self.on_shutdown:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()


def my_get_asgi_application():
    django.setup(set_prefix=False)
    return MyASGIHandler()


application = my_get_asgi_application()
