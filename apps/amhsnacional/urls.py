from django.conf.urls import url, include
from django.urls import path, re_path

from apps.amhsnacional.views import view_nuevo
from apps.amhsnacional.views import view_recibidos
from apps.amhsnacional.views import view_api_recibidos
from apps.amhsnacional.views import view_nuevo
#from apps.amhsnacional.views import api_usuarios_amhs
#from apps.amhsnacional.views import api_recididos_usuario

 # view_form_plan_vuelo, post_new, post_detail

urlpatterns = [
    #url('tablero/',view_tablero, name='view_tablero'), #ver pagina de administrador controlador
    #gestion de rutas
    #path('formulario/', view_formulario, name="view_formulario"),
    
    url('recibidos/', view_recibidos, name="view_recibidos"),
    url('get_msjs/', view_api_recibidos, name="view_api_recibidos"),
    url('formulario/', view_nuevo, name="view_nuevo"),
    #url('dependencias/', api_usuarios_amhs, name="api_usuarios_amhs"),
    #url('recibidos/', api_recididos_usuario, name="api_recididos_usuario"),
    
]