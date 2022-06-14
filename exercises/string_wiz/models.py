from django.db import models

# Create your models here.

class Translation_Question(models.Model):
    translation_question_text = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date published')

class Translation_Answer(models.Model):
    translation_question_text = models.ForeignKey(Translation_Question, on_delete=models.CASCADE, default=0)
    translation_answer_text = models.CharField(max_length=10000)
