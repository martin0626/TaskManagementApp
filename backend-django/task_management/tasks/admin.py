from django.contrib import admin
from .models import Task


@admin.register(Task)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'user', 'status']
