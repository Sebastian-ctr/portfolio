# Generated by Django 3.1.7 on 2021-07-13 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_photoimage_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photoimage',
            old_name='post',
            new_name='photo',
        ),
    ]