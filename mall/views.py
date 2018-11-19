from django.shortcuts import render


def index(request):
    request.session["title"] = "聆听"
    context = {
        "tag": "index",
    }

    return render(request, "mall/index.html", context)
