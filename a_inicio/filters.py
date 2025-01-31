import django_filters
from django import forms

from .models import *

# def lasComunas(request):

#      if request is None:
#          return Comuna.objects.all()

#      id_region = request.a_inicio_region.id
#      return Comuna.objects.filter(codigo_region=id_region)


# STATUS_CHOICES0 = ((1,"Casa"),(2,"Departamento"),(3,"Sitio"),(4,"Comercial"),(5,"Otro"))
STATUS_CHOICES = [(x.id,x.Region) for x in list(Region.objects.all())]
STATUS_CHOICES1 = [(x.id,x.comuna) for x in list(Comuna.objects.filter())]
STATUS_CHOICES2 = [(x.id,x.tipo_usuario) for x in list(Tipo_usuario.objects.filter())]

import django_filters
from django import forms
from .models import Clientes, Region, Comuna, Tipo_usuario

class ClientesFilter(django_filters.FilterSet):

    id = django_filters.NumberFilter()
    id.label = 'Código Perfil'

    nickname = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Filtrar por Nombre'
    )

    id_tipo_usuario = django_filters.ChoiceFilter(choices=STATUS_CHOICES2, empty_label=("Seleccionar"), widget=forms.Select(attrs={'class': 'form-control'}))
    id_tipo_usuario.label = 'Busco'

    id_region = django_filters.ChoiceFilter(choices=STATUS_CHOICES, empty_label=("Seleccionar Región"), widget=forms.Select(attrs={"class": "form-control", "id": "id_region"}))
    id_region.label = 'Región'

    id_comuna = django_filters.ChoiceFilter(choices=STATUS_CHOICES1, empty_label=("Seleccionar Comuna"), widget=forms.Select(attrs={"class": "form-control", "id": "id_comuna"}))
    id_comuna.label = 'Comuna'

    class Meta:
        model = Clientes
        fields = ['nickname', 'id_tipo_usuario', 'id_region', 'id_comuna']


