from django.db import models
from datetime import datetime

# Create your models here.
class Usuario_ezpin(models.Model):
    designador = models.CharField(primary_key=True, max_length=8)
    descripcion = models.CharField(max_length=85)
    icao_amhs = models.CharField(max_length=100)
    #prefijo = models.CharField(max_length=100)

    def __str__(self):
        return '{}-{}'.format(self.icao_amhs, self.designador)

    class Meta:
        ordering = ['designador']


class Grupo_ezpin(models.Model):
    #predeterminado = models.CharField(primary_key=True, max_length=8)
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=85)
    integrantes = models.ManyToManyField(Usuario_ezpin)
    def __str__(self):
        return '{} - {}'.format(self.id_grupo, self.nombre_grupo)
    class Meta:
        ordering = ['-id_grupo']


class Prioridad(models.Model):
    prioridad = models.CharField(max_length=2, primary_key=True)

    def __str__(self):
        return '{}'.format(self.prioridad)

    class Meta:
        ordering = ['-prioridad']


class Air_mensaje(models.Model):
    id_airmensaje = models.AutoField(primary_key=True)

    origen = models.ForeignKey(
        Usuario_ezpin,
        related_name='origen_msj',
        on_delete=models.PROTECT,
        #primary_key=True,
    )

    asunto = models.CharField(max_length=80)

    prioridad = models.ForeignKey(
        Prioridad, on_delete=models.PROTECT, blank=False, null=False)

    mensaje = models.TextField()


    grupo_destino = models.ManyToManyField(Grupo_ezpin, blank=True)

    dependencia_destino = models.ManyToManyField(Usuario_ezpin, blank=False)

    hora_enviado = models.DateTimeField(default=datetime.now, blank=False)

    visto = models.BooleanField(default=False)
    hora_visto = models.DateTimeField(blank=True, null=True)

    adjunto = models.FileField(upload_to='documents-%Y-%m-%d/', blank=True)

    guardado = models.BooleanField(default=False)

    eliminado = models.BooleanField(default=False)

    archivado = models.BooleanField(default=False)

    enviado = models.BooleanField(default=False)


    def __str__(self):
        return '{} - {} - {}'.format(self.id_airmensaje, self.prioridad, self.asunto)

    class Meta:
        ordering = ['-id_airmensaje']

class Directorio(models.Model):
    id_directorio = models.OneToOneField(
        Usuario_ezpin,
        related_name='directorio_user',
        on_delete=models.PROTECT,
        primary_key=True,
    )
    grupo = models.ManyToManyField(Grupo_ezpin)
    def __str__(self):
        return '{} - {}'.format(self.id_directorio, self.id_directorio.descripcion)
    class Meta:
        ordering = ['-id_directorio']
