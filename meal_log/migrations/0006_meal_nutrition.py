# Generated by Django 3.1.4 on 2020-12-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_log', '0005_meal_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='nutrition',
            field=models.TextField(default='Not entered'),
            preserve_default=False,
        ),
    ]
