# Generated by Django 3.1.7 on 2021-04-01 09:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 4, 1, 9, 46, 1, 936996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 9, 46, 1, 935997, tzinfo=utc)),
        ),
    ]
