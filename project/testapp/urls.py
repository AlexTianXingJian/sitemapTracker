from django.urls import path
from.views import displayTest


urlpatterns = [
    path('', displayTest),
]