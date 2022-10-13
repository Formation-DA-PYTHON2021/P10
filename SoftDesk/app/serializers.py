from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only__fields = ('author_id', 'issue_id', 'comment_id', 'created_time')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class IssueListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'
        read_only__fields = ('project_id', 'author', 'title', 'created_time')

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)


class IssueDetailSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = '__all__'
        read_only__fields = ('project_id', 'author', 'title', 'created_time')

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def get_comments(self, instance):
        queryset = instance.comments.filter(active=True)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only__fields = ('author', 'project_id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError('Le nom du projet existe déjà')
        return value


class ProjectDetailSerializer(serializers.ModelSerializer):

    issues = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'
        read_only__fields = ('author', 'project_id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def get_issues(self, instance):
        queryset = instance.issues.filter(active=True)
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data


class ContributorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project_id', 'role', 'contributor_id')

    def create(self, validated_data):
        return Contributor.objects.create(**validated_data)

class ContributorDetailSerializer(serializers.ModelSerializer):

    projects = serializers.SerializerMethodField()

    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project_id', 'role', 'contributor_id')

    def create(self, validated_data):
        return Contributor.objects.create(**validated_data)

    def get_projects(self, instance):
        queryset = instance.issues.filter(active=True)
        serializer = ProjectListSerializer(queryset, many=True)
        return serializer.data
