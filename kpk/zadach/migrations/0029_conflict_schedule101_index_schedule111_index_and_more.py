# Generated by Django 4.2.15 on 2024-09-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0028_listprepod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conflict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(blank=True, null=True)),
                ('group_number', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=9)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('teacher', models.CharField(blank=True, max_length=255, null=True)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='schedule101',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule111',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule121',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule201',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule202',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule211',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule221',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule231',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule241',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule301',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule302',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule311',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule321',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule331',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule341',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule401',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule402',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule411',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule421',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule431',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule441',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
