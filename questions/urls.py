from django.urls import path
from questions import views


app_name = 'questions'

urlpatterns=[
    path('', views.index, name='index'),
    path('question/1/', views.question, name='question_show'),
]