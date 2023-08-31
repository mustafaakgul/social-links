from django.urls import path
from apps.accounts.api.views import (
                        ProfileView,
                        UpdatePasswordView,
                        CreateUserView,
                        UpdateProfileView,
                        LogoutView
                        )


app_name = "accounts"


urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
    path('update', UpdateProfileView.as_view(), name='update_profile'),

    path('change-password', UpdatePasswordView.as_view(), name='change_password'),
    path('register', CreateUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]