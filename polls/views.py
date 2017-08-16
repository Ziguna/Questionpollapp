from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from polls.models import Category, Question, Choice
from django.core.urlresolvers import reverse_lazy
from polls.forms import CategoryCreateForm, QuestionCreateForm, ChoiceCreateForm
from django.shortcuts import get_object_or_404


class CategoryListView(ListView):

    model = Category
    template_name = "category_list.html"


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


class CategoryDeleteView(DeleteView):

    '''
    Used to delete the movie and return it to the main page.
    '''
    model = Category
    template_name = "delete_category.html"
    field = [
    ]
    success_url = reverse_lazy('main_page')


class QuestionListView(DetailView):

    model = Question
    template_name = "choice_list.html"
    form_class = QuestionCreateForm

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        k = self.kwargs["pk"]
        #context["p"] = Question.objects.get(id=k)

        return context


class QuestionCreateView(CreateView):

    template_name = "question_create.html"
    form_class = QuestionCreateForm

    success_url = reverse_lazy('main_page')

    def get_initial(self):
        initial = super().get_initial()
        initial['question_category'] = self.kwargs["pk"]

        return initial


class QuestionUpdateView(UpdateView):
    '''
    Used to update the name, description, relesed date of the particular movie in this section
    '''
    model = Question
    template_name = "question_create.html"
    form_class = QuestionCreateForm

    success_url = reverse_lazy('main_page')


class QuestionDeleteView(DeleteView):

    '''
    Used to delete the movie and return it to the main page.
    '''
    model = Question
    template_name = "delete_question.html"
    field = [
    ]
    success_url = reverse_lazy('main_page')


class ChoiceListView(ListView):

    model = Choice
    template_name = "choice_list.html"

    def get_context_data(self, **kwargs):
        context = super(ChoiceListView, self).get_context_data(**kwargs)
        context['c'] = Choice.objects.all()
        return context


class ChoiceCreateView(CreateView):

    template_name = "choice_create.html"
    form_class = ChoiceCreateForm

    success_url = reverse_lazy('main_page')


class DisplayVoteResult(DetailView):

    model = Choice
    template_name = "display_result.html"

    def get_context_data(self, **kwargs):

        context = super(DisplayVoteResult, self).get_context_data(**kwargs)
        m = self.kwargs["pk"]
        question = get_object_or_404(Question, id=m)
           
        try:
            selected_choice = question.choice_set.get(id=self.request.GET['choice'])
            context["n"] = Question.objects.get(id=m)
            selected_choice.votes += 1
            selected_choice.save()

            return context

        except Exception:

            context['n'] = Question.objects.get(id=m)
            context['Message'] = "Please Select or Create Choice first"
 
            return context



  