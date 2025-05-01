from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from theatre_service.models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
)
from theatre_service.serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
)

class PublicPlayViewSet(ReadOnlyModelViewSet):
    queryset = Play.objects.prefetch_related('genres', 'actors')
    serializer_class = PlaySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "actors__first_name", "actors__last_name"]
    ordering_fields = ['title', 'created_at']
    ordering = ['title']
    permission_classes = [AllowAny]


class PublicPerformanceViewSet(ReadOnlyModelViewSet):
    queryset = Performance.objects.select_related('play', 'theatre_hall')
    serializer_class = PerformanceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["play__title", "play__actors__first_name", "play__actors__last_name"]
    ordering_fields = ['show_time']
    ordering = ['show_time']
    permission_classes = [AllowAny]


class PublicGenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    ordering_fields = ['name']
    ordering = ['name']
    permission_classes = [AllowAny]


class PublicActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    ordering_fields = ['last_name', 'first_name']
    ordering = ['last_name']
    permission_classes = [AllowAny]


class PublicTheatreHallViewSet(ReadOnlyModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
    ordering_fields = ['name']
    ordering = ['name']
    permission_classes = [AllowAny]
