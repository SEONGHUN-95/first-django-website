# Generated by Django 3.1.3 on 2022-03-07 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cash', '0006_auto_20220306_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
