# Generated by Django 2.2.4 on 2020-01-07 04:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20200107_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 4, 0, 33, 95082, tzinfo=utc), verbose_name='发表时间'),
        ),
    ]
