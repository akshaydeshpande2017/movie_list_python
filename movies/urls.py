from django.urls import path
from . import views

urlpatterns = [
    path('search', views.FetchMovies.as_view()),
]
