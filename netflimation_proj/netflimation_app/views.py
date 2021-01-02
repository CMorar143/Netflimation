from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from netflimation_app.forms import Search
from django.urls import reverse
import requests
import json

# Create your views here.
class home(TemplateView):
	template_name = "index.html"

	def get(self, request):
		if request.user.is_authenticated:
			return redirect("search")
		else:
			return redirect("account_login")

		return render(request, self.template_name)



class search(TemplateView):
	template_name = "search.html"

	def get(self, request):
		search = Search()
		return render(request, self.template_name, {'search': search, 'results': None})

	def post(self, request):
		search = Search(request.POST)

		if search.is_valid():
			title = search.cleaned_data['search_input']
			print(title)
			return render(request, self.template_name, {'search': search, 'results': title})

		else:
			print("not valid")
			return render(request, self.template_name, {'search': search, 'results': None})