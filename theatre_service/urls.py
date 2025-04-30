from django.urls import path, include
from django.conf import settings
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

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

app_name = "theatre_service"
