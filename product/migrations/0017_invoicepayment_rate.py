# Generated by Django 3.2.8 on 2021-10-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20211028_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicepayment',
            name='rate',
            field=models.FloatField(default=1),
        ),
    ]
