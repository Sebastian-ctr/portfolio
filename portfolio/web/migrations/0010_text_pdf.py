# Generated by Django 3.1.7 on 2021-08-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20210729_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='pdf',
            field=models.FileField(default=None, null=True, upload_to='media_cdn'),
        ),
    ]
