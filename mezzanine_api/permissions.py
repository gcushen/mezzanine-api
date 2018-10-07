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


class IsAppAuthenticated(permissions.BasePermission):
    """
    OAuth2 Service Account for Apps (Client Credentials grant type)
    Enable applications to obtain an access token for their own account, outside the context of any specific user.
    """
    def has_permission(self, request, view):
        if (request.auth is not None and request.auth.application is not None):
            return True

        # Permission denied as a valid authentication token was not found.
        return False
