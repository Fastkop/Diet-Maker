# Generated by Django 3.0.6 on 2020-06-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
