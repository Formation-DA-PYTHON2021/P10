"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.Views import ProjectViewset

router = routers.SimpleRouter()
router.register('projects', ProjectViewset, basename='projects')
"""router.register('projects/{id}', ProjectViewset, basename='projects_id')
router.register('projects/{id}/users', ContributorViewset, basename='projects_id_user')
router.register('projects/{id}/user/{id}', ProjectViewset, basename='projects_id_user_id')
router.register('projects/{id}/issues', IssueViewset, basename='issues')
router.register('projects/{id}/issues/{id}', IssueViewset, basename='issues_id')
router.register('projects/{id}/issues/{id}/comments', CommentViewset, basename='comments')
router.register('projects/{id}/issues/{id}/comments/{id}', CommentViewset, basename='comments_id')
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]

"""    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),"""