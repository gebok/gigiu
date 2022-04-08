# Generated by Django 4.0 on 2022-04-08 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('gigiuhr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CallRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('call_made_to', models.CharField(max_length=50)),
                ('destination_org', models.CharField(max_length=100)),
                ('town_province', models.CharField(max_length=100)),
                ('comments', models.TextField(max_length=200)),
                ('date_called', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(max_length=30)),
                ('call_operator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
                ('call_requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gigiuhr.employee')),
                ('call_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigiucall.calltype')),
                ('research_centre', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigiuhr.researchcentre')),
            ],
        ),
    ]
