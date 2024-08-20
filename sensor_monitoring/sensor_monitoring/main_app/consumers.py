from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Sensor, SensorReading

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

