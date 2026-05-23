from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login_view'),
    path('home/', views.home, name='home'),
    path('water/', views.water, name='water'),
    path('feelings/', views.feelings, name='feelings'),
    path('alert/', views.alert, name='alert'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('settings/', views.settings, name='settings'),
]
