# Generated by Django 2.2 on 2020-07-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='static/assets/img/cabin.png', upload_to='uploads/'),
        ),
    ]
