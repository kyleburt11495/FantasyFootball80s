from django.shortcuts import render
import json

# Create your views here.
def login(request):
	return render(request, 'login.html')
  
def draft(request):
    return render(request, 'base.html')