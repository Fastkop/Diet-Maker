# Generated by Django 3.0.6 on 2020-06-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200609_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default=None, upload_to='Profile-Photos'),
        ),
    ]
