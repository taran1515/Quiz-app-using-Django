# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
from django.http import HttpResponse
# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  choice = []
  ques = Question.objects.all()
  length = len(ques)
  que = []
  for i in range(length):
    que.append(ques[i])


  return render(request, 'home.html',{
    'question':que,
    'length':length,
    'choice':choice
  })


@login_required
def submit(request):
  return render(request, 'submit.html')

@login_required
def skip(request):
  return render(request, 'skip.html')