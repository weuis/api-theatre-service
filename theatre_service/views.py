from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from theatre_service.filters import PerformanceFilter, PlayFilter, ReservationFilter

from theatre_service.models import (
    Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket
)
from theatre_service.serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    PlayDetailSerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    PerformanceDetailSerializer,
    ReservationSerializer,
    TicketSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class PlayViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PlayFilter
    search_fields = ["title", "actors__first_name", "actors__last_name"]

    def get_queryset(self):
        return Play.objects.prefetch_related('genres', 'actors')

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return PlayDetailSerializer
        return PlaySerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PerformanceFilter
    search_fields = ["play__title", "play__actors__first_name", "play__actors__last_name"]

    def get_queryset(self):
        return Performance.objects.select_related('play', 'theatre_hall')

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return PerformanceDetailSerializer
        return PerformanceSerializer



class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservationFilter

    def get_queryset(self):
        return Reservation.objects.select_related('user').prefetch_related('tickets')


class TicketViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Ticket.objects.select_related('performance', 'reservation')

    serializer_class = TicketSerializer
