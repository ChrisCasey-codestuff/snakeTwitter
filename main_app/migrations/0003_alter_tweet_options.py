# Generated by Django 4.2 on 2023-04-25 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_tweet_user_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-date_time']},
        ),
    ]
