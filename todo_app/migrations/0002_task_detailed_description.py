# Generated by Django 4.1.1 on 2022-09-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
