from django.shortcuts import render, get_object_or_404
from movie.models import Act, Actor, Movie

# Create your views here.
def detail(request, actorid):
    actor = get_object_or_404(Actor, actorid= actorid)
    movies = Movie.objects.filter(act__actorid=actorid)
    return render(request, 'cast-detail.html', locals())