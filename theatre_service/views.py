from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Genre
from .serializers import GenreSerializer


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
