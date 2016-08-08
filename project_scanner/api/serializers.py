from rest_framework import serializers
from django.utils.timezone import now
from api.models import Location, Scanner, Scan, LANGUAGE_CHOICES, STYLE_CHOICES

'''
from api.models import *
from api.serializers import ScanSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

scan = Scan.objects.get(pk=5)
serializer = ScanSerializer(scan)
serializer.data
'''

class ScanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Scan
		fields = ('id', 'scanner', 'datetime')
# class ScanSerializer(serializers.Serializer):
	# pk = serializers.IntegerField(read_only=True)
	# scan = ScanField()
	
	# def create(self, validated_data):
	# 	scanner_pk = int(validated_data.get('scanner_pk'))
	# 	scan_scanner = Scanner.objects.get(pk=scanner_pk)
	# 	scan_datetime = now()
	# 	return Scan.objects.create(scanner=scan_scanner, datetime=scan_datetime)

	# def update(self, instance, validated_data):
	# 	get_scanner = lambda x: Scanner.objects.get(pk=x) if x else instance.scanner
	# 	instance.scanner = get_scanner(validated_data.get('scanner_pk', None))
	# 	instance.datetime = validated_data.get('datetime', instance.datetime)
	# 	instance.save()
	# 	return instance




