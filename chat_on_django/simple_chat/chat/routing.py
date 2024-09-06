from django.urls import re_path
from . import consumers

websocket_url_patterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]
