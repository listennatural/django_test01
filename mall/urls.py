from django.urls import path, include

from . import views

app_name = "mall"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("admin/", include("mallAdmin.urls")),
]
