# from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login_view,name="login"),
]