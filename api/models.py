from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Scan
	# Scanner id
	# Datetime
	# Chron jobs to turn things off 
# Scanner
	# Scanner id
	# Location id
	# Description
# Location
	# Location id
	# Address
	# City
	# State
	# Zip code
	# Admin (not technically a model)
	# Email
	# Password
# Add library with API keys


class Location(models.Model):
	address = models.CharField(max_length=300)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=100)
	zipcode = models.IntegerField(null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField()

	def __str__(self):
		return self.address

class Scanner(models.Model): 
	location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True,related_name='scanner')
	description = models.CharField(max_length=300)
	def __str__(self):
		return self.location.address + ": " + self.description + " (id=" + str(self.pk) + ")"

class Scan(models.Model):
	scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, null=True, blank=True,related_name='scan')
	datetime = models.DateTimeField(null=True, blank=True, default=timezone.now())
	def __str__(self):
		if self.scanner != None: 
			return self.scanner.description + ": " + str(self.datetime)
		else: 
			return "None: " + str(self.datetime)

	class Meta:
		ordering = ('datetime',)

