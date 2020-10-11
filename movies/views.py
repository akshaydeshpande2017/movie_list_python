from . import models as movie_models
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer


class FetchMovies(APIView):
    def get(self, request, *args, **kwargs):
        if len(request.GET.keys()) > 0:
            filters = {
                "director": request.GET.get("Director"),
                "name": request.GET.get("Movie"),
                "imdb_score": request.GET.get("imdb_rating"),
                "genre": request.GET.getlist("Genre")
            }
            movie_list = movie_models.Movie.objects.filter_movies(filters)
        else:
            movie_list = movie_models.Movie.objects.all()
        return Response(MovieSerializer(movie_list, many=True).data)
