# Generated by Django 4.2.15 on 2024-08-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0016_remove_listspec_list_par231_alter_listspec_list_par'),
    ]

    operations = [
        migrations.AddField(
            model_name='listspec',
            name='list_par231',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule231'),
        ),
    ]