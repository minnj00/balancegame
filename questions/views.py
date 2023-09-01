from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    return render(request, 'index.html')

def question(request):
    twoquestion = Question.objects.get(id=1)

    context = {
        'twoquestion': twoquestion
    }

    return render(request, 'question_show.html', context)