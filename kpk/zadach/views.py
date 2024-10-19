from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import ListSpec, Schedule201, ListGroup, Schedule101, Schedule111, Schedule121, Schedule202, Schedule211, \
    Schedule221, Schedule231, Schedule241, Schedule301, Schedule302, Schedule311, Schedule321, Schedule331, Schedule341, \
    Schedule401, Schedule402, Schedule411, Schedule421, Schedule431, Schedule441, ListPrepod, Conflict
from .serializers import ListSpecSerializer, ListGroupSerializer, ScheduleSerializer201, TimeSerializer, \
    ListPrepodSerializer
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class ListSpecApi(APIView):
    # Отображение всех задач
    def get(self, request, pk=None):
        if pk is not None:
            ListSpec_obj = get_object_or_404(ListSpec, pk=pk)
            serializer = ListSpecSerializer(ListSpec_obj)
            return Response(serializer.data)
        else:
            ListSpeci = ListSpec.objects.all()
            serializer = ListSpecSerializer(ListSpeci, many=True)
            return Response(serializer.data)

    # Добавление новой задачи
    def post(self, request):
        serializer = ListSpecSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListGroupApi(APIView):
    def get(self, request, pk=None):
        teacher_name = request.query_params.get('teacher', None)

        if pk is not None:
            list_group_obj = get_object_or_404(ListGroup, pk=pk)
            serializer = ListGroupSerializer(list_group_obj)
            return Response(serializer.data)
        else:
            list_group = ListGroup.objects.all()

            if teacher_name:
                filtered_groups = []

                for group in list_group:
                    group_data = {
                        'id': group.id,
                        'title': group.title,
                    }

                    # Создаем словарь для хранения уроков по полям
                    lessons_dict = {}

                    for lesson_field in [
                        'list_par101', 'list_par111', 'list_par121',
                        'list_par201', 'list_par202', 'list_par211',
                        'list_par221', 'list_par231', 'list_par241',
                        'list_par301', 'list_par302', 'list_par311',
                        'list_par321', 'list_par331', 'list_par341',
                        'list_par401', 'list_par402', 'list_par411',
                        'list_par421', 'list_par431', 'list_par441'
                    ]:
                        # Получаем связанные уроки для каждого поля
                        related_lessons = getattr(group, lesson_field).filter(teacher__icontains=teacher_name)

                        # Если есть уроки, добавляем их в словарь
                        if related_lessons.exists():
                            serialized_lessons = ScheduleSerializer201(related_lessons, many=True).data
                            lessons_dict[lesson_field] = serialized_lessons

                    # Получаем время предмета
                    related_times = group.time.all()
                    serialized_times = TimeSerializer(related_times, many=True).data

                    # Если есть отфильтрованные уроки, добавляем их в группу
                    if lessons_dict:
                        group_data.update(lessons_dict)  # Обновляем group_data с уроками
                        group_data['time'] = serialized_times  # Добавляем время
                        filtered_groups.append(group_data)

                return Response(filtered_groups)

            serializer = ListGroupSerializer(list_group, many=True)
            return Response(serializer.data)
class ListPrepodApi(APIView):
    # Отображение всех задач
    def get(self, request, pk=None):
        if pk is not None:
            ListPrepod_obj = get_object_or_404(ListPrepod, pk=pk)
            serializer = ListPrepodSerializer( ListPrepod_obj)
            return Response(serializer.data)
        else:
            ListPrepodi = ListPrepod.objects.all()
            serializer = ListPrepodSerializer(ListPrepodi, many=True)
            return Response(serializer.data)

