from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    sensor_type = models.CharField(max_length=50)

class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    times_temp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
