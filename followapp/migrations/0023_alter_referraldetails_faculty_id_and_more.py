# Generated by Django 4.0.6 on 2022-08-11 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followapp', '0022_referraldetails_remove_referral_behavior_problem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referraldetails',
            name='faculty_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='referraldetails',
            name='reasons',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='referraldetails',
            name='subject_referred',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
