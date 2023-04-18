import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumers(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
             'type': 'chat_message',
             'message': message
        }))

    def disconnect(self, close_code):
        self.close(close_code)

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
