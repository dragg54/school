from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from payment import views as payment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/student/', include("student.urls"), name="student"),
    path('api/v1/payment/<str:pk>', payment_views.CreateCheckoutSessionView.as_view(), name='payment')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
