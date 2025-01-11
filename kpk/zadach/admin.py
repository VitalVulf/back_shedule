from django.contrib import admin
from django.http import HttpResponse
from django.core.management import call_command
from .models import ListSpec, ListGroup, Schedule201, Schedule231, Schedule111, Schedule441, Schedule101, Schedule121, \
    Schedule131, Schedule431, Schedule421, Schedule202, Schedule311, Schedule321, Schedule331, Schedule341, Schedule401, \
    Schedule402, \
    Schedule411, Schedule302, Schedule301, Schedule241, Schedule221, Schedule211, ListPrepod, Conflict, \
    ListEror, News, Time_subject, ChangedSchedule


@admin.action(description='Сделать единый бэкап всей базы данных')
def backup_database(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="backup.json"'

    # Бэкап всей базы данных в один файл
    call_command('dumpdata', stdout=response)

    return response


# Регистрация всех моделей и добавление действия для бэкапа
class BaseAdmin(admin.ModelAdmin):
    actions = [backup_database]
admin.site.register(Time_subject, BaseAdmin)
admin.site.register(ListSpec, BaseAdmin)
admin.site.register(ChangedSchedule, BaseAdmin)
admin.site.register(ListGroup, BaseAdmin)
admin.site.register(Schedule101, BaseAdmin)
admin.site.register(Schedule111, BaseAdmin)
admin.site.register(Schedule121, BaseAdmin)
admin.site.register(Schedule131, BaseAdmin)
admin.site.register(Schedule201, BaseAdmin)
admin.site.register(Schedule202, BaseAdmin)
admin.site.register(Schedule211, BaseAdmin)
admin.site.register(Schedule221, BaseAdmin)
admin.site.register(Schedule231, BaseAdmin)
admin.site.register(Schedule241, BaseAdmin)
admin.site.register(Schedule301, BaseAdmin)
admin.site.register(Schedule302, BaseAdmin)
admin.site.register(Schedule311, BaseAdmin)
admin.site.register(Schedule321, BaseAdmin)
admin.site.register(Schedule331, BaseAdmin)
admin.site.register(Schedule341, BaseAdmin)
admin.site.register(Schedule401, BaseAdmin)
admin.site.register(Schedule402, BaseAdmin)
admin.site.register(Schedule411, BaseAdmin)
admin.site.register(Schedule421, BaseAdmin)
admin.site.register(Schedule431, BaseAdmin)
admin.site.register(Schedule441, BaseAdmin)
admin.site.register(ListPrepod, BaseAdmin)
admin.site.register(Conflict, BaseAdmin)
admin.site.register(ListEror, BaseAdmin)
admin.site.register(News, BaseAdmin)