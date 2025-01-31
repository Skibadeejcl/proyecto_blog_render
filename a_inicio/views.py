from django.shortcuts import render, get_object_or_404



def home(request):
    # Verificar si el usuario ya confirmó ser mayor de edad
    is_adult = request.session.get('is_adult', False)

    # Cli = Clientes.objects.order_by('-last_updated').all()
    # Cli = Clientes.objects.order_by('-last_updated').filter(mostrar=True)
    # Cli = Clientes.objects.order_by('-last_updated').filter(mostrar=False, id_tipo_usuario=1)
    Cli = Clientes.objects.order_by('-last_updated').filter(mostrar=True)
    #clientes = Clientes.objects.filter(preferencial=True)

    # myFilter = ClientesFilter(request.GET, queryset=Cli)
    # Cli = myFilter.qs

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(Cli, 100)
        Cli = paginator.page(page)
    except:
        raise Http404

    # Contexto para la plantilla
    context = {'entity':Cli, 'paginator':paginator, 'show_modal': not is_adult,} # Solo mostrar el modal si no es mayor de edad

    return render(request, 'home.html', context)

     # return render(request, 'home.html', {'clientes': clientes})

from django.shortcuts import render, redirect
from a_inicio.models import *
from a_inicio.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt
import json

from .filters import ClientesFilter


def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user='+str(form.cleaned_data['username']))
    else:
        form = UserForm()

    return render(request, 'registration/register.html',{'form':form})

def register_tipoView(request):
    username = request.GET['user']
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form = TipoForm(request.POST)
            print(form)
            #tipo = form.cleaned_data['tipo']
            rut = form.cleaned_data['rut']
            # tipos_usuario = form.cleaned_data['tipos_usuario']
            # direccion = form.cleaned_data['direccion']
            # telefono = form.cleaned_data['telefono']
            user = User.objects.filter(username=username)[0]
            #tipo_user = Tipo_user.objects.filter(id=int(tipo))[0]
            #datos = Profile(user=user, id_tipo_user=tipo_user, rut=rut, direccion=direccion, telefono=telefono)
            # datos = Profile(user=user, rut=rut, direccion=direccion, telefono=telefono)
            datos = Profile(user=user, rut=rut)
            datos.save()
            return HttpResponseRedirect('/login/')
    else:
        form = TipoForm()
    return render(request, 'registration/register_tipo.html',{'form':form})

@login_required
def dashboardView(request, user_id=None):
    if user_id:
        # Verificar si es superusuario
        if not request.user.is_superuser:
            return redirect('home')  # O puedes redirigir a una página de error si no es superusuario
        
        # Obtener al usuario específico
        current_user = get_object_or_404(User, id=user_id)
    else:
        current_user = request.user  # Si no se pasa un user_id, mostramos el dashboard del usuario actual
    
    # Obtener los clientes asociados a este usuario
    Cli = Clientes.objects.filter(id_user_id=current_user.id).order_by('-last_updated')

    return render(request, 'dashboard.html', {'clientes': Cli, 'current_user': current_user})


