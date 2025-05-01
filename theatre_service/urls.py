from django.urls import path, include
from rest_framework.routers import DefaultRouter

from theatre_service.views import (
    GenreViewSet, ActorViewSet, PlayViewSet, TheatreHallViewSet,
    PerformanceViewSet, ReservationViewSet, TicketViewSet
)

from theatre_service.public_views import (
    PublicPlayViewSet, PublicPerformanceViewSet,
    PublicGenreViewSet, PublicActorViewSet, PublicTheatreHallViewSet
)

authenticate_router = DefaultRouter()

authenticate_router.register('genre', GenreViewSet, basename='genre')
authenticate_router.register('actors', ActorViewSet, basename='actor')
authenticate_router.register('plays', PlayViewSet, basename='play')
authenticate_router.register('theatrehalls', TheatreHallViewSet, basename='theatrehall')
authenticate_router.register('performances', PerformanceViewSet, basename='performance')
authenticate_router.register('reservations', ReservationViewSet, basename='reservation')
authenticate_router.register('tickets', TicketViewSet, basename='ticket')

public_router = DefaultRouter()

public_router.register(r'plays', PublicPlayViewSet, basename='public-play')
public_router.register(r'performances', PublicPerformanceViewSet, basename='public-performance')
public_router.register(r'genres', PublicGenreViewSet, basename='public-genre')
public_router.register(r'actors', PublicActorViewSet, basename='public-actor')
public_router.register(r'halls', PublicTheatreHallViewSet, basename='public-hall')


urlpatterns = [
     path('', include(authenticate_router.urls)),
     path('public/',include(public_router.urls)),

]


app_name = 'theatre'
