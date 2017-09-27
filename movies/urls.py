from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import (MovieList, 
                    MovieCreate, 
                    MovieDetail, 
                    ReviewCreate,

                    MovieAPIList,
                    MovieAPIDetail
                )

app_name = 'Movie'
urlpatterns = [
    url(r'^$', MovieList.as_view(), name='list'),
    url(r'^create/', MovieCreate.as_view(), name='create'),
    url(r'^movie/(?P<slug>[\w-]+)/$', MovieDetail.as_view(), name='detail'),
    url(r'^movie/review/(?P<slug>[\w-]+)/$', ReviewCreate.as_view(), name='review'),

    url(r'^movies/$', MovieAPIList.as_view(), name='api_list'),
    url(r'^movies/(?P<slug>[\w-]+)/$', MovieAPIDetail.as_view(), name='api_detail'),

] 

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)