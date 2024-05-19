from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.hashers import check_password


# Create your models here.


class Userinfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_pass = models.CharField(max_length=128)  # 使用128长度以容纳哈希密码
    user_email = models.CharField(
        max_length=30, unique=True, blank=False, null=True)
    last_login = models.DateTimeField(auto_now=True)  # 新添加的字段

    def verify_password(self, raw_password):
        return check_password(raw_password, self.user_pass)


class LoggedInUser(models.Model):
    user = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    login_time = models.DateTimeField(default=timezone.now)  # 新增字段

    def __str__(self):
        return self.user.user_name


class OnlineUser(models.Model):
    user = models.OneToOneField(
        Userinfo, on_delete=models.CASCADE, related_name='online_status')
    last_online = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.user_name + " is online"


class Role(models.Model):
    role_name = models.CharField(max_length=20, default="普通用户", unique=True)
    description = models.TextField(blank=True)
    user_to_role = models.ManyToManyField(Userinfo, related_name="roles")

    def __str__(self):
        return self.role_name
