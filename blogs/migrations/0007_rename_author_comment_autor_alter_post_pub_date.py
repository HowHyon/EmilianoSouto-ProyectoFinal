# Generated by Django 4.2.6 on 2023-11-24 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_post_pub_date_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='autor',
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 17, 41, 34, 258272, tzinfo=datetime.timezone.utc)),
        ),
    ]
