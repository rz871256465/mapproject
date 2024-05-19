from django.urls import re_path
from chathome import consumers as chathome_consumers
from map import consumers as map_consumers

websocket_urlpatterns = [
    re_path(r'chathome/(?P<group>\w+)/$',
            chathome_consumers.ChatConsumer.as_asgi()),
    re_path(r'indexpage/(?P<group>\w+)/$',
            map_consumers.OnlineUserConsumer.as_asgi()),
]
