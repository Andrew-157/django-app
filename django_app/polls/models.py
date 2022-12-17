from django.db import models


class Question(models.Model):

    question_text = models.CharField(max_length=128)
    published_at = models.DateTimeField('published at')


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
    is_valid = models.BooleanField(default=False)


class Results(models.Model):

    result = models.IntegerField(default=0)
