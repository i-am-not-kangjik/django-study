from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": lastest_question_list,
    }
    print('request = ', request)
    print('context = ', context)
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def votes(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
