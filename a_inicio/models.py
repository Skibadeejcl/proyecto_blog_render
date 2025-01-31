from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from moviepy import VideoFileClip
from django.core.exceptions import ValidationError
import tempfile
from PIL import Image
import os
from django.conf import settings
import uuid


# Create your models here.

class Usuario(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

class Tipo_usuario(models.Model):
    tipo_usuario = models.TextField()

    def __str__(self):
        return self.tipo_usuario

class Tipo_nation(models.Model):
    tipo_nation = models.TextField()

    def __str__(self):
        return self.tipo_nation

class Comuna(models.Model):
    comuna = models.CharField(max_length=100)
    codigo_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='codigo_region', blank=True, null=True)

    def __str__(self):
        return self.comuna

class Region(models.Model):
    Region = models.CharField(max_length=100)

    def __str__(self):
        return self.Region

#class Tipo_user(models.Model):
#    tipo_user = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #id_tipo_user = models.ForeignKey('a_inicio.Tipo_user', on_delete=models.CASCADE, null=True)
    rut = models.TextField(max_length=20, unique=True, null=False)                   #Eliminar y cambiar por "RUT, DNI o N° Pasaporte" (sacar lógica de comprobación de RUT)
    # direccion = models.TextField()
    # telefono = models.TextField()
    # nickname = models.TextField()
    #correo = models.TextField()

class Dias_lab(models.Model):
    dias_lab = models.CharField(max_length=100)

    def __str__(self):
        return self.dias_lab

class Horario(models.Model):
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.horario
    
class Servicio(models.Model):
    servicio = models.CharField(max_length=100)

    def __str__(self):
        return self.servicio

def validar_duracion_video(value):
    max_duration = 8  # Duración máxima en segundos
    clip = None

    try:
        # Si Django está manejando el archivo con un manejador temporal
        if hasattr(value, 'temporary_file_path'):
            clip = VideoFileClip(value.temporary_file_path())  # Usamos el archivo temporal proporcionado por Django
        else:
            # Si no es un archivo temporal, lo manejamos de otra manera
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(value.read())  # Escribimos el archivo temporal
                temp_file.flush()
                clip = VideoFileClip(temp_file.name)  # Procesamos el archivo temporal

        # Comprobamos si la duración supera el máximo permitido
        if clip.duration > max_duration:
            raise ValidationError(f"La duración del video no puede superar los {max_duration} segundos.")
    except Exception as e:
        raise ValidationError(f"No se pudo procesar el video. Error: {e}")
    finally:
        if clip:
            clip.reader.close()  # Cierra el archivo de video
            if clip.audio:
                try:
                    clip.audio.reader.close_proc()  # Cierra el proceso de audio si está presente
                except AttributeError:
                    pass  # Si no tiene audio o no se puede cerrar el proceso, lo ignoramos

