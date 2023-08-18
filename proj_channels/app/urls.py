from django.urls import path

from app.views import *


urlpatterns = [
    path('',home, name='home'),
    path('registration',registration, name='registration'),
    path('user_login/',user_login, name = 'user_login'),
    path('user_logout/', user_logout, name = 'user_logout'),
    path("chat/", index, name="index"),
    path("chat/<str:room_name>/", room, name="room"),
]