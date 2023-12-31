# Generated by Django 4.1.7 on 2023-03-25 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('lectures', '0004_remove_lecture_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='date',
        ),
        migrations.CreateModel(
            name='LectureDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_documents', to='wagtaildocs.document')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_documents', to='lectures.lecture')),
            ],
        ),
    ]
