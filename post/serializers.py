
from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(HyperlinkedModelSerializer):
    created = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    updated = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    
    # user = UserSerializer()
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'created', 'updated']

