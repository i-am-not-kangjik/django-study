from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in lastest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def votes(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