# проверка на совпадение в расписание
@receiver(pre_save)
def check_for_conflicts(sender, instance, **kwargs):
    if sender in [Schedule101, Schedule111, Schedule201, Schedule121, Schedule202, Schedule211,
                  Schedule221, Schedule231, Schedule241, Schedule301, Schedule302, Schedule311,
                  Schedule321, Schedule331, Schedule341,
                  Schedule401, Schedule402, Schedule411, Schedule421, Schedule431, Schedule441]:

        # Получаем все модели расписания
        schedule_models = [Schedule101, Schedule111, Schedule201, Schedule121, Schedule202, Schedule211,
                           Schedule221, Schedule231, Schedule241, Schedule301, Schedule302, Schedule311,
                           Schedule321, Schedule331, Schedule341,
                           Schedule401, Schedule402, Schedule411, Schedule421, Schedule431, Schedule441]

        # Сравниваем с аналогичными записями в других моделях
        for model in schedule_models:
            if model != sender:  # Исключаем текущую модель
                # Находим все записи с тем же днем, кабинетом и индексом
                conflicts = model.objects.filter(day=instance.day, classroom=instance.classroom, index=instance.index)
                for conflict_instance in conflicts:
                    # Если совпадение найдено, создаем запись в Conflict
                    combined_subjects = f"{instance.subject}, {conflict_instance.subject}"  # Объединяем предметы
                    Conflict.objects.create(
                        index=conflict_instance.index,
                        group_number=f"{sender.__name__} - {model.__name__}",
                        day=conflict_instance.day,
                        classroom=conflict_instance.classroom,
                        subject=combined_subjects  # Записываем объединенные предметы
                    )
 # конфликт по препод
        for model in schedule_models:
            if model != sender:
                conflicts1 = model.objects.filter(day=instance.day, teacher=instance.teacher, index=instance.index)
                for conflict_instance in conflicts1:
                    combined_subjects = f"{instance.subject}, {conflict_instance.subject}"  # Объединяем предметы
                    Conflict.objects.create(
                        index=conflict_instance.index,
                        group_number=f"{sender.__name__} - {model.__name__}",
                        day=conflict_instance.day,
                        classroom=conflict_instance.classroom,
                        subject=combined_subjects,  # Записываем объединенные предметы
                        teacher=conflict_instance.teacher
                    )

@receiver(post_save)
def create_conflict(sender, instance, created, **kwargs):
    if created and sender in [Schedule101, Schedule111, Schedule201, Schedule121, Schedule202, Schedule211,
                              Schedule221, Schedule231, Schedule241, Schedule301, Schedule302, Schedule311,
                              Schedule321, Schedule331, Schedule341,
                              Schedule401, Schedule402, Schedule411, Schedule421, Schedule431, Schedule441]:
        day = instance.day
        classroom = instance.classroom
        subject = instance.subject
        teacher = instance.teacher

        # Получаем все модели расписания
        schedule_models = [Schedule101, Schedule111, Schedule201, Schedule121, Schedule202, Schedule211,
                           Schedule221, Schedule231, Schedule241, Schedule301, Schedule302, Schedule311,
                           Schedule321, Schedule331, Schedule341,
                           Schedule401, Schedule402, Schedule411, Schedule421, Schedule431, Schedule441]

        # Сравниваем с аналогичными записями в других моделях
        for model in schedule_models:
            if model != sender:  # Исключаем текущую модель
                # Находим все записи с тем же днем, кабинетом и индексом
                conflicts = model.objects.filter(day=day, classroom=classroom, index=instance.index)

                for conflict_instance in conflicts:
                    combined_subjects = f"{subject}, {conflict_instance.subject}"  # Объединяем предметы
                    Conflict.objects.create(
                        index=conflict_instance.index,
                        group_number=f"{sender.__name__} - {model.__name__}",  # Название моделей как номер группы
                        day=conflict_instance.day,
                        classroom=conflict_instance.classroom,
                        subject=combined_subjects  # Записываем объединенные предметы
                    )
                conflicts1 = model.objects.filter(day=instance.day, teacher=instance.teacher, index=instance.index)

                for conflict_instance in conflicts1:
                    combined_subjects = f"{subject}, {conflict_instance.subject}"  # Объединяем предметы
                    Conflict.objects.create(
                        index=conflict_instance.index,
                        group_number=f"{sender.__name__} - {model.__name__}",  # Название моделей как номер группы
                        day=conflict_instance.day,
                        classroom=conflict_instance.classroom,
                        subject=combined_subjects  # Записываем объединенные предметы
                    )