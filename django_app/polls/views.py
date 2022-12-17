from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question


def index(request):

    template = loader.get_template('polls/index.html')

    question_list = Question.objects.order_by('-published_at')[:10]

    return HttpResponse(template.render({'question_list': question_list}, request))


def poll(request, poll_id):

    return HttpResponse(f'Poll: {poll_id}')
