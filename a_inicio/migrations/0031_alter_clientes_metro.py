# Generated by Django 4.1 on 2025-01-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_inicio', '0030_alter_clientes_image1_alter_clientes_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='metro',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
