from rest_framework.permissions import IsAuthenticated

from books.constants import ADMIN

class AdminPermission(IsAuthenticated):
    message = 'Доступ разрешен только админам!'

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.roles == ADMIN