from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from hello.forms import SearchForm 
from django.http import HttpResponseRedirect


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
        if form.is_valid():
            searchTerm = form.cleaned_data['userInput']
            form = SearchForm()
            context = {'form': form, 'searchTerm': searchTerm}
            return render(request, "search.html", context)


    else:    
        form = SearchForm()
        searchTerm = 'none'
    context = {'form': form, 'searchTerm': searchTerm}
    return render(request, "search.html", context)