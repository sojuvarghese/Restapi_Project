from django.shortcuts import render
from rest_framework import viewsets
from .models import Srepo
from .serializer import StudentSer
from rest_framework.response import Response
# Create your views here.

class Studentapi(viewsets.ViewSet):
    def list(self, request):
        stu = Srepo.objects.all()
        serializer = StudentSer(stu, many=True)
        return Response(serializer.data)
