from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from theatre_service.models import Genre, Actor, Play, TheatreHall, Performance, Reservation

class TheatreServiceTests(APITestCase):
    def setUp(self):
        self.client = self.client_class()

        self.registered_user = get_user_model().objects.create_user(
            username="user", email="user@example.com", password="1234"
        )
        self.client.force_authenticate(user=self.registered_user)

        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.play = Play.objects.create(title="Hamlet", description="A Shakespearean play")
        self.play.genres.add(self.genre)
        self.play.actors.add(self.actor)
        self.theatre_hall = TheatreHall.objects.create(name="Main Hall", rows=10, seats_in_row=15)
        self.performance = Performance.objects.create(
            play=self.play, theatre_hall=self.theatre_hall, show_time="2025-06-01T20:00:00Z"
        )
        self.reservation = Reservation.objects.create(user=self.registered_user)

    def test_create_reservation_authenticated(self):
        url = '/api/v1/theatre/authenticated_only/reservations/'
        data = {"user": self.registered_user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_ticket_authenticated(self):
        url = '/api/v1/theatre/authenticated_only/tickets/'
        data = {
            "performance": self.performance.id,
            "row": 1,
            "seat": 1,
            "reservation": self.reservation.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_view_actor_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = '/api/v1/theatre/public/actors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_genre_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = '/api/v1/theatre/public/genres/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_performance_detail_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = f'/api/v1/theatre/public/performances/{self.performance.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_play_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = '/api/v1/theatre/public/plays/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
