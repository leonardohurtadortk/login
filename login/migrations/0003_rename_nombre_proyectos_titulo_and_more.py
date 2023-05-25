# Generated by Django 4.2.1 on 2023-05-25 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_project_proyectos_rename_task_tareas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectos',
            old_name='nombre',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='tareas',
            old_name='nombre',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='tareas',
            old_name='assigned_to',
            new_name='usuario_asignado',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='due_date',
        ),
        migrations.AddField(
            model_name='tareas',
            name='creada',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas',
            name='importante',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tareas',
            name='puntos',
            field=models.IntegerField(default=1, verbose_name='auth.User'),
            preserve_default=False,
        ),
    ]
