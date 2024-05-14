# Generated by Django 5.0.3 on 2024-05-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0026_remove_booking_guest_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bath',
            field=models.IntegerField(default=1, verbose_name='Душ кол-во'),
        ),
        migrations.AddField(
            model_name='room',
            name='bed',
            field=models.IntegerField(default=1, verbose_name='Кровать кол-во'),
        ),
    ]