from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):

    question_list = Question.objects.order_by('-published_at')[:10]
    context = {'question_list': question_list}

    return render(request, 'polls/index.html', context)


def poll(request, poll_id):

    return HttpResponse(f'Poll: {poll_id}')
