# Generated by Django 3.2.8 on 2021-10-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_seller_old_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight_value',
            field=models.IntegerField(default='0', max_length=100),
        ),
    ]