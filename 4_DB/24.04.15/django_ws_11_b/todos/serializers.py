from rest_framework import serializers
from .models import Todo, Recomment


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer):

    class Meta :
        model = Todo
        fields = ('work', 'is_completed', )

class RecommentSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()

    class Meta:
        model = Recomment
        fields = "__all__"
        read_only_fields = ('todo', )
