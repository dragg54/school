from django.urls import path
from . import views

urlpatterns = [
    path("profile/create", views.CreateStudentProfileAPIView.as_view(), name="create_profile"),
    path("get-students", views.GetAllStudentProfile.as_view(), name="get students"),
    path("get-student/<str:pk>", views.GetStudentProfile.as_view(), name="get student"),
    path("delete-student/<str:pk>", views.DeleteStudentProfile.as_view(), name="delete student"),
    path("profile/update", views.UpdateStudentProfile.as_view(), name="update student")
]
