# Generated by Django 3.1.6 on 2021-02-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0023_interview_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='declined',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_apply_by_date',
            field=models.CharField(default='05/03/21', max_length=12),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_date_posted',
            field=models.CharField(default='19/02/21', editable=False, max_length=12),
        ),
    ]
