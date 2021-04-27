from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.template.response import TemplateResponse

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
    grupos = Grupo_ezpin.objects.raw('select * from amhsnacional_grupo_ezpin') # Grupo_ezpin.objects.all()
    lista = []
    for i in grupos:
        lista.append((i.id_grupo, i.nombre_grupo))
    return lista


def dependendencias_directorio():
    dependencias = Usuario_ezpin.objects.all()
    lista = []
    for x in dependencias:
        lista.append([ x.designador, x.icao_amhs+x.designador])

    return lista

######################################
#            NUEVO GRUPO             #
######################################

class FormularioGrupo(forms.ModelForm):
    nombre_grupo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'asunto'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'asunto'}))
    integrantes = forms.MultipleChoiceField(
            choices=dependendencias_directorio(),
            widget=forms.SelectMultiple(attrs={'class':'menu__tres col-sm-5', 'multiple':"multiple", 'id':'id_integrantes'} ),
            required=False,
        )


    def __init__(self, *args, **kwargs):
        super(FormularioGrupo, self).__init__(*args, **kwargs)
        #nameuser=user.get_username().split('@')[0]
        self.fields['integrantes'].queryset = Usuario_ezpin.objects.all()
    class Meta:
        model = Grupo_ezpin
        
        fields = ('nombre_grupo','descripcion','integrantes')


#def view_new_grupo(request):
#    if request.user.is_authenticated and request.user.is_active:
#        
#    else:
#        return redirect('login')




class Formulario(forms.ModelForm):
    origen = forms.ModelChoiceField(queryset=Usuario_ezpin.objects.filter(designador=""),  widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'origen'}))  # forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'value':'nada'}))
    asunto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'asunto'}))
    prioridad = forms.ModelChoiceField(queryset=Prioridad.objects.all(),  widget=forms.Select(attrs={'class': 'form-select', 'id':'prioridad'})  )

    mensaje = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'rows':5,'cols':20}
        )
    ),

    grupo_destino = forms.MultipleChoiceField(
            choices=grupos_directorio(),
            widget=forms.SelectMultiple(attrs={'class':'menu__uno', 'id':'id_grupodestino'}),
            required=False,
        )

    dependencia_destino = forms.MultipleChoiceField(
            choices=dependendencias_directorio(),
            widget=forms.SelectMultiple(attrs={'class':'menu__dos', 'id':'id_dependenciadestino', 'placeholder':'Dependencia destino'}),
            required=False,
        )

    hora_enviado = forms.DateTimeField(initial=datetime.today)
    adjunto = forms.FileField(required=False )
    guardado = forms.BooleanField(required=False)

    def __init__(self, user, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        nameuser=user.get_username().split('@')[0]
        self.fields['origen'].queryset = Usuario_ezpin.objects.filter(designador=nameuser)
        self.asunto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'asunto', 'value':nameuser}))

    class Meta:
        model = Air_mensaje
        fields = ('origen', 'asunto', 'prioridad', 'grupo_destino',
                  'dependencia_destino', 'mensaje', 'hora_enviado', 'adjunto', 'guardado')


def view_nuevo(request):
    if request.user.is_authenticated and request.user.is_active:
        if request.method == 'POST':
            form = Formulario(request.user,request.POST, request.FILES)
            if form.is_valid():
                #post= form.save(commit=False)
                # form=Air_mensaje(adjunto=request.FILES['id_adjunto'])
                form.save()
                return redirect('view_nuevo')
            else:
                return render(request, 'template_amhsnacional/m_nuevos.html', {'form': form})

        else:
            #form = Formulario(initial={'asunto': "HOL MNDO",})
            form = Formulario(user=request.user)
            #form.setOrigen("SLLPZTZX")
        return render(request, 'template_amhsnacional/m_nuevos.html', {'form': form})
    else:
        return redirect('login')

def serializarEnviados(msj):
    return {
        'id_airmensaje' : msj.id_airmensaje, 
        'visto' : msj.visto,  
        'origen_id' : msj.origen_id, 
        'prioridad_id' : msj.prioridad_id, 
        'asunto' : msj.asunto, 
        'mensaje' : msj.mensaje
    }
