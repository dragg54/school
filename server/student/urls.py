from django.urls import path
from . import views


urlpatterns = [
    path("profile/create", views.CreateStudentProfileAPIView.as_view(), name="create_profile")
]