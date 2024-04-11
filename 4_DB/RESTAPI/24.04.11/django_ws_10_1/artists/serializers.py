from rest_framework import serializers
from .models import Artist

# Create your models here.
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = ('name', 'agency', 'debut_data', )
        fields = "__all__"