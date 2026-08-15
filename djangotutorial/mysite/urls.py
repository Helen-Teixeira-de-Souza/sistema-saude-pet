from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redireciona todas as rotas da clínica para o app 'clinica'
    path('', include('clinica.urls')), 
]