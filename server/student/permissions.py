from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from role.models import Role


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user:
            return True if user.is_superuser else False