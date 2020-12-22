import os
from celery import Celery
from project_celery.settings import BROKER_URL
# Setup Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_celery.settings')

app = Celery('project_celery', backend="django-db", broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
