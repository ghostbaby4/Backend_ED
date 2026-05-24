from django.db import models

class Contacto(models.Model):

    TIPOS_CLIENTE = [
        ('Persona', 'Persona'),
        ('Empresa', 'Empresa'),
    ]

    DEPARTAMENTOS = [
        ('Managua', 'Managua'),
        ('León', 'León'),
        ('Granada', 'Granada'),
        ('Masaya', 'Masaya'),
        ('Carazo', 'Carazo'),
        ('Chinandega', 'Chinandega'),
        ('Estelí', 'Estelí'),
        ('Matagalpa', 'Matagalpa'),
        ('Jinotega', 'Jinotega'),
        ('Boaco', 'Boaco'),
    ]

    SERVICIOS = [
        ('Soporte técnico', 'Soporte técnico'),
        ('Mantenimiento preventivo', 'Mantenimiento preventivo'),
        ('Instalación de redes', 'Instalación de redes'),
        ('Reparación de equipos', 'Reparación de equipos'),
    ]

    nombre = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    telefono = models.CharField(max_length=20)

    correo = models.EmailField()

    tipo_cliente = models.CharField(
        max_length=20,
        choices=TIPOS_CLIENTE
    )

    departamento = models.CharField(
        max_length=50,
        choices=DEPARTAMENTOS
    )

    servicio_interes = models.CharField(
        max_length=100,
        choices=SERVICIOS
    )

    comentario = models.TextField()

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre