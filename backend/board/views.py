from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets as vs
from rest_framework import permissions as pm

from .models import Post, Comment, Board
from .serializers import PostSerializer, CommentSerializers, BoardSerializer
from .permissions import isAdminOrReadOnly


# Create your views here.

class BoardViewSet(vs.ModelViewSet):
    serializer_class = BoardSerializer
    permission_classes = [isAdminOrReadOnly]
    queryset = Board.objects.all()


class PostViewSet(vs.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [pm.IsAuthenticatedOrReadOnly]

    def get_board(self):
        return get_object_or_404(Board, pk=self.kwargs["board_pk"])
    
    def get_queryset(self):
        post_list = Post.objects.filter(board=self.get_board())
        return post_list

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user, board=self.get_board())


class CommentViewSet(vs.ModelViewSet):
    serializer_class = CommentSerializers
    permission_classes = [pm.IsAuthenticatedOrReadOnly]

    def get_post(self):
        post = Post.objects.get(pk=self.kwargs["post_pk"])
        return post
        
    def get_queryset(self):
        comment_list = Comment.objects.filter(post=self.get_post())
        return comment_list

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), writer=self.request.user)