# Generated by Django 3.0.6 on 2020-08-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200824_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='photo',
            field=models.ImageField(default=None, upload_to='Meal-photos'),
        ),
    ]
