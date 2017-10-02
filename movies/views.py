from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse
from django.db.models import Avg
from django.utils.decorators import method_decorator

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.generic import (
        ListView, 
        CreateView, 
        DetailView,
        UpdateView,
        DeleteView, 
    )
from django.views.generic.edit import FormMixin

from .forms import MovieForm, ReviewForm
from .models import Movie, Review
from .serializers import MovieSerializer

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
        
class MovieUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'staff_member_required'
    login_url = 'Profile:sign_in'
    model = Movie
    form_class = MovieForm

    def handle_no_permission(self):
        messages.error(self.request, 'Only member of staff can update movies')
        return super(MovieUpdate, self).handle_no_permission()

class MovieDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'staff_member_required'
    login_url = 'Profile:sign_in'
    model = Movie
    success_url = reverse_lazy('Movie:list')

    def handle_no_permission(self):
        messages.error(self.request, 'Only member of staff can delete movies')
        return super(MovieDelete, self).handle_no_permission()

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

# Movies API views 

class MovieAPIList(ListAPIView):
    queryset = Movie.objects.all() 
    serializer_class = MovieSerializer

class MovieAPIDetail(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"

# Review views

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
