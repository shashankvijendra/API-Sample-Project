import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Task, Lkstatuscode
from .serializers import TaskSerializer
from rest_framework.viewsets import GenericViewSet
# Create your views here.


class TaskAPIView(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get(self, request, pk=None):
        if pk is None:
            return Response(TaskSerializer(Task.objects.all(), many=True).data)
        return Response(TaskSerializer(Task.objects.get(pk=pk)).data)
    
    
    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

    def put(self, request, pk=None):
        data = request.data
        task = Task.objects.get(pk=pk)
        task.task_for = data['task_for']
        if task.lk_status_code != data['lk_status_code']:
            if lk_status_code := Lkstatuscode.objects.filter(
                lk_status_code=data['lk_status_code']).first():
                task.lk_status_code = lk_status_code
        task.save()
        return Response(TaskSerializer(Task.objects.get(pk=pk)).data)
        # return Response(serializer.errors, status=400)