#MOSTRAR LOS MENSAJES RECIBIDOS DEL USUARIO X
def api_enviados(request):
    #if request.user.is_authenticated and request.user.is_active and request.user.groups.filter(name='AISNACIONAL').exists():
    if request.method =="GET":
        #get_abreviatura = str(request.GET.dict()['abreviatura'])
        get_usuario = str(request.GET.get('usuario')).upper()

        #id_asunto | descripcion_asunto | fraseologia_asunto
        lista_recibidos = Air_mensaje.objects.raw("select id_airmensaje, visto,  origen_id, prioridad_id, asunto, mensaje from amhsnacional_air_mensaje where origen_id like %(get_usuario)s and enviado=true and  archivado=false and  eliminado=false and guardado=false;" , { 'get_usuario' : ""+get_usuario+""} )
        
        lista_recibidos = [ serializarEnviados(msj) for msj in lista_recibidos ]

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
    if request.user.is_authenticated and request.user.is_active:
        lista_usuarios = Usuario_ezpin.objects.all()
        
        lista_usuarios = [ serializarUsuario(user) for user in lista_usuarios ]

        devolucion = {
            'lista_usuarios': lista_usuarios,
        }

        return HttpResponse(json.dumps(devolucion), content_type='application/json')
    else:
        return redirect('login')


def serializarGrupo(grupo):
    return {
        'id_grupo':grupo.id_grupo,
        'nombre': grupo.nombre_grupo,
        'descripcion': grupo.descripcion,
        'integrantes': "dependencias servidor",
    }

#MOSTRAR TODOS LOS USIARIOS AMHS
def api_grupos_amhs(request):
    if request.user.is_authenticated and request.user.is_active:
        lista_grupos = Grupo_ezpin.objects.raw('select * from amhsnacional_grupo_ezpin')
        
        lista_grupos = [ serializarGrupo(grupo) for grupo in lista_grupos ]

        devolucion = {
            'lista_grupos': lista_grupos,
        }

        return HttpResponse(json.dumps(devolucion), content_type='application/json')
    else:
        return redirect('login')


def view_eliminar_grupo(request):
    if request.user.is_authenticated and request.user.is_active:
        if request.method =="GET":
            get_grupo = str(request.GET.get('id_grupo'))
            grupo = Grupo_ezpin.objects.filter(id_grupo=int(get_grupo)).delete()
            return render(request, 'template_amhsnacional/m_directorio.html')
        else:
            return render(request, 'template_amhsnacional/m_directorio.html')
    else:
        return redirect('login')





def serializarRecibidos(msj):
    if msj.adjunto:
        archivo=msj.adjunto.url
    else:
        archivo="nada"
    return {
        'id_airmensaje': msj.id_airmensaje,  
        'asunto': msj.asunto,  
        'mensaje': msj.mensaje,  
        'prioridad_id': msj.prioridad_id,  
        'origen_id': msj.origen_id,  
        'usuario_ezpin_id': msj.usuario_ezpin_id,
        'hora_enviado': str(msj.hora_enviado)    ,
        'adjunto':archivo 
    }

def view_recibidos(request):
    if request.user.is_authenticated and request.user.is_active:
        mensaje = Air_mensaje.objects.get(id_airmensaje=30)
        return render(request, 'template_amhsnacional/m_recibidos.html', {'mensaje':mensaje})
        #return HttpResponse(dev olucion, content_type='application/json')
    else:
        return redirect('login')



