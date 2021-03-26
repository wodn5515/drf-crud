from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets as vs
from rest_framework import permissions as pm
from rest_framework.generics import CreateAPIView, DestroyAPIView

from .models import Post, Comment, Board
from .serializers import PostSerializer, CommentSerializer, BoardSerializer, SubCommentSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# Create your views here.

class BoardViewSet(vs.ModelViewSet):
    serializer_class = BoardSerializer
    permission_classes = [IsAdminOrReadOnly]
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
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_post(self):
        post = Post.objects.get(pk=self.kwargs["post_pk"])
        return post

    def get_comment(self):
        parent_comment = Comment.objects.get(pk=self.request.GET.get("parent"))
        return parent_comment
        
    def get_queryset(self):
        comment_list = Comment.objects.filter(post=self.get_post())
        return comment_list

    def perform_create(self, serializer):
        if self.request.GET.get("parent", False):
            serializer.save(parent=self.get_comment(), writer=self.request.user)
        else:
            serializer.save(post=self.get_post(), writer=self.request.user)
