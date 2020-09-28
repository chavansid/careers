from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status
# Create your views here.


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = User.objects.all()
    serializer_class = UserSerializer
