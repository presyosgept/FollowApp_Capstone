# Generated by Django 4.0.6 on 2022-07-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerings',
            name='id',
        ),
        migrations.AlterField(
            model_name='offerings',
            name='offer_no',
            field=models.CharField(max_length=225, primary_key=True, serialize=False),
        ),
    ]
