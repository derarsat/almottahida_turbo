# Generated by Django 3.2.8 on 2021-10-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20211028_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discount_reason',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
