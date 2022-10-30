import os

from celery import Celery

# path of setting in out project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'statistic_app.settings')

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
CELERY_TIMEZONE = "Europe/Moscow"
# load task modules from all registered Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def bar():
    return "hello NIKITA REDIS"
