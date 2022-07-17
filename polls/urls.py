from django.urls import path
from django.http import HttpResponse

from . import views

def string_testing(request, test_string: str):
    return HttpResponse(test_string.upper())

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<str:test_string>/', string_testing, name='string testing')
]