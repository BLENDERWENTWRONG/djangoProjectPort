# Generated by Django 4.1.3 on 2022-12-04 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]