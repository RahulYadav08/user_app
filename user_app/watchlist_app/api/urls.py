from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail

from watchlist_app.api.views import WatchListAV, MovieDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    # path('list/', movie_list, name = 'movie-list'),
    # path('<int:pk>', movie_detail, name = 'movie-detail'),
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name = 'movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name = 'stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'movie-detail'),
]