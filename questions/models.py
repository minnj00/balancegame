from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    question_a = models.TextField()
    question_b = models.TextField()
    