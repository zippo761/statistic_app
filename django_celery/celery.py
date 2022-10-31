import os

from celery import Celery

# from celery.schedules import crontab

# path of setting in out project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'statistic_app.settings')

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
CELERY_TIMEZONE = "Europe/Moscow"
# load task modules from all registered Django apps
app.autodiscover_tasks()
