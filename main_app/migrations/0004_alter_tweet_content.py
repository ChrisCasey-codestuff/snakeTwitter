# Generated by Django 4.2 on 2023-04-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_tweet_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(max_length=250, verbose_name=''),
        ),
    ]