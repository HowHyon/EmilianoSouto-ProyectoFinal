# Generated by Django 4.2.6 on 2023-11-25 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 21, 21, 5, 338321, tzinfo=datetime.timezone.utc)),
        ),
    ]
