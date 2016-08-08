from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

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

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Location(models.Model):
	address = models.CharField(max_length=300)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=100)
	zipcode = models.IntegerField(null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField()

class Scanner(models.Model): 
	location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
	description = models.CharField(max_length=300)

class Scan(models.Model):
	scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		ordering = ('datetime',)

