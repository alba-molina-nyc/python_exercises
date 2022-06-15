from urllib import response
from django.shortcuts import get_object_or_404
from .models import Translation_Question, Translation_Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader



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

# def pig_latinfied(request, Translation_Question_id):
#     response = "You are 👀 at where the translation is going to go for ❓ #️⃣ %s, from 💂🏻‍♀️ English 💂🏻‍♀️ ➡️ 🐽Pig Latin🐽"
#     return HttpResponse(response % Translation_Question_id)

# , Translation_Question_id
def enter_word(request):
    template = loader.get_template('enter_word.html')
    context = {}
    return HttpResponse(template.render(context, request))


    # translation_question_text = get_object_or_404(Translation_Question, pk=Translation_Question_id)
    # try:
    #     selected_translation = Translation_Question.translation_set_answer.get(pk=request.POST['translation_answer'])
    # except (KeyError, Translation_Answer.DoesNotExist):
    #     return render(request, 'details.html', {
    #         'translation_question_text' : translation_question_text,
    #         'error_message': "Sorry we could not find that word",
    #     })
    # else:
    #     selected_translation.save()
    #     return HttpResponseRedirect(reverse(), args=(translation_question_text.id,))




#  try:
#         selected_translation = Translation_Question.translation_answer.get(pk=request.POST['translation_question_text'])
#     except (KeyError, translation_question_text.DoesNotExist):
#         return render(request, 'details.html', {
#             'translation_question_text' : translation_question_text,
#             'error_message': "Sorry we could not find that word"
#         })
#     else:
#         selected_translation.save()
#         return HttpResponseRedirect(reverse(results), args=(translation_question_text.id,))