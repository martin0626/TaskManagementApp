from django.urls import path

from .views import RegisterApiView, LoginApiView, LogoutApiView

urlpatterns = (
    path('signUp/', RegisterApiView.as_view(), name='api register user'),
    path('signIn/', LoginApiView.as_view(), name='api login user'),
    path('signOut/', LogoutApiView.as_view(), name='api logout user'),
)