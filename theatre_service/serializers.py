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


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class PlaySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Play
        fields = ['id', 'title', 'description', 'genres', 'actors']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        # Handle genres and actors, ensuring they are updated correctly
        genres_data = validated_data.pop('genres', [])
        actors_data = validated_data.pop('actors', [])

        instance.genres.set([genre['id'] for genre in genres_data])
        instance.actors.set([actor['id'] for actor in actors_data])

        instance.save()
        return instance


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ['id', 'name', 'rows', 'seats_in_row']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rows = validated_data.get('rows', instance.rows)
        instance.seats_in_row = validated_data.get('seats_in_row', instance.seats_in_row)
        instance.save()
        return instance


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer()
    theatre_hall = TheatreHallSerializer()

    class Meta:
        model = Performance
        fields = ['id', 'play', 'theatre_hall', 'show_time']

    def update(self, instance, validated_data):
        instance.show_time = validated_data.get('show_time', instance.show_time)

        # Handling nested updates for play and theatre_hall
        play_data = validated_data.get('play', {})
        theatre_hall_data = validated_data.get('theatre_hall', {})

        instance.play = Play.objects.get(id=play_data['id']) if play_data else instance.play
        instance.theatre_hall = TheatreHall.objects.get(id=theatre_hall_data['id']) if theatre_hall_data else instance.theatre_hall

        instance.save()
        return instance


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'created_at', 'user']

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class TicketSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()
    reservation = ReservationSerializer()

    class Meta:
        model = Ticket
        fields = ['id', 'row', 'seat', 'performance', 'reservation']

    def update(self, instance, validated_data):
        instance.row = validated_data.get('row', instance.row)
        instance.seat = validated_data.get('seat', instance.seat)

        # Handling nested updates for performance and reservation
        performance_data = validated_data.get('performance', {})
        reservation_data = validated_data.get('reservation', {})

        instance.performance = Performance.objects.get(id=performance_data['id']) if performance_data else instance.performance
        instance.reservation = Reservation.objects.get(id=reservation_data['id']) if reservation_data else instance.reservation

        instance.save()
        return instance
