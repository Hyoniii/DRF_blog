from django.urls import include, path
from rest_framework import urls

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view())
]
