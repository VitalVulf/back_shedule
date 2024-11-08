# Generated by Django 4.2.15 on 2024-08-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0021_listspec_list_par202'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название группы')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule101',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule111',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule121',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule211',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule221',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule241',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule301',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule302',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule311',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule321',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule331',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule341',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule401',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule402',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule411',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule421',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule431',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule441',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='listspec',
            name='list_par',
        ),
        migrations.RemoveField(
            model_name='listspec',
            name='list_par202',
        ),
        migrations.RemoveField(
            model_name='listspec',
            name='list_par231',
        ),
        migrations.AlterField(
            model_name='listspec',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Специальности'),
        ),
        migrations.DeleteModel(
            name='zadach',
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par101',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule101'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par111',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule111'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par121',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule121'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par201',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule201'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par202',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule202'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par211',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule211'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par221',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule221'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par231',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule231'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par241',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule241'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par301',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule301'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par302',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule302'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par311',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule311'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par321',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule321'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par331',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule331'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par341',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule341'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par401',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule401'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par402',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule402'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par411',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule411'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par421',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule421'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par431',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule431'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par441',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule441'),
        ),
        migrations.AddField(
            model_name='listspec',
            name='groups',
            field=models.ManyToManyField(related_name='ListSpeci', to='zadach.listgroup'),
        ),
    ]
