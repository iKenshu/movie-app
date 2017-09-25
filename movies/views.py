from django.shortcuts import render, redirect 
from django.core.urlresolvers import reverse
from django.db.models import Avg

from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin

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

class MovieDetail(FormMixin, DetailView):
    model = Movie
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('Movie:detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        movie = Movie.objects.get(slug=slug) 
        context['rating'] = Review.objects.filter(movie=movie).aggregate(Avg('rating'))
        context['form'] = ReviewForm(initial={'movie': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
       form.instance.user = self.request.user
       form.instance.movie = Movie.objects.get(slug=self.kwargs['slug'])
       form.save()
       return super(MovieDetail, self).form_valid(form)

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    