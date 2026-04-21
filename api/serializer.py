from rest_framework import serializers
from core.models import Student 
from employees.models import Employee

#function to convert model instance to json format
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

#class to convert employee model instance to json format
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'