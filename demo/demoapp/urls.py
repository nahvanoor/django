from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("login/",views.login),
    path("register",views.register),
    path("admin_home/",views.admin_home),
    path("user_home",views.user_home),
    path("book",views.book),
    path("show_book",views.show_book),
    path("user_book",views.user_book),
    path("updatebook/<id>",views.updatebook),
    path("delete_book/<id>",views.delete_book),
    path("menucard",views.menucard),
    path("show_menu",views.show_menu),
    path("user_menu",views.user_menu),
    path("updatemenu/<id>",views.updatemenu),
    path("deletemenu/<id>",views.deletemenu)
    
]
