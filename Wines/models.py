from django.db import models

# Create your models here.
class Wine(models.Model):
	country = models.CharField(max_length=100, null=True, blank=True)
	description = models.CharField(max_length=1000, null=True, blank=True)
	designation = models.CharField(max_length=250, null=True, blank=True)
	points = models.IntegerField(default=-1)
	price = models.FloatField(default=-1.0)
	province = models.CharField(max_length=250, null=True, blank=True)
	region_1 = models.CharField(max_length=250, null=True, blank=True)
	region_2 = models.CharField(max_length=250, null=True, blank=True)
	variety = models.CharField(max_length=250, null=True, blank=True)
	winery = models.CharField(max_length=250, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return str(self.id) + ' -- ' + str(self.designation)