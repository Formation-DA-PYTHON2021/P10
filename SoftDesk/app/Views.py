from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework import status

from .models import Project, Issue, Comment, Contributor
from .serializers import (
    UserSerializer,
    SignupSerializer,
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer)
from .permissions import (
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
        return Response(
            {
                "user": UserSerializer(
                    user,
                    context=self.get_serializer_context()).data
            }
        )


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission, IsAuthenticated]

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

    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = {
            "title": request.POST.get('title', None),
            "description": request.POST.get('description', None),
            "type": request.POST.get('type', None),
            "author": request.POST.get('author', None),
        }
        serializer = self.serializer_class(data=data, context={'author': user})
        if serializer.is_valid():
            serializer.save()
            project = serializer.save()
            try:
                contributor = Contributor.objects.create(project_id=project,
                                                         user_id=user,
                                                         role='AUTHOR')
            except TypeError:
                error_message = {
                    'error': 'failed to create contributor',
                }
                raise APIException(detail=error_message)

            contributor.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IssuePermission, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_contrib = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contrib:
            project_ids.append(contrib.project_id.id)
        return Issue.objects.filter(id__in=project_ids)

    def list(self, request, project_pk=None):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []
        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)

        queryset = Issue.objects.filter(project_id=project_pk)
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Issue.objects.filter(pk=pk, project_id=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = IssueSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None, project_pk=None, **kwargs):
        partial = kwargs.pop('partial', False)
        queryset = Issue.objects.filter(pk=pk, project_id=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, pk=None, project_pk=None):
        queryset = Issue.objects.filter(pk=pk, project_id=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Contributor.objects.filter(id__in=project_ids)

    def list(self, request, project_pk=None):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []
        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)

        queryset = Contributor.objects.filter(project_id=project_pk)
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Contributor.objects.filter(pk=pk, project_id=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ContributorSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None, project_pk=None):
        queryset = Contributor.objects.filter(pk=pk, project_id=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [CommentPermission, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributor.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.project_id.id)
        return Comment.objects.filter(id__in=project_ids)

    def list(self, request, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(issue_id__project=project_pk,
                                          issue_id=issue_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(pk=pk,
                                          issue_id=issue_pk,
                                          issue_id__project=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(instance)
        return Response(serializer.data)

    def update(self, request,
               pk=None,
               project_pk=None,
               issue_pk=None,
               **kwargs):
        partial = kwargs.pop('partial', False)
        queryset = Comment.objects.filter(pk=pk,
                                          issue_id=issue_pk,
                                          issue_id__project=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, pk=None, project_pk=None, issue_pk=None,):
        queryset = Comment.objects.filter(pk=pk,
                                          issue_id=issue_pk,
                                          issue_id__project=project_pk)
        instance = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
