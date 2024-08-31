from django.urls import re_path
from . import consumers

websocket_url_patterns = [
    re_path(r'ws/sensors/$', consumers.SensorConsumer.as_asgi()),
]
