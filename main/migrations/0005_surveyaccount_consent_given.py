# Generated by Django 3.0.6 on 2020-06-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_reporttoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyaccount',
            name='consent_given',
            field=models.BooleanField(default=False),
        ),
    ]
