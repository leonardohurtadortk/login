# Generated by Django 4.2.1 on 2023-05-25 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_proyecto_tarea_remove_tareas_proyecto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='titulo',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='titulo',
            new_name='nombre',
        ),
    ]
