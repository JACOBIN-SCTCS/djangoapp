# Generated by Django 2.0 on 2018-01-08 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('RA', 'Regular-Academic'), ('RNA', 'Regular-NonAcademic'), ('C1', 'Contract Staff(1 year)'), ('C6', 'Contract Staff (6 months)'), ('AS', 'Ad-Hoc Staff'), ('PF', 'Part-time-staff'), ('OT', 'Office Trainee'), ('DT', 'Department Trainee')], default='RA', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
