from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    question_a = models.TextField()
    question_b = models.TextField()

class UserAnswer(models.Model):
    ANSWER_CHOICES = [
        (0, '0'),
        (1, '1'),
    ]
    answer = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
