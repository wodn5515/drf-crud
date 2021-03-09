from rest_framework.permissions import BasePermission, SAFE_METHODS


class isAdminOrReadOnly(BasePermission):
    """
    읽기권한은 모두, 나머지는 관리자만
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )