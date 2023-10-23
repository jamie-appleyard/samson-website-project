# Generated by Django 3.1.7 on 2021-03-15 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210223_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vettingstatus',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='vetting_status', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
