from .models import Location, Station, Car
from rest_framework import serializers

class StatitionListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Station
        fields = ('address', 'is_opening', )

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = "__all__"
        read_only_fields = ('address', )

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"