from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from schoolApp.models import studentRecord
from schoolApp.serializers import studentRecordSerializer

# Create your views here.

@csrf_exempt
def studentRecordApi(request,id=0):
    # Read data
    if request.method == 'GET':
        records = studentRecord.objects.all()
        records_serializer = studentRecordSerializer(records,many=True)
        return JsonResponse(records_serializer.data,safe=False)
    # Insert data
    elif request.method == 'POST':
        insert_data = JSONParser().parse(request)
        records_serializer = studentRecordSerializer(data=insert_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Data added successfully",safe=False)
        return JsonResponse("Failed to add data",safe=False)
    # Update data
    elif request.method == 'PUT':
        update_data = JSONParser().parse(request)
        record = studentRecord.objects.get(rollnumber=update_data['rollnumber'])
        records_serializer = studentRecordSerializer(record,data=update_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Updated successfully",safe=False)
        return JsonResponse("Failed to update data",safe=False)
    elif request.method == 'DELETE':
        record = studentRecord.objects.get(rollnumber = id)
        record.delete()
        return JsonResponse("Deleted successfully",safe=False)
    return JsonResponse("Failed to delete data",safe=False)
