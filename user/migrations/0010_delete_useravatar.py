# Generated by Django 4.1.3 on 2022-12-11 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAvatar',
        ),
    ]
