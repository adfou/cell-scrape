from django.urls import path

from . import views

urlpatterns = [
    #path('result/', views.vote, name='vote'),
    #path('fuq/', views.vote, name='vote'),
    path('', views.index, name='index'),
       # ex: /polls/5/
    path('<int:paragraph_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:paragraph_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:paragraph_id>/vote/', views.paragraph_Qayan, name='vote'),
]