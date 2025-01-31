from django.shortcuts import render
from .forms import ContactoForm

from e_contacto.models import opciones_consultas
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.conf import settings

def render_contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado exitosamente"

            nombre = formulario.cleaned_data['nombre']
            correo = formulario.cleaned_data['correo']
            telefono = formulario.cleaned_data['telefono']
            tipo_consulta = dict(opciones_consultas)[formulario.cleaned_data['tipo_consulta']]
            mensaje = formulario.cleaned_data['mensaje']

            EmailMessage(
               '{} de {}'.format(tipo_consulta, nombre),
               'Mensaje:\n {}\n\n'.format(mensaje) + 'Teléfono: {}\n Correo: {}'.format(telefono, correo),
               'horasex@gmail.com', # Send from (your website)
               ['jimmycala@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[correo] # Email from the form to get back to
                    ).send()
            
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)

# def render_contacto(request):
#     data = {
#         'form': ContactoForm()
#     }

#     if request.method == 'POST':
#         print(request.POST)  # Muestra los datos enviados en la terminal
#         formulario = ContactoForm(data=request.POST)
#         if formulario.is_valid():
#             print("Formulario válido")  # Verifica si se valida correctamente
#             formulario.save()
#             data["mensaje"] = "¡Mensaje enviado exitosamente!"
#         else:
#             data["form"] = formulario

#     return render(request, 'contacto.html', data)