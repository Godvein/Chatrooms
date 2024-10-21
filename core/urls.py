from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('createroom/', views.createRoom, name = "create_room"),
    path('chat/<int:id>/', views.joinRoom, name = "join_room"),
    path('deleteroom/<int:id>/', views.deleteroom, name = "delete_room")
]