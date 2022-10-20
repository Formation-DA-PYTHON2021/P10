from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView
from django.conf import settings

from .models import Project, Issue, Comment, Contributor
from .serializers import (
    UserSerializer,
    SignupSerializer,
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer)
from .permissions import (
    IsAuthenticated,
    ProjectPermission,
    ContributorPermissions,
    IssuePermission,
    CommentPermission)


class SignupViewset(GenericAPIView):

    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data})

class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Project.objects.filter(id__in=project_ids)

    def list(self, request,):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)

        queryset = Project.objects.filter(id__in=project_ids)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)

        queryset = Project.objects.filter(id__in=project_ids)
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IssuePermission]

    def get_queryset(self):
        user = self.request.user
        user_contrib = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contrib:
            project_ids.append(contrib.project_id.id)
        return Issue.objects.filter(id__in=project_ids)

    def list(self, request, project_pk=None):
        queryset = Issue.objects.filter(project=project_pk)
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Issue.objects.filter(pk=pk, project=project_pk)
        issue = get_object_or_404(queryset, pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ContributorPermissions]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []
        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Contributor.objects.filter(id__in=project_ids)

    def list(self, request, project_pk=None):
        queryset = Contributor.objects.filter(project=project_pk)
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Contributor.objects.filter(pk=pk, project=project_pk)
        contributor = get_object_or_404(queryset, pk=pk)
        serializer = IssueSerializer(contributor)
        return Response(serializer.data)


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentPermission]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Comment.objects.filter(id__in=project_ids)

    def list(self, request, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(issue_id__project=project_pk, issue_id=issue_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(pk=pk, issue_id=issue_pk, issue_id__project=project_pk)
        issue = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(issue)
        return Response(serializer.data)
