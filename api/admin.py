from django.contrib import admin

from .models import Location, Scanner, Scan
# Register your models here.

admin.site.register(Location)
admin.site.register(Scanner)
admin.site.register(Scan)