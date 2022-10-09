from django.db import models
from places.fields import PlacesField


class MyLocationModel(models.Model):
    location = PlacesField()


# Create your models here.
class Language(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"
