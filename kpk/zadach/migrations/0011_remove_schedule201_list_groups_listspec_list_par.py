# Generated by Django 4.2.15 on 2024-08-21 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0010_rename_list_par_schedule201_list_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule201',
            name='list_groups',
        ),
        migrations.AddField(
            model_name='listspec',
            name='list_par',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='zadach.schedule201'),
        ),
    ]
