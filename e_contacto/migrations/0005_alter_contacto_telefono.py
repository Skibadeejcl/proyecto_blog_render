# Generated by Django 4.1.7 on 2023-07-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_contacto', '0004_alter_contacto_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
