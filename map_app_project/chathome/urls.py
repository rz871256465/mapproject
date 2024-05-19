from django.urls import path
from . import views
from .views import download_data_as_excel



urlpatterns = [

    path('', views.chathome, name='chathome'),
    path('<name_id>/', views.chatpair, name='chatpair'),
    path('pairing/', views.pairing, name='pairing'),
    path('download_excel/', views.download_data_as_excel, name='download_excel'),
    path('download_excel_another/', views.download_data_as_excel_another, name='download_excel_another'),
    path('download_excel_map/', views.download_data_as_excel_map, name='download_excel_map'),
    path('', views.save_maze, name='save_maze'),
]
