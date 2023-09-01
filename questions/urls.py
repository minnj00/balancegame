from django.urls import path
from questions import views


app_name = 'questions'

urlpatterns=[
    path('', views.index, name='index'),
    path('question/random/', views.random_question, name='random_question'),
    path('question/<int:id>/', views.question, name='question_show'),
    path('answer/', views.answer_question, name='answer_question'),
]

