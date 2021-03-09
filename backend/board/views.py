from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets as vs
from rest_framework import permissions as pm

from .models import Post, Comment, Board
from .serializers import PostSerializer, CommentSerializers, BoardSerializer
from .mixins import CommentMixin
from .permissions import isAdminOrReadOnly


# Create your views here.

class BoardViewSet(vs.ModelViewSet):
    serializer_class = BoardSerializer
    permission_classes = [isAdminOrReadOnly]


class PostViewSet(vs.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [pm.IsAuthenticatedOrReadOnly]

    def get_board(self):
        return get_object_or_404(Board, pk=self.kwargs["board_pk"])
    
    def get_queryset(self):
        post_list = Post.objects.filter(menu=self.get_board())
        return post_list

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user, board=self.get_board())


class CommentViewSet(CommentMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [pm.IsAuthenticatedOrReadOnly]

    def get_post(self):
        post = Post.objects.get(pk=self.kwargs["post_pk"])
        return post

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.get_post())
        serializer.save(post=post, writer=self.request.user)