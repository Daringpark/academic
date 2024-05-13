from rest_framework import serializers
from .models import Post

# Create your models here.
class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'