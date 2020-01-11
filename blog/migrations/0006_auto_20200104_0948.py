# Generated by Django 2.2.4 on 2020-01-04 01:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200103_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='公告标题')),
                ('body', models.TextField(verbose_name='公告内容')),
                ('publish', models.DateTimeField(default=datetime.datetime(2020, 1, 4, 1, 48, 10, 609591, tzinfo=utc), verbose_name='发表时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 4, 1, 48, 10, 608589, tzinfo=utc), verbose_name='发表时间'),
        ),
    ]
