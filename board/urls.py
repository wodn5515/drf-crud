from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("comment", CommentViewSet, basename="comment")

urlpatterns = router.urls
