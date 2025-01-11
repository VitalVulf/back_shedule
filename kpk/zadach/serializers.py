from .models import ListSpec, ListGroup,ListPrepod
from .models import ListSpec,Schedule201,Schedule202,Schedule211,Schedule221,Schedule231,Schedule241,Schedule301,\
    Schedule302,Schedule311,Schedule321,Schedule331,Schedule341,Schedule401,Schedule402,Schedule411,Schedule421, \
    Schedule431,Schedule441,Schedule101,Schedule121,Schedule111,ListEror,Schedule131,News,Time_subject
from rest_framework import serializers


# уроки
class ScheduleSerializer101(serializers.ModelSerializer):
    class Meta:
        model = Schedule101
        fields = '__all__'
class ScheduleSerializer111(serializers.ModelSerializer):
    class Meta:
        model = Schedule111
        fields = '__all__'

class ScheduleSerializer121(serializers.ModelSerializer):
    class Meta:
        model = Schedule121
        fields = '__all__'

class ScheduleSerializer201(serializers.ModelSerializer):
    class Meta:
        model = Schedule201
        fields = '__all__'

class ScheduleSerializer202(serializers.ModelSerializer):
    class Meta:
        model = Schedule202
        fields = '__all__'

class ScheduleSerializer211(serializers.ModelSerializer):
    class Meta:
        model = Schedule211
        fields = '__all__'
# группы
class ScheduleSerializer221(serializers.ModelSerializer):
    class Meta:
        model = Schedule221
        fields = '__all__'

class ScheduleSerializer231(serializers.ModelSerializer):
    class Meta:
        model = Schedule231
        fields = '__all__'

class ScheduleSerializer231(serializers.ModelSerializer):
    class Meta:
        model = Schedule231
        fields = '__all__'

class ScheduleSerializer241(serializers.ModelSerializer):
    class Meta:
        model = Schedule241
        fields = '__all__'

class ScheduleSerializer301(serializers.ModelSerializer):
    class Meta:
        model = Schedule301
        fields = '__all__'

class ScheduleSerializer302(serializers.ModelSerializer):
    class Meta:
        model = Schedule302
        fields = '__all__'

class ScheduleSerializer311(serializers.ModelSerializer):
    class Meta:
        model = Schedule311
        fields = '__all__'

class ScheduleSerializer321(serializers.ModelSerializer):
    class Meta:
        model = Schedule321
        fields = '__all__'

class ScheduleSerializer331(serializers.ModelSerializer):
    class Meta:
        model = Schedule331
        fields = '__all__'

class ScheduleSerializer341(serializers.ModelSerializer):
    class Meta:
        model = Schedule341
        fields = '__all__'

class ScheduleSerializer401(serializers.ModelSerializer):
    class Meta:
        model = Schedule401
        fields = '__all__'

class ScheduleSerializer402(serializers.ModelSerializer):
    class Meta:
        model = Schedule402
        fields = '__all__'

class ScheduleSerializer411(serializers.ModelSerializer):
    class Meta:
        model = Schedule411
        fields = '__all__'

class ScheduleSerializer421(serializers.ModelSerializer):
    class Meta:
        model = Schedule421
        fields = '__all__'

class ScheduleSerializer431(serializers.ModelSerializer):
    class Meta:
        model = Schedule431
        fields = '__all__'

class ScheduleSerializer441(serializers.ModelSerializer):
    class Meta:
        model = Schedule441
        fields = '__all__'

class ScheduleSerializer131(serializers.ModelSerializer):
    class Meta:
        model = Schedule131
        fields = '__all__'
class ListGroupSerializer(serializers.ModelSerializer):
    list_par101 = ScheduleSerializer101(many=True, read_only=True) # связь с уроками
    list_par111 = ScheduleSerializer111(many=True, read_only=True)
    list_par121 = ScheduleSerializer121(many=True, read_only=True)
    list_par131 = ScheduleSerializer131(many=True, read_only=True)
    list_par201 = ScheduleSerializer201(many=True, read_only=True)
    list_par202 = ScheduleSerializer202(many=True, read_only=True)
    list_par211 = ScheduleSerializer211(many=True, read_only=True)
    list_par221 = ScheduleSerializer221(many=True, read_only=True)
    list_par231 = ScheduleSerializer231(many=True, read_only=True)
    list_par241 = ScheduleSerializer241(many=True, read_only=True)
    list_par301 = ScheduleSerializer301(many=True, read_only=True)
    list_par302 = ScheduleSerializer302(many=True, read_only=True)
    list_par311 = ScheduleSerializer311(many=True, read_only=True)
    list_par321 = ScheduleSerializer321(many=True, read_only=True)
    list_par331 = ScheduleSerializer331(many=True, read_only=True)
    list_par341 = ScheduleSerializer341(many=True, read_only=True)
    list_par401 = ScheduleSerializer401(many=True, read_only=True)
    list_par402 = ScheduleSerializer402(many=True, read_only=True)
    list_par411 = ScheduleSerializer411(many=True, read_only=True)
    list_par421 = ScheduleSerializer421(many=True, read_only=True)
    list_par431 = ScheduleSerializer431(many=True, read_only=True)
    list_par441 = ScheduleSerializer441(many=True, read_only=True)
    class Meta:
        model=ListGroup
        fields=('id', 'title', 'list_par101','list_par111', 'list_par121','list_par131', 'list_par201', 'list_par202', 'list_par211',
                'list_par221', 'list_par231', 'list_par241','list_par301' ,'list_par302' ,'list_par311','list_par321',
                'list_par331' ,'list_par341' ,'list_par401','list_par402','list_par411','list_par421','list_par431', 'list_par441')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Удаляем пустые списки из представления
        if not representation['list_par101']:
            representation.pop('list_par101')
        if not representation['list_par111']:
            representation.pop('list_par111')
        if not representation['list_par121']:
            representation.pop('list_par121')
        if not representation['list_par131']:
            representation.pop('list_par131')
        if not representation['list_par201']:
            representation.pop('list_par201')
        if not representation['list_par202']:
            representation.pop('list_par202')
        if not representation['list_par211']:
            representation.pop('list_par211')
        if not representation['list_par221']:
            representation.pop('list_par221')
        if not representation['list_par231']:
            representation.pop('list_par231')
        if not representation['list_par241']:
            representation.pop('list_par241')
        if not representation['list_par301']:
            representation.pop('list_par301')
        if not representation['list_par302']:
            representation.pop('list_par302')
        if not representation['list_par311']:
            representation.pop('list_par311')
        if not representation['list_par321']:
            representation.pop('list_par321')
        if not representation['list_par331']:
            representation.pop('list_par331')
        if not representation['list_par341']:
            representation.pop('list_par341')
        if not representation['list_par401']:
            representation.pop('list_par401')
        if not representation['list_par402']:
            representation.pop('list_par402')
        if not representation['list_par411']:
            representation.pop('list_par411')
        if not representation['list_par421']:
            representation.pop('list_par421')
        if not representation['list_par431']:
            representation.pop('list_par431')
        if not representation['list_par441']:
            representation.pop('list_par441')

        return representation
class ListSpecSerializer(serializers.ModelSerializer):
    groups = ListGroupSerializer(many=True, read_only=True)
    class Meta:
        model=ListSpec
        fields='__all__'


class ListPrepodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListPrepod
        fields='__all__'

class ListErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListEror
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_subject
        fields = '__all__'