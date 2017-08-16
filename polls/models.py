import datetime
from django.db import models
from datetime import datetime


class Category(models.Model):

    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):

    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now)
    question_category = models.ForeignKey(Category, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

