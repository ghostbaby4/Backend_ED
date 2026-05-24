from django.contrib import admin
from apps.seguridad.usuarios.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    pass

# Register your models here.
