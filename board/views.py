from django.shortcuts import render
from rest_framework import viewsets as vs
from rest_framework import permissions as pm
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializers
from .mixins import CommentMixin


# Create your views here.

class PostViewSet(vs.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [pm.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        menu = self.request.GET.get("menu", "")
        if menu:
            post_list = Post.objects.filter(menu=menu)
        else:
            post_list = Post.objects.all()
        return post_list

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


class CommentViewSet(CommentMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [pm.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.request.GET.get("post", ""))
        serializer.save(post=post, writer=self.request.user)