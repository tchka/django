# Generated by Django 2.2 on 2020-11-01 13:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20201101_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 13, 59, 45, 579896, tzinfo=utc)),
        ),
    ]
