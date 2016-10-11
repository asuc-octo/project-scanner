from django.db import models
from django.utils import timezone
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
    current_occupancy = models.IntegerField(default=0)
    def __str__(self):
        return self.address

class Scanner(models.Model): 
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True,related_name='scanner')
    description = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.location.address + ": " + self.description + " (id=" + str(self.pk) + ")"

class Scan(models.Model):
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, null=True, blank=True,related_name='scan')
    datetime = models.DateTimeField(null=True, blank=True, default=timezone.now)
    def __str__(self):
        if self.scanner != None: 
            return self.scanner.description + ": " + str(self.datetime)
        else: 
            return "None: " + str(self.datetime)
    class Meta:
        ordering = ('datetime',)
    # every time a new scan is created, update the current occupancy of the location
    def save(self,  *args, **kwargs):
        # Only runs code if object being created 
        if not self.pk:
            location = self.scanner.location
            # Update the current occupancy of this location: all the scans seen today by the scanners associated with this location
            scanner_objs = Scanner.objects.filter(location=location)
            num_scans = 0
            print scanner_objs
            for s in scanner_objs:
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                scan_objs = Scan.objects.filter(scanner=s, datetime__range=(today_min,today_max))
                print scan_objs
                print len(scan_objs)
                num_scans += len(scan_objs)
            print num_scans
            # Add 1 to account for the current scan that hasn't been saved yet
            location.current_occupancy=num_scans+1
            location.save()
            print location.current_occupancy
        super(Scan, self).save(*args, **kwargs)
    # Also update current occupancy when scan is deleted    
    def delete(self, *args, **kwargs):
        location = self.scanner.location
        if self.datetime.date()==timezone.now().date():
            location.current_occupancy -= 1
            location.save()
        super(Scan, self).delete(*args, **kwargs)
        
        

