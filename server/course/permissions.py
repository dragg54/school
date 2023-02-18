from rest_framework import permissions

from role.models import Role


class IsSuperAdminPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        return True if request.user.is_superuser else False


class IsStudentPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        student = Role.objects.get(user=user.id)
        return True if student else False
