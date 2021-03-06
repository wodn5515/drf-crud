from django.db import models
from account.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(verbose_name="메뉴명", max_length=10)

    class Meta:
        verbose_name = "메뉴"
        verbose_name_plural = "메뉴"

    def __str__(self):
        return self.name
    

class Post(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(verbose_name="제목", max_length=50)
    content = models.TextField(verbose_name="내용")
    create_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(verbose_name="링크", blank=True)
    tag = models.ManyToManyField(User, related_name="posts", blank=True)

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subcomments", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    content = models.TextField(verbose_name="내용")
    tag = models.ManyToManyField(User, related_name="comments", blank=True)

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글"

    def __str__(self):
        return f"{self.writer.nickname} - {self.content}"