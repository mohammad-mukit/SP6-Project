# from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('add_student',views.add_student,name="add_student"),
    path('search/',views.search,name="search"),
    path('show_all_student/',views.show_all_student,name="show_all_student"),
    path('delete/<int:pk>',views.delete,name="delete"),
    
]