from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=140)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to="posters")
    director = models.CharField(max_length=140)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=140)

    class Meta:
        ordering = ["-created_by"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.comment
