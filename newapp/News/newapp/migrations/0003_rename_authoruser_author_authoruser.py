# Generated by Django 4.0.4 on 2022-05-27 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_rename_comment_comment_commentpost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='authoruser',
            new_name='authorUser',
        ),
    ]
