import os

from celery import Celery
from celery.schedules import crontab

# path of setting in out project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'statistic_app.settings')

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
CELERY_TIMEZONE = "Europe/Moscow"

app.conf.timezone = 'UTC'

# load task modules from all registered Django apps
app.autodiscover_tasks()

# celery beat tasks
app.conf.beat_schedule = {
    'update-database-every-35-seconds': {
        'task': 'dashboard.tasks.update_database',
        'schedule': crontab(hour=7, minute=30, day_of_week=1)
    },
}
