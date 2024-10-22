from django.urls import path
from . import views
from core.views import home
urlpatterns = [
    path('', home.as_view(), name = "home"),
    path('createroom/', views.createRoom, name = "create_room"),
    path('chat/<int:id>/', views.joinRoom, name = "join_room"),
    path('deleteroom/<int:id>/', views.deleteroom, name = "delete_room"),
    path('about/', views.about, name = "about")
    
]