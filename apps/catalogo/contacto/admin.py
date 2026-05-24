from django.contrib import admin
from apps.catalogo.contacto.models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['nombre', 'apellido', 'telefono', 'correo', 'tipo_cliente', 'departamento', 'servicio_interes', 'comentario', 'fecha_registro']

# Register your models here.
