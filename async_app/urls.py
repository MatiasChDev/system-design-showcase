from django.urls import path

from . import views

urlpatterns = [
    path("sync/", views.sync, name="sync"),
    path("", views.async_view, name="async"),
]
