# Generated by Django 3.0.6 on 2020-06-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_surveyaccount_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyaccount',
            name='last_email',
            field=models.DateField(blank=True, null=True),
        ),
    ]
