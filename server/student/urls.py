from django.urls import path
from . import views

urlpatterns = [
    path("profile/create", views.CreateStudentProfileAPIView.as_view(), name="create_profile"),
    path("getstudents", views.GetAllStudents.as_view(), name="get students"),
    path("getstudent/<str:pk>", views.GetStudent.as_view(), name="get student"),
]
