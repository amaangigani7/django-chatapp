from django.shortcuts import render
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your views here.
async def home(request):

    channel_layer = get_channel_layer()
    
    for i in range(10):
        data = {'count': i}
        await channel_layer.group_send(
            'event_sharif',
            {
                'type': 'send_notification',
                'message': data
            }  
        )
        time.sleep(1)

    return render(request, "index.html")