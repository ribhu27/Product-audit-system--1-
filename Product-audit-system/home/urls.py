from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [path('',views.home, name='home'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/login/',views.login,name='login'),
    path('register/', views.user_register, name="register"),
    path('logout/',views.logout,name='logout'),
    path('login/result',views.result,name='result'),
    path('register/login/result', views.result, name="result"),
    path('login/logout/',views.logout,name='logout'),
    path('register/login/logout/',views.logout,name='logout'),]

