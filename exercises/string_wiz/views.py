from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html', {})

def detail(request, Translation_Question_id):
    response = "you are looking at the results for question %s."
    return HttpResponse(Translation_Question_id)