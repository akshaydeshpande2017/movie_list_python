from . import models as movie_models
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer


class FetchMovies(APIView):
    def get(self, request, *args, **kwargs):
        movie_list = movie_models.Movie.objects.all()

        if request.GET.get("Director"):
            movie_list = movie_list.filter(director__icontains=request.GET.get("Director"))
        if request.GET.get("Movie"):
            movie_list = movie_list.filter(name__icontains=request.GET.get("Movie"))
        if request.GET.get("Genre"):
            movie_list = movie_list.filter(genre__name__icontains=request.GET.get("Genre"))
        if request.GET.get("imdb_rating"):
            movie_list = movie_list.filter(genre__name__icontains=request.GET.get("imdb_rating"))
        return Response(MovieSerializer(movie_list, many=True).data)
