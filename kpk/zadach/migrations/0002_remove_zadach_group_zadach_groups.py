# Generated by Django 4.2.15 on 2024-08-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zadach',
            name='group',
        ),
        migrations.AddField(
            model_name='zadach',
            name='groups',
            field=models.ManyToManyField(related_name='zadachi', to='zadach.listspec'),
        ),
    ]
