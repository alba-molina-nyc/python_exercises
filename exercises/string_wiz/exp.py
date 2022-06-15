from django.shortcuts import get_object_or_404, render
from .models import Translation_Question, Translation_Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
def enter_word(Translation_Question_id):
    translation_question_text = get_object_or_404(Translation_Question, pk=Translation_Question_id)
    print(translation_question_text)