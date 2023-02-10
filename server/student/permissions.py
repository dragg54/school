from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from role.models import Role


class IsStudentPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user:
            user_role = Role.objects.get(user=user.id).role
            return False if user_role is "student" else True
