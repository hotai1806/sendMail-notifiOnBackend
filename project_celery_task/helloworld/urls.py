from .views import *

from django.conf.urls import url
from django.urls import path


urlpatterns = [
    path('', get_respone, name='hello-respone'),
    path('api/<int:pk>/', get_object)
]