class Clientes(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    id_tipo_usuario = models.ForeignKey('a_inicio.Tipo_usuario', on_delete=models.CASCADE, null=True) # Ho, Mu, Tra, Mas
    id_tipo_nation = models.ForeignKey('a_inicio.Tipo_nation', on_delete=models.CASCADE, null=True) # chi, arg, per, col, etc
    id_comuna = models.ForeignKey('a_inicio.Comuna', on_delete=models.CASCADE, null=True)
    id_region = models.ForeignKey('a_inicio.Region', on_delete=models.CASCADE, null=True)
    nickname = models.CharField(default="No name", max_length=30)
    estado = models.CharField(max_length=50, default='', blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    telefono = models.CharField(default=0, max_length=9)
    id_dias_lab = models.ForeignKey('a_inicio.Dias_lab', on_delete=models.CASCADE, null=True)
    id_horario = models.ForeignKey('a_inicio.Horario', on_delete=models.CASCADE, null=True)
    medida_alta = models.IntegerField(default=0)
    medida_media = models.IntegerField(default=0)
    medida_baja = models.IntegerField(default=0)
    estatura = models.CharField(max_length=4)
    ubicacion = models.CharField(max_length=200)
    metro = models.CharField(max_length=200, default='', blank=True, null=True)
    edad = models.IntegerField(default=0)
    id_servicio = models.ForeignKey('a_inicio.Servicio', on_delete=models.CASCADE, null=True)
    servicios_add = models.CharField(max_length=200, default='', blank=True, null=True)
    tarifa = models.IntegerField(default=0)
    video_file = models.FileField(upload_to="a_inicio/videos", blank=True, null=True, validators=[validar_duracion_video])  # Directorio donde se guardarán los videos
    image_portada1 = models.ImageField(upload_to="a_inicio/images", default="bootcamp-desarrollo-aplicaciones-full-stack-python-trainee.png")
    image_estado = models.ImageField(upload_to="a_inicio/images", blank=True, null=True)  # Imagen del estado
    image1 = models.ImageField(upload_to="a_inicio/images")
    image2 = models.ImageField(upload_to="a_inicio/images")
    image3 = models.ImageField(upload_to="a_inicio/images")
    image4 = models.ImageField(upload_to="a_inicio/images", blank=True)
    image5 = models.ImageField(upload_to="a_inicio/images", blank=True)
    image6 = models.ImageField(upload_to="a_inicio/images", blank=True)
    image7 = models.ImageField(upload_to="a_inicio/images", blank=True)
    image8 = models.ImageField(upload_to="a_inicio/images", blank=True)
    image9 = models.ImageField(upload_to="a_inicio/images", blank=True)
    image10 = models.ImageField(upload_to="a_inicio/images", blank=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    last_updated = models.DateTimeField(auto_now=True)  # Fecha y hora de la última actualización
    mostrar = models.BooleanField(default=False)
    # preferencial = models.BooleanField(default=False)

#    , null=True, default="logo_navbar.jpg"
#   image5 = models.ImageField(upload_to="a_inicio/images", blank=True, default="logo_navbar.jpg")

    def get_estado(self):
        return self.estado
    
    
    def save(self, *args, **kwargs):
        # Lista de los campos de imagen y video que deseas manejar
        campos_archivo = [
            'video_file', 'image_portada1', 'image_estado', 'image1', 'image2', 'image3',
            'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10'
        ]

        # Diccionario para almacenar las rutas de los archivos antiguos
        archivos_antiguos = {}

        # Verificar si la instancia ya existe en la base de datos
        if self.pk:
            try:
                instancia_anterior = Clientes.objects.get(pk=self.pk)
                for campo in campos_archivo:
                    archivo_anterior = getattr(instancia_anterior, campo)
                    archivo_actual = getattr(self, campo)

                    # Si el archivo ha cambiado, almacenarlo
                    if archivo_anterior and archivo_anterior != archivo_actual:
                        if os.path.exists(archivo_anterior.path):
                            archivos_antiguos[campo] = archivo_anterior.path

                            # Si es un video, intentar procesarlo
                            if campo == 'video_file' and archivo_anterior.name.endswith(('mp4', 'avi', 'mov', 'mpg')):
                                try:
                                    clip = VideoFileClip(archivo_anterior.path)
                                    clip.reader.close()  # Cierra el archivo de video
                                    if clip.audio:
                                        try:
                                            clip.audio.reader.close_proc()  # Cierra el proceso del audio si está presente
                                        except AttributeError:
                                            pass
                                except Exception as e:
                                    print(f"Error al procesar el video {archivo_anterior.name}: {e}")
                                os.remove(archivo_anterior.path)  # Eliminar el archivo anterior de video
            except Clientes.DoesNotExist:
                pass

        # Guardar la instancia antes de procesar las imágenes
        super().save(*args, **kwargs)

        # Ruta de la marca de agua
        watermark_path = os.path.join(settings.MEDIA_ROOT, "marca_de_agua.png")
        if not os.path.exists(watermark_path):
            print("⚠️ Marca de agua no encontrada. Se omite el procesamiento.")
            return

        # Lista de campos de imagen a procesar
        image_fields = [
            'image_portada1', 'image_estado', 'image1', 'image2', 'image3', 'image4',
            'image5', 'image6', 'image7', 'image8', 'image9', 'image10'
        ]

        for field_name in image_fields:
            image_field = getattr(self, field_name)
            if image_field:  # Verifica si hay una imagen en este campo
                image_path = os.path.join(settings.MEDIA_ROOT, image_field.name)

                # Verificar que el archivo exista antes de procesarlo
                if os.path.exists(image_path):
                    with Image.open(image_path) as img:
                        img = img.convert("RGBA")  # Convertir a RGBA para soportar transparencias

                        # Cargar la imagen de la marca de agua
                        with Image.open(watermark_path) as watermark:
                            watermark = watermark.convert("RGBA")

                            # Ajustar la opacidad de la marca de agua
                            opacity = 150  # Valor entre 0 (transparente) y 255 (opaco)
                            watermark = watermark.copy()
                            alpha = watermark.split()[3]  # Extrae el canal alfa de la marca de agua
                            alpha = alpha.point(lambda p: p * (opacity / 255))  # Ajusta la opacidad
                            watermark.putalpha(alpha)

                            # Redimensionar la marca de agua proporcionalmente al tamaño de la imagen original
                            scale_factor = 0.3  # Ajusta el tamaño de la marca de agua (30% del ancho de la imagen)
                            watermark = watermark.resize(
                                (int(img.width * scale_factor),
                                 int(watermark.height * img.width / watermark.width * scale_factor)),
                                Image.ANTIALIAS
                            )

                            # Determinar la posición de la marca de agua (esquina inferior derecha)
                            watermark_position = (
                                img.width - watermark.width - 10,  # 10 px de margen a la derecha
                                img.height - watermark.height - 10  # 10 px de margen inferior
                            )

                            # Combinar la marca de agua con la imagen original usando transparencia
                            img.paste(watermark, watermark_position, watermark)

                        # Crear un nuevo nombre para la imagen con un UUID
                        new_filename = f"{uuid.uuid4()}.jpg"
                        new_image_path = os.path.join(settings.MEDIA_ROOT, "a_inicio/images", new_filename)

                        # Sobrescribir el archivo original con la imagen resultante (convertir a RGB para guardar como JPEG)
                        img = img.convert("RGB")
                        img.save(new_image_path, "JPEG", quality=90)  # Cambia la calidad si lo necesitas

                        # Actualizar el campo de la imagen con el nuevo nombre
                        setattr(self, field_name, f"a_inicio/images/{new_filename}")

                        # Guardar los cambios en la instancia
                        super().save(update_fields=[field_name])

                        # Eliminar la imagen original (antes de la marca de agua) si no es la misma
                        if os.path.exists(image_path):
                            os.remove(image_path)

        # Eliminar imágenes y videos antiguos si han sido reemplazados o limpiados
        for field_name, old_image_path in archivos_antiguos.items():
            new_image_field = getattr(self, field_name)

            # Si el archivo de imagen ha cambiado, eliminar el archivo anterior
            if new_image_field and old_image_path != new_image_field.path:
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            # Si el campo ha sido limpiado (casilla "Limpiar" activada), eliminar la imagen resultante
            if not new_image_field and old_image_path and os.path.exists(old_image_path):
                os.remove(old_image_path)









    def delete(self, *args, **kwargs):
        # Lista de los campos de imagen y video que deseas manejar
        campos_archivo = [
            'video_file', 'image_portada1', 'image_estado',
            'image1', 'image2', 'image3', 'image4', 'image5',
            'image6', 'image7', 'image8', 'image9', 'image10'
        ]

        # Eliminar los archivos asociados antes de borrar la entrada
        for campo in campos_archivo:
            archivo = getattr(self, campo)
            if archivo and os.path.exists(archivo.path):
                if campo == 'video_file' and archivo.name.endswith(('mp4', 'avi', 'mov', 'mpg')):
                    try:
                        clip = VideoFileClip(archivo.path)
                        clip.reader.close()  # Cierra el archivo de video
                        if clip.audio:
                            try:
                                clip.audio.reader.close_proc()  # Cierra el proceso del audio si está presente
                            except AttributeError:
                                pass
                    except Exception:
                        pass  # Ignorar errores al cerrar el archivo de video
                os.remove(archivo.path)  # Eliminar el archivo

        # Eliminar la instancia del modelo
        super().delete(*args, **kwargs)

    
    # def save(self, *args, **kwargs):
    #     # Guardar la imagen original primero
    #     super().save(*args, **kwargs)

    #     # Ruta completa de la imagen subida
    #     image_path = os.path.join(settings.MEDIA_ROOT, self.image_portada1.name)

    #     # Abrir la imagen subida
    #     with Image.open(image_path) as img:
    #         img = img.convert("RGBA")  # Convertir a RGBA para soportar transparencias

    #         # Cargar la imagen de la marca de agua
    #         watermark_path = os.path.join(settings.MEDIA_ROOT, "marca_de_agua.png")
    #         with Image.open(watermark_path) as watermark:
    #             watermark = watermark.convert("RGBA")

    #             # Redimensionar la marca de agua proporcionalmente al tamaño de la imagen original
    #             scale_factor = 0.3  # Ajusta el tamaño de la marca de agua (30% del ancho de la imagen)
    #             watermark = watermark.resize(
    #                 (int(img.width * scale_factor), int(watermark.height * img.width / watermark.width * scale_factor)),
    #                 Image.ANTIALIAS
    #             )

    #             # Determinar la posición de la marca de agua (esquina inferior derecha)
    #             watermark_position = (
    #                 img.width - watermark.width - 10,  # 10 px de margen a la derecha
    #                 img.height - watermark.height - 10  # 10 px de margen inferior
    #             )

    #             # Combinar la marca de agua con la imagen original
    #             img.paste(watermark, watermark_position, watermark)

    #         # Sobrescribir el archivo original con la imagen resultante (convertir a RGB para guardar como JPEG)
    #         img = img.convert("RGB")
    #         img.save(image_path, "JPEG", quality=90)  # Cambia la calidad si lo necesitas



@receiver(post_delete, sender=Clientes)
def eliminar_archivos_asociados(sender, instance, **kwargs):
    # Lista de los campos de imagen y video que deseas manejar
    campos_archivo = ['video_file', 'image_portada1', 'image_estado', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10']

    for campo in campos_archivo:
        archivo = getattr(instance, campo)
        if archivo and os.path.exists(archivo.path):
            if campo == 'video_file' and archivo.name.endswith(('mp4', 'avi', 'mov', 'mpg')):
                try:
                    clip = VideoFileClip(archivo.path)
                    clip.reader.close()  # Cierra el archivo de video
                    if clip.audio:
                        try:
                            clip.audio.reader.close_proc()  # Cierra el proceso del audio si está presente
                        except AttributeError:
                            pass  # Si no tiene audio o no se puede cerrar el proceso, lo ignoramos
                except Exception:
                    pass  # Ignorar si el video no puede ser procesado
            os.remove(archivo.path)  # Eliminar el archivo asociado