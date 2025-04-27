from rest_framework import serializers
from theatre_service.models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket
)
from theatre_user.models import CustomUser


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class PlaySerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())

    class Meta:
        model = Play
        fields = ['id', 'title', 'description', 'genres', 'actors']

class PlayDetailSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Play
        fields = ('id', 'title', 'description', 'genres', 'actors')


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ['id', 'name', 'rows', 'seats_in_row']


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ('id', 'play', 'theatre_hall', 'show_time')


class PerformanceDetailSerializer(serializers.ModelSerializer):
    play = PlaySerializer()
    theatre_hall = serializers.StringRelatedField()

    class Meta:
        model = Performance
        fields = ('id', 'play', 'theatre_hall', 'show_time')


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'created_at']


class TicketSerializer(serializers.ModelSerializer):
    performance = serializers.PrimaryKeyRelatedField(queryset=Performance.objects.all())
    reservation = serializers.PrimaryKeyRelatedField(queryset=Reservation.objects.all())

    class Meta:
        model = Ticket
        fields = ['id', 'row', 'seat', 'performance', 'reservation']

    def validate(self, attrs):
        performance = attrs["performance"]
        num_seats = performance.theatre_hall.seats_in_row

        Ticket.validate_seat(
            attrs["seat"],
            num_seats,
            serializers.ValidationError
        )

        return attrs
