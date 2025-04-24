from django.urls import path
from theatre_service.views import (
   GenreList,
   GenreDetail,
   ActorList,
   ActorDetail,
   PlayList,
   PlayDetail,
   TheatreHallList,
   TheatreHallDetail,
   PerformanceList,
   PerformanceDetail,
   ReservationList,
   ReservationDetail
)



urlpatterns = [
   path("genre/", GenreList.as_view(), name="genre-list"),
   path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
   path('actors/', ActorList.as_view(), name='actor-create'),
   path('actors/<int:pk>/', ActorDetail.as_view(), name='actor-detail'),
   path('plays/', PlayList.as_view(), name='play-list-create'),
   path('plays/<int:pk>/', PlayDetail.as_view(), name='play-detail'),
   path('theatrehalls/', TheatreHallList.as_view(), name='theatrehall-list'),
    path('theatrehalls/<int:pk>/', TheatreHallDetail.as_view(), name='theatrehall-detail'),
    path('performances/', PerformanceList.as_view(), name='performance-list'),
    path('performances/<int:pk>/', PerformanceDetail.as_view(), name='performance-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
]

app_name = "theatre_service"