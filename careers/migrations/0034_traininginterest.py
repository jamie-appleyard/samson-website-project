# Generated by Django 3.1.8 on 2021-08-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0033_auto_20210818_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]