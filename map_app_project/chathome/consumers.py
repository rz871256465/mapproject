import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from django.db import connection,models
from django.apps import apps
from .constants.global_variables import generate_maze,maze
import time
CONN_LIST = []


class ChatConsumer(WebsocketConsumer):
    maze_data = None
    def websocket_connect(self, message):
        from map.models import Userinfo

        from map.backends import CustomAuthBackend
        
        # 有客户端来向后端发送websocket连接的请求时，自动触发
        # 服务端允许和客户端创建连接

        self.accept()
        ChatConsumer.maze_data=generate_maze(20, 20) 
        self.username = " "
        group = self.scope['url_route']['kwargs'].get("group")
        a=maze
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        print("a的值为：",a)
        self.connect_to_mysql()
    
        
       
       
      
    def connect_to_mysql(self):
        from map.models import Userinfo
        # 连接 MySQL 数据库
        try:
            # 在这里使用模型进行数据库操作
            data = Userinfo.objects.all()

            print("数据库连接成功！")
        except Exception as e:
            print("数据库连接失败:", e)


    def create_chat_table_if_not_exists(self, senderuser):
    # 根据 senderuser 构建聊天记录表的表名
        table_name = f"chat_{senderuser.lower()}"

    # 检查该表是否已经存在
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES LIKE %s", [table_name])
            table_exists = cursor.fetchone()

        if not table_exists:
            with connection.cursor() as cursor:
                cursor.execute(f'''
                    CREATE TABLE {table_name} (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        message TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        
                    )
                ''')
        return table_name
    def store_message_in_table(self, table_name, message):
    # 在指定的表中存储消息
        with connection.cursor() as cursor:
            cursor.execute(f'''
                INSERT INTO {table_name} (message, created_at)
                VALUES (%s, NOW())
            ''', [message])

    def websocket_receive(self, message):
        from game.models import Map
        # print("Received message:", message, type(message))
        if 'text' in message and message['text'] == "createmap":
            maze_data=ChatConsumer.maze_data  # 传入迷宫的行数和列数
            json_maze_data = json.dumps(maze_data)
            self.send(json_maze_data)
            # print(maze_data)
            # self.send(maze_data)
        elif 'text' in message and "creat_map" in message['text']:
            message_data = json.loads(message['text'])
            map_name = message_data.get('map_text')
            
            maze_data=Map.objects.values('maze').filter(name=map_name).first()
            maze_data_with_type = {'type': 'maze', **maze_data}  # Add 'type': 'maze' to the maze_data dictionary
            json_maze_data = json.dumps(maze_data_with_type)
            self.send(json_maze_data)
            # print(maze_data)
            
           
        else:
            username = self.username

            group = self.scope['url_route']['kwargs'].get("group")
            async_to_sync(self.channel_layer.group_send)(group, {
                "type": "xx.oo",
                'message': message,
                "username": username,
            })
            message_data = json.loads(message['text'])
            senderuser = message_data.get('senderuser', '')
            textinfor = message_data.get('message', '')
            # print(senderuser,textinfor)



            chat_table_name = self.create_chat_table_if_not_exists(senderuser)

            self.store_message_in_table(chat_table_name, textinfor)

            if 'action' in message_data and message_data['action'] == 'move':
                group = self.scope['url_route']['kwargs'].get("group")
                # 根据移动方向更新光标位置的代码
                # 例如：更新光标位置后，发送新的光标位置信息给群组中的其他客户端
                async_to_sync(self.channel_layer.group_send)(group, {
                    "type": "update_cursor",
                    "position": message_data['red_cell_position'],
                })

    def xx_oo(self, event):

        text = event['message']['text']

        username = event['username']
        message_to_send = f"{text}"
        self.send(message_to_send)

    def update_cursor(self, event):
        position = event['position']
        # 根据移动方向更新光标位置的代码
        # 然后将新的光标位置发送给当前 WebSocket 连接的客户端
        self.send(text_data=json.dumps({
            
            "action": "move",
            "red_cell_position": position
        }))

        
    def websocket_disconnect(self, message):
        # 断开连接
        group = self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_discard)(
            group, self.channel_name)
        raise StopConsumer()