from rest_framework import permissions
from mezzanine_api import settings


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a superuser, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS or
           (request.user and request.user.is_authenticated() and request.user.is_superuser)):
            return True
        return False

'''
This method checks that the client has used an authentication method which isn't binded to
any user but to application (identified by id:secret). E.g OAuth2 -> Client Credentials grant type
This method will be called for posts and categories. pages are protected by default if they are created with login_required checkbox
'''    
class IsAppAuthenticated(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if(request.auth!=None and request.auth.application!=None):
            return True
			
        print("permission is denied, valid authentication token wasn't found")   
        return False 
