# Generated by Django 4.1.3 on 2022-12-04 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]