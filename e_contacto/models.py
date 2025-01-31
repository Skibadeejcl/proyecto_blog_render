from django.db import models
import datetime

opciones_consultas = [
    [0, "Consulta"],
    [1, "Publicarme"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    correo = models.EmailField(null=False)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    tipo_consulta = models.IntegerField(choices=opciones_consultas, null=False)
    mensaje = models.TextField(null=False)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nombre
    

