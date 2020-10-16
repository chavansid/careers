from django.shortcuts import render
from datetime import datetime,date
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
from .BaseModelViewset import BaseModelViewSet
from django.core.mail import send_mail
from django.conf import settings
from .pagination import PaginationHandlerMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class UserViewSet(BaseModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','email','Profile__gender']
    head = "user"

class ProfileViewSet(BaseModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend,]
    filter_fields = ['User__created_at']
    search_fields = ['bio', 'city']
    serializer_class = ProfileSerializer
    model = Profile
    queryset = Profile.objects.all()
    pagination_class = PageNumberPagination
    head = "profile"
   

class EducationViewSet(BaseModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filter_fields = ['start_date', 'end_date']
    search_fields = ['school', 'degree']
    serializer_class = EducationSerializer
    model = Education
    queryset = Education.objects.all()
    pagination_class = PageNumberPagination
    head = "education"

class ExperienceViewSet(BaseModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend,]
    filter_fields = ['start_date', 'end_date']
    search_fields = ['title', 'company_name']
    serializer_class = ExperienceSerializer
    model = Experience
    queryset = Experience.objects.all()
    pagination_class = PageNumberPagination
    head = "experience"

class FeedViewSet(BaseModelViewSet):
    serializer_class = FeedSerializer
    model = Feed
    queryset = Feed.objects.all()
    pagination_class = PageNumberPagination

def emailconf(request):

    subject = 'Thank you for registering'
    message = 'welcome'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['siddhesh.ch@engineerbabu.in']

    send_mail(subject,message,email_from, recipient_list)

    return HttpResponseRedirect('http://127.0.0.1:8000/users/')


