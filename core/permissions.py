from rest_framework import permissions

class IsAgenceMember(permissions.BasePermission):
    def has_permission(self, request, view):
        # Exemple simple, adapte selon ton besoin
        return request.user and request.user.is_authenticated and request.user.is_staff
