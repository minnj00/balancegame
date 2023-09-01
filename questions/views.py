from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, UserAnswer
import random
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def question(request,id):
    twoquestion = get_object_or_404(Question, id=id)

    context = {
        'twoquestion': twoquestion
    }

    return render(request, 'question_show.html', context)

@login_required
def random_question(request):
    total_questions = Question.objects.count()
    if total_questions == 0:
        # Handle case with no questions in the database
        return redirect('questions:index')  # Or some other appropriate action

    random_id = random.randint(1, total_questions)
    return redirect('questions:question_show', id=random_id)


def answer_question(request):
    if request.method == "POST":
        answer = request.POST.get('answer')
        if answer in ['0', '1']:
            UserAnswer.objects.create(answer=answer)
            return redirect('some_success_url')  # Redirect to some success page or the same page
        else:
            # Handle the error. Maybe display a message to the user.
            pass

    return render(request, 'answer_question.html')

