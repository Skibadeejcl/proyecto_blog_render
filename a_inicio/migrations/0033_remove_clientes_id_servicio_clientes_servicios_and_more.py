# Generated by Django 4.1 on 2025-01-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_inicio', '0032_servicio_remove_clientes_servicios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='id_servicio',
        ),
        migrations.AddField(
            model_name='clientes',
            name='servicios',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
