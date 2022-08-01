# Generated by Django 4.0.6 on 2022-07-23 13:46

import django.contrib.postgres.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('followapp', '0007_alter_chessboard_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=220)),
                ('degree_program', models.CharField(max_length=220)),
                ('subject_referred', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), size=None), size=None)),
                ('reasons', models.CharField(max_length=10000)),
                ('counselor_id', models.CharField(max_length=220)),
                ('faculty_id', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), size=None), size=None)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=220)),
                ('behavior_problem', multiselectfield.db.fields.MultiSelectField(choices=[('CHEATING', 'CHEATING'), ('TARDINESS', 'TARDINESS'), ('DISRESPECTFUL', 'DISRESPECTFUL'), ('BAD ATTITUDE', 'BAD ATTITUDE'), ('OTHERS', 'OTHERS')], max_length=220)),
                ('feedback', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name_plural': 'Referral',
            },
        ),
        migrations.DeleteModel(
            name='ChessBoard',
        ),
    ]
