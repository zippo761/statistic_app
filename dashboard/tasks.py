import csv

from django_celery.celery import app

from .models import CustomsData


@app.task
def update_database():

    with open(r'C:\Users\stoka\PycharmProjects\statistic_app') as f:
        r = csv.reader(f)
        for row in r:
            _, created = CustomsData.objects.get_or_create(
                data_x=row[0],
                data_y=row[1],
            )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
