from django.contrib import admin

from .models import Movie, Review

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'synopsis', 'director')
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'comment')