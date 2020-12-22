from .views import *

from django.conf.urls import url
from django.urls import path


urlpatterns = [
    path('', get_respone,),
    path('api/<int:pk>', get_object),
    path('send-email', send_email_with_celery),
    path('health', healthCheck)
]
