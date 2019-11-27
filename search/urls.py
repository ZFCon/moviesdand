from django.urls import path
from .views import *

urlpatterns = [
    path('movie/<int:id>', movie, name='movie'),
    path('genre/<genre>/<int:id>', genre, name='genre')
]
