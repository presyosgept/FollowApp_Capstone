# Generated by Django 4.0.6 on 2022-07-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followapp', '0013_alter_referral_faculty_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetScheduleCounselor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=220)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('choice', models.CharField(max_length=220)),
            ],
            options={
                'verbose_name_plural': 'SetScheduleCounselor',
            },
        ),
    ]