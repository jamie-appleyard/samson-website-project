# Generated by Django 3.1.8 on 2021-06-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.DeleteModel(
            name='Paragraph',
        ),
    ]
