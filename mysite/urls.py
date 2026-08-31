from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('tutor/', include('tutor.urls')),
    path('pet/', include('pet.urls')),
]
=======
    path('pet/', include('pet.urls')),
<<<<<<< HEAD
    path('tutor/', include('tutor.urls')),
]
>>>>>>> 69d85cd120c33d9eb80c9fb0b5e5f1b52e5271c9
=======
]
>>>>>>> c4f1770c51029167788f53a46aa7ece544801fd3
