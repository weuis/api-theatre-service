from django.urls import path
from theatre_service.views import (
   GenreList,
   GenreDetail,
   ActorList,
   ActorDetail,
   PlayList,
   PlayDetail,
)



urlpatterns = [
   path("genre/", GenreList.as_view(), name="genre-list"),
   path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
   path('actors/', ActorList.as_view(), name='actor-create'),
   path('actors/<int:pk>/', ActorDetail.as_view(), name='actor-detail'),
   path('plays/', PlayList.as_view(), name='play-list-create'),
   path('plays/<int:pk>/', PlayDetai.as_view(), name='play-detail'),
]

app_name = "theatre_service"