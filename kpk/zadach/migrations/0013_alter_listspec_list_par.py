# Generated by Django 4.2.15 on 2024-08-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0012_remove_listspec_list_par_listspec_list_par'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listspec',
            name='list_par',
            field=models.ManyToManyField(related_name='schedules', to='zadach.schedule201'),
        ),
    ]
