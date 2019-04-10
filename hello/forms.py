from django import forms


class SearchForm(forms.Form):
    userInput = forms.CharField(label='Search Term')