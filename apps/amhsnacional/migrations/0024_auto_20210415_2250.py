# Generated by Django 3.1.7 on 2021-04-15 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amhsnacional', '0023_auto_20210415_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='air_mensaje',
            old_name='dependencia_destino',
            new_name='dependencia_destin',
        ),
    ]