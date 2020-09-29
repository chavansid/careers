
from rest_framework import serializers
from accounts.models import User , Profile
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    def validated_password(self,value):
        return make_password(value)
    profile = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = '__all__'
        extra_fields = 'profile'

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
        )
        profile_data = validated_data.pop('profile')
        Profile.objects.create(
            user = user,
            selfie_image = profile_data['selfie_image'],
            bio = profile_data['bio'],
            headline = profile_data['headline']
            
        )
        return user
    
    def put(self, request, uuid, format=None):
        user = self.get_object(uuid)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"true","message":"data updated succesfully.","data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        user = self.get_object(uuid)
        user.delete()
        return Response({"status":"true","message":"data Deleted succesfully."},status=status.HTTP_204_NO_CONTENT)
        