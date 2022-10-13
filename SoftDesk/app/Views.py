from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Project, Issue, Comment
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ContributorDetailSerializer,
    ContributorListSerializer,
    IssueListSerializer,
    IssueDetailSerializer,
    CommentSerializer)
from .permissions import (
    IsAdminAuthenticated,
    ProjectPermission,
    ContributorPermissions,
    IssuePermission,
    CommentPermission)


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAdminAuthenticated, ProjectPermission]

    def get_queryset(self):
        return Project.objects.filter(active=True)

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get.object().disable()
        return Response


class IssueViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAdminAuthenticated, IssuePermission]

    def get_queryset(self):
        queryset = Issue.objects.filter(active=True)
        project_id = self.request.GET.get('project_id')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response


class ContributorViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContributorListSerializer
    serializer_class = ContributorDetailSerializer
    permission_classes = [IsAdminAuthenticated, ContributorPermissions]

    def get_queryset(self):
        queryset = Project.objects.filter(active=True)
        project_id = self.request.GET.get('project_id')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAdminAuthenticated, CommentPermission]

    def get_queryset(self):
        queryset = Comment.objects.filter(active=True)
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset
