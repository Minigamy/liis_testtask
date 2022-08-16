from rest_framework import permissions


class IsSubOrAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.private:
                if request.user.groups.filter(name__in=['Author', 'Subscriber']).exists() or request.user.is_staff:
                    return True
                return False
            else:
                return True
        return obj.author == request.user
