from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User , Profile , Education ,Experience ,Feed
from accounts.serializers import UserSerializer , ProfileSerializer , EducationSerializer , ExperienceSerializer ,FeedSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import Http404 , HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .Baseview import BaseDetails
from django.core.mail import send_mail
from django.conf import settings
from .pagination import PaginationHandlerMixin
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class UserList(generics.ListCreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"true","message":"data Posted succesfully.","data":{"uuid": serializer.data['uuid']}}, status=status.HTTP_201_CREATED)
        return Response({'message': 'user with this email already exist',}, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(BaseDetails):
    model_class = User
    serializer_class = UserSerializer
    head = "user"

class ProfileDetail(BaseDetails):
    model_class = Profile
    serializer_class = ProfileSerializer
    head = "profile"

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, **kwargs):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})

class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def get(self, request, **kwargs):
        education = Education.objects.all()
        serializer = EducationSerializer(education, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})


class EducationDetail(BaseDetails):
    model_class = Education
    serializer_class = EducationSerializer
    head = "education"

class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get(self, request, **kwargs):
        experience = Experience.objects.all()
        serializer = ExperienceSerializer(experience, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})

class ExperienceDetail(BaseDetails):
    model_class = Experience
    serializer_class = ExperienceSerializer
    head = "experience"

class Feedpage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get(self, request, **kwargs):
        fed = Feed.objects.all()
        serializer = FeedSerializer(fed, many=True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})

def emailconf(request):

    subject = 'Thank you for registering'
    message = 'It means a world to us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['vineeth.t@engineerbabu.in']

    send_mail(subject,message,email_from, recipient_list)

    return HttpResponseRedirect('http://127.0.0.1:8000/users/')


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'
class MyListAPI(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = ProfileSerializer
    def get(self, request, format=None, *args, **kwargs):
        instance = Dataset.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
 many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
