from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, Artist_ListSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    artists = Artist.objects.all()
    if request.method == "GET":
        serializer = Artist_ListSerializer(artists, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk = artist_pk)
    if request.method == "GET":
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)