# Generated by Django 4.1.7 on 2025-01-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_contacto', '0006_alter_contacto_tipo_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'Consulta'], [1, 'Publicarme']]),
        ),
    ]
