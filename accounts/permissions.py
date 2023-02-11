from rest_framework import permissions
from .models import User
from rest_framework.views import View
from rest_framework.request import Request


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user
    
class IsAuthenticatedToGet(permissions.BasePermission):
    def has_permission(self, request:Request, view: View):

        if request._request.method == "GET":
            return bool(request.user and request.user.is_authenticated)

        return True