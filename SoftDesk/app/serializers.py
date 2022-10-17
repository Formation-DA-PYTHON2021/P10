from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only__fields = ('author_id', 'issue_id', 'comment_id', 'created_time')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'
        read_only__fields = ('author', 'title', 'created_time', 'assignee_user_id')

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only__fields = ('author_user_id',)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError('Le nom du projet existe déjà')
        return value


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project_id', 'role', 'user_id')

    def create(self, validated_data):
        return Contributor.objects.create(**validated_data)
