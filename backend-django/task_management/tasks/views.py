from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Task
from .serializers import TaskSerializer, CreateTaskSerializer


# Create your views here.
class AllTasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Task.objects.all().filter(user=self.request.user)


class CreateTasksView(generics.CreateAPIView):
    serializer_class = CreateTaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UpdateTaskView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.all().filter(user=self.request.user)
