from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Comuna, Region, Clientes, Tipo_usuario, Tipo_nation, Dias_lab, Horario, Servicio

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    first_name.label = 'Nombres'
    last_name = forms.CharField()
    last_name.label = 'Apellidos'
    email = forms.EmailField(validators=[EmailValidator()])
    email.label = 'Correo Electrónico'

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = { 'username':_("Nombre de Usuario para Iniciar Sesión")}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("El correo electrónico ya está registrado. Por favor, usa otro."))
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(_("El nombre de usuario ya está registrado. Por favor, elige otro."))
        return username

class TipoForm(forms.Form):
    # tipos_usuario = ((1,"Mujer"),(2,"Hombre"),(3,"Transexual"),(4,"Masajista"))
    # id_tipo_usuario = forms.ChoiceField(choices=[(k, '{} - {}'.format(k, v)) for (k, v) in tipos_usuario], label='Yo soy (Seleccionar)')
    rut = forms.CharField(label='rut', max_length=20)
    # direccion = forms.CharField(label='direccion', max_length=100)
    # nickname = forms.CharField(label='Seudónimo/Nombre de artístico', max_length=100)
    # telefono = forms.CharField(label='telefono', max_length=100)

    # def clean_rut(self):
    #     rut = self.cleaned_data.get('rut')
    #     print(f"Verificando RUT: {rut}")  # Depuración: verifique el valor de rut
    #     if Clientes.objects.filter(rut=rut).exists():
    #         raise ValidationError(_("El N° de Documento ya está registrado."))
    #     return rut

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email']
        labels = {'email':_('Nuevo Correo Electrónico')}

# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name', 'last_name', 'email']
#         labels = {'first_name':_('Nombre'), 'last_name':_('Apellidos'), 'email':_('Correo Electrónico')}

def validar_tarifa(valor):
    try:
        # Intenta convertir el valor a un número
        float(valor.replace(",", "").replace(".", ""))
    except ValueError:
        raise ValidationError("La tarifa debe ser un número válido.")


