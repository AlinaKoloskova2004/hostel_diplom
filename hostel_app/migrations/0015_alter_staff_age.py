# Generated by Django 4.1.7 on 2023-05-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0014_alter_staff_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='age',
            field=models.IntegerField(verbose_name='Дата рождения'),
        ),
    ]