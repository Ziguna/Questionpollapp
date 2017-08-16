from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from polls.models import Category, Question, Choice
from django.core.urlresolvers import reverse_lazy
from polls.forms import CategoryCreateForm, QuestionCreateForm, ChoiceCreateForm
from django.shortcuts import get_object_or_404


class CategoryListView(ListView):
    '''
    Shows up all the list of question categories in the main page.
    '''
    model = Category
    template_name = "category_list.html"


class CategoryCreateView(CreateView):
    '''
    Used to create a new question category.
    '''
    template_name = "category_create.html"
    form_class = CategoryCreateForm

    success_url = reverse_lazy('main_page')


class CategoryDetailView(DetailView):
    '''
    Used to show the list of all the questions in the particular category.
    '''
    model = Category
    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['a'] = Question.objects.all()
        context['total_question'] = Question.objects.filter(question_category__name=self.object.name).count()
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
    '''
    Displays the particular selected question
    '''
    model = Question
    template_name = "choice_list.html"
    form_class = QuestionCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         
        return context


class QuestionCreateView(CreateView):
    '''
    Used to create a new question in a particular catergory
    and get_initial method is used to set the initial value of the question.
    and pass the id to the question_category.
    '''

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
    '''
    Use to show the list of all the choices in the particular question of the certain category.
    '''

    model = Choice
    template_name = "choice_list.html"

    def get_context_data(self, **kwargs):
        context = super(ChoiceListView, self).get_context_data(**kwargs)
        context['c'] = Choice.objects.all()

        return context


class ChoiceCreateView(CreateView):
    '''
    Use to add or create a new choice in a certain question.
    get_initial method is used to get the initial id and keep the id in the 'question'.
    '''

    template_name = "choice_create.html"
    form_class = ChoiceCreateForm

    success_url = reverse_lazy('main_page')

    def get_initial(self):
        initial = super().get_initial()
        initial['question'] = self.kwargs["pk"]

        return initial


class DisplayVoteResult(DetailView):
    '''
    Display the voting results of a certain question.
    '''

    model = Choice
    template_name = "display_result.html"

    def get_context_data(self, **kwargs):

        context = super(DisplayVoteResult, self).get_context_data(**kwargs)
        m = self.kwargs["pk"]
        question = get_object_or_404(Question, id=m)  # Prints the particular question if id=m
        try:
            selected_choice = question.choice_set.get(id=self.request.GET['choice'])  # Prints the selected choice
            context["n"] = Question.objects.get(id=m)  # Prints the particular question
            selected_choice.votes += 1  # increase the number of votes
            selected_choice.save()

            return context

        except Exception:

            context['n'] = Question.objects.get(id=m)
            context['Message'] = "Please Select or Create Choice first"

            return context



 