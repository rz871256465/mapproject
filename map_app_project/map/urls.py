from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('index/', views.index, name='index'),
    path('toregister/', views.toregister, name='toregister'),
    path('register/', views.register, name='register'),
    path('indexpage/', views.indexpage, name='indexpage'),
    # path('submit_data/',views.submit_data,name='submit_data')
    path('roleselect/', views.roleselect, name='roleselect'),
    path('usermanual/',views.usermanual,name='usermanual' )
]
