# Generated by Django 4.1.7 on 2023-03-25 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_lecture_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='link',
        ),
    ]
