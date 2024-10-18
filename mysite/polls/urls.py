
from django.urls import path
from . import views

app_name = 'polls'  

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('question/new/', views.question_view, name='question_new'),
    path('choice/new/', views.choice_view, name='choice_new'),]
