from django.urls import path, re_path

from . import views

app_name = "mallAdmin"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("index/", views.index, name="index"),
    re_path(".*", views.index),
]
