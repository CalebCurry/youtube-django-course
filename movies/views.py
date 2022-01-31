from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})