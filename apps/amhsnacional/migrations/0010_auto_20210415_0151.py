# Generated by Django 3.1.7 on 2021-04-15 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amhsnacional', '0009_auto_20210415_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air_mensaje',
            name='adjunto',
            field=models.FileField(blank=True, upload_to='%Y/%m/%d/'),
        ),
    ]