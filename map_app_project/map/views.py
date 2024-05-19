from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .models import Userinfo
from django.utils import timezone
from .models import Userinfo, OnlineUser
from openpyxl import Workbook
from .backends import CustomAuthBackend
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST



# Create your views here.


def custom_login(request):
    if request.method == "POST":
        useremail = request.POST.get('email')
        password = request.POST.get('pwd')
        custom_backend = CustomAuthBackend()
        user = custom_backend.authenticate(
            request, user_email=useremail, user_pass=password)
        print("User:", user)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # 认证成功，更新或创建在线状态
    
        # if request.session.get('_auth_user_id'):
        # # 如果会话中存在'_auth_user_id'键，说明用户已登录
        #     print("用户在线")
        #     # 重定向到主页或其他适当的视图
            request.session["username"] = user.user_name

            OnlineUser.objects.update_or_create(
                user=user, defaults={'last_online': timezone.now()})
            print(f"OnlineUser record created for {request.user.user_name}")

            print("XXXXXX__________", type(user.user_name))

            OnlineUser.objects.update_or_create(
                user=user, defaults={'last_online': timezone.now()})
            print(f"OnlineUser record created for {user.user_name}")

            return redirect('map:indexpage')

        else:
            # 认证失败，输出调试信息
            print("Authentication failed for user:", useremail)
            messages.error(request, 'Username OR password is incorrect')
            return redirect('map:login')
            # return HttpResponse("Invalid login details")
    else:
        # 显示登录表单
        return render(request, 'registration/login.html')


def my_view(request):
    user = request.user  # 获取当前登录用户对象
    return render(request, 'indexpage', {'user': user})


def indexpage(request):
    online_users = OnlineUser.objects.all()
    print(online_users)  # 添加这行来检查在线用户列表
    print("indexpage function is called")  # 这行用于调试
    return render(request, 'map/index.html', {'online_users': online_users})


def show_name(request):
    user = request.user
    show_username = user.user_name
    return render(request, '../chathome/chathome.html', {"show_username": show_username})


def index(request):

    users = Userinfo.objects.all()
    return render(request, 'map/index.html', {'user': request.user, 'users': users})

def usermanual(request):

    return render(request,'map/usermanual.html')


def toregister(request):
    return render(request, 'registration/register.html')


def register(request):
    userget = request.POST.get("user", '')
    passget = request.POST.get("pwd", '')
    useremail = request.POST.get("user_email", '')
    if userget and passget and useremail:
        # Check if the username already exists
        if Userinfo.objects.filter(user_name=userget).exists():
            # If the username already exists, return an error message
            messages.error(
                request, "This username has already been registered")
            return redirect('map:toregister')
            # return HttpResponse("This username has already been registered")
        if Userinfo.objects.filter(user_email=useremail).exists():
            messages.error(
                request, "This email address has already been registered")
            return redirect('map:toregister')
            # return HttpResponse("This email address has already been registered")

        else:
            # If the username does not exist, create a new user
            usersave = Userinfo(user_name=userget,
                                user_pass=passget, user_email=useremail)
            usersave.save()
            messages.success(
                request, "registration successful")
            return redirect('map:login')
            # return HttpResponse("register success")

    else:
        return HttpResponse("Please enter your complete account number,password and email")


def download_data_as_excel(request):
    # Query your SQL data using Django ORM
    users = Userinfo.objects.all()

    # Create a new Excel workbook
    workbook = Workbook()
    worksheet = workbook.active

    # Write headers to the first row
    headers = ['Username', 'Password', 'Email']
    worksheet.append(headers)


    # Write data rows
    for user in users:
        row = [user.user_name, user.user_pass, user.user_email]
        worksheet.append(row)

    # Create the HTTP response with Excel content type
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=user_data.xlsx'

    # Save the workbook content to the HTTP response
    workbook.save(response)

    return response

    # return HttpResponse("Please enter your complete account number,password and email")

# def submit_data(request):
#     if request.method == 'POST':
#         num = request.POST.get('num')  # 获取表单中名为'num'的数据
#         # 将数据赋值给name_id
#         name_id = "545555555555"
#         print(name_id)
#         # 可以对数据进行后续处理
#         return redirect('/chathome/', {"name_id": name_id})
#     else:
#         return HttpResponse('请求方法错误')


def custom_logout(request):
    if request.user.is_authenticated:
        print("正在注销用户：", request.user)  # 添加的打印语句
        # 获取当前用户
        user = request.user
        try:
            # 尝试获取 OnlineUser 记录
            online_user = OnlineUser.objects.get(user=user)
            # 设置用户状态为下线
            online_user.is_online = False
            online_user.save()
            print(f"OnlineUser record updated for {user.user_name}")
        except OnlineUser.DoesNotExist:
            pass  # 如果 OnlineUser 记录不存在，不执行任何操作

        # 使用 Django 的注销功能
        logout(request)
        print("用户已成功注销")
    return redirect('/')  # 重定向到登录页面的URL


def roleselect(request):
    if request.method == 'POST':
        room_number = request.POST.get('num')  # 从POST请求中获取房间号
    else:
        room_number = None  # 如果不是POST请求，则没有房间号
    return render(request, 'map/roleselect.html', {'room_number': room_number})
