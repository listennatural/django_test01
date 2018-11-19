from django.shortcuts import render

from .models import *


def index(request):
    request.session["title"] = ""
    projects = Project.objects.order_by()

    context = {
        "projects": projects,
    }
    return render(request, 'index/index.html', context)
