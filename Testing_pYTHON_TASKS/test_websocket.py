import asyncio
import websockets
import json
import random
import time

async def sensor_data():
    async with websockets.connect('ws://localhost:8000/ws/sensor_data/') as websocket:
        while True:
            temperatura_data = {
                'sensor_id': 'temperaturechart',
                'value': random.uniform(20.0, 30.0)
            }
            humidity_data = {
                'sensor_id': 'humiditychart',
                'value': random.uniform(10.0, 75.0)
            }
            await websocket.send(json.dumps(temperatura_data))
            await websocket.send(json.dumps(humidity_data))

            await asyncio.sleep(1)
            print("Hello")

asyncio.get_event_loop().run_until_complete(sensor_data())
