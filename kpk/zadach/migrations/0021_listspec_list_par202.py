# Generated by Django 4.2.15 on 2024-08-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0020_schedule202'),
    ]

    operations = [
        migrations.AddField(
            model_name='listspec',
            name='list_par202',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule202'),
        ),
    ]
