from django import forms
from django.contrib.auth.models import User, Group

class Search(forms.Form):
	search_input = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_field login_input'}))
