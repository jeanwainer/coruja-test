from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Customers API",
      default_version='v1',
      description="CORUJA techincal test API",
      contact=openapi.Contact(email="wainer@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('api/', include('core.urls')),
    re_path(r'swagger(?P<format>\.json|\.yaml$)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




