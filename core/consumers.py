import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    #initial connection to consumer
    def connect(self):
        self.accept()

        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'

        #synced room_group_name to channel name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
    #when message is received from websocket
    def receive(self, text_data):
        json_text_data = json.loads(text_data)
        message = json_text_data["message"]
        
        #syncing group to the message
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type" : "chat_message",
                "message" : message
            }
        )
#message sent back to websocket
    def chat_message(self, event):
            message = event["message"]
            self.send(text_data=json.dumps({
                 "type" : "chat",
                 "message" : message
            }))
    