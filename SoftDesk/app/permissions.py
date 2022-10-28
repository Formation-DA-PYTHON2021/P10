from rest_framework import permissions
from .models import Project, Contributor


def valid_contrib(user, project):
    for contrib in Contributor.objects.filter(project_id=project.id):
        if user == contrib.user_id:
            return True
    return False


class ContributorPermissions(permissions.BasePermission):
    """
    Les contributeurs peuvent voir d'autres contributeurs et lire les détails les concernant.
    Les auteurs peuvent voir, lire, ajouter, mettre à jour ou supprimer un contributeur.
    """

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if valid_contrib(request.user, project):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        return False


class ProjectPermission(permissions.BasePermission):
    """
    Tout le monde peut créer un projet.
    Les auteurs peuvent créer, lire, mettre à jour et supprimer un projet.
    Les contributeurs peuvent voir leurs projets, lire un projet.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'list']:
            return valid_contrib(request.user, obj)

        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.author


class IssuePermission(permissions.BasePermission):
    """
    L'auteur d'une issue peut mettre à jour et supprimer ses issues.
    Les contributeurs du projet peuvent lister tous les problèmes du projet, lire les problèmes ou créer des problèmes.
    """

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if valid_contrib(request.user, project):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        return False


class CommentPermission(permissions.BasePermission):

    """
    Les auteurs de commentaires peuvent mettre à jour ou supprimer leurs commentaires.
    Les contributeurs du projet peuvent Lister tous les commentaires d'une issue, Lire un commentaire ou
    Créer un commentaire.
    """

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if valid_contrib(request.user, project):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        return False
