# Generated by Django 5.1.4 on 2025-02-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0034_remove_listgroup_time_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conflict',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9),
        ),
    ]
