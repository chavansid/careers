
from rest_framework import serializers
from accounts.models import User , Profile
from django.contrib.auth.hashers import make_password


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    def validated_password(self,value):
        return make_password(value)
    profile_ser = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
        )
        profile_data = validated_data.pop('profile_ser')
        Profile.objects.create(
            user = user,
            selfie_image = profile_data['selfie_image'],
            bio = profile_data['bio'],
            headline = profile_data['headline']
            
        )

        return user