from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class IndexView(APIView):
    """
    API view for searching Movies
    """
    allowed_methods = ['GET']
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
