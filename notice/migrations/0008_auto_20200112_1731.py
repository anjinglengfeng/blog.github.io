# Generated by Django 2.2.7 on 2020-01-12 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_auto_20200112_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 12, 9, 31, 32, 72305, tzinfo=utc), verbose_name='发表时间'),
        ),
    ]