# Generated by Django 3.1.6 on 2021-02-18 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0022_auto_20210218_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='application',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='careers.interviewapp'),
            preserve_default=False,
        ),
    ]
