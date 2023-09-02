"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from apps.common.views import HomeView, AboutView, trigger_error, loggerDefault

# api/v1/... -> Semantic Versioning 1.0.0 MAJOR.MINOR.PATCH

urlpatterns = [
    # Versioning
    # path('api/v2/', include(('your_app.urls', 'your_app'), namespace='v1')),
    # path('api/v3/', include(('your_app_v2.urls', 'your_app_v2'), namespace='v2')),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App's Endpoints
    path('sentry-debug/', trigger_error),
    path("logging/", loggerDefault, name="app_base_logging"),
    path('api/v1/home/', HomeView.as_view(), name='home'),
    path('api/v1/about', AboutView, name='about'),
    path('api/v1/accounts/', include('apps.accounts.api.urls')),
    path('api/v1/links/', include('apps.links.api.urls')),
    path('api/v1/tags/', include('apps.tags.api.urls')),
    path('api/v1/sentry/', trigger_error),
]
