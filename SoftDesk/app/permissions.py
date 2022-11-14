from rest_framework import permissions
from .models import Contributor


class ContributorPermissions(permissions.BasePermission):
    """
    Les contributeurs peuvent voir d'autres contributeurs
    et lire les détails les concernant.
    Les auteurs peuvent voir, lire, ajouter, mettre à jour
    ou supprimer un contributeur.
    """

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs['pk']
        contributors = [
            contrib.user_id for contrib in Contributor.objects.filter(
                project_id=project_id).select_related('project_id')
        ]

        contributors.append(obj.author.id)

        if request.method in permissions.SAFE_METHODS:
            return bool(request.user in contributors)

        return bool(obj.author.id == request.user.id)


class ProjectPermission(permissions.BasePermission):
    """
    Tout le monde peut créer un projet.
    Les auteurs peuvent créer, lire, mettre à jour et supprimer un projet.
    Les contributeurs peuvent voir leurs projets, lire un projet.
    """

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs['pk']
        contributors = [
            contrib.user_id for contrib in Contributor.objects.filter(
                project_id=project_id).select_related('project_id')
        ]

        contributors.append(obj.author.id)
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user in contributors)

        return bool(obj.author.id == request.user.id)


class IssuePermission(permissions.BasePermission):
    """
    L'auteur d'une issue peut mettre à jour et supprimer ses issues.
    Les contributeurs du projet peuvent lister tous les problèmes du projet,
    lire les problèmes ou créer des problèmes.
    """

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs['pk']
        contributors = [
            contrib.user_id for contrib in Contributor.objects.filter(
                project_id=project_id).select_related('project_id')
        ]

        contributors.append(obj.author.id)

        if request.method in permissions.SAFE_METHODS:
            return bool(request.user in contributors)
        return bool(obj.author.id == request.user.id)


class CommentPermission(permissions.BasePermission):

    """
    Les auteurs de commentaires peuvent mettre à jour ou
    supprimer leurs commentaires.
    Les contributeurs du projet peuvent Lister tous
    les commentaires d'une issue,
    Lire un commentaire ou
    Créer un commentaire.
    """

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs['pk']
        contributors = [
            contrib.user_id for contrib in Contributor.objects.filter(
                project_id=project_id).select_related('project_id')
        ]

        contributors.append(obj.author.id)

        if request.method in permissions.SAFE_METHODS:
            return bool(request.user in contributors)
        return bool(obj.author.id == request.user.id)
