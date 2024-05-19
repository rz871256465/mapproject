from django.contrib import admin


from .models import Userinfo,OnlineUser

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'last_login')

admin.site.register(Userinfo, YourModelAdmin)
  
class OnlineUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_online')

admin.site.register(OnlineUser, OnlineUserAdmin)