from django.urls import path
from . import views

app_name = 'polls'

###### Thi swas the hard way to write code
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results', views.result, name='result'),
#     path('<int:question_id>/vote', views.vote, name= 'vote')
# ]

#######33this is the shortcut provided by django
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote', views.vote, name= 'vote')
]