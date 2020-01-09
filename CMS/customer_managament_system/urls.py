from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('api_registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
