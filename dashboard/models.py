from django.db import models


class StatisticData(models.Model):
    data_x = models.CharField(max_length=50)
    data_y = models.CharField(max_length=50)

class DashboardData(models.Model):
    data_x = models.CharField(max_length=50)
    data_y = models.CharField(max_length=50)
