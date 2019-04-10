from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from hello.forms import SearchForm 


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
    else:    
        form = SearchForm()
    return render(request, "search.html", {'form': form})