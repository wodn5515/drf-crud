from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, BoardViewSet

router = routers.DefaultRouter()
router.register(r"boards", BoardViewSet, basename="board")
router.register(r"boards/(?P<board_pk>\d+)/posts", PostViewSet, basename="post")
router.register(r"boards/(?P<board_pk>\d+)/posts/(?P<post_pk>\d+)/comments", CommentViewSet, basename="comment")

urlpatterns = router.urls
