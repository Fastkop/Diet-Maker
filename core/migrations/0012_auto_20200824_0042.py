# Generated by Django 3.0.6 on 2020-08-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200705_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
