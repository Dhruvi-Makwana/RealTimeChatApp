import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumers(WebsocketConsumer):
    # groups = ["broadcast"]

    def connect(self):
        # print("hello")
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        # print(text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # print('message', message)
        self.send(text_data=json.dumps({
             'type': 'chat_message',
             'message': message
        }))

    def disconnect(self, close_code):
        pass
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name, self.channel_name
        # )

    def chat_message(self, event):
        message = event['message']
        print(message)
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
