from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register(r"comment/(?P<post>\d+)", CommentViewSet, basename="comment")

urlpatterns = router.urls
