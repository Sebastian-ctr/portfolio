# Generated by Django 3.1.7 on 2021-07-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='content',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.FileField(default=None, upload_to='media_cdn'),
        ),
    ]
