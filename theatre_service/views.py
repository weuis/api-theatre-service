from rest_framework import viewsets
from theatre_service.models import (
    Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket
)
from theatre_service.serializers import (
    GenreSerializer, ActorSerializer, PlaySerializer, PlayDetailSerializer,
    TheatreHallSerializer,
    PerformanceSerializer, PerformanceDetailSerializer,
    ReservationSerializer, TicketSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class PlayViewSet(viewsets.ModelViewSet):
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
    def get_queryset(self):
        return Performance.objects.select_related('play', 'theatre_hall')

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return PerformanceDetailSerializer
        return PerformanceSerializer



class ReservationViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Reservation.objects.select_related('user').prefetch_related('tickets')

    serializer_class = ReservationSerializer


class TicketViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Ticket.objects.select_related('performance', 'reservation')

    serializer_class = TicketSerializer
