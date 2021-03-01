from rest_framework import serializers as sz
from .models import Post, Comment

class CommentSerializers(sz.ModelSerializer):
    writer = sz.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.nickname

    class Meta:
        model = Comment
        fields = ["writer", "created_at", "content"]

class PostSerializer(sz.ModelSerializer):
    writer = sz.SerializerMethodField()
    comments = CommentSerializers(many=True)

    def get_writer(self, obj):
        return obj.writer.nickname

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["writer", "create_at"]