from django.conf.urls import url

from .views import SignUp, SignIn, SignOut

app_name = 'Profile'
urlpatterns = [
    url(r'^signup/', SignUp.as_view(), name='sign_up'),
    url(r'^signin/$', SignIn.as_view(), name='sign_in'),
    url(r'^signout/$', SignOut.as_view(), name='sign_out'),
]