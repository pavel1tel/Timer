from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import urls as account_urls
from .views import main


urlpatterns = [
    path('', main, name='timer'),
    path('api/', include('timer.api.urls'), name = 'api')
]