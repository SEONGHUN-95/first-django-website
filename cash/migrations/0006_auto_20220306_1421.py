# Generated by Django 3.1.3 on 2022-03-06 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0005_auto_20220306_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]