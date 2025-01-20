# filepath: /workspace/taskmaster/tasks/admin.py
from django.contrib import admin
from .models import Category, Task

admin.site.register(Category)
admin.site.register(Task)

# Register your models here.
