from rest_framework.serializers import ModelSerializer

from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only__fields = ('author', 'project_id')


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project_id', 'role', 'contributor_id')


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'
        read_only__fields = ('project_id', 'author', 'title', 'created_time')


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only__fields = ('author_id', 'issue_id', 'comment_id', 'created_time')
