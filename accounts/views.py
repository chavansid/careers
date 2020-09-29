from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User , Profile
from accounts.serializers import UserSerializer , ProfileSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"status":"true","message":"data Retrive succesfully.","data":serializer.data})
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"true","message":"data Posted succesfully.","data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   
class ProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    '''def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        file = request.data('file')
        selfie_image = Profile.objects.Create(selfie_image=file)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

    