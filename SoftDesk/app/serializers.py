from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Contributor, Issue, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'issue_pk': 'issue_id__pk',
        'project_pk': 'issue_id__project__pk'
    }
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class IssueSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project_pk',
    }
    class Meta:
        model = Issue
        fields = '__all__'

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError('Le nom du projet existe déjà')
        return value


class ContributorSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project_pk',
    }
    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project_id', 'role', 'user_id')

    def create(self, validated_data):
        return Contributor.objects.create(**validated_data)
