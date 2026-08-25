from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutor/', include('tutor.urls')),
    path('pet/', include('pet.urls')),
]
