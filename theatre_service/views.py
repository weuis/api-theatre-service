from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Genre, Actor, Play, TheatreHall, Performance
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return JsonResponse({'data': serializer.data})

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


class GenreDetail(APIView):
    def get(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)
        serializer = GenreSerializer(genre)
        return JsonResponse({'data': serializer.data})

    def put(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        genre.delete()
        return JsonResponse({}, status=204)


class ActorList(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return JsonResponse({'data': serializer.data})

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


class ActorDetail(APIView):
    def get(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)
        serializer = ActorSerializer(actor)
        return JsonResponse({'data': serializer.data})

    def put(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        actor.delete()
        return JsonResponse({}, status=204)


class PlayList(APIView):
    def get(self, request):
        plays = Play.objects.all()
        serializer = PlaySerializer(plays, many=True)
        return JsonResponse({'data': serializer.data})

    def post(self, request):
        serializer = PlaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


class PlayDetail(APIView):
    def get(self, request, pk):
        try:
            play = Play.objects.get(pk=pk)
        except Play.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)
        serializer = PlaySerializer(play)
        return JsonResponse({'data': serializer.data})

    def put(self, request, pk):
        try:
            play = Play.objects.get(pk=pk)
        except Play.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        serializer = PlaySerializer(play, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            play = Play.objects.get(pk=pk)
        except Play.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        play.delete()
        return JsonResponse({}, status=204)


class TheatreHallList(APIView):
    def get(self, request):
        theatre_halls = TheatreHall.objects.all()
        serializer = TheatreHallSerializer(theatre_halls, many=True)
        return JsonResponse({'data': serializer.data})

    def post(self, request):
        serializer = TheatreHallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


class TheatreHallDetail(APIView):
    def get(self, request, pk):
        try:
            theatre_hall = TheatreHall.objects.get(pk=pk)
        except TheatreHall.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)
        serializer = TheatreHallSerializer(theatre_hall)
        return JsonResponse({'data': serializer.data})

    def put(self, request, pk):
        try:
            theatre_hall = TheatreHall.objects.get(pk=pk)
        except TheatreHall.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        serializer = TheatreHallSerializer(theatre_hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            theatre_hall = TheatreHall.objects.get(pk=pk)
        except TheatreHall.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        theatre_hall.delete()
        return JsonResponse({}, status=204)


class PerformanceList(APIView):
    def get(self, request):
        performances = Performance.objects.all()
        serializer = PerformanceSerializer(performances, many=True)
        return JsonResponse({'data': serializer.data})

    def post(self, request):
        serializer = PerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


class PerformanceDetail(APIView):
    def get(self, request, pk):
        try:
            performance = Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)
        serializer = PerformanceSerializer(performance)
        return JsonResponse({'data': serializer.data})

    def put(self, request, pk):
        try:
            performance = Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        serializer = PerformanceSerializer(performance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            performance = Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=404)

        performance.delete()
        return JsonResponse({}, status=204)