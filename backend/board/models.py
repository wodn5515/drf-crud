from django.db import models
from account.models import User

# Create your models here.

class Menu(models.Model):
    name = models.CharField(verbose_name="메뉴명", max_length=10)

    class Meta:
        verbose_name = "메뉴"
        verbose_name_plural = "메뉴"

    def __str__(self):
        return self.name
    

class Post(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목", max_length=50)
    content = models.TextField(verbose_name="내용")
    create_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(verbose_name="링크")

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    content = models.TextField(verbose_name="내용")

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글"

    def __str__(self):
        return f"{self.writer.nickname} - {self.content}"