def view_api_recibidos(request):
    if request.user.is_authenticated and request.user.is_active:
        #get_abreviatura = str(request.GET.dict()['abreviatura'])
        get_usuario = request.user.username.split('@')[0]

        #	--MOSTRAR EL MENSAJE QUE TENGA EL DETINO: USUARIO=SLLPZRZA
        #	--MOSTRAR EL MENSAJE QUE TENGA COMO DESTINO EL USUARIO=SLLPZRZA, QUE ESTA DENTRO DE UN GRUPO 
        #lista_recibidos = Air_mensaje.objects.raw("select distinct(id_airmensaje), tab1.asunto, tab1.mensaje, tab1.prioridad_id, tab1.origen_id, tab1.usuario_ezpin_id,tab1.hora_enviado, tab1.adjunto from ( 	select id_airmensaje,tabmsj.asunto,tabmsj.mensaje, tabmsj.prioridad_id,tabmsj.origen_id,tabuser.usuario_ezpin_id,tabmsj.hora_enviado, tabmsj.adjunto         from amhsnacional_air_mensaje as tabmsj 	        inner join amhsnacional_air_mensaje_dependencia_destino AS tabuser 	        on tabmsj.id_airmensaje = tabuser.air_mensaje_id 	and 	        tabuser.usuario_ezpin_id like %(get_usuario)s ) as tab1 union ( select id_airmensaje, asunto, mensaje, prioridad_id, origen_id, usuario_ezpin_id,hora_enviado from (select * from amhsnacional_air_mensaje as tabmsj inner join amhsnacional_air_mensaje_grupo_destino as tabgrup on tabmsj.id_airmensaje = tabgrup.air_mensaje_id ) as tabgrup inner join amhsnacional_grupo_ezpin_integrantes as tabgrupo_user on tabgrup.grupo_ezpin_id = tabgrupo_user.grupo_ezpin_id and tabgrupo_user.usuario_ezpin_id like %(get_usuario)s ) order by hora_enviado desc " , { 'get_usuario' : ""+get_usuario+""} )
        lista_recibidos = Air_mensaje.objects.raw("select distinct(id_airmensaje), tab1.asunto, tab1.mensaje, tab1.prioridad_id, tab1.origen_id, tab1.usuario_ezpin_id,tab1.hora_enviado, tab1.adjunto from ( 	select id_airmensaje,tabmsj.asunto,tabmsj.mensaje, tabmsj.prioridad_id,tabmsj.origen_id,tabuser.usuario_ezpin_id,tabmsj.hora_enviado, tabmsj.adjunto         from amhsnacional_air_mensaje as tabmsj 	        inner join amhsnacional_air_mensaje_dependencia_destino AS tabuser 	        on tabmsj.id_airmensaje = tabuser.air_mensaje_id 	and 	        tabuser.usuario_ezpin_id like %(get_usuario)s ) as tab1 union ( select id_airmensaje, asunto, mensaje, prioridad_id, origen_id, usuario_ezpin_id,hora_enviado, adjunto from (select * from amhsnacional_air_mensaje as tabmsj inner join amhsnacional_air_mensaje_grupo_destino as tabgrup on tabmsj.id_airmensaje = tabgrup.air_mensaje_id ) as tabgrup inner join amhsnacional_grupo_ezpin_integrantes as tabgrupo_user on tabgrup.grupo_ezpin_id = tabgrupo_user.grupo_ezpin_id and tabgrupo_user.usuario_ezpin_id like %(get_usuario)s ) order by hora_enviado desc " , { 'get_usuario' : ""+get_usuario+""} )
        
        lista_recibidos = [ serializarRecibidos(msj) for msj in lista_recibidos ]

        devolucion = {
            'get_usuario':get_usuario,
            'lista_recibidos': lista_recibidos,
        }
        #devolucion=json.dumps(devolucion)
        return HttpResponse(json.dumps(devolucion), content_type='application/json')
        #return JsonResponse(devolucion,status=200)
        #return TemplateResponse(request, 'template_amhsnacional/m_recibidos.html', devolucion)
        #return render(request, 'template_amhsnacional/m_recibidos.html', devolucion)
        #return HttpResponse(dev olucion, content_type='application/json')
    else:
        return redirect('login')

## MENSAJES ENVIADOS POR EL USUARIO X
def view_enviados(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'template_amhsnacional/m_enviados.html')
    else:
        return redirect('login')

## TEMPLATE DE MENSJES NUEVOS
def view_nuevo_mensaje(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'template_amhsnacional/recibidos_nuevo.html')
    else:
        return redirect('login')

## TEMPLATE DE MENSJES NUEVOS
def view_guardados(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'template_amhsnacional/recibidos_nuevo.html')
    else:
        return redirect('login')

## TEMPLATE DE MENSJES NUEVOS
def view_eliminados(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'template_amhsnacional/recibidos_nuevo.html')
    else:
        return redirect('login')

## TEMPLATE DE DIRECTORIO PARA CREAR GRUPO
def view_directorio(request):
    if request.user.is_authenticated and request.user.is_active:
        if request.method == 'POST':
            form = FormularioGrupo(request.POST)
            if form.is_valid():
                #post= form.save(commit=False)
                # form=Air_mensaje(adjunto=request.FILES['id_adjunto'])
                form.save()
                return redirect('view_directorio')
            else:
                return render(request, 'template_amhsnacional/m_directorio.html', {'form': form})

        else:
            #form = Formulario(initial={'asunto': "HOL MNDO",})
            form = FormularioGrupo()
            #form.setOrigen("SLLPZTZX")
        return render(request, 'template_amhsnacional/m_directorio.html', {'form': form})
    else:
        return redirect('login')
