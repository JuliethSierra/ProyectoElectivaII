from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from .models import todo_coleccion
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>App is running</h1>")

def add_task(request):
    records = {
        "id": "1",
        "title": "task", 
        "description": "add task", 
        "completed": "false"
    }
    todo_coleccion.insert_one(records)
    return HttpResponse("New task is added")


def get_all_task(request):
    task = todo_coleccion.find()
    return HttpResponse(task)
    
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    def index(request):
        return HttpResponse("<h1>App is running</h1>")

    def add_task(request):
        records = {
            "id": "1",
            "title": "task", 
            "description": "add task", 
            "completed": "false"
        }
        todo_coleccion.insert_one(records)
        return HttpResponse("New task is added")


    def get_all_task(request):
        task = todo_coleccion.find()
        return HttpResponse(task)