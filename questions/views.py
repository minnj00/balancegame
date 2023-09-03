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

    return render(request, 'answer_question.html', context)

@login_required
def random_question(request):
    total_questions = Question.objects.count()
    if total_questions == 0:
        # Handle case with no questions in the database
        return redirect('questions:index')  # Or some other appropriate action

    random_id = random.randint(1, total_questions)
    return redirect('questions:question_show', id=random_id)


def answer_question(request,id, answer_id):
    if request.method == "POST":
        answer = answer_id
        question = Question.objects.get(id=id)
        user = request.user
        if answer in [0, 1]:
            UserAnswer.objects.create(answer=answer, question=question, user=user)
            return redirect('questions:answer_statistics', id=question.id)  # Redirect to some success page or the same page
        else:
            # Handle the error. Maybe display a message to the user.
            twoquestion = question
        context={
            'twoquestion': twoquestion,
        }
 

    return render(request, 'answer_question.html', context)



def answer_statistics(request, id):
    total_answers = UserAnswer.objects.filter(question_id=id).count()
    questions = Question.objects.get(id=id)

    if total_answers == 0:
        context = {
            'questions': questions,
            'total_answers': total_answers,
            'count_0': count_0,
            'count_1': count_1,
            'percentage_0': 0,
            'percentage_1': 0
        }
    else:
        count_0 = UserAnswer.objects.filter(question_id=id, answer=0).count()
        count_1 = UserAnswer.objects.filter(question_id=id, answer=1).count()

        percentage_0 = int((count_0 / total_answers) * 100)
        percentage_1 = int((count_1 / total_answers) * 100)

        context = {
            'questions': questions,
            'count_0': count_0,
            'count_1': count_1,
            'total_answers': total_answers,
            'percentage_0': percentage_0,
            'percentage_1': percentage_1
        }

    return render(request, 'statistics.html', context)

