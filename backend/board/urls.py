from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, BoardViewSet, SubCommentCreateView

router = routers.DefaultRouter()
router.register(r"boards", BoardViewSet, basename="board")
router.register(r"boards/(?P<board_pk>\d+)/posts", PostViewSet, basename="post")
router.register(r"boards/(?P<board_pk>\d+)/posts/(?P<post_pk>\d+)/comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("boards/<int:board_pk>/posts/<int:post_pk>/comments/<int:comment_pk>/reply/", SubCommentCreateView.as_view())
]


urlpatterns += router.urls
