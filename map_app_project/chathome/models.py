from django.db import models

# Create your models here.


class Userinfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_pass = models.CharField(max_length=100)
    user_email = models.EmailField()

    def __str__(self):
        return self.user_name
class ChatMessage(models.Model):
    sender = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.user_name} - {self.timestamp}"

def store_message(senderuser, message_text):
    sender = Userinfo.objects.get(user_name=senderuser)

    # 创建或获取与该发送者相关联的聊天记录表
    chat_table_name = f"chat_{senderuser.lower()}"
    ChatMessage._meta.db_table = chat_table_name
    ChatMessage.objects.create(sender=sender, message=message_text)