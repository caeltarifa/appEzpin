# Generated by Django 3.1.7 on 2021-04-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('predeterminado', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre_grupo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=85)),
                ('integrantes', models.ManyToManyField(to='amhsnacional.Usuario_ezpin')),
            ],
            options={
                'ordering': ['predeterminado'],
            },
        ),
    ]
