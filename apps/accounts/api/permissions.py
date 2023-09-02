from rest_framework.permissions import BasePermission
from rest_framework import permissions


class NotAuthenticated(BasePermission):
    message = "You already have an account."

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user