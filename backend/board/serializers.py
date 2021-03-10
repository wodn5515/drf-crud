from rest_framework import serializers as sz
from .models import Post, Comment, Board

class CommentSerializers(sz.ModelSerializer):
    writer = sz.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.nickname

    class Meta:
        model = Comment
        exclude = ("post",)
        read_only_fields = ["writer", "created_at", "post"]

class PostSerializer(sz.ModelSerializer):
    writer = sz.SerializerMethodField()
    comments = CommentSerializers(many=True, read_only=True)
    comment_count = sz.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["writer", "create_at", "board", "comment_count"]

    def get_writer(self, obj):
        return obj.writer.nickname

    def get_comment_count(self, obj):
        return obj.comments.count()

class BoardSerializer(sz.ModelSerializer):

    class Meta:
        model = Board
        fields = "__all__"
