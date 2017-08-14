from django import forms
from .models import Category, Question, Choice


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'question_category')


class ChoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')
# Create your views here.

