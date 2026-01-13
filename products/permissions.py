from rest_framework.permissions import BasePermission#parent class

class IsUser(BasePermission):#Permission check
    def has_permission(self, request, view):#API access for USER role
        return (
            request.user.is_authenticated and #JWT token valid yes/no
            request.user.role == 'USER'
        )
        
class IsAdmin(BasePermission): #Permission check
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'ADMIN'
        )