# Generated by Django 3.1.5 on 2021-01-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0008_auto_20210127_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_apply_by_date',
            field=models.CharField(default='11/02/21', max_length=12),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_date_posted',
            field=models.CharField(default='28/01/21', editable=False, max_length=12),
        ),
    ]