from django.conf.urls import url

from .views import SignUp, SignIn, SignOut

app_name = 'Profile'
urlpatterns = [
    url(
        regex='^signup/',
        view=SignUp.as_view(),
        name='sign_up'
    ),
    url(
        regex='^signin/$',
        view=SignIn.as_view(),
        name='sign_in'
    ),
    url(
        regex='^logout/$',
        view=SignOut.as_view(),
        name='sign_out'
    ),
]
