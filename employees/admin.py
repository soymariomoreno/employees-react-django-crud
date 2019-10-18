from django.contrib import admin
from .models import Employees # add this

# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):  # add this
  list_display = ('first_name', 'last_name', 'about', 'avatar', 'cv') # add this

# Register your models here.
admin.site.register(Employees, EmployeesAdmin) #