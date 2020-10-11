from django.core.management.base import BaseCommand
import json
from ...models import Movie, Genre


class Command(BaseCommand):
    help = "Uploads Movie list"

    def handle(self, *args, **options):
        with open('imdb.json') as f_obj:
            movie_details = json.load(f_obj)

        for movie in movie_details:
            m, _ = Movie.objects.get_or_create(
                name=movie.get("name"),
                director=movie.get("director"),
                imdb_score=movie.get("imdb_score"),
                popularity=movie.get("99popularity"),
            )
            for gen in movie.get("genre"):
                g, _ = Genre.objects.get_or_create(name=gen.strip())
                m.genre.add(g)
            m.save()

        # movie_list = []
        #     movie_list.append(Movie(
        #         director=movie.get("director"),
        #         imdb_score=movie.get("imdb_score"),
        #         name=movie.get("name"),
        #         popularity=movie.get("99popularity"),
        #         genre=Movie.genre.add(*movie.get("genre"))
        #         #genre=movie.get("genre"),
        #     ))
        # Movie.objects.bulk_create(movie_list)
