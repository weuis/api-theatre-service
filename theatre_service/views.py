from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from theatre_service.permissions import IsAdminOrAuthenticatedReadOnly
from theatre_service.filters import PerformanceFilter, PlayFilter, ReservationFilter

from theatre_service.models import (
    Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket
)
from theatre_service.serializers import (
    GenreSerializer, ActorSerializer, PlaySerializer, PlayDetailSerializer,
    TheatreHallSerializer, PerformanceSerializer, PerformanceDetailSerializer,
    ReservationSerializer, TicketSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    ordering_fields = ['name']
    ordering = ['name']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    ordering_fields = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PlayFilter
    search_fields = ["title", "actors__first_name", "actors__last_name"]
    ordering_fields = ['title', 'created_at']
    ordering = ['title']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_queryset(self):
        return Play.objects.prefetch_related('genres', 'actors')

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return PlayDetailSerializer
        return PlaySerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
    ordering_fields = ['name']
    ordering = ['name']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PerformanceFilter
    search_fields = ["play__title", "play__actors__first_name", "play__actors__last_name"]
    ordering_fields = ['show_time', 'created_at']
    ordering = ['show_time']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_queryset(self):
        return Performance.objects.select_related('play', 'theatre_hall')

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return PerformanceDetailSerializer
        return PerformanceSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReservationFilter
    ordering_fields = ['created_at', 'user']
    ordering = ['created_at']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_queryset(self):
        return Reservation.objects.select_related('user').prefetch_related('tickets')


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['performance__show_time']
    ordering = ['performance__show_time']
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_queryset(self):
        return Ticket.objects.select_related('performance', 'reservation')
