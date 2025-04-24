from django.urls import path
from theatre_service.views import GenreList, GenreDetail



urlpatterns = [
   path("genre/", GenreList.as_view(), name="genre-list"),
   path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "theatre_service"