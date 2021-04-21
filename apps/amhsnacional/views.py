from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db import models
from datetime import datetime

import json

# Create your views here.


from django import forms
#from .forms import PostForm
from .models import Air_mensaje
from .models import Grupo_ezpin
from .models import Usuario_ezpin
from .models import Prioridad


def grupos_directorio():
    grupos = Grupo_ezpin.objects.all()
    lista = []
    for i in grupos:
        lista.append((i.id_grupo, i.nombre_grupo))
    return lista


def dependendencias_directorio():
    dependencias = Usuario_ezpin.objects.all()
    lista = []
    for x in dependencias:
        lista.append((x.designador, x.designador))

    return lista


class Formulario(forms.ModelForm):
    origen = forms.ModelChoiceField(queryset=Usuario_ezpin.objects.filter(designador=""),  widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'origen'}))  # forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'value':'nada'}))
    asunto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'asunto'}))
    prioridad = forms.ModelChoiceField(queryset=Prioridad.objects.all(),  widget=forms.Select(attrs={'class': 'form-select', 'id':'prioridad'})  )

    mensaje = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Add a description of your event",}
        ),
    ),

    grupo_destino = forms.MultipleChoiceField(
            choices=grupos_directorio(),
            widget=forms.SelectMultiple(attrs={'class':'js-example-basic-multiple', 'id':'id_grupodestino'}),
            required=True,
        )

    dependencia_destino = forms.MultipleChoiceField(
            choices=dependendencias_directorio(),
            widget=forms.SelectMultiple(attrs={'class':'js-example-basic-multiple2', 'id':'id_dependenciadestino', 'placeholder':'Dependencia destino'}),
            required=True,
        )
    hora_enviado = forms.DateTimeField(initial=datetime.today)
    adjunto = forms.FileField( )
    guardado = forms.BooleanField()

    def __init__(self, user, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)

        self.fields['origen'].queryset = Usuario_ezpin.objects.filter(designador=user.get_username().split('@')[0])

    class Meta:
        model = Air_mensaje
        fields = ('origen', 'asunto', 'prioridad', 'grupo_destino',
                  'dependencia_destino', 'mensaje', 'hora_enviado', 'adjunto', 'guardado')


def view_nuevo(request):
    if request.method == 'POST':
        form = Formulario(request.POST, request.FILES)
        if form.is_valid():
            #post= form.save(commit=False)
            # form=Air_mensaje(adjunto=request.FILES['id_adjunto'])
            form.save()
            return redirect('view_nuevo')
        else:
            print("error en files form")
    else:
        #form = Formulario(initial={'asunto': "HOL MNDO",})
        form = Formulario(request.user)
        #form.setOrigen("SLLPZTZX")
    return render(request, 'template_amhsnacional/recibidos_nuevo.html', {'form': form})


def serializarRecibidos(msj):
    return {
        'id_airmensaje' : msj.id_airmensaje, 
        'visto' : msj.visto,  
        'origen_id' : msj.origen_id, 
        'prioridad_id' : msj.prioridad_id, 
        'asunto' : msj.asunto, 
        'mensaje' : msj.mensaje
    }
#MOSTRAR LOS MENSAJES RECIBIDOS DEL USUARIO X
def api_recididos(request):
    #if request.user.is_authenticated and request.user.is_active and request.user.groups.filter(name='AISNACIONAL').exists():
    if request.method =="GET":
        #get_abreviatura = str(request.GET.dict()['abreviatura'])
        get_usuario = str(request.GET.get('usuario')).upper()

        #id_asunto | descripcion_asunto | fraseologia_asunto
        lista_recibidos = Air_mensaje.objects.raw("select id_airmensaje, visto,  origen_id, prioridad_id, asunto, mensaje from amhsnacional_air_mensaje where origen_id like %(get_usuario)s and enviado=true and  archivado=false and  eliminado=false and guardado=false;" , { 'get_usuario' : ""+get_usuario+""} )
        
        lista_recibidos = [ serializarRecibidos(msj) for msj in lista_recibidos ]

        devolucion = {
            'lista_recibidos': lista_recibidos,
        }

        return HttpResponse(json.dumps(devolucion), content_type='application/json')
    else:
        return HttpResponse(json.dumps([{'Error':'GET'}]), content_type='application/json')
    #else:
    #    return redirect('login')

def serializarUsuario(user):
    return {
        'designador': user.designador,
        'descripcion': user.descripcion,
        'icao_amhs': user.icao_amhs,
    }
#MOSTRAR TODOS LOS USIARIOS AMHS
def api_usuarios_amhs(request):
    #if request.user.is_authenticated and request.user.is_active and request.user.groups.filter(name='AISNACIONAL').exists():
    if request.method =="GET":
        #get_abreviatura = str(request.GET.dict()['abreviatura'])
        get_usuario = str(request.GET.get('usuario')).upper()

        lista_usuarios = Usuario_ezpin.objects.all()
        
        lista_usuarios = [ serializarUsuario(user) for user in lista_usuarios ]

        devolucion = {
            'lista_usuarios': lista_usuarios,
        }

        return HttpResponse(json.dumps(devolucion), content_type='application/json')
    else:
        return HttpResponse(json.dumps([{'Error':'GET'}]), content_type='application/json')