from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    읽기권한은 모두, 나머지는 관리자만
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

class IsOwnerOrReadOnly(BasePermission):
    """
    오브젝트 권한은 작성자에게, 나머진 모두
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user==obj.writer
        )