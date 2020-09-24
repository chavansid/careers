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
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
