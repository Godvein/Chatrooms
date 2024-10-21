from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('createroom/', views.createRoom, name = "create_room")
]