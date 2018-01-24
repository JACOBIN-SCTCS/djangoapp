# Generated by Django 2.0 on 2018-01-24 11:39

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_rec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 1, 24, 11, 39, 17, 575256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
