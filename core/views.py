from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def core(request):
    student_data = {
        "name": "John Doe",
        "age": 20,
        "grade": "A"
    }
    return JsonResponse(student_data)