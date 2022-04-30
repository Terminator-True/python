from django.http import *
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
#Models
from .models import Choice, Question


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'vistes/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'vistes/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'vistes/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'vistes/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


"""
def index(request):
    Vistes no genériques
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = '| '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'vistes/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'vistes/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vistes/results.html', {'question': question})
"""