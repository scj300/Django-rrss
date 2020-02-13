
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from .models import Post

class PostSerializer(HyperlinkedModelSerializer):
    created = serializers.DateTimeField(format='%d-%M-%Y %H:%M:%S')
    updated = serializers.DateTimeField(format='%d-%M-%Y %H:%M:%S')
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'created', 'updated']