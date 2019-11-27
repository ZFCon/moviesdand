from django.shortcuts import render
from django.db.models import Q
from movie.models import Movie
from .utils import chunks

# Create your views here.
def movie(request, id):
    dic = request.GET
    q = dic.get('q', None)
    if q is not None:
        lookups = Q(title__icontains = q) | Q(year__icontains = q)
        item = Movie.objects.filter(lookups).distinct()
        pages = 0
        if item.exists():
            chun = list(chunks(item, 20))
            pages = len(chun)
            items = chun[id-1]
    return render(request, 'search.html', locals())

def genre(request, genre, id):
    lookups = Q(genres__icontains = genre)
    item = Movie.objects.filter(lookups).order_by('-year')
    pages = 0
    if item.exists():
        chun = list(chunks(item, 20))
        pages = len(chun)
        items = chun[id-1]
    return render(request, 'genre.html', locals())

    