from django.contrib import admin

from .models import Payment, PaymentHistory

# Register your models here.
admin.site.register(Payment)
admin.site.register(PaymentHistory)