# Generated by Django 4.0.6 on 2022-08-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followapp', '0020_referral_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTime',
            fields=[
                ('time_id', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('time1', models.TimeField()),
                ('time2', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'NewTime',
            },
        ),
    ]
