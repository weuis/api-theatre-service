from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Genre, Actor
from .serializers import GenreSerializer, ActorSerializer


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

