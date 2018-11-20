from django.shortcuts import render

from mall.models import *

def index(request):
    request.session["title"] = "后台管理"
    context = {
        "tag": "index",
    }

    return render(request, "mallAdmin/index.html", context)