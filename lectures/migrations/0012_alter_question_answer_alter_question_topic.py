# Generated by Django 4.1.7 on 2023-06-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0011_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, help_text='Q and A', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(blank=True, help_text='Topic questioned', max_length=100, null=True),
        ),
    ]
