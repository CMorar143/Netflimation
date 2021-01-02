from django import forms
from django.contrib.auth.models import User, Group

COLORS = (
	('white', 'White'),
	('red', 'Red'),
	('orange', 'Orange'),
	('yellow', 'Yellow'),
	('cyan', 'Aqua'),
	('green', 'Green'),
	('blue', 'Blue'),
	('purple', 'Purple'),
	('pink', 'Pink')
)

class Search(forms.Form):
	ping = forms.ModelChoiceField(queryset=Group.objects.all(), initial=0, widget=forms.Select(attrs={'class': 'input_field login_input'}))
	to_color = forms.ChoiceField(choices=COLORS, initial='red', widget=forms.Select(attrs={'class': 'input_field login_input'}))
	from_color = forms.ChoiceField(choices=COLORS, initial='cyan', widget=forms.Select(attrs={'class': 'input_field login_input'}))
