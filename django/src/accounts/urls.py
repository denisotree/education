from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    login_view,
    register_view,
    RegistrationView,
    AccountLoginView
)

app_name = 'accounts'

urlpatterns = [
    path('', AccountLoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
