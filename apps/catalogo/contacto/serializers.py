from rest_framework import serializers
from .models import Contacto


class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacto

        fields = [
            'nombre',
            'apellido',
            'telefono',
            'correo',
            'tipo_cliente',
            'departamento',
            'servicio_interes',
            'comentario',
            'fecha_registro'
        ]
        read_only_fields = ['fecha_registro']