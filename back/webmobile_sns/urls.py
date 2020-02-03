"""webmobile_sns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import check_token


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="This is for a SNS which allows someone to write something at the middle of the night",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="midnight@ssafy.com"),
      license=openapi.License(name="SSAFY License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    # path('api/v1/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token, name='auth-token'),
    path('api/check/', check_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
