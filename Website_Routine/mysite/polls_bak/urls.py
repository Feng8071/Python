from django.urls import path

from . import views
#form views.py import index

app_name = 'polls'
urlpatterns = [
#    path('', views.index, name='index'),    
#     path('', vm.index, name='index'),  
    ## ex: /polls/5
    #path('<int:question_id>/', views.detail, name='detail'),
    ## ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    ## ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),

    #改进版
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
