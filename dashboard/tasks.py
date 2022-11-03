import csv
from django_celery.celery import app
from dashboard.models import DashboardData
from celery.schedules import crontab


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        update_database(),
    )

@app.task
def update_database():
    with open("/home/cabox/workspace/statistic_app/tickers.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row['Company'], row['Symbol'])

            data = DashboardData.objects.create(data_x=row['Company'],
                                                data_y=row['Symbol'])
            
        data.save()
        print('SAVE ALREADY')
