# Generated by Django 3.2.8 on 2021-10-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20211025_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight_value',
            field=models.IntegerField(default=0),
        ),
    ]
