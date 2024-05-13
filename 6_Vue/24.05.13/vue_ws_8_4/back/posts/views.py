from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Post
from .serializers import PostListSerializer

# Create your views here.
@api_view(['GET'])
def posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
