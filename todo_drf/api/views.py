from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class tasklist(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class taskdetail(APIView):
    def get_object(self, id):
        try:
            return Task.objects.filter(id=id)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, id=None):
        tasks = self.get_object(id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def put(self, request, id=None):
        tasks = self.get_object(id)
        serializer = TaskSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        tasks = self.get_object(id)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)