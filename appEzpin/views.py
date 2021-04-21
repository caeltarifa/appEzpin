from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.http import JsonResponse
from django.http import HttpResponse
import json
from datetime import datetime

#from apps.amhsnacional.models import Grupo_ezpin
#Usuario_barion
# Create your views here.

def view_pagina_principal(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('login')


def view_clasificar_usuario_login(request):
    if request.user.is_authenticated:
        #metar = Metar_trafico.objects.raw("select * from plan_vuelo_flp_trafico where hora_amhs like '12%%%%' order by id_amhs desc limit 20")
        return redirect('view_nuevo')#, {'metar': metar})
        #return render(request, 'index.html')
    else:
        return redirect('login')

