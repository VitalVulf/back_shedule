from django.db import models


class TimeUR(models.Model):
    title = models.CharField('Время урока ', max_length=255)

    def __str__(self):
        return self.title

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "
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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "
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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "


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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

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
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения номера урока
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    subject = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    classroom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.day} - {self.subject} {self.teacher} "

# Таблица с группами
class ListGroup(models.Model):
    title = models.CharField('Название группы', max_length=255)
    list_par101 = models.ManyToManyField(Schedule101, related_name='schedules',blank=True) # связь с уроками
    list_par111=models.ManyToManyField(Schedule111, related_name='schedules',blank=True)
    list_par121=models.ManyToManyField(Schedule121, related_name='schedules',blank=True)
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
    time = models.ManyToManyField(TimeUR,related_name='schedules', blank=True)
    def __str__(self):
        return self.title

# таблица со специальностями
class ListSpec(models.Model):
    title = models.CharField('Специальности', max_length=255)
    groups = models.ManyToManyField(ListGroup, related_name='ListSpeci')

    def __str__(self):
        return self.title

class ListPrepod(models.Model):
    title = models.CharField('Фамилия И.О. преподавателя:', max_length=255)
    def __str__(self):
        return self.title

class Conflict(models.Model):
    index = models.PositiveIntegerField(null=True, blank=True)  # Поле для хранения индекса урока
    group_number = models.CharField(max_length=50)
    day = models.CharField(max_length=9)
    subject = models.CharField(max_length=100,null=True, blank=True)
    teacher = models.CharField(max_length=255,null=True, blank=True)
    classroom = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.group_number} - {self.day} - {self.classroom} - {self.subject} - {self.teacher} - Index: {self.index}"

class ListEror(models.Model):
    title = models.CharField('Название ошибки:', max_length=255)

    def __str__(self):
        return self.title
class News(models.Model):
    title = models.CharField(max_length=200)  # для заголовка
    content = models.TextField()  # для текста новости
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title