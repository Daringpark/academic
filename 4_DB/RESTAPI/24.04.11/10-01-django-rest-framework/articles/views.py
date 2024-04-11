from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# 전체 리스트 확인, POST CREATE
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

# READ, UPDATE, DELETE
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data = request.data, partial = True)
        # instance = article
        # partial = True를 이용해서 부분 update를 가능케 한다.

        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)
        
        # BAD_REQUEST의 부분을 raise_exception = True 부분에서 처리를 가능하게 해준다.
        # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

    
