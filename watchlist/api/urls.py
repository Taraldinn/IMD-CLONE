from django.urls import path, include

from watchlist.api.views import StreamPlatformAV, movie_details, movie_list, StreamDetailAV

urlpatterns = [
    path('movie/', movie_list.as_view(), name='movie-list'),
    path('movie/<int:pk>/', movie_details.as_view(), name='movie-details'),
    path('ott/', StreamPlatformAV.as_view(), name='stream'),
    path('ott/<int:pk>', StreamDetailAV.as_view(), name='streamplatform-detail')

]
