# Generated by Django 4.1.4 on 2023-02-11 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='stripe_price_id',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
