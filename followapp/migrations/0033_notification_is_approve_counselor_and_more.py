# Generated by Django 4.0.6 on 2022-11-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followapp', '0032_notification_is_counseled'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_approve_counselor',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_approve_student',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_reSched',
            field=models.BooleanField(default=False),
        ),
    ]
