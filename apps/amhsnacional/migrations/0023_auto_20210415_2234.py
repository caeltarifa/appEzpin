# Generated by Django 3.1.7 on 2021-04-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amhsnacional', '0022_auto_20210415_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='air_mensaje',
            old_name='direccion_destino',
            new_name='dependencia_destino',
        ),
        migrations.AlterField(
            model_name='air_mensaje',
            name='grupo_destino',
            field=models.ManyToManyField(blank=True, to='amhsnacional.Grupo_ezpin'),
        ),
    ]
