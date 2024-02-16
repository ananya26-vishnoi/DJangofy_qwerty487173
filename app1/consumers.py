
from channels.generic.websocket import AsyncWebsocketConsumer
class TranscribeASR(AsyncWebsocketConsumer):
    async def connect(self):
        print("Incoming connection request")
        await self.accept()

    async def disconnect(self, close_code):
        pass
        
    async def receive(self, text_data):
        pass
