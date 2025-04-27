from django.urls import path, include
from rest_framework.routers import DefaultRouter
from theatre_service.views import (
    GenreViewSet, ActorViewSet, PlayViewSet, TheatreHallViewSet,
    PerformanceViewSet, ReservationViewSet, TicketViewSet
)

router = DefaultRouter()

router.register('genre', GenreViewSet, basename='genre')
router.register('actors', ActorViewSet, basename='actor')
router.register('plays', PlayViewSet, basename='play')
router.register('theatrehalls', TheatreHallViewSet, basename='theatrehall')
router.register('performances', PerformanceViewSet, basename='performance')
router.register('reservations', ReservationViewSet, basename='reservation')
router.register('tickets', TicketViewSet, basename='ticket')


urlpatterns = [
    path('', include(router.urls)),
]

app_name = "theatre_service"
