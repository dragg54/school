from django.urls import path
from rest_framework.authtoken import views
from . import  views as auth_view

urlpatterns = [
    path("get-token", views.obtain_auth_token, name= "get token"),
    path("user/new", auth_view.CreateUser.as_view())
]