def indexView(request):
    # Cli = Clientes.objects.filter(mostrar=True).order_by('-date')
    # Cli = Clientes.objects.filter(mostrar=True).order_by('-last_updated')
    Cli = Clientes.objects.filter(mostrar=True).order_by('-last_updated')

    myFilter = ClientesFilter(request.GET, queryset=Cli)
    Cli = myFilter.qs

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(Cli, 30)
        Cli = paginator.page(page)
    except:
        raise Http404

    context = {'entity':Cli, 'paginator':paginator, 'myFilter':myFilter}
    #context = {'clientes':Cli, 'paginator':paginator, 'myFilter':myFilter}

    return render(request, 'indexavisos.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)

    context={'u_form': u_form}
    return render(request, 'registration/update_profile.html', context)



@login_required
def new_clienteView(request):
    if not request.user.is_superuser and Clientes.objects.filter(id_user=request.user).exists():
        return render(request, 'error_entrada.html', {'message': 'Ya has creado una entrada en tu cuenta.'})
    
    if request.method == 'POST':
        u_form = ClienteForm(request.POST, request.FILES)
        if u_form.is_valid():
            u_form = ClienteForm(request.POST, request.FILES)
            print(u_form)
            id_tipo_usuario = u_form.cleaned_data['id_tipo_usuario']
            id_tipo_nation = u_form.cleaned_data['id_tipo_nation']
            id_comuna = u_form.cleaned_data['id_comuna']
            id_region = u_form.cleaned_data['id_region']
            nickname = u_form.cleaned_data['nickname']
            # estado = u_form.cleaned_data['estado']
            descripcion = u_form.cleaned_data['descripcion']
            telefono = u_form.cleaned_data['telefono']
            id_dias_lab = u_form.cleaned_data['id_dias_lab']
            id_horario = u_form.cleaned_data['id_horario']
            medida_alta = u_form.cleaned_data['medida_alta']
            medida_media = u_form.cleaned_data['medida_media']
            medida_baja = u_form.cleaned_data['medida_baja']
            estatura = u_form.cleaned_data['estatura']
            ubicacion = u_form.cleaned_data['ubicacion']
            metro = u_form.cleaned_data['metro']
            edad = u_form.cleaned_data['edad']
            id_servicio = u_form.cleaned_data['id_servicio']
            servicios_add = u_form.cleaned_data['servicios_add']
            tarifa = u_form.cleaned_data['tarifa']
            video_file = u_form.cleaned_data['video_file']
            image_portada1 = u_form.cleaned_data['image_portada1']
            image1 = u_form.cleaned_data['image1']
            image2 = u_form.cleaned_data['image2']
            image3 = u_form.cleaned_data['image3']
            image4 = u_form.cleaned_data['image4']
            image5 = u_form.cleaned_data['image5']
            image6 = u_form.cleaned_data['image6']
            image7 = u_form.cleaned_data['image7']
            image8 = u_form.cleaned_data['image8']
            image9 = u_form.cleaned_data['image9']
            image10 = u_form.cleaned_data['image10']
            mostrar = u_form.cleaned_data['mostrar']
            print(u_form.cleaned_data)
            tipo_usuario = Tipo_usuario.objects.filter(id=int(id_tipo_usuario)).first()
            tipo_nation = Tipo_nation.objects.filter(id=int(id_tipo_nation)).first()
            comuna = Comuna.objects.filter(id=int(id_comuna)).first()
            reg = Region.objects.filter(id=int(id_region)).first()
            tipo_dias_lab = Dias_lab.objects.filter(id=int(id_dias_lab)).first()
            tipo_horario = Horario.objects.filter(id=int(id_horario)).first()
            tipo_servicio = Servicio.objects.filter(id=int(id_servicio)).first()
            current_user = request.user
            user = User.objects.filter(id=current_user.id)
            cli = Clientes(
                            id_tipo_usuario=tipo_usuario,
                            id_tipo_nation=tipo_nation,
                            id_comuna=comuna,
                            id_region=reg,
                            nickname=nickname,
                            # estado=estado,
                            descripcion=descripcion,
                            telefono=telefono,
                            id_dias_lab=tipo_dias_lab,
                            id_horario=tipo_horario,
                            medida_alta=medida_alta,
                            medida_media=medida_media,
                            medida_baja=medida_baja,
                            estatura=estatura,
                            ubicacion=ubicacion,
                            metro=metro,
                            edad=edad,
                            id_servicio=tipo_servicio,
                            servicios_add=servicios_add,
                            tarifa=tarifa,
                            video_file = video_file,
                            image_portada1 = image_portada1,
                            image1 = image1,
                            image2 = image2,
                            image3 = image3,
                            image4 = image4,
                            image5 = image5,
                            image6 = image6,
                            image7 = image7,
                            image8 = image8,
                            image9 = image9,
                            image10 = image10,
                            mostrar=mostrar                            
                            )
            print(user)
            cli.id_user_id = current_user.id
            cli.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = ClienteForm()

    context = {'u_form': u_form}
    return render(request, 'new_cliente.html', context)



@login_required
def clientes_update(request):
    cliente_id = request.GET['id_cliente']
    if request.method == 'POST':
        cliente_id = request.GET['id_cliente']
        cliente = Clientes.objects.filter(id=cliente_id).first()
        u_form = ClientesUpdateForm(request.POST, request.FILES, instance=cliente)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect(f'/dashboard/{cliente.id_user.id}/')
    else:
        cliente = Clientes.objects.filter(id=cliente_id).first()
        u_form = ClientesUpdateForm(instance=cliente)
    context = {'u_form': u_form}
    return render(request, 'registration/update_cliente.html', context)


@login_required
def clientes_delete(request):
    cliente_id = request.GET['id_cliente']
    record = Clientes.objects.get(id=cliente_id)
    record.delete()
    return HttpResponseRedirect('/dashboard/')




def clientes_detail(request, clientes_id):
    # Obtener la entrada
    clientes = get_object_or_404(Clientes, pk=clientes_id)

    # Renderizar la plantilla de visualización
    return render(request, 'cliente_detail.html', {'clientes': clientes})


@login_required
def clientes_detail_edit(request, clientes_id):
    clientes = get_object_or_404(Clientes, pk=clientes_id)

    # Verificar si el usuario actual es el propietario de la entrada
    if clientes.id_user != request.user and not request.user.is_superuser:
        return render(request, 'error_edit_user.html', status=403)

    if request.method == "POST":
        form = ClientesForm(request.POST, request.FILES, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('cliente_detail', clientes_id=clientes.id)
    else:
        form = ClientesForm(instance=clientes)
        
    return render(request, 'edit_entry.html', {'form': form, 'clientes': clientes} )

def politicas_privacidad(request):
    # Obtener la entrada
    # clientes = get_object_or_404(Clientes, pk=clientes_id)

    # Renderizar la plantilla de visualización
    return render(request, 'politicas_privacidad.html')


@csrf_exempt
def set_adult_session(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("is_adult", False):
            request.session['is_adult'] = True
            return JsonResponse({"message": "Session updated successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def load_comunas(request):
    region_id = request.GET.get('region_id')
    if region_id:
        comunas = Comuna.objects.filter(codigo_region=region_id).order_by('codigo_region')
        data = [{'id': comuna.id, 'name': comuna.comuna} for comuna in comunas]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)



# @login_required
# def lista_clientes(request):
#     # Recuperar todos los datos del modelo Clientes
#     clientes = Clientes.objects.all()
#     return render(request, 'clientes_lista.html', {'clientes': clientes})

# @login_required
# def lista_clientes(request):
#     # Recuperar todos los datos de la tabla Clientes y relaciones
#     clientes = Clientes.objects.select_related(
#         'usuario__profile',  # Relación con User y luego con Profile
#         'id_tipo_usuario',
#         'id_tipo_nation',
#         'id_comuna',
#         'id_region'
#     ).all()

#     return render(request, 'clientes_completa.html', {'clientes': clientes})

# def lista_clientes(request):
#     # Instancia de los formularios
#     user_form = UserForm()
#     tipo_form = TipoForm()
#     user_update_form = UserUpdateForm()
#     cliente_form = ClienteForm()
#     clientes_form = ClientesForm()
#     clientes_update_form = ClientesUpdateForm()

#     context = {
#         'user_form': user_form,
#         'tipo_form': tipo_form,
#         'user_update_form': user_update_form,
#         'cliente_form': cliente_form,
#         'clientes_form': clientes_form,
#         'clientes_update_form': clientes_update_form,
#     }

#     return render(request, 'formulario_completo.html', context)

# Decorador para verificar si el usuario es superusuario
def superuser_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)

@superuser_required
@login_required
def lista_clientes(request):
    # Obtenemos todos los usuarios y sus datos relacionados
    usuarios = User.objects.all()
    datos_completos = []

    for usuario in usuarios:
        try:
            # Obtenemos el perfil del usuario
            profile = Profile.objects.get(user=usuario)
        except Profile.DoesNotExist:
            profile = None

        # Obtenemos todos los clientes relacionados con el usuario
        clientes = Clientes.objects.filter(id_user=usuario)

        if clientes.exists():
            for cliente in clientes:
                datos_completos.append({
                    'id': cliente.id if cliente.id else "No definida",
                    'nickname': cliente.nickname,
                    'username': usuario.username,
                    'id_user': usuario.id,
                    'email': usuario.email,
                    'first_name': usuario.first_name,
                    'last_name': usuario.last_name,
                    'rut': profile.rut if profile else "No definido",
                    'tipo_usuario': cliente.id_tipo_usuario.tipo_usuario if cliente.id_tipo_usuario else "No definido",
                    'nacionalidad': cliente.id_tipo_nation.tipo_nation if cliente.id_tipo_nation else "No definido",
                    'comuna': cliente.id_comuna.comuna if cliente.id_comuna else "No definida",
                    'region': cliente.id_comuna.codigo_region.Region if cliente.id_comuna and cliente.id_comuna.codigo_region else "No definida",
                    'telefono': cliente.telefono if cliente else "No definido",
                    'fecha_registro': usuario.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
                    'mostrar': cliente.mostrar,
                })
        else:
            datos_completos.append({
                'id': "No definida",
                'nickname': "No definido",
                'username': usuario.username,
                'id_user': usuario.id,  # Agregar esta clave aquí
                'email': usuario.email,
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'rut': profile.rut if profile else "No definido",
                'tipo_usuario': "No definido",
                'nacionalidad': "No definido",
                'comuna': "No definida",
                'region': "No definida",
                'telefono': "No definido",
                'fecha_registro': usuario.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
                'mostrar': "No definido",
            })
    
    # Ordenar la lista por "id_user"
    datos_completos = sorted(datos_completos, key=lambda x: x['id_user'], reverse=False)

    return render(request, 'clientes_lista.html', {'datos_completos': datos_completos})