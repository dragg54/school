from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/student/', include("student.urls"), name="student"),
    path('api/v1/payment/', include('payment.urls'), name='payment'),
    path('api/v1/auth/', include('auth.urls'), name="token"),
    path('api/v1/course/', include('course.urls'), name="course")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
