# Generated by Django 4.2.7 on 2023-11-13 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0013_alter_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
