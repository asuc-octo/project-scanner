from rest_framework import generics
from api.models import *
from api.serializers import ScanSerializer

class ScanList(generics.ListCreateAPIView):
	"""
	List all scans
	"""
	queryset = Scan.objects.all()
	serializer_class = ScanSerializer
class ScanDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a scan instance.
	"""
	queryset = Scan.objects.all()
	serializer_class = ScanSerializer

class ScannerList(generics.ListAPIView):
	"""
	List all scanners
	"""
	queryset = Scanner.objects.all()
	serializer_class = ScannerSerializer

class ScannerDetail(generics.RetrieveAPIView):
	"""
	Retrieve, update or delete a scanner instance.
	"""
	queryset = Scanner.objects.all()
	serializer_class = ScannerSerializer 

class LocationList(generics.ListAPIView):
	"""
	List all locations
	"""
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveAPIView):
	"""
	Retrieve, update or delete a location instance.
	"""
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	