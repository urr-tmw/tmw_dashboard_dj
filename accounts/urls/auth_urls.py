from django.urls import path

from accounts.views.auth.login_view import LoginAPIView
from accounts.views.auth.refresh_token_view import RefreshTokenAPIView
from accounts.views.auth.logout_view import LogoutAPIView
from accounts.views.auth.me_view import MeAPIView
urlpatterns = [
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),
    path(
    "refresh/",
    RefreshTokenAPIView.as_view(),
    name="refresh-token",
),
    path(
        "logout/",
        LogoutAPIView.as_view(),
        name="logout",
    ),
    path(
        "me/",
        MeAPIView.as_view(),
        name="current-user",
    ),
]