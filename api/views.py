from django.http import JsonResponse

def hello_api(request):
    return JsonResponse({"status": "success", "message": "Django and Postgres are connected!"})