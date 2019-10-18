# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import EmployeesSerializer      # add this
from .models import Employees                     # add this

class EmployeesView(viewsets.ModelViewSet):       # add this
  serializer_class = EmployeesSerializer          # add this
  queryset = Employees.objects.all()              # add this