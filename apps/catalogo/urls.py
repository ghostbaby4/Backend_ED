from django.urls import path, include

from apps.catalogo.contacto.views import ContactoAPIView

urlpatterns = [
    path('contactos/', include('apps.catalogo.contacto.urls')),
]