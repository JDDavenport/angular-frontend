from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms
# from homepage import models as hmod
from django.contrib.auth import models as pmod



@view_function
def process_request(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            searchTerm = form.cleaned_data['userInput']   
            # p1 = pmod.Permission.objects.get(id=1)
            # a1 = hmod.overdoses.objects.filter(abbrev = 'UT')
            # searchTerm = a1.abbrev
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
