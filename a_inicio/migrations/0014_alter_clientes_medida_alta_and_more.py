# Generated by Django 4.1 on 2025-01-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_inicio', '0013_alter_clientes_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='medida_alta',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='medida_baja',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='medida_media',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
