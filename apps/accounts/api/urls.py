from django.urls import path
from apps.accounts.api.views import (
                        ProfileView,
                        UpdatePasswordView,
                        CreateUserView,
                        UpdateProfileView,
                        LogoutView,
                        LogoutAllView
                        )


app_name = "accounts"


urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
    path('update', UpdateProfileView.as_view(), name='auth_update_profile'),

    path('change-password', UpdatePasswordView.as_view(), name='auth_change_password'),
    path('register', CreateUserView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]