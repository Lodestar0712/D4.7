# Generated by Django 4.0.4 on 2022-05-27 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='commentPost',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentuser',
            new_name='commentUser',
        ),
    ]