from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    MovieList,
    MovieCreate,
    MovieDetail,
    MovieUpdate,
    MovieDelete,
    ReviewCreate,

    MovieAPIList,
    MovieAPIDetail
)

app_name = 'Movie'
urlpatterns = [
    url(
        regex='^$',
        view=MovieList.as_view(),
        name='list'),
    url(
        regex='^create/',
        view=MovieCreate.as_view(),
        name='create'),
    url(
        regex='^movie/(?P<slug>[\w-]+)/$',
        view=MovieDetail.as_view(),
        name='detail'),
    url(
        regex='^movie/(?P<slug>[\w-]+)/edit$',
        view=MovieUpdate.as_view(),
        name='update'),
    url(
        regex='^movie/(?P<slug>[\w-]+)/delete$',
        view=MovieDelete.as_view(),
        name='delete'),
    url(
        regex='^movie/review/(?P<slug>[\w-]+)/$',
        view=ReviewCreate.as_view(),
        name='review'),

    url(
        regex='^api/movies/$',
        view=MovieAPIList.as_view(),
        name='api_list'),
    url(
        regex='^api/movies/(?P<slug>[\w-]+)/$',
        view=MovieAPIDetail.as_view(),
        name='api_detail'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
