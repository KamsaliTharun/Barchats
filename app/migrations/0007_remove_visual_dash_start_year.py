# Generated by Django 4.2 on 2023-05-03 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_visual_dash_end_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visual_dash',
            name='start_Year',
        ),
    ]
