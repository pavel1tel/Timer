from django.urls import path
from .views import (
    CreateActivityAPIView,
    ListActivityAPIView,
)


urlpatterns = [
    path('create' ,CreateActivityAPIView.as_view()),
    path('list' ,ListActivityAPIView.as_view()),

]