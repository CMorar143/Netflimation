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
		

		return render(request, self.template_name)