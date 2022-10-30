import csv

from models import CustomsData

path = '../tickers.csv'


with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = CustomsData.objects.get_or_create(
            data_x=row[0],
            data_y=row[1],
        )
        # creates a tuple of the new object or
        # current object and a boolean of if it was created
