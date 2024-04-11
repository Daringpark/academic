from rest_framework import serializers
from .models import Artist


class Artist_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'debut_date',)

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'