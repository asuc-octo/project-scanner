from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializers import ScanSerializer

@api_view(['GET', 'POST'])
def scan_list(request, format=None):
    """
    List all code scans, or create a new scan.
    """
    if request.method == 'GET':
        scans = Scan.objects.all()
        serializer = ScanSerializer(scans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def scan_detail(request, pk, format=None):
	try:
		scan = Scan.objects.get(pk=pk)
	except Scan.DoesNotExist:
		return Response(status=status.HTTP_400_BAD_REQUEST)
	if request.method == 'GET':
		serializer = ScanSerializer(scan)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ScanSerializer(scan, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		scan.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)