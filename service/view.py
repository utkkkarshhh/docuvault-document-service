from django.conf import settings
from django.shortcuts import render

def home_view(request):
    context = {
        "APP_NAME": settings.APP_NAME,
        "BASE_URL": settings.BASE_URL,
    }
    return render(request, "home.html", context)
