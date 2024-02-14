from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('room', views.room, name='room'),
    path('messages/<str:name>', views.messages, name='messages'),
    path('login', views.login, name="login"),
    path('accounts/login/', views.login, name='login'),
    path('logout', views.logout, name="logout")
]
