from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),  # Esto enlaza las rutas de 'polls' a la raíz del sitio
    path('admin/', admin.site.urls),
]

