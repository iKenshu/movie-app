from django.test import TestCase
from django.contrib.auth.models import User

from .models import Movie


class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='ikenshu', password='12345')
        test_user.save()
        Movie.objects.create(
            title='Get Out',
            synopsis='wow movie',
            slug='get-out',
            created_by=test_user
        )

    def test_title_max_lenght(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('title').max_length
        self.assertEquals(max_length, 140)

    def test_slug(self):
        movie = Movie.objects.get(id=1)
        self.assertEquals(movie.slug, 'get-out')
