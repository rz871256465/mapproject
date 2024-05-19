from django.db import models
from django.contrib.auth import get_user_model
from map.models import Userinfo

User = get_user_model()

class Map(models.Model):
    name = models.CharField(max_length=100, unique=True)
    maze = models.JSONField()  # 存储地图数据，例如，可以是地图的布局信息
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

# Create your models here.
