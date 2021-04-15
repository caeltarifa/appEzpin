# Generated by Django 3.1.7 on 2021-04-15 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amhsnacional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Air_mensaje',
            fields=[
                ('id_airmensaje', models.IntegerField(primary_key=True, serialize=False)),
                ('mensaje', models.TextField()),
                ('descripcion', models.CharField(max_length=85)),
                ('visto', models.BooleanField(default=False)),
                ('hora_enviado', models.DateTimeField(auto_now_add=True)),
                ('direccion_destino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='amhsnacional.usuario_ezpin')),
                ('grupo_destino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='amhsnacional.grupo_ezpin')),
            ],
            options={
                'ordering': ['-id_airmensaje'],
            },
        ),
    ]
