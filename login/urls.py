from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    # path('login/',views.loginpage,name='login'),
     path('register/login/',views.register,name='login'),
     path('home/',views.home,name='home'),
     path('home/ask/',views.ask,name='ask'),
     path('home/logout/',views.logout,name='logout'),
     path('ask/posted/',views.posted,name='posted'),
     path('home/questions/',views.questions,name='questions'),
     path('postanswer/',views.postanswer,name='postanswer'),
     path('answering/',views.answering,name='answering'),
        
    
]
