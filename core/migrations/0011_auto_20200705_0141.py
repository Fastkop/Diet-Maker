# Generated by Django 3.0.6 on 2020-07-05 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_food_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='type',
        ),
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.ManyToManyField(to='core.FoodType'),
        ),
    ]
