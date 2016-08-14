from rest_framework import generics
from api.models import *
from api.serializers import UserSerializer, ScanSerializer, ScannerSerializer, LocationSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ScanList(generics.ListCreateAPIView):
	"""
	List all scans
	"""
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
	# authentication_classes = ('TokenAuthentication',)
	# permission_classes = (IsAuthenticated,)
	queryset = Scan.objects.all()
	serializer_class = ScanSerializer
class ScanDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a scan instance.
	"""
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
	# authentication_classes = ('TokenAuthentication',)
	# permission_classes = (IsAuthenticated,)
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
	# authentication_classes = ('TokenAuthentication',)
	# permission_classes = (IsAuthenticated,)
	queryset = Scanner.objects.all()
	serializer_class = ScannerSerializer 

class LocationList(generics.ListAPIView):
	"""
	List all locations
	"""
	# authentication_classes = ('TokenAuthentication',)
	# permission_classes = (IsAuthenticated,)
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveAPIView):
	"""
	Retrieve, update or delete a location instance.
	"""
	# authentication_classes = ('TokenAuthentication',)
	# permission_classes = (IsAuthenticated,)
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	