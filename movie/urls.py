from django.urls import path
from .views import *

urlpatterns = [
    path('<movieid>', detail, name='detail'),
    path('watch/<movieid>', watch, name='watch'),
    path('request/<movieid>', requested, name='request'),
    path('lucky/', lucky, name='lucky'),
]
