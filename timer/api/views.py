from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from timer.models import Activity
from .serializers import (
    ActivityCreatSerializer,
    ActivityListSerializer,
)


class CreateActivityAPIView(CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivityCreatSerializer

    def get_queryset(self):
        time = self.request.query_params.get('time')
        print(time)
        tip = self.request.query_params.get('type', None)
        user = self.request.query_params.get('user', None)
        return [tip, user, time]

    def perform_create(self, serializer):
        data = self.get_queryset()
        serializer.save(user=self.request.user, type=data[0], time=data[2])


class ListActivityAPIView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivityListSerializer
