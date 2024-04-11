from .models import Todo
from rest_framework import serializers

# Create your models here.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"