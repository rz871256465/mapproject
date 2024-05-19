from django.urls import path
from . import views

urlpatterns = [
    path('create_map/', views.create_map, name='create_map'),
    path('map/<int:map_id>/', views.map_detail, name='map_detail'),
]