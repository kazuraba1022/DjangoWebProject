
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render   # Added for this step
from datetime import datetime

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )