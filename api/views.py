import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt
def task_list_create(request):
    # --- CREATE (Post a new task) ---
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title'),
            description=data.get('description', '')
        )
        return JsonResponse({
            "message": "Task created successfully!",
            "task": {"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed}
        }, status=201)

    # --- READ ALL (Get list of all tasks) ---
    elif request.method == 'GET':
        tasks = Task.objects.all()
        # Convert database objects into a list of dictionaries (Python Basics)
        task_list = [{"id": t.id, "title": t.title, "description": t.description, "is_completed": t.is_completed} for t in tasks]
        return JsonResponse(task_list, safe=False)


@csrf_exempt
def task_detail_update_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found!"}, status=404)

    # --- UPDATE (Change a task status or title) ---
    if request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.is_completed = data.get('is_completed', task.is_completed)
        task.save() # Saves changes to PostgreSQL
        return JsonResponse({"message": "Task updated successfully!"})

    # --- DELETE (Remove a task) ---
    elif request.method == 'DELETE':
        task.delete() # Deletes from PostgreSQL
        return JsonResponse({"message": "Task deleted successfully!"})