from rest_framework import serializers as sz
from .models import Post, Comment, Board

class SubCommentSerializer(sz.ModelSerializer):
    writer = sz.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("content", "writer", "created_at")
        read_only_fields = ["writer", "created_at"]

    def get_writer(self, obj):
        return obj.writer.nickname


class CommentSerializer(sz.ModelSerializer):
    writer = sz.SerializerMethodField()
    subcomments = SubCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        exclude = ("parent",)
        read_only_fields = ["writer", "created_at", "post", "subcomments"]

    def get_writer(self, obj):
        return obj.writer.nickname


class PostSerializer(sz.ModelSerializer):
    writer = sz.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = sz.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["writer", "create_at", "board", "comment_count", "comments"]

    def get_writer(self, obj):
        return obj.writer.nickname

    def get_comment_count(self, obj):
        return obj.comments.count()
        

class BoardSerializer(sz.ModelSerializer):
    post_count = sz.SerializerMethodField()

    class Meta:
        model = Board
        fields = ("name", "post_count")

    def get_post_count(self, obj):
        return obj.posts.count()
