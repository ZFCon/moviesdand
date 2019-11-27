from django.shortcuts import render, redirect
from movie.models import Movie
from search.utils import chunks

# Create your views here.
def red(request):
    return redirect('index', id=1)

def index(request, id):
    pages = 0
    if Movie.objects.order_by('-year').exists():
        item = Movie.objects.order_by('-year')
        chun = list(chunks(item, 20))
        pages = len(chun)
        items = chun[id-1]
    return render(request, 'index.html', locals())