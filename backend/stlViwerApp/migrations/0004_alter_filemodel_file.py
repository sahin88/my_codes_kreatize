# Generated by Django 3.2.7 on 2021-09-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stlViwerApp', '0003_auto_20210910_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
