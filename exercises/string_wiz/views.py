from django.http import HttpResponse
from django.shortcuts import loader
from .models import Translation_Question



# Create your views here.

def home(request):
    latest_translation_question_list = Translation_Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('home.html')
    context = {
        'latest_translation_question_list': latest_translation_question_list,
    }
    
    return HttpResponse(template.render(context, request))

def detail(request, Translation_Question_id):
    response = "You are 👀 at where the user is going to enter their ❓ #️⃣ %s before it is translated from 💂🏻‍♀️ English 💂🏻‍♀️ ➡️ 🐽Pig Latin🐽"
    return HttpResponse(response % Translation_Question_id)

def pig_latinfied(request, Translation_Question_id):
    response = "You are 👀 at where the translation is going to go for ❓ #️⃣ %s, from 💂🏻‍♀️ English 💂🏻‍♀️ ➡️ 🐽Pig Latin🐽"
    return HttpResponse(response % Translation_Question_id)