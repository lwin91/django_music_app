from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	# ex: /music/5/
    path('<int:song_id>/', views.detail, name='detail'),
    # ex: /music/5/results/
    path('<int:song_id>/results/', views.results, name='results'),
    # ex: /music/5/view/
    path('<int:song_id>/view/', views.view, name='view'),
]