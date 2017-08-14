from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from polls.models import Category, Question, Choice
from django.core.urlresolvers import reverse_lazy
from polls.forms import CategoryCreateForm, QuestionCreateForm, ChoiceCreateForm


class CategoryListView(ListView):

    model = Category
    template_name = "category_list.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context


class CategoryCreateView(CreateView):

    template_name = "category_create.html"
    form_class = CategoryCreateForm

    success_url = reverse_lazy('main_page')


class CategoryDetailView(DetailView):

    model = Category
    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['a'] = Question.objects.all()
        return context


class QuestionListView(ListView):

    model = Question
    template_name = "question_list.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        return context


class QuestionCreateView(CreateView):

    template_name = "question_create.html"
    form_class = QuestionCreateForm

    success_url = reverse_lazy('main_page')


class ChoiceListView(ListView):

    model = Choice
    template_name = "choice_list.html"

    def get_context_data(self, **kwargs):
        context = super(ChoiceListView, self).get_context_data(**kwargs)
        return context


class ChoiceCreateView(CreateView):

    template_name = "choice_create.html"
    form_class = ChoiceCreateForm

    success_url = reverse_lazy('main_page')


