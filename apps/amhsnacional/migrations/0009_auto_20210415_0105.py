# Generated by Django 3.1.7 on 2021-04-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amhsnacional', '0008_auto_20210415_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air_mensaje',
            name='hora_visto',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]