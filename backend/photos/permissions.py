from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class IsObjectOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user