from rest_framework.viewsets import ModelViewSet


from .models import Project, Issue, Comment, Contributor
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer)
from .permissions import (
    IsAdminAuthenticated,
    ProjectPermission,
    ContributorPermissions,
    IssuePermission,
    CommentPermission)


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IssuePermission, ProjectPermission]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Project.objects.filter(id__in=project_ids)


class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAdminAuthenticated, IssuePermission]

    def get_queryset(self):
        user = self.request.user
        user_contrib = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contrib:
            project_ids.append(contrib.project_id.id)
        return Issue.objects.filter(id__in=project_ids)


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAdminAuthenticated, ContributorPermissions]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []
        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Contributor.objects.filter(id__in=project_ids)


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAdminAuthenticated, CommentPermission]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Comment.objects.filter(id__in=project_ids)
