# Generated by Django 5.0.6 on 2024-06-12 10:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='DateBookings',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]