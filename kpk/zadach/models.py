from django.db import models

class Time_subject(models.Model):
    time = models.CharField("Время урока", max_length=255)
    def __str__(self):
        return self.time

    class Meta:
        verbose_name = "Расписание звонков"  # Название модели в единственном числе
        verbose_name_plural = "Расписание звонков"  # Название модели во множественном числе

# таблица с уроками 101 группы
class Schedule101(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 101"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 101"  # Название модели во множественном числе
# таблица 111
class Schedule111(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
       return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 111"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 111"  # Название модели во множественном числе
# таблица 121
class Schedule121(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 121"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 121"  # Название модели во множественном числе

class Schedule201(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 201"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 201"  # Название модели во множественном числе

class Schedule202(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 202"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 202"  # Название модели во множественном числе

class Schedule211(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"
    class Meta:
        verbose_name = "Расписание 211"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 211"  # Название модели во множественном числе

class Schedule221(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 221"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 221"  # Название модели во множественном числе

class Schedule231(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 231"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 231"  # Название модели во множественном числе

class Schedule241(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 241"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 241"  # Название модели во множественном числе

class Schedule301(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 301"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 301"  # Название модели во множественном числе

class Schedule302(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 302"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 302"  # Название модели во множественном числе

class Schedule311(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"
    class Meta:
        verbose_name = "Расписание 311"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 311"  # Название модели во множественном числе


class Schedule321(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 321"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 321"  # Название модели во множественном числе

class Schedule331(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 331"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 331"  # Название модели во множественном числе

class Schedule341(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 341"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 341"  # Название модели во множественном числе

class Schedule401(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 401"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 401"  # Название модели во множественном числе

class Schedule402(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 402"  # Название модели в единственном числе
        verbose_name_plural = "Расписание 402"  # Название модели во множественном числе

class Schedule411(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 411"  # Название модели в единственном числе
        verbose_name_plural = "Расписания 411"  # Название модели во множественном числе

class Schedule421(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"
    class Meta:
        verbose_name = "Расписание 421"  # Название модели в единственном числе
        verbose_name_plural = "Расписания 421"  # Название модели во множественном числе
class Schedule431(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 431"  # Название модели в единственном числе
        verbose_name_plural = "Расписания 431"  # Название модели во множественном числе

class Schedule441(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 441"  # Название модели в единственном числе
        verbose_name_plural = "Расписания 441"  # Название модели во множественном числе

class Schedule131(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField("День", max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    has_changes = models.BooleanField("Изменения", default=False)
    def __str__(self):
        return f"{self.get_day_display()} - {self.index} - {self.subject} - {self.teacher} - {self.classroom}"

    class Meta:
        verbose_name = "Расписание 131"  # Название модели в единственном числе
        verbose_name_plural = "Расписания 131"  # Название модели во множественном числе

# Таблица с группами
class ListGroup(models.Model):
    title = models.CharField('Название группы', max_length=255)
    list_par101 = models.ManyToManyField(Schedule101, related_name='schedules', blank=True) # связь с уроками
    list_par111 = models.ManyToManyField(Schedule111, related_name='schedules', blank=True)
    list_par121 = models.ManyToManyField(Schedule121, related_name='schedules', blank=True)
    list_par131 = models.ManyToManyField(Schedule131, related_name='schedules', blank=True)
    list_par201 = models.ManyToManyField(Schedule201, related_name='schedules', blank=True)
    list_par202 = models.ManyToManyField(Schedule202, related_name='schedules', blank=True)
    list_par211 = models.ManyToManyField(Schedule211, related_name='schedules', blank=True)
    list_par221 = models.ManyToManyField(Schedule221, related_name='schedules', blank=True)
    list_par231 = models.ManyToManyField(Schedule231, related_name='schedules', blank=True)
    list_par241 = models.ManyToManyField(Schedule241, related_name='schedules', blank=True)
    list_par301 = models.ManyToManyField(Schedule301, related_name='schedules', blank=True)
    list_par302 = models.ManyToManyField(Schedule302, related_name='schedules', blank=True)
    list_par311 = models.ManyToManyField(Schedule311, related_name='schedules', blank=True)
    list_par321 = models.ManyToManyField(Schedule321, related_name='schedules', blank=True)
    list_par331 = models.ManyToManyField(Schedule331, related_name='schedules', blank=True)
    list_par341 = models.ManyToManyField(Schedule341, related_name='schedules', blank=True)
    list_par401 = models.ManyToManyField(Schedule401, related_name='schedules', blank=True)
    list_par402 = models.ManyToManyField(Schedule402, related_name='schedules', blank=True)
    list_par411 = models.ManyToManyField(Schedule411, related_name='schedules', blank=True)
    list_par421 = models.ManyToManyField(Schedule421, related_name='schedules', blank=True)
    list_par431 = models.ManyToManyField(Schedule431, related_name='schedules', blank=True)
    list_par441 = models.ManyToManyField(Schedule441, related_name='schedules', blank=True)

    # Новое поле для расписания звонков на субботу
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список групп "  # Название модели в единственном числе
        verbose_name_plural = "Список групп"  # Название модели во множественном числе

# таблица со специальностями
class ListSpec(models.Model):
    title = models.CharField('Специальности', max_length=255)
    groups = models.ManyToManyField(ListGroup, related_name='ListSpeci')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список специальностей"  # Название модели в единственном числе
        verbose_name_plural = "Список специальностей"  # Название модели во множественном числе
class ListPrepod(models.Model):
    title = models.CharField('Фамилия И.О. преподавателя:', max_length=255)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список преподавателей"  # Название модели в единственном числе
        verbose_name_plural = "Список преподавателей"  # Название модели во множественном числе

class Conflict(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    index = models.PositiveIntegerField(null=True, blank=True)
    group_number = models.CharField(max_length=50)
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)  # Добавили choices!
    subject = models.CharField(max_length=100, null=True, blank=True)
    teacher = models.CharField(max_length=255, null=True, blank=True)
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.group_number} - {self.get_day_display()} - {self.classroom} - {self.subject} - {self.teacher} - Index: {self.index}"

    class Meta:
        verbose_name = "Конфликт"  # Название модели в единственном числе
        verbose_name_plural = "Конфликты"  # Название модели во множественном числе

class ListEror(models.Model):
    title = models.CharField('Название ошибки:', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список ошибок"  # Название модели в единственном числе
        verbose_name_plural = "Список ошибок"  # Название модели во множественном числе

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)  # для заголовка
    content = models.TextField()  # для текста новости
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список новостей"  # Название модели в единственном числе
        verbose_name_plural = "Список новостей"  # Название модели во множественном числе

class ChangedSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    index = models.PositiveIntegerField("Номер урока", null=True, blank=True)
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)  # Добавили choices!
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Преподаватель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)
    change_date = models.DateTimeField("Дата изменения", auto_now_add=True)
    source_model = models.CharField("Источник", max_length=255,null=True)  # Хранит имя модели-источника

    def __str__(self):
        return f"{self.source_model} - {self.get_day_display()} - {self.classroom} - {self.subject} - {self.teacher} - Index: {self.index}"

    class Meta:
        verbose_name = "Список изменений"  # Название модели в единственном числе
        verbose_name_plural = "Список изменений"  # Название модели во множественном числе