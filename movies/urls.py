from django.urls import path

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
    MovieAPIDetail,
)

app_name = "Movie"
urlpatterns = [
    path(route="", view=MovieList.as_view(), name="list"),
    path(route="create/", view=MovieCreate.as_view(), name="create"),
    path(
        route="movie/<slug:slug>/", view=MovieDetail.as_view(), name="detail"
    ),
    path(
        route="movie/<slug:slug>/edit/",
        view=MovieUpdate.as_view(),
        name="update",
    ),
    path(
        route="movie/<slug:slug>/delete/",
        view=MovieDelete.as_view(),
        name="delete",
    ),
    path(
        route="movie/review/<slug:slug>/",
        view=ReviewCreate.as_view(),
        name="review",
    ),
    path(route="api/movies/", view=MovieAPIList.as_view(), name="api_list"),
    path(
        route="api/movies/<slug:slug>/",
        view=MovieAPIDetail.as_view(),
        name="api_detail",
    ),
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
