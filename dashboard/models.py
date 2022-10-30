from django.db import models


class CustomsData(models.Model):
	data_x = models.CharField(max_length=120)
	data_y = models.CharField(max_length=120)

	def __str__(self):
		return self.data_y, self.data_y
