import asyncio
import os

import aiohttp
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from loguru import logger
from todoist_api_python.api_async import TodoistAPIAsync

from system_design_project.client_session import get_todoist_api

# Create your views here.


class TasksView(View):
    async def get(self, request):
        api = await get_todoist_api()
        try:
            tasks = await api.get_tasks()
            formatted_tasks = [
                {"id": task.id, "content": task.content} for task in tasks
                ]
            return render(request, 'base.html', {"tasks": formatted_tasks})
        except Exception as error:
            return HttpResponse(error)
