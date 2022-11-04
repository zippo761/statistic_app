from django.db import models


class DashboardData(models.Model):
    data_x = models.TextField()
    data_y = models.TextField()
