from .views import *
from django.urls import path


urlpatterns = [
    path('', LandingPage.as_view(), name='landing-page')
]
