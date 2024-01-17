from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    http_method_names = ['get','post','put','patch','delete']
    serializer_class = StudentSerializer
    