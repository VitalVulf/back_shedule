# Generated by Django 5.1.4 on 2024-12-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadach', '0031_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangedSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока')),
                ('day', models.CharField(max_length=9, verbose_name='День')),
                ('subject', models.CharField(max_length=255, verbose_name='Предмет')),
                ('teacher', models.CharField(max_length=255, verbose_name='Преподаватель')),
                ('classroom', models.CharField(max_length=50, verbose_name='Кабинет')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('source_model', models.CharField(max_length=255, null=True, verbose_name='Источник')),
            ],
            options={
                'verbose_name': 'Список изменений',
                'verbose_name_plural': 'Список изменений',
            },
        ),
        migrations.CreateModel(
            name='Schedule131',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока')),
                ('day', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День')),
                ('subject', models.CharField(max_length=255, verbose_name='Предмет')),
                ('teacher', models.CharField(max_length=255, verbose_name='Преподаватель')),
                ('classroom', models.CharField(max_length=50, verbose_name='Кабинет')),
                ('has_changes', models.BooleanField(default=False, verbose_name='Изменения')),
            ],
            options={
                'verbose_name': 'Расписание 131',
                'verbose_name_plural': 'Расписания 131',
            },
        ),
        migrations.CreateModel(
            name='Time_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255, verbose_name='Время урока')),
            ],
            options={
                'verbose_name': 'Расписание звонков',
                'verbose_name_plural': 'Расписание звонков',
            },
        ),
        migrations.RemoveField(
            model_name='listgroup',
            name='time',
        ),
        migrations.AlterModelOptions(
            name='conflict',
            options={'verbose_name': 'Конфликт', 'verbose_name_plural': 'Конфликты'},
        ),
        migrations.AlterModelOptions(
            name='listeror',
            options={'verbose_name': 'Список ошибок', 'verbose_name_plural': 'Список ошибок'},
        ),
        migrations.AlterModelOptions(
            name='listgroup',
            options={'verbose_name': 'Список групп ', 'verbose_name_plural': 'Список групп'},
        ),
        migrations.AlterModelOptions(
            name='listprepod',
            options={'verbose_name': 'Список преподавателей', 'verbose_name_plural': 'Список преподавателей'},
        ),
        migrations.AlterModelOptions(
            name='listspec',
            options={'verbose_name': 'Список специальностей', 'verbose_name_plural': 'Список специальностей'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Список новостей', 'verbose_name_plural': 'Список новостей'},
        ),
        migrations.AlterModelOptions(
            name='schedule101',
            options={'verbose_name': 'Расписание 101', 'verbose_name_plural': 'Расписание 101'},
        ),
        migrations.AlterModelOptions(
            name='schedule111',
            options={'verbose_name': 'Расписание 111', 'verbose_name_plural': 'Расписание 111'},
        ),
        migrations.AlterModelOptions(
            name='schedule121',
            options={'verbose_name': 'Расписание 121', 'verbose_name_plural': 'Расписание 121'},
        ),
        migrations.AlterModelOptions(
            name='schedule201',
            options={'verbose_name': 'Расписание 201', 'verbose_name_plural': 'Расписание 201'},
        ),
        migrations.AlterModelOptions(
            name='schedule202',
            options={'verbose_name': 'Расписание 202', 'verbose_name_plural': 'Расписание 202'},
        ),
        migrations.AlterModelOptions(
            name='schedule211',
            options={'verbose_name': 'Расписание 211', 'verbose_name_plural': 'Расписание 221'},
        ),
        migrations.AlterModelOptions(
            name='schedule221',
            options={'verbose_name': 'Расписание 221', 'verbose_name_plural': 'Расписание 221'},
        ),
        migrations.AlterModelOptions(
            name='schedule231',
            options={'verbose_name': 'Расписание 231', 'verbose_name_plural': 'Расписание 231'},
        ),
        migrations.AlterModelOptions(
            name='schedule241',
            options={'verbose_name': 'Расписание 241', 'verbose_name_plural': 'Расписание 241'},
        ),
        migrations.AlterModelOptions(
            name='schedule301',
            options={'verbose_name': 'Расписание 301', 'verbose_name_plural': 'Расписание 301'},
        ),
        migrations.AlterModelOptions(
            name='schedule302',
            options={'verbose_name': 'Расписание 302', 'verbose_name_plural': 'Расписание 302'},
        ),
        migrations.AlterModelOptions(
            name='schedule311',
            options={'verbose_name': 'Расписание 311', 'verbose_name_plural': 'Расписание 311'},
        ),
        migrations.AlterModelOptions(
            name='schedule321',
            options={'verbose_name': 'Расписание 321', 'verbose_name_plural': 'Расписание 321'},
        ),
        migrations.AlterModelOptions(
            name='schedule331',
            options={'verbose_name': 'Расписание 331', 'verbose_name_plural': 'Расписание 331'},
        ),
        migrations.AlterModelOptions(
            name='schedule341',
            options={'verbose_name': 'Расписание 341', 'verbose_name_plural': 'Расписание 341'},
        ),
        migrations.AlterModelOptions(
            name='schedule401',
            options={'verbose_name': 'Расписание 401', 'verbose_name_plural': 'Расписание 401'},
        ),
        migrations.AlterModelOptions(
            name='schedule402',
            options={'verbose_name': 'Расписание 402', 'verbose_name_plural': 'Расписание 402'},
        ),
        migrations.AlterModelOptions(
            name='schedule411',
            options={'verbose_name': 'Расписание 411', 'verbose_name_plural': 'Расписания 411'},
        ),
        migrations.AlterModelOptions(
            name='schedule421',
            options={'verbose_name': 'Расписание 421', 'verbose_name_plural': 'Расписания 421'},
        ),
        migrations.AlterModelOptions(
            name='schedule431',
            options={'verbose_name': 'Расписание 431', 'verbose_name_plural': 'Расписания 431'},
        ),
        migrations.AlterModelOptions(
            name='schedule441',
            options={'verbose_name': 'Расписание 441', 'verbose_name_plural': 'Расписания 441'},
        ),
        migrations.AddField(
            model_name='schedule101',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule111',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule121',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule201',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule202',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule211',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule221',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule231',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule241',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule301',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule302',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule311',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule321',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule331',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule341',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule401',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule402',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule411',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule421',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule431',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AddField(
            model_name='schedule441',
            name='has_changes',
            field=models.BooleanField(default=False, verbose_name='Изменения'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='schedule101',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule101',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule101',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule101',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule101',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule111',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule111',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule111',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule111',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule111',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule121',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule121',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule121',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule121',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule121',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule201',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule201',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule201',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule201',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule201',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule202',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule202',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule202',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule202',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule202',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule211',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule211',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule211',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule211',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule211',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule221',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule221',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule221',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule221',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule221',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule231',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule231',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule231',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule231',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule231',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule241',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule241',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule241',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule241',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule241',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule301',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule301',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule301',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule301',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule301',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule302',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule302',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule302',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule302',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule302',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule311',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule311',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule311',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule311',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule311',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule321',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule321',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule321',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule321',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule321',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule331',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule331',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule331',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule331',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule331',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule341',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule341',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule341',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule341',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule341',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule401',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule401',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule401',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule401',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule401',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule402',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule402',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule402',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule402',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule402',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule411',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule411',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule411',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule411',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule411',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule421',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule421',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule421',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule421',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule421',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule431',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule431',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule431',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule431',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule431',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule441',
            name='classroom',
            field=models.CharField(max_length=50, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='schedule441',
            name='day',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='schedule441',
            name='index',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='schedule441',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='schedule441',
            name='teacher',
            field=models.CharField(max_length=255, verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='listgroup',
            name='list_par131',
            field=models.ManyToManyField(blank=True, related_name='schedules', to='zadach.schedule131'),
        ),
        migrations.DeleteModel(
            name='TimeUR',
        ),
    ]
