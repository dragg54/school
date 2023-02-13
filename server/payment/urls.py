from django.urls import path

from . import views

urlpatterns = [
    path('webhook', views.my_webhook_view, name="webhook"),
    path('<str:pk>', views.CreateCheckoutSessionView.as_view(), name='create_payment'),
]
