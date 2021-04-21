from django.contrib import admin

from apps.amhsnacional.models import Grupo_ezpin
from apps.amhsnacional.models import Usuario_ezpin
from apps.amhsnacional.models import Air_mensaje
from apps.amhsnacional.models import Prioridad
from apps.amhsnacional.models import Directorio
# Register your models here.
admin.site.register(Grupo_ezpin)
admin.site.register(Usuario_ezpin)
admin.site.register(Air_mensaje)
admin.site.register(Prioridad)
admin.site.register(Directorio)





