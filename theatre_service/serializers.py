from rest_framework import serializers
from django.conf import settings
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

    def validate(self, attrs):
        theatre_hall = attrs['theatre_hall']
        show_time = attrs['show_time']
        buffer = settings.PERFORMANCE_TIME_BUFFER

        overlapping = Performance.objects.filter(
            theatre_hall=theatre_hall,
            show_time__range=(show_time - buffer, show_time + buffer)
        )

        if self.instance:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise serializers.ValidationError({
                "show_time": "There is already a performance scheduled in this hall around this time."
            })

        return attrs


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
        row = attrs["row"]
        seat = attrs["seat"]

        theatre_hall = performance.theatre_hall

        if not (1 <= row <= theatre_hall.rows):
            raise serializers.ValidationError({
                "row": f"Row must be in the range [1, {theatre_hall.rows}]"
            })

        if not (1 <= seat <= theatre_hall.seats_in_row):
            raise serializers.ValidationError({
                "seat": f"Seat must be in the range [1, {theatre_hall.seats_in_row}]"
            })

        if Ticket.objects.filter(
                performance=performance,
                row=row,
                seat=seat
        ).exists():
            raise serializers.ValidationError(
                {"seat": "This seat is already taken for the selected performance."}
            )

        return attrs
