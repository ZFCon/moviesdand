from .models import Movie

def view(movieid):
    obj = Movie.objects.get(movieid=movieid)
    obj.views += 1
    obj.save()