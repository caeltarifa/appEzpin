# Generated by Django 3.1.7 on 2021-04-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amhsnacional', '0014_directorio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo_ezpin',
            options={'ordering': ['-id_grupo']},
        ),
        migrations.RemoveField(
            model_name='grupo_ezpin',
            name='predeterminado',
        ),
        migrations.AddField(
            model_name='air_mensaje',
            name='asunto',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_ezpin',
            name='id_grupo',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]