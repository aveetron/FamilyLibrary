# Generated by Django 2.2 on 2020-07-18 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200718_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
    ]