from django.shortcuts import render, redirect 
from django.core.urlresolvers import reverse

from django.views.generic import ListView, CreateView, DetailView

from .forms import MovieForm, ReviewForm
from .models import Movie, Review

# Create your views here.

class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'

class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return redirect('Movie:list')

class MovieDetail(DetailView):
    model = Movie

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('Movie:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.movie = Movie.objects.get(slug=self.kwargs['slug'])
        form.save()
        return super(ReviewCreate, self).form_valid(form)