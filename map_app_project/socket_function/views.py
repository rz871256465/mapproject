import json
from django.shortcuts import render ,HttpResponse
from django.http import JsonResponse



DB=[]
def communication(request):
    return render(request,'communication.html')

def send_msg(request):
    print("接收到客户请求",request.GET) 
    text =  request.GET.get('text')
    DB.append(text)
    return HttpResponse("OK")

def get_msg(request):
     index = request.GET.get('index')
     index = int(index)
     context = {
            "data":DB[index:],
            "max_index":len(DB),
     }
     return JsonResponse(context)
# Create your views here.
