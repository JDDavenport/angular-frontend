from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.db import models
from .models import Greeting
from django import forms

# Create your views here.
def index(request):
    r = 'yo'
    print(r)
    return HttpResponse('<pre>' + r + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def searchDoctor(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            searchTerm = form.cleaned_data['userInput']   
#            p1 = pmod.Permission.objects.get(id=1)
#            a1 = hmod.overdoses.objects.filter(abbrev = 'UT')
#            searchTerm = p1.codename
            args = {'form': form, 'searchTerm': searchTerm}
            return request.dmp.render('search.html', args)
    else:
        searchTerm = "none"
        form = MyForm()
    args = {'form': form, 'searchTerm': searchTerm}
    return request.dmp.render('search.html', args)

class MyForm(forms.Form):
    '''An example form'''
    userInput = forms.CharField(label='Search Term')

    def clean_data(self):
        return self.cleaned_data 
