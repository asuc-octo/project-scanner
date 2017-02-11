from django.db import models
from django.contrib.auth.models import User
import datetime

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
    name = models.CharField(max_length=100)
    _current_occupancy = models.IntegerField(default=0, db_column='current_occupancy')
    def __str__(self):
        return self.address
    @property 
    def current_occupancy(self):
        scanner_objs = Scanner.objects.filter(location=self)
        num_scans = 0
        for s in scanner_objs:
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
            scan_objs = Scan.objects.filter(scanner=s, datetime__range=(today_min,today_max))
            num_scans += len(scan_objs)
        return num_scans
        

class Scanner(models.Model): 
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True,related_name='scanner')
    description = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.location.address + ": " + self.description + " (id=" + str(self.pk) + ")"

class Scan(models.Model):
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, null=True, blank=True,related_name='scan')
    datetime = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
    def __str__(self):
        if self.scanner != None: 
            return self.scanner.description + ": " + str(self.datetime)
        else: 
            return "None: " + str(self.datetime)
    class Meta:
        ordering = ('datetime',)
        
        

