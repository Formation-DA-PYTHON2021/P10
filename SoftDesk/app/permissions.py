from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .models import Project, Issue, Comment


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.is_superuser)


class ProjectPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            project = get_object_or_404(Project, id=view.kwargs['project_pk'])
            if request.method in permissions.SAFE_METHODS:
                return project in Project.objects.filter(contributors__user=request.user)
            return request.user == project.author_user_id
        except KeyError:
            return True


class ContributorPermissions(BasePermission):
    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['project_pk'])
        if request.method in permissions.SAFE_METHODS:
            return project in Project.objects.filter(contributor__user=request.user)
        return request.user == project.author_user_id


class IssuePermission(BasePermission):
    def has_permission(self, request, view):
        project = get_object_or_404(Issue, id=view.kwargs['project_pk'])
        try:
            issue = get_object_or_404(Issue, id=view.kwargs['issue_pk'])
            return request.user == issue.author
        except KeyError:
            return project in Project.object.filter(contributors__user=request.user)


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['project_pk'])
        try:
            comment = get_object_or_404(Comment, id=view.kwargs['comment_pk'])
            if request.method in permissions.SAFE_METHODS:
                return project in Project.objects.filter(contributors__user=request.user)
            return request.user == comment.author_id
        except KeyError:
            return project in Project.objects.filter(contributors__id=request.user)
