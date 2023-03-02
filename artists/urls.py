from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artists, name='artists'),
    #path('<artist_id>', views.artists_detail, name='artist_detail'),
]
