from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a superuser, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS or
           (request.user and request.user.is_authenticated() and request.user.is_superuser)):
            return True
        return False
