from datetime import timedelta, datetime

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Sensor, SensorReading

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connection")
        await self.accept()

    async def disconnect(self, close_code):
        print("disconnection")

    async def receive(self, text_data):
        data = json.loads(text_data)
        sensor_id = data['sensor_id']
        value = data['value']

        sensor = await Sensor.objects.get(id=sensor_id)
        reading = SensorReading(sensor=sensor, value=value)
        await reading.save()

        time_thresheld = datetime.now() - timedelta(hours=1)

        readings = SensorReading.objects.filter(sensor=sensor, times_temp=time_thresheld)

        min_value = min(v.value for v in readings)
        max_value = max(v.value for v in readings)
        med_value = sum(v.value for v in readings) / len(readings)

        await self.send(text_data=json.dumps({
            'sensor_id': sensor_id,
            'min_value': min_value,
            'max_value': max_value,
            'med_value': med_value
        }))
        print("receive")
