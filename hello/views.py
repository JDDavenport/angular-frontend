from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.db import models
from .models import Greeting

# Create your views here.
def index(request):
    r = 'dam'
    print(r)
    return HttpResponse('<pre>' + r + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
