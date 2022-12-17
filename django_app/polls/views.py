from django.shortcuts import render

from .models import Question, Choice


def index(request):

    question_list = Question.objects.order_by('-published_at')[:10]
    context = {'question_list': question_list}

    return render(request, 'polls/index.html', context)


def poll(request, poll_id):

    question = Question.objects.get(pk=poll_id)
    choices = Choice.objects.filter(question=poll_id)

    context = {'question': question, 'choices': choices}

    return render(request, 'polls/question.html', context)
