from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('import/', views.import_data, name='import'),
    path('xml/', views.parse_xml, name='xml'),
    path('fetch/', views.fetch_url, name='fetch'),
    path('uaf/', views.use_after_free, name='uaf'),
    path('dangerous/', views.dangerous_function, name='dangerous'),
    path('vuln/', views.vulnerable_endpoint, name='vuln'),
]
