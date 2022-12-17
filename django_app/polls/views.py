from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate as auth
from django.contrib.auth import logout as lo

from .models import Question, Choice


def create_user(request):

    permission = Permission.objects.create(
        codename='super_mega_admin', name='Super Mega Admin', content_type_id=1)
    user = User.objects.create_user(username='senator',
                                    email='usa_top@gmail.com',
                                    password='love_democracy')

    return HttpResponse('Success!')


def authenticate(request):

    get_object_or_404(User, username='jack')

    user = auth(username='jack', password='password')

    if not user:
        return HttpResponse('Invalid')

    return HttpResponse('Success!')


def index(request):

    question_list = Question.objects.order_by('-published_at')[:10]
    context = {'question_list': question_list}

    if request.user.is_authenticated and request.user.has_perm('polls.super_mega_admin'):
        return render(request, 'polls/index.html', context)
    else:
        return HttpResponse('Invalid Index')


def poll(request, poll_id):

    question = Question.objects.get(pk=poll_id)
    choices = Choice.objects.filter(question=poll_id)

    context = {'question': question, 'choices': choices}

    return render(request, 'polls/question.html', context)


def results(request):

    choice_id = request.POST['choice']
    choice = Choice.objects.get(pk=choice_id)

    if not choice.is_valid:
        return HttpResponse('Incorrect')

    return HttpResponse('Correct')


def logout(request):

    lo(request)
