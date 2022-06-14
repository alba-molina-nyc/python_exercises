"""

def home(request):
    latest_translation_question_list = Translation_Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('home.html')
    context = {
        'latest_translation_question_list': latest_translation_question_list,
    }
    
    return HttpResponse(template.render(context, request))


    
That code loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects.
"""