class ClienteForm(forms.Form):
    tipos_usuario = [(x.id,x.tipo_usuario) for x in list(Tipo_usuario.objects.filter())]
    id_tipo_usuario = forms.ChoiceField(choices=tipos_usuario, label='Yo Soy (Seleccionar)')

    tipos_nation = [(x.id,x.tipo_nation) for x in list(Tipo_nation.objects.filter())]
    id_tipo_nation = forms.ChoiceField(choices=tipos_nation, label='Nacionalidad (Seleccionar)')
    
    

    # def nombre_comuna(e):
    #     return e[1]
    # comunas.sort(key=nombre_comuna)

    # id_comuna = forms.ChoiceField(choices=comunas, label='Comuna (Seleccionar)')
    # regiones = [(x.id,x.Region) for x in list(Region.objects.filter())]
    # id_region = forms.ChoiceField(choices=regiones, label='Región (Seleccionar)')

    regiones = [(x.id, x.Region) for x in list(Region.objects.all())]
    id_region = forms.ChoiceField(
        choices=[("", "Seleccionar Región")] + regiones,
        label="Región (Seleccionar)",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_region"}),
    )

    comunas = [(x.id,x.comuna) for x in list(Comuna.objects.filter())]
    id_comuna = forms.ChoiceField(
        choices=[("", "Seleccionar Comuna")]+ comunas,
        label="Comuna (Seleccionar)",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_comuna"}),
    )

    dias_labs = [(x.id,x.dias_lab) for x in list(Dias_lab.objects.filter())]
    id_dias_lab = forms.ChoiceField(
        choices=[("", "Seleccionar Días")]+ dias_labs,
        label="Días Disponible (Seleccionar)",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_dias_lab"}),
    )

    horarios = [(x.id,x.horario) for x in list(Horario.objects.filter())]
    id_horario = forms.ChoiceField(
        choices=[("", "Seleccionar Horario")]+ horarios,
        label="Horario Disponible (para detalles, en Descripción)",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_horario"}),
    )

    servicios = [(x.id,x.servicio) for x in list(Servicio.objects.filter())]
    id_servicio = forms.ChoiceField(
        choices=[("", "Seleccionar Servicio")]+ servicios,
        label="Servicio (Seleccionar)",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_servicio"}),
    )

    # tipos_operacion = ((1,"Venta"),(2,"Arriendo"))
    # id_tipo_operacion = forms.ChoiceField(choices=[(k, '{} - {}'.format(k, v)) for (k, v) in tipos_operacion], label='Tipo operación (Seleccionar)')

    nickname = forms.CharField(label='Seudónimo', max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Nombre artístico'}))
    # estado = forms.CharField(label='Estado (opcional)', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Te espero!'}), required=False)
    descripcion = forms.CharField(label='Descripción (opcional)', required=False, max_length=330, widget=forms.Textarea(attrs={'rows':3}))
    telefono = forms.CharField(label='Teléfono (9 dígitos)', max_length=9, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 912345678 (sin +56)'}))
    # dias_lab = forms.CharField(label='Días Disponibilidad', max_length=100)                         #cambiar a choicefield "Lunes a Viernes, Lunes a Sábado, Lunes a Domingo"
    # horario = forms.CharField(label='Horario Disponibilidad', max_length=100)                       #cambiar a choicefield "Mañana, Tarde, Noche"
    medida_alta = forms.CharField(label='Medida Busto (en cm)', max_length=100)
    medida_media = forms.CharField(label='Medida Cintura (en cm)', max_length=100)
    medida_baja = forms.CharField(label='Medida Cadera (en cm)', max_length=100)
    estatura = forms.CharField(label='Estatura (en metros)', max_length=4, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 1,60'}))
    ubicacion = forms.CharField(label='Ubicación Referencial', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Apoquindo con Manquehue'}))
    metro = forms.CharField(label='Estación de Metro (Opcional)', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Baquedano'}))
    edad = forms.CharField(label='Edad', max_length=100)
    # servicios = forms.CharField(label='Servicios', max_length=100)
    servicios_add = forms.CharField(label='Servicios Adicionales (Opcional)', max_length=100, required=False)
    tarifa = forms.CharField(label='Tarifa', max_length=7, validators=[validar_tarifa], widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 80000 (sín punto separador)'}))  # Agrega el validador personalizado
    # precio = forms.CharField(label='Precio ($ o UF)', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Especificar si es en $ o UF. Ejemplo: $20.000.000 o 2.500 UF'}))
    video_file = forms.FileField(label='Video de 6 segundos máximo (Opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'video/*', 'autocomplete': 'off'}))
    image_portada1 = forms.ImageField(label='Foto principal (requerida)', required=True, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image1 = forms.ImageField(label='Foto 1 (Requerida)', required=True, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image2 = forms.ImageField(label='Foto 2 (Requerida)', required=True, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image3 = forms.ImageField(label='Foto 3 (Requerida)', required=True, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image4 = forms.ImageField(label='Foto 4 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image5 = forms.ImageField(label='Foto 5 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image6 = forms.ImageField(label='Foto 6 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image7 = forms.ImageField(label='Foto 7 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image8 = forms.ImageField(label='Foto 8 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image9 = forms.ImageField(label='Foto 9 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    image10 = forms.ImageField(label='Foto 10 (opcional)', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'autocomplete': 'off'}))
    mostrar = forms.BooleanField(label='Autorizar Perfil (Mostrar) - Sólo Superusuario', required=False)
    

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['estado', 'image_estado']
        labels = {  
                    'estado':_("Estado (Opcional):"),
                    'image_estado':_("Imagen del Estado (Opcional):")
                    }

class ClientesUpdateForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [  
                    'id_tipo_usuario',
                    'id_tipo_nation',
                    'id_comuna',
                    'id_region',
                    'nickname',
                    'descripcion',
                    'telefono',
                    'id_dias_lab',
                    'id_horario',
                    'medida_alta',
                    'medida_media',
                    'medida_baja',
                    'estatura',
                    'ubicacion',
                    'metro',
                    'edad',
                    'id_servicio',
                    'servicios_add',
                    'tarifa',
                    'video_file',
                    'image_portada1',
                    'image1',
                    'image2',
                    'image3',
                    'image4',
                    'image5',
                    'image6',
                    'image7',
                    'image8',
                    'image9',
                    'image10',
                    'mostrar'
                    ]
        labels = {  
                    'id_tipo_usuario':_("Yo Soy (Seleccionar) - Sólo Superusuario"),
                    'id_tipo_nation':_("Nacionalidad (Seleccionar) - Sólo Superusuario"),
                    'id_comuna':_("Comuna (Seleccionar) - Sólo Superusuario"),
                    'id_region':_("Región (Seleccionar) - Sólo Superusuario"),
                    'nickname':_("Seudónimo - Sólo Superusuario"),
                    'descripcion':_("Descripción (Opcional)"),
                    'telefono':_("Teléfono (sin +56)"),
                    'id_dias_lab':_("Días Disponible"),
                    'id_horario':_("Horario Disponible (para detalles, en Descripción)"),
                    'medida_alta':_("Medida Busto"),
                    'medida_media':_("Medida Cintura"),
                    'medida_baja':_("Medida Cadera"),
                    'estatura':_("Estatura"),
                    'ubicacion':_("Ubicación"),
                    'metro':_("Estación de Metro (Opcional)"),
                    'edad':_("Edad"),
                    'id_servicio':_("Servicio"),
                    'servicios_add':_("Servicios Adicionales (Opcional)"),
                    'tarifa':_("Tarifa"),
                    'video_file':_("Video de 6 segundos máximo (Opcional)"),
                    'image_portada1':_("Foto Portada"),
                    'image1':_("Foto 1"),
                    'image2':_("Foto 2"),
                    'image3':_("Foto 3"),
                    'image4':_("Foto 4 (Opcioanl)"),
                    'image5':_("Foto 5 (Opcioanl)"),
                    'image6':_("Foto 6 (Opcioanl)"),
                    'image7':_("Foto 7 (Opcioanl)"),
                    'image8':_("Foto 8 (Opcioanl)"),
                    'image9':_("Foto 9 (Opcioanl)"),
                    'image10':_("Foto 10 (Opcioanl)"),
                    'mostrar':_("Autorizar Perfil (Mostrar) - Sólo Superusuario")
                    }
        


