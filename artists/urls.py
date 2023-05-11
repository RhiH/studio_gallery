from django.urls import path
from . import views

urlpatterns = [
    path('', views.artists, name='artists'),
    path('', views.all_artists, name='all_artists'),
]
