from rest_framework import permissions


class IsAdminAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class ProjectPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        else:
            return False


class ContributorPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.user_id
        else:
            return False


class IssuePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        else:
            return False


class CommentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author_id
        else:
            return False
