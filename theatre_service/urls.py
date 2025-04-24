from django.urls import path
from theatre_service.views import (
   GenreList,
   GenreDetail,
   ActorList,
   ActorDetail,
)



urlpatterns = [
   path("genre/", GenreList.as_view(), name="genre-list"),
   path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
   path('actors/', ActorList.as_view(), name='actor-create'),
   path('actors/<int:pk>/', ActorDetail.as_view(), name='actor-detail'),
]

app_name = "theatre_service"