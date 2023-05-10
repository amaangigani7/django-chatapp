import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from core import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

application = get_asgi_application()

ws_patterns = [
    path('ws/test/', consumers.TestConsumer.as_asgi()),
    path('ws/new/', consumers.NewConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'http': application,
    'websocket': URLRouter(ws_patterns)
})