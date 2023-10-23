# Generated by Django 3.1.5 on 2021-02-10 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210125_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('user_status', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='VettingStatus',
            fields=[
                ('vetting_status', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
            ],
        ),
    ]
