from django.http import JsonResponse
from django.shortcuts import render
from core.models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def coreViews(request): 
    if request.method == "GET":
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
    
    return Response(serializer.data,status=status.HTTP_200_OK)