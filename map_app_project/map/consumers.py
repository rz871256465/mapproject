from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
import json

class OnlineUserConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        from .models import OnlineUser
        self.accept()  # 接受WebSocket连接

        # 获取所有在线用户信息
        online_users = OnlineUser.objects.all()

        # 可以在这里设置一个逻辑来确定谁被认为是在线的
        # 例如，您可以设置一个时间阈值，如您之前的逻辑所示
        time_threshold = timezone.now() - timezone.timedelta(minutes=15)
        online_users = [online_user for online_user in online_users if online_user.last_online > time_threshold]

        # 发送在线用户列表给客户端
        self.send(text_data=json.dumps({
            'type': 'online_users',
            'data': [{'user_id': user.user.user_id, 'user_name': user.user.user_name} for user in online_users]
        }))

    def websocket_receive(self, message):
        from .models import Userinfo, OnlineUser
        text_data_json = json.loads(message['text'])
        user_name = self.scope["session"].get("username")
        message_type = text_data_json.get('type', '')
        print(user_name)
        if user_name:
            try:
                user = Userinfo.objects.get(user_name=user_name)
                self.send(json.dumps({'user_id': user.user_id}))
                print("用户的id:",user.user_id)
            except Userinfo.DoesNotExist:
                self.send(json.dumps({'error': 'User not found'}))
        else:
            self.send(json.dumps({'error': 'User name is empty or not provided'}))

        if message_type == 'disconnect_request':
            print("处理 disconnect_request")
            
            try:
                user_info = Userinfo.objects.get(user_name=user_name)
                online_users = OnlineUser.objects.get(user=user_info)
                print(f"找到用户 {user_name}, 正在设置为离线")
                # 设置用户为离线
                online_users.last_online = timezone.now() - timezone.timedelta(days=1)
                online_users.save()
                print(f"用户 {user_name} 已设置为离线")
            except (Userinfo.DoesNotExist, OnlineUser.DoesNotExist):
                print(user_info)
                print("未找到用户或在线用户")
                self.send(text_data=json.dumps({'error': 'User not found or not online'}))
            finally:
                print("关闭连接")
                self.close()

    def websocket_disconnect(self, message):
        
        print("关闭")
        raise StopConsumer()  # 停止Consumer，关闭连接

