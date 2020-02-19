
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        return PostSerializer
    
    def create(self, request, *args, **kwargs):
        '''
        request: user that makes de post petition
        '''
        Post.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            author = request.user
        )
        return HttpResponse()