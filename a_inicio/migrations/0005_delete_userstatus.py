# Generated by Django 4.1 on 2024-12-14 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inicio', '0004_remove_userstatus_user_userstatus_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserStatus',
        ),
    ]
