from rest_framework import serializers as sz
from .models import Post, Comment, Board

class CommentSerializers(sz.ModelSerializer):
    writer = sz.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.nickname

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["writer", "created_at", "post"]

class PostSerializer(sz.ModelSerializer):
    writer = sz.SerializerMethodField()
    comments = CommentSerializers(many=True, read_only=True)

    def get_writer(self, obj):
        return obj.writer.nickname

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["writer", "create_at", "board"]

class BoardSerializer(sz.ModelSerializer):

    class Meta:
        model = Board
        fields = "__all__"
