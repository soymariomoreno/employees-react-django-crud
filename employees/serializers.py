# todo/serializers.py
from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employees
    fields = ('id', 'first_name', 'last_name', 'about', 'avatar', 'cv')