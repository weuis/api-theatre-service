from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    Access is allowed only:
    - For GET requests (list, retrieve) — if the user is authorized
    - For all other methods — only if the user is_staff
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (request.user.is_staff and request.user)
