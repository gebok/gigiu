# Generated by Django 4.0 on 2022-04-08 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gigiuattendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='enroll_id',
            new_name='enrol_id',
        ),
    ]