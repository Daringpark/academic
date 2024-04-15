from rest_framework import serializers
from .models import Location, Station, Car


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('address', )

class StationSerializer(serializers.ModelSerializer):
    
    address = LocationSerializer(read_only = True)

    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ('address', )

class StationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('address', 'is_opening',)
        

        