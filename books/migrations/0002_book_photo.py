# Generated by Django 2.2 on 2020-07-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
