# Generated by Django 4.1.7 on 2023-04-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0006_lecture_lecture_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='lecture_file',
        ),
        migrations.AddField(
            model_name='lecture',
            name='transcript',
            field=models.TextField(blank=True, help_text='Transcript of the lecture'),
        ),
    ]