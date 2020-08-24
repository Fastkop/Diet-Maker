# Generated by Django 3.0.6 on 2020-06-20 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_diet_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='diet',
        ),
        migrations.AddField(
            model_name='meal',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]