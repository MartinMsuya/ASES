from rest_framework import serializers
from Backend.models import Projects
from django.contrib.auth.models import User



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields= '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
