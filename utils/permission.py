from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()


class BasePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class BaseAllowAny(AllowAny):
    def has_permission(self, request, view):
        return True
