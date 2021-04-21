# Generated by Django 3.1.7 on 2021-04-15 21:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('amhsnacional', '0018_auto_20210415_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('prioridad', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-prioridad'],
            },
        ),
        migrations.CreateModel(
            name='Usuario_ezpin',
            fields=[
                ('designador', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=85)),
            ],
            options={
                'ordering': ['designador'],
            },
        ),
        migrations.CreateModel(
            name='Grupo_ezpin',
            fields=[
                ('id_grupo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_grupo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=85)),
                ('integrantes', models.ManyToManyField(to='amhsnacional.Usuario_ezpin')),
            ],
            options={
                'ordering': ['-id_grupo'],
            },
        ),
        migrations.CreateModel(
            name='Air_mensaje',
            fields=[
                ('id_airmensaje', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=80)),
                ('mensaje', models.TextField()),
                ('visto', models.BooleanField(default=False)),
                ('hora_enviado', models.DateTimeField(default=datetime.datetime.now)),
                ('hora_visto', models.DateTimeField(blank=True, null=True)),
                ('adjunto', models.FileField(blank=True, upload_to='documents-%Y-%m-%d/')),
                ('direccion_destino', models.ManyToManyField(to='amhsnacional.Usuario_ezpin')),
                ('grupo_destino', models.ManyToManyField(to='amhsnacional.Grupo_ezpin')),
                ('prioridad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='amhsnacional.prioridad')),
            ],
            options={
                'ordering': ['-id_airmensaje'],
            },
        ),
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id_direct', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='directorio_user', serialize=False, to='amhsnacional.usuario_ezpin')),
                ('dependencia', models.ManyToManyField(to='amhsnacional.Usuario_ezpin')),
                ('grupo', models.ManyToManyField(to='amhsnacional.Grupo_ezpin')),
            ],
            options={
                'ordering': ['-id_direct'],
            },
        ),
    ]