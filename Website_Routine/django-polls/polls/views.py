from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Question,Choice
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  #最近的5个投票问题
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html', context)

    #template = loader.get_template('polls/index.html')
    #context = {
    #        'latest_question_list': latest_question_list,
    #    }
    #return HttpResponse(template.render(context,request))

    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("QUestion does not exist")
    #return render(request, 'polls/detail.html', {'question':question})

    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    #return HttpResponse("You're looking at the results of question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    #response = "You're voting on question %s." 
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
            })
        #raise Http404("QUestion does not exist")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpReponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice 
        # user hits the back button.
        #raise Http404("QUestion does not exist")

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))#多个参数，用户将要被重定向的URL


from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
