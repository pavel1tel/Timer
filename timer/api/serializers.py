from rest_framework.serializers import ModelSerializer
from timer.models import Activity


class ActivityCreatSerializer(ModelSerializer):
    class Meta():
        model = Activity
        exclude = ['user',
                   'type',
                   'time']


class ActivityListSerializer(ModelSerializer):
    class Meta():
        model = Activity
        fields = '__all__'
