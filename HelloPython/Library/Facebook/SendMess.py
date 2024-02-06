from fbchat import Client
from fbchat.models import Message

class MessengerBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # Kiểm tra nếu tin nhắn là "hello"
        if message_object.text.lower() == "hello":
            # Gửi tin nhắn đến người gửi
            self.send(Message(text="Xin chào!"), thread_id=thread_id, thread_type=thread_type)

# Thay thế 'your_email' và 'your_password' bằng thông tin đăng nhập Facebook của bạn
client = MessengerBot("nvthanh154fb@gmail.com", "$154thienduong")
client.listen()
