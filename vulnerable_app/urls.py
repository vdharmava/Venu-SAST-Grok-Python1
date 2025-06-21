from django.urls import path, include

urlpatterns = [
    path('', include('auth_app.urls')),
    # Vuln 12: CWE-306 - Missing Authentication for Critical Function
    path('admin/', include('django.contrib.admin.urls')),
]
