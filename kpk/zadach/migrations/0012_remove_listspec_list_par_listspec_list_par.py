# Generated by Django 4.2.15 on 2024-08-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0011_remove_schedule201_list_groups_listspec_list_par'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listspec',
            name='list_par',
        ),
        migrations.AddField(
            model_name='listspec',
            name='list_par',
            field=models.ManyToManyField(related_name='Speci', to='zadach.schedule201'),
        ),
    ]