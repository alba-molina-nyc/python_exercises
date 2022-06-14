from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html', {})

def detail(request, Translation_Question_id):
    response = "You are 👀 at where the user is going to enter their ❓ #️⃣ %s before it is translated from 💂🏻‍♀️ English 💂🏻‍♀️ ➡️ 🐽Pig Latin🐽"
    return HttpResponse(response % Translation_Question_id)

def pig_latinfied(request, Translation_Question_id):
    response = "You are 👀 at where the translation is going to go for ❓ #️⃣ %s, from 💂🏻‍♀️ English 💂🏻‍♀️ ➡️ 🐽Pig Latin🐽"
    return HttpResponse(response % Translation_Question_id)