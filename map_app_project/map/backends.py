from .models import Userinfo

class CustomAuthBackend:
    def authenticate(self, request, user_email=None, user_pass=None):
        try:
            user = Userinfo.objects.get(user_email=user_email)
            print("User found:", user.user_email,"password",user.user_pass)  # 打印用户对象
            if user.user_pass == user_pass:  # 直接比较用户输入的密码与数据库中存储的密码
                return user
            else:
                return None
        except Userinfo.DoesNotExist:
            return None