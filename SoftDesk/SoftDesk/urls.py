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
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.Views import ProjectViewset, IssueViewset, CommentViewset, ContributorViewset, SignupViewset

router = routers.SimpleRouter()
router.register(r"projects/?", ProjectViewset, basename='projects')

issue_router = routers.NestedSimpleRouter(
    router,
    r"projects/?",
    lookup="project",
    trailing_slash=False
)
issue_router.register(r"issues/?", IssueViewset, basename="issues")

comment_router = routers.NestedSimpleRouter(
    issue_router,
    r"issues/?",
    lookup="issue",
    trailing_slash=False
)
comment_router.register(r"comments/?", CommentViewset, basename="comments")

contributor_router = routers.NestedSimpleRouter(
    router,
    r"projects/?",
    lookup="project",
    trailing_slash=False
)
contributor_router.register(r"users/?", ContributorViewset, basename="users")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupViewset.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'', include(router.urls)),
    path(r'', include(issue_router.urls)),
    path(r'', include(comment_router.urls)),
    path(r'', include(contributor_router.urls)),
]
