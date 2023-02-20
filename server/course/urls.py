from django.urls import path
from . import views

urlpatterns = [
    path("course/add", views.CreateCourseView.as_view(), name= "add course")
]