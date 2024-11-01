
import csv
from django.http import HttpResponse
from django.shortcuts import render

from .models import SensorReading, Sensor

def export_reading_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="reading.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sensor', 'Times_Temp', 'Value'])
    readings = SensorReading.objects.all().values_list('sensor', 'times_temp', 'value')
    for r in readings:
        writer.writerow(r)
    return response

def index(request):
    return render(request, 'sensor_app/index.html')
