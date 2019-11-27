from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.db.models import Q
from .models import Act, Movie, Actor, Frame, Comment
from random import choice
from .forms import CommentForm
from .utils import *

# Create your views here.
def detail(request, movieid):
    movie = get_object_or_404(Movie, movieid=movieid)
    cast = Actor.objects.filter(act__movieid=movieid)
    watch = Frame.objects.filter(movieid = movieid).exists()
    rating = {'rate':movie.rate, 'rating': movie.rate*10}
    star = int(movie.rate)
    stars=[]
    for a in range(10):
        if star != 0:
            stars.append(1)
            star -= 1
        else:
            stars.append(0)
    rating['stars'] = stars
    genres = movie.genres.split('|')
    view(movieid)
    return render(request, 'movie-detail.html', locals())

def requested(request, movieid):
    item = get_object_or_404(Movie, movieid=movieid)
    item.requested += 1
    item.save()
    return redirect('movie:detail', movieid=movieid)

def watch(request, movieid):
    frames = get_list_or_404(Frame, movieid = movieid)
    forms = CommentForm()
    movie = get_object_or_404(Movie, movieid = movieid)
    related = Movie.objects.filter(Q(genres__in = movie.genres.split('|')))[:4]

    if Comment.objects.filter(movieid = movieid).exists():
        comments = Comment.objects.filter(movieid = movieid)

    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            comment = forms.cleaned_data.get('comment')
            new_comment = Comment(comment=comment, movieid=Movie(movieid=movieid))
            new_comment.save()
    return render(request, 'movie-watching.html', locals())

def lucky(request):
    return redirect('movie:detail', movieid= choice(Movie.objects.all()).movieid)