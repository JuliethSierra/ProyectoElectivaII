from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from .models import todo_coleccion
from django.http import HttpResponse

import logging
# Create your views here.


from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from bson.json_util import dumps, ObjectId
import logging
import json

def index(request):
    return HttpResponse("<h1>App is running</h1>")



def get_all_tasks(request):
    try:
        tasks = list(todo_coleccion.find())  # Convertir el cursor a una lista de diccionarios
        # Convertir ObjectId a cadena en cada diccionario
        for task in tasks:
            task['_id'] = str(task['_id'])
        return JsonResponse(tasks, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@require_http_methods(["POST"])
def add_task(request):
    try:
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")
        completed = data.get("completed")

        if not title or not description:
            return JsonResponse({"error": "Title and description are required"}, status=400)

        record = {
            "title": title,
            "description": description,
            "completed": completed
        }
        todo_coleccion.insert_one(record)
        return JsonResponse({"message": "New task is added"}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        logging.error(f"Error adding task: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)
    

def delete_task(request):
    logger = logging.getLogger(__name__)
    try:
        data = json.loads(request.body.decode('utf-8'))
        task_id = data.get("_id")
        result = todo_coleccion.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count == 1:
            logger.info("Tarea eliminada correctamente.")
            return JsonResponse({"message": "Task deleted"}, status=200)
        else:
            logger.warning("Tarea no encontrada.")
            return JsonResponse({"error": "Task not found"}, status=404)
    except Exception as e:
        logger.error("Error al eliminar la tarea: %s", e)
        return JsonResponse({"error": "Error interno del servidor"}, status=500)
    
def update_task(request):
    logger = logging.getLogger(__name__)
    try:
        data = json.loads(request.body.decode('utf-8'))  # Obtener los datos enviados desde el frontend
        task_id = data.get("_id")
        updates = {
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "completed": data.get("completed", True)
        }
        # Actualizar la tarea en la base de datos
        result = todo_coleccion.update_one({"_id": ObjectId(task_id)}, {"$set": updates})

        # Verificar si la tarea se actualizó correctamente
        if result.matched_count == 1:
            logger.info("Tarea actualizada correctamente.")
            return JsonResponse({"message": "Tarea actualizada correctamente."}, status=200)
        else:
            logger.warning("Tarea no encontrada.")
            return JsonResponse({"error": "Tarea no encontrada."}, status=404)
    except Exception as e:
        logger.error("Error al actualizar la tarea: %s", e)
        return JsonResponse({"error": "Error interno del servidor"}, status=500)

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    