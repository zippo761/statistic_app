import csv

from dashboard.models import StatisticData
from django_celery.celery import app


@app.task
def update_database():
    with open(r"C:\Users\stoka\PycharmProjects\statistic_app\tickers.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = StatisticData.c(data_x=row['Company'],
                                 data_y=row['Symbol'])

        data.save()
        print('SAVE ALREADY')
