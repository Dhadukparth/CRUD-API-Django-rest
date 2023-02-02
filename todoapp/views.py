from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List' : '/todos/',
        'Details View' : '/todo/<str: pk>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str: pk>/',
        'Delete': '/todo-update/<str: pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    allTodos = todos.objects.all().values()
    return Response({"Todos List":allTodos})


@api_view(['GET'])
def todoListDetails(request, pk):
    getTodo = todos.objects.filter(id=pk).values()
    return Response({"Todo Details":getTodo})

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        todos.objects.create(id=serializer.data.get("id"),
                                title=serializer.data.get("title"),
                                description=serializer.data.get("description"))
        return Response({"Message":"Create Successfully"})
    else:
        return Response({"Message":"Sorry! Todo Is Not Create."})


@api_view(['POST'])
def todoUpdate(request, pk):
    getTodo = todos.objects.get(id=pk)
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        getTodo.title = serializer.data.get("title")
        getTodo.description = serializer.data.get("description")
        getTodo.save()
        return Response({"Message":"Update Successfully"})
    else:
        return Response({"Message":"Sorry! Todo Is Not Updated."})


@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = todos.objects.get(id=pk)
    todo.delete()
    return Response({"Message":"Delete Successfully"})