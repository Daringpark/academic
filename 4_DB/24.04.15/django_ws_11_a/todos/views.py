from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer, RecommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def todo(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    if request.method == "GET":
        serializer =  TodoSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == "DELETE":
        todo.delete()
        result = f'[제목 : {todo.work}, 할일 내용 : {todo.content} ]의 할일 메모를 삭제 하셨습니다.'
    return Response(result, status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def recommend_create(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    if request.method == "POST":
        recomment = RecommentSerializer(data = request.data)
        if recomment.is_valid(raise_exception=True):
            recomment.save(todo = todo)
            return Response(recomment.data, status=status.HTTP_201_CREATED)
        
