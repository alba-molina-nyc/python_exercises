from django.db import models
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Translation_Question(models.Model):
    translation_question_text = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.translation_question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Translation_Answer(models.Model):
    translation_question_text = models.ForeignKey(Translation_Question, on_delete=models.CASCADE, default=0)
    translation_answer_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.translation_answer